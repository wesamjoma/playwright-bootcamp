from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_open_login_page(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    expect(page).to_have_url("https://www.saucedemo.com/")

def test_login_success(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_locked_out_user(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.error_message).to_contain_text("locked out")
    

def test_login_wrong_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()
