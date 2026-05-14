from playwright.sync_api import Page, expect 


def test_fake_api_response(page: Page):
    page.route("**/api/users/2", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body='{"id": 999, "name": "FAKE USER", "email": "fake@test.com"}'
    ))
    
    page.goto("https://reqres.in/api/users/2")

def test_fake_500_error (page: Page):
   
     
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    page.route("https://www.saucedemo.com/", lambda route: route.fulfill(
        status=500, 
        body= "Server Error"
    ))

    page.goto("https://www.saucedemo.com/cart.html")

    
