# Review Rails browser sessions

Read the provider’s current Rails guide and the application’s accepted session
and identity decisions. Compare the protocol integration and the session store
separately. An example that assigns to Rails’ `session` works through a
configurable store. Check how that example handles OAuth state, CSRF, callbacks,
and logout before carrying its storage choices into another application.

## Choose storage from the logout guarantee

Rails’ encrypted CookieStore can hold a small identity reference and expiry.
Clearing the cookie on logout removes that browser’s copy. If an earlier copy
must stop working immediately, use server-side session state or a server-side
revocation check. Confirm whether logout should end the application session,
the identity provider’s single sign-on session, or both. Track verification of
live provider behavior separately from request specs that stub the provider.

If the application uses persistent authenticated sessions, trace anonymous CSRF
bootstrap, OAuth request, failed callback, and stale-cookie reads through the
actual middleware and adapter. Check the installed implementation. A method
named like a read can insert a row while resolving a missing session ID. Where
anonymous persistence is unnecessary, consider short-lived encrypted cookies for
handshake state and create the persistent session after successful sign-in.
Keep the handshake token bound to its own session and verify which endpoint
supplies CSRF tokens for subsequent authenticated actions.

## Make the callback boundary visible

Trace who writes identity data before deciding what to trust. OmniAuth puts its
authentication result in the Rack environment at `omniauth.auth`. Check where
the provider strategy validates the ID token and where it gets the claims the
controller uses. Strong Parameters allowlist client input for mass assignment.
Take issuer, subject, and email verification from the validated provider result.

Name operations that cross the middleware boundary. For example,
`verified_provider_claims` can read the provider result after middleware has
validated it, and `stage_authenticated_session` can pass the resolved identity
to session middleware via an internal Rack environment key. Keep provider hash
paths and request mutations inside those methods. Trace both the writer and
reader of a handoff because Rails' `request.set_header` can write an internal
Rack key whose name never appears in an HTTP header.

Read callbacks in execution order, including inherited CSRF verification.
Each `prepend_before_action` goes to the front of the chain. If sign-out or
a denied request must avoid persisting a replacement session, trace revocation
and the end-of-request commit separately. A method such as
`reset_session_without_replacement` can express both operations in one call.

[OmniAuth authentication hash](https://github.com/omniauth/omniauth#integrating-omniauth-into-your-application) · [Rails controller callbacks and Strong Parameters](https://guides.rubyonrails.org/action_controller_overview.html) · [Rack session implementation](https://github.com/rack/rack-session/blob/main/lib/rack/session/abstract/id.rb)

## Verify the observable behavior

- Check row counts before and after anonymous bootstrap, failure, and a request
  with a stale cookie. Verify successful sign-in rotates the session, logout
  revokes it, and invalid CSRF leaves the authenticated session intact.
- For public sign-in routes, check abuse controls at the deployment boundary.
  A per-process limiter applies independently to each worker. For persistent
  sessions, verify how abandoned rows expire when the client never comes back.
- Check that routes, the browser client, and the API contract agree on signed-out
  responses and failure handling. Separate an implemented API denial from any
  outstanding browser recovery flow or provider logout requirement.

[Rails session stores](https://guides.rubyonrails.org/action_controller_overview.html#session-stores) · [Rails session security](https://guides.rubyonrails.org/security.html#sessions) · [Auth0 Rails example](https://developer.auth0.com/resources/guides/web-app/rails/basic-authentication)
