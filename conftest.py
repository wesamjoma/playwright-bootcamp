import pytest 
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_page import ProductsPage



@pytest.fixture
def logged_in_page(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    return page


@pytest.fixture
def products_page(logged_in_page: Page):
    return ProductsPage(logged_in_page)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": "auth.json"
    }
