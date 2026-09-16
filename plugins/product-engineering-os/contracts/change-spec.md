# Technical change contract v1

The normalized technical artifact is `peos/changes/<change_id>/change-spec.md`.

It contains:

1. lifecycle frontmatter;
2. linked approved product requirement and repository evidence;
3. technical current state and target state;
4. affected repositories, components, contracts, data, infrastructure, and owners;
5. behavioral delta sections: `ADDED`, `MODIFIED`, `REMOVED`, and `RENAMED`, using `None` explicitly where empty;
6. alternatives and tradeoffs;
7. compatibility, migration, rollout, rollback, observability, security/privacy, and failure behavior;
8. validation strategy and traceability to acceptance criteria;
9. ADR decision with reason and link when required;
10. unresolved decisions and implementation constraints.

For quick work, this may be a short “Technical notes” section inside the product requirement instead of a separate file. It must still describe affected code and validation.
