from playwright.sync_api import Page ,expect 
 

class CartPage:    
    def __init__(self,page:Page):
        self.page = page
        self.product_name = page.locator(".inventory_item_name")

    def remove_product_from_cart(self, product_name: str):
        self.page.locator(".cart_item").filter(has_text=product_name).get_by_role("button", name="Remove").click()
    
    def go_to_checkout(self):
        self.page.get_by_role("button", name="Checkout").click()

    def verify_empty_cart(self):
      expect(self.page.locator("//span[@data-test='shopping-cart-badge']")).to_have_count(0)


    def verify_cart_count(self, expected_count: int):
        expect(self.page.locator("//span[@data-test='shopping-cart-badge']")).to_have_text(str(expected_count))
