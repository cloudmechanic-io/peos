# BMAD adapter: design

- Quick: use the technical-analysis portion of `bmad-spec`; keep technical notes with the requirement unless escalation criteria appear.
- Feature: use `bmad-spec` for repository-grounded design, then involve the architect and affected discipline roles.
- Strategic or architecture-significant: use `bmad-architecture` and the architect role; create ADRs only under PEOS ADR criteria.

Regardless of BMAD output, normalize to `contracts/change-spec.md`. Explicitly write product and technical current/target state, affected contracts, and ADDED/MODIFIED/REMOVED/RENAMED behavior. Add migration, compatibility, rollout, rollback, observability, security, failure behavior, and validation. Do not design from the requirement alone: inspect the relevant repositories.

If BMAD is unavailable, report the missing provider and installation command without changing the public capability.
