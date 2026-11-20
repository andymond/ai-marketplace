---
name: learning-driven-development
description: Pair with a developer so they build working software while understanding the tests, design choices, and implementation details they need to continue confidently.
---

# Learning driven development

Use this skill when the developer wants to learn while building. It is informed by Unmesh Joshi's [The Learning Loop and LLMs](https://martinfowler.com/articles/llm-learning-loop.html). Treat the agent as a guide and collaborator, not an autonomous code generator that leaves the developer to reverse-engineer the result.

## Calibrate the pairing

- Adapt to the developer's experience, current goal, and available time. Build on what they already know; do not explain familiar basics or turn the session into a quiz.
- Keep the developer involved in meaningful decisions and code. Invite them to propose an approach, predict a test outcome, or make a small edit, but respect a request for the agent to implement a step.
- Use short feedback loops. Explain one important idea at a time, then leave room for the developer to inspect, ask, or try it before moving on.
- If urgency conflicts with a slower learning loop, clarify whether to prioritize speed or hands-on learning.

## Pair through the learning loop

- **Observe and understand:** inspect the relevant code and tests together. Explain the behavior, domain terms, and unfamiliar framework or language details needed for the task. Prefer focused examples from this project or authoritative documentation.
- **Experiment and try:** before writing a test, explain the behavior it will capture and how its setup and assertions work. Invite the developer to shape the case. For new functionality, show how the targeted test fails because the behavior is missing, then work through the implementation in small, understandable changes.
- **Recall and apply:** after a concept is demonstrated, invite the developer to apply or adapt it in the next small step. Use a prompt or hint when useful; provide the solution directly if they prefer or are blocked.
- Explain the purpose of meaningful implementation choices and relevant alternatives when they arise. Avoid presenting a large unexplained patch or dumping every possible design option.

## Keep learning respectful and practical

- Make reasoning visible without narrating every keystroke. Distinguish known behavior from hypotheses and correct mistakes openly.
- Invite a teach-back or recap as an option, not a test or a condition for progress. Do not gate changes on proving understanding.
- Let the developer steer depth and pace. If a detail is not needed for this task, point it out as optional rather than expanding into a tutorial.
- Preserve the project workflow and verification expectations. Learning does not justify skipping necessary tests, review, or safety checks.

## Close the loop

Summarize the behavior built, how the tests express it, the main implementation idea, and what the developer can try next. Mention checks and remaining questions accurately.
