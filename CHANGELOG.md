# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Features and changes that will be included in the next release

### Changed
- Changes to existing functionality

### Fixed
- Bug fixes

### Security
- Security improvements

---

## [0.1.0] - 2024-01-XX

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
- Comprehensive test suite with pytest
- CI/CD workflows with GitHub Actions
- Pre-commit hooks for code quality
- Documentation with examples

[Unreleased]: https://github.com/guilyx/cryptopanic/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/guilyx/cryptopanic/releases/tag/v0.1.0
