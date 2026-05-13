from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.cart_page import cart_page

def test_checkout(page: Page):
    #login 
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user","secret_sauce")    
    # add product to cart
    products_page = ProductsPage(page)          
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.go_to_cart()
    # go to checkout
    checkout = cart_page(page)
    checkout.go_to_checkout()
    
    # verify checkout page
    expect(page.get_by_text("Checkout: Your Information")).to_be_visible()
    