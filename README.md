# Selenium-Framework
# Test Automation Framework using Python & Selenium.

## 1. Setup Instructions

### Prerequisites:
- Python 3.12+
- Git

### Steps to Install:
# Install dependencies
pip install selenium

## 2. Running Tests Locally

### Run UI Tests:
pytest tests/ui/

### Run API Tests:
pytest tests/api/

### View Test Results:
- Screenshots are saved in the `screenshots/` folder.
- Videos are saved in the 'videos/' folder.
- Test reports are available in the `reports/` folder.

## 3. API Testing Setup & Example

The framework includes API testing using the `requests` library. Example test:

import requests

def test_api_response():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200, "API response failed"
    print(response.json())

## 4. Generating Reports (HTML & XML)

pytest tests/ --html=reports/report.html --junitxml=reports/output.xml

## 5. CI/CD Integration (GitHub Actions)

A GitHub Actions pipeline (`ci_cd_pipeline.yml`) is included. It runs tests on every push and PR to `main`.

### CI/CD Workflow Steps:
1. Clone repository/Checkout code
2. Set up Python and install dependencies
3. Run UI and API tests using `pytest`
4. Upload test results as artifacts

To trigger the pipeline, push changes to the `main` branch or create a pull request.
