# BMAD adapter: shape

Use BMAD as an elicitation engine, not as the public artifact format.

## Routing

- Quick: use `bmad-spec` questioning only as needed; normalize directly to concise acceptance criteria.
- Feature: use `bmad-brainstorming` when the problem is unclear, then `bmad-product-brief` when discovery needs a bridge, and `bmad-prd` for the requirement.
- Strategic: use `bmad-brainstorming`, research when authorized, optionally `bmad-prfaq`, then `bmad-product-brief` and `bmad-prd`.

Apply the product role contract. Inspect existing product behavior before writing current state. Normalize only decision-relevant BMAD output to `contracts/product-requirement.md`; do not copy a second competing document set into the change folder.

If the BMAD skills are unavailable, keep the PEOS capability name and stop with exact BMAD installation guidance. Do not silently substitute an invented methodology unless the client explicitly selects a different adapter.
