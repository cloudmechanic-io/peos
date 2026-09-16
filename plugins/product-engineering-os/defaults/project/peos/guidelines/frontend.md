# Frontend guidelines

- Follow the repository’s established component, state, routing, styling, and test conventions before adding abstractions.
- Keep components cohesive: separate domain/data orchestration from reusable presentation when that boundary reduces coupling.
- Prefer explicit inputs, typed contracts, and derived state over duplicated or synchronized local state.
- Model loading, empty, error, partial, retry, offline, and permission states where relevant.
- Preserve keyboard access, focus behavior, semantic structure, readable contrast, and screen-reader labels.
- Avoid breaking navigation, deep links, analytics, localization, responsive layouts, and supported clients.
- Test observable user behavior; avoid tests coupled only to component internals.
- Consider bundle/runtime cost and avoid dependencies for functionality the existing stack already provides.
