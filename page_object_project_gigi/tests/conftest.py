import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture
def setup_jw_org():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.jw.org/en/")
        remove_cookies_banner(page)

        yield page
        page.close()
        browser.close()

def remove_cookies_banner(page):
    accept_cookies_button = page.locator("[class='lnc-button lnc-button--primary lnc-acceptCookiesButton']")
    accept_cookies_button.click()