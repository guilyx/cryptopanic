# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

---

## [0.1.0] - 2026-01-08

### Added
- Initial release
- `CryptoPanicClient` class for API interactions
- Support for `/posts/` endpoint with all filtering options
- Support for `/portfolio/` endpoint
- Comprehensive exception handling:
  - `CryptoPanicAPIError` (base exception)
  - `CryptoPanicAuthenticationError` (401)
  - `CryptoPanicForbiddenError` (403)
  - `CryptoPanicRateLimitError` (429)
  - `CryptoPanicServerError` (500)
- Pydantic models for all API responses:
  - `Post`, `Instrument`, `Source`, `Votes`, `Content`
  - `PostsResponse`, `PortfolioResponse`
- Full type hints throughout the codebase
- Comprehensive test suite with pytest (89% coverage)
- CI/CD workflows with GitHub Actions
- Pre-commit hooks for code quality
- PyPI publishing workflow with automated release process
- PyPI trusted publishing support with environment protection
- Integration tests with environment variable support
- Codecov integration for coverage reporting
- Documentation with examples

### Changed
- Updated models to handle optional API response fields
- Consolidated publishing documentation into README
- Improved CHANGELOG structure following Keep a Changelog format

### Fixed
- Fixed Pydantic validation errors for optional fields (source, url, description)
- Fixed datetime import in client for runtime usage
- Fixed type checking configuration for Python 3.10+

[Unreleased]: https://github.com/guilyx/cryptopanic/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/guilyx/cryptopanic/releases/tag/v0.1.0
