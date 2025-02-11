from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="function", autouse=True)
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_login_valid_user(setup):
    page = setup
    page.goto("https://example-ecommerce.com")
    page.fill("input[name='username']", "testuser")
    page.fill("input[name='password']", "password123")
    page.click("button[type='submit']")
    assert page.locator("text='Welcome, testuser'").is_visible()
