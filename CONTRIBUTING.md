# Contributing to cryptopanic

Thank you for your interest in contributing to cryptopanic! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/guilyx/cryptopanic.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Install in development mode: `make install-dev` or `pip install -e ".[dev]"`
5. Install pre-commit hooks: `pre-commit install`

## Development Setup

```bash
# Install dependencies
make install-dev

# Run tests
make test

# Run tests with coverage
make test-cov

# Format code
make format

# Run linters
make lint

# Type checking
make type-check
```

## Code Style

- We use [Black](https://black.readthedocs.io/) for code formatting (line length: 100)
- We use [Ruff](https://github.com/astral-sh/ruff) for linting
- We use [mypy](https://mypy.readthedocs.io/) for type checking
- All code must pass pre-commit hooks before committing

## Commit Messages

We follow the conventional commit format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat(client): add pagination helper method

Add a helper method to easily navigate through paginated results
from the API. This simplifies the common use case of fetching
all pages of results.

Closes #123
```

## Testing

- All new features must include tests
- Aim for high test coverage (maintain >90%)
- Run tests before submitting: `make test`
- Write both unit tests and integration tests where appropriate

### Environment Variables for Testing

Unit tests use mocked API responses and don't require a real API token. However, if you want to run integration tests that make real API calls, you'll need to set the `CRYPTOPANIC_AUTH_TOKEN` environment variable:

```bash
# Run integration tests locally
export CRYPTOPANIC_AUTH_TOKEN=your_token_here
pytest tests/test_integration.py
```

### GitHub Secrets Setup

For CI/CD, the repository uses GitHub Secrets to store sensitive tokens securely:

**Required Secrets:**

1. **CODECOV_TOKEN** (for coverage reporting):
   - Go to your repository settings
   - Navigate to **Settings → Secrets and variables → Actions**
   - Click **New repository secret**
   - Name: `CODECOV_TOKEN`
   - Value: Your Codecov token (get it from https://codecov.io)
   - Click **Add secret**

2. **CRYPTOPANIC_AUTH_TOKEN** (optional, for integration tests):
   - Go to your repository settings
   - Navigate to **Settings → Secrets and variables → Actions**
   - Click **New repository secret**
   - Name: `CRYPTOPANIC_AUTH_TOKEN`
   - Value: Your CryptoPanic API token
   - Click **Add secret**

The CI workflow will automatically use these secrets. Note that integration tests are excluded from the main CI workflow by default to avoid rate limiting, but can be run manually via the integration workflow.

## Pull Request Process

1. Ensure all tests pass: `make test`
2. Ensure code is formatted: `make format`
3. Ensure linters pass: `make lint`
4. Update documentation if needed
5. Update CHANGELOG.md with your changes
6. Submit a pull request with a clear description

## Reporting Issues

When reporting issues, please include:
- Python version
- Package version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages or stack traces

## Questions?

Feel free to open an issue for any questions or concerns!
