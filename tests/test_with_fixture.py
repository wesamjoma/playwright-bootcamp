from playwright.sync_api import Page, expect
from pages.product_page import ProductsPage


def test_add_to_cart_with_fixture(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    
    expect(products_page.cart_badge).to_have_text("1")


def test_go_to_cart_with_fixture(products_page):
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.go_to_cart()


def test_cart_badge_starts_empty(products_page):
    expect(products_page.cart_badge).not_to_be_visible()
