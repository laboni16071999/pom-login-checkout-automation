import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    browser_context = browser.new_context()
    page = browser_context.new_page()
    try:
        yield page
    except Exception:
        page.screenshot(path="checkout-failure.png", full_page=True)
        raise
    finally:
        browser_context.close()
        browser.close()
        playwright.stop()
