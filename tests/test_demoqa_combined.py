from playwright.sync_api import Page, expect , Playwright


def test_login_via_api_then_browse(page: Page, playwright: Playwright):
    # API LOGIN
    api = playwright.request.new_context(base_url="https://demoqa.com")
    
    login_response = api.post("/Account/v1/GenerateToken", data={
        "userName": "wesamjoma",
        "password": "test_@1234"
    })
    
    assert login_response.status == 200
    
    # SAVE THE TOKEN
    data = login_response.json()
    token = data["token"]
    user_id = data["userId"] if "userId" in data else None
    print(data)
    print(f"Got token: {token[:30]}...")  # show first 30 chars for debugging