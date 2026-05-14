# Playwright E2E Testing Framework

End-to-end test automation framework built with **Python + Playwright**.

## Tech Stack
- Python 3.13
- Playwright
- pytest
- GitHub Actions (CI/CD)

## Project Structure
pages/          # Page Object Model classes
tests/          # Test files
conftest.py     # Shared fixtures
setup_auth.py   # Auth state setup

## Features
- Page Object Model (POM)
- API testing (GET, POST, PUT, DELETE)
- Network interception & mocking
- Auth state management
- CI/CD with GitHub Actions

## How to Run

```bash
# Install dependencies
pip install pytest-playwright
playwright install

# Generate auth state
python setup_auth.py

# Run all tests
pytest tests/ -v
```

## Test Results
Tests run automatically on every push via GitHub Actions.