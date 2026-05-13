import re 
from playwright.sync_api import Page, expect 
from pages.login_page import LoginPage
from pages.product_page import ProductsPage 

def test_purchase_flow(page: Page):
    # Login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    # Add product to cart
    products_page = ProductsPage(page)
    products_page.add_product_to_cart("Sauce Labs Backpack")
    # Go to cart
    products_page.go_to_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
