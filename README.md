# 🚀 Selenium Python + Pytest-BDD + Allure Report

Automation testing project menggunakan **Selenium**, **Pytest-BDD**, dan integrasi dengan **Allure Report** untuk reporting yang interaktif.

---

## 📂 Project Structure

├── features/ # File feature BDD (Gherkin)
│ ├── companies.feature
│ └── login.feature
│
├── steps/ # Step definitions
│ ├── companies.py
│ └── login.py
│
├── helpers/ # Helper functions (click, wait, dropdown, etc.)
│ ├── clickElement.py
│ ├── select_dropdown.py
│ └── waitForElement.py
│
├── xpaths/ # Locator definitions
│ ├── init.py
│ └── xpath_web.py
│
├── conftest.py # Global fixtures (browser setup, hooks, etc.)
├── test_runner.py # Optional test runner script
└── README.md # Project documentation

yaml
Copy code

---

## 🛠️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/delkodeeel/selenium-python-pytest.git
cd selenium-python-pytest
**### 2. Install Dependencies**
bash
Copy code
pip install selenium pytest pytest-bdd allure-pytest
**### 3. ▶️ Running Tests**
Run all tests
bash
Copy code
pytest -v
Run specific test file
bash
Copy code
pytest steps/login.py
Run tests with Allure results
bash
Copy code
pytest steps/login.py --alluredir=reports/allure-results
**### 5. 📊 Generate Allure Report**
bash
Copy code
allure serve reports/allure-results
