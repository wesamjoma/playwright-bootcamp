from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Login normally
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # Save the session to a file
    context.storage_state(path="auth.json")
    
    browser.close()