# Safi Farm

[![CI](https://github.com/ZuriJabari/farm/actions/workflows/ci.yml/badge.svg)](https://github.com/ZuriJabari/farm/actions/workflows/ci.yml)

A modern farm management system designed for efficient agricultural operations.

## Project Status
- ✅ CI/CD Setup
- ✅ Branch Protection
- ✅ Code Quality Checks
- ✅ Security Scanning
- ✅ GPG Signing
- 🚧 Initial Development

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ZuriJabari/farm.git
   cd farm
   ```

2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

3. Set up pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Development

### Branch Structure
- `main`: Production-ready code
- `develop`: Main development branch
- Feature branches: `feature/*`
- Bug fixes: `fix/*`
- Hotfixes: `hotfix/*`
- Releases: `release/*`

### Commit Convention
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test updates
- `chore`: Maintenance tasks

### Security
- All commits must be signed with GPG
- Branch protection rules are enforced
- Status checks must pass before merging
- Linear history is required

### Pull Request Guidelines
- Changes should be made through pull requests
- Commit messages must follow conventional commits format
- Branch must be up to date before merging
- All commits must be signed with GPG
- All status checks must pass