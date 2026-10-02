# References

## CODATA Minority Report

This adaptation builds on the CODATA Minority Report, which is **not** vendored into this repository.

- Repository: https://github.com/codata/the-minority-report
- Pinned commit: `a7cb9cbf90cffb186c69699b5a188f970d22e5b9` (`a7cb9cb`)

Every candidate package records that commit in `provenance.upstream`, so any output can be traced to
the upstream version it derives from without a copy of upstream living here.

To read it locally:

```
git clone https://github.com/codata/the-minority-report references/the-minority-report
cd references/the-minority-report && git checkout a7cb9cb
```

That path is in `.gitignore`. It was tracked here until 2 October 2026; a verbatim copy of another
project's repository is not ours to redistribute, and in this case it also republished a credential
that appears in plain text in the upstream README.
