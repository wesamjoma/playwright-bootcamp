from playwright.sync_api import Playwright, Page , expect 

def test_save_and_reuse_value (page: Page, playwright: Playwright):

    api = playwright.request.new_context(base_url="https://httpbin.org")

    #step1: first request get your IP 

    first_response = api.get("/get")
    my_ip = first_response.json()["origin"]

    print(f"My IP is:{my_ip}")

    #step2: use the IP in the second request to validate it 

    second_response = api.get("/headers", headers={
        "X-My-IP": my_ip 
    })

    received_ip = second_response.json()["headers"]["X-My-Ip"]

    print(f"Server received: {received_ip}")

    assert received_ip == my_ip

    api.dispose()