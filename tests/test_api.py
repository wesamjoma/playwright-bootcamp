from playwright.sync_api import Playwright , page 

def test_get_request(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://httpbin.org")
    response = api.get("/get")
    assert response.status == 200
    
    data = response.json()

    assert data ["url"] == "https://httpbin.org/get"

def test_post_request  (playwright: Playwright):
    api = playwright.request.new_context(base_url="https://httpbin.org")
    response = api.post("/post" , data= {
        "name": "wesam",
        "role": "QA Engineer"
    })
    
    assert response.status == 200 

    data = response.json()
    assert data ["json"]["name"] == "wesam"
    assert data ["json"]["role"] == "QA Engineer"

def test_put_request(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://httpbin.org")
    response = api.put("/put", data ={
        "name": "ahmed",
        "role": "doctor"
            
    })

    assert response.status == 200

    data = response.json()
    assert data ["json"]["name"] == "ahmed"
    assert data ["json"]["role"] == "doctor"

def test_delete_request(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://httpbin.org")

    response = api.delete('/delete')
    assert response.status == 200


def test_request_with_headers(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://httpbin.org")
    
    response = api.get("/headers", headers={
        "Authorization": "Bearer my-fake-token-123",
        "X-Custom-Header": "qa-test-run"
    })
    
    assert response.status == 200
    
    data = response.json()
    #print(data)

    
    # httpbin /headers echoes back the headers we sent
    assert data["headers"]["Authorization"] == "Bearer my-fake-token-123"
    assert data["headers"]["X-Custom-Header"] == "qa-test-run"
    
def test_request_with_params(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://httpbin.org")
    
    response = api.get("/get", params={
        "role": "admin",
        "active": "true"
    })
    
    assert response.status == 200
    
    data = response.json()
    
    # httpbin echoes the params back as "args"
    assert data["args"]["role"] == "admin"
    assert data["args"]["active"] == "true"

    page.route("**/*.jpg", lambda route: route.abort())
    
    api.dispose()



