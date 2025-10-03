# 🚀 Selenium Python + Pytest-BDD + Allure Report

Automation testing project menggunakan **Selenium**, **Pytest-BDD**, dan integrasi dengan **Allure Report** untuk reporting yang interaktif.

---

## 📂 Project Structure

<img width="500" height="561" alt="Screenshot 2025-10-03 at 10 29 28" src="https://github.com/user-attachments/assets/7e703951-e95d-4fa8-8150-28f1b64645bd" />


---

## 🛠️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/delkodeeel/selenium-python-pytest.git
cd selenium-python-pytest
### 1. Clone Repository
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
