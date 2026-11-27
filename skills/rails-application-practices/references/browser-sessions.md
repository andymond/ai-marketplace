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
