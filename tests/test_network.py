from playwright.sync_api import Page , expect 
import time 

# def slow_down(route):
#      time.sleep(2)
#      route.continue_()

# def test_slow_network(page: Page):
#     page.route("**/*", slow_down)
    
#     page.goto("https://www.saucedemo.com/")
    
#     expect(page.get_by_role("textbox", name="Username")).to_be_visible()

# def test_block_all_images (page: Page):
#     page.route("**/*.{jpg,png,gif,svg}", lambda route: route.abort())

#     page.goto("https://www.saucedemo.com/")
#     page.get_by_role("textbox", name="Username").fill("standard_user")
#     page.locator("#password").fill("secret_sauce")
#     page.get_by_role("button", name="Login").click() 


    
def test_block_analytics_for_speed(page: Page):
        page.route("**/*.css", lambda route: route.abort())
    
        page.goto("https://www.saucedemo.com/")
        page.get_by_role("textbox", name="Username").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
def test_no_data_leaks_to_third_party(page: Page):
    captured_urls = []
    page.on("request", lambda request: captured_urls.append(request.url))
    
def test_no_data_leaks_to_third_party(page: Page):
    captured_urls = []
    
    page.on("request", lambda request: captured_urls.append(request.url))
    
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # Print all URLs for inspection
    for url in captured_urls:
        print(f"Captured URL: {url}")
    
    # Assert no requests went to known tracking domains
    for url in captured_urls:
        assert "google-analytics.com" not in url
        assert "facebook.com" not in url
        assert "doubleclick.net" not in url

        # How many requests went out total?
        print(f"Total requests: {len(captured_urls)}")

        # How many were for the saucedemo domain?
        saucedemo_requests = [u for u in captured_urls if "saucedemo" in u]
        print(f"Saucedemo requests: {len(saucedemo_requests)}")

        # How many were image requests?
        image_requests = [u for u in captured_urls if ".jpg" in u or ".png" in u]
        print(f"Image requests: {len(image_requests)}")

    

