from playwright.sync_api import Page


class ProductsPage:

    def __init__(self,page:Page):
        self.page = page
        self.cart_link = page.locator("//a [@data-test='shopping-cart-link']")
        self.cart_badge = page.locator("//span [@data-test='shopping-cart-badge']") 
        self.page_title = page.get_by_text("Products")

    def add_product_to_cart(self, product_name: str):
        self.page.locator(".inventory_item").filter(has_text=product_name).get_by_role("button", name="Add to cart").click()
    
    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()

    
