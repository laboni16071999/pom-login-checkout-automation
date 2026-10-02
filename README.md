# POM UI Automation: Login and Checkout

A compact Python, Playwright, and pytest project that automates one SauceDemo purchase flow using the Page Object Model.

## Flow

Log in → add a backpack → verify the cart → enter checkout details → finish the order.

## Run locally (Windows / PowerShell)

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v
```

The test runs headlessly. If it fails, it saves `checkout-failure.png` in the project root.

## CI

GitHub Actions runs the test on every push and pull request. It installs Python dependencies and Chromium, runs pytest, and uploads the JUnit result (plus a failure screenshot if one was created).

To activate CI, push this project to a GitHub repository. No production deployment is needed for this test-framework project; the workflow continuously validates the checkout flow.
