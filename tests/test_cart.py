from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.cart_page import CartPage

def test_cart_remove_product(page: Page):
    # Login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user","secret_sauce")

    # add product to cart 
    products_page = ProductsPage(page)
    products_page.add_product_to_cart("Sauce Labs Backpack")


    # add second product to cart 
    products_page = ProductsPage(page)
    products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    products_page.go_to_cart()

    #checkout badge totalnumber 
    

    # remove products from cart 

    remove_product = CartPage(page)

    remove_product.verify_cart_count(2)

    # verify product is removed from cart
    
    remove_product.remove_product_from_cart("Sauce Labs Backpack")
    remove_product.remove_product_from_cart("Sauce Labs Bolt T-Shirt")
    remove_product.verify_empty_cart()




