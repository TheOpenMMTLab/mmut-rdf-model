# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [0.0.3] - 2026-04-17
### Added
- SHACL shapes are now included in the package as `py_mmut_rdf/mmut-shapes.ttl`.
- Added SHACL validation tests (positive and negative), including TTL fixture-based tests.
- Added Python usage example for SHACL validation to the README.

### Changed
- Package versioning is now derived automatically from Git tags via Poetry dynamic versioning.
- GitHub Actions release workflow now fetches full Git history/tags and supports publish on `v*` tag pushes.

## [0.0.1] - 2025-07-22
### Added
- first experimental draw