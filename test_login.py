from playwright.sync_api import Playwright, sync_playwright, expect

baseUrl = "http://localhost:3000/"

def test_SuccessLogin(page):
    page.goto(baseUrl)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("aqa")
    page.get_by_placeholder("Username").press("Enter")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("AQA123")
    page.get_by_role("button", name="Login").click()

    expect(page, "Unsuccessful login with correct username and password").to_have_url(baseUrl + "welcome")

def test_SuccessLogout(page):
    page.goto(baseUrl)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("test")
    page.get_by_placeholder("Username").press("Enter")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("test123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Logout").click()

    expect(page, "Unsuccessful logout").to_have_url(baseUrl)

def test_EmptyForm(page):
    page.goto(baseUrl)
    page.get_by_role("button", name="Login").click()
    expect(page, "Successful login with empty fields username+password").to_have_url(baseUrl)

def test_IncorrectUsername(page):
    page.goto(baseUrl)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("admin1")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin")
    page.get_by_role("button", name="Login").click()

    (expect(page.get_by_text("User not found"), "Success login with incorrect username")\
        .to_have_text("User not found"))

def test_IncorrectPassword(page):
    page.goto(baseUrl)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin1")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Incorrect password"), "Success login with incorrect password")\
        .to_have_text("Incorrect password")

def test_EmptyPassword(page):
    page.goto(baseUrl)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Incorrect password"), "Success login with empty password")\
        .to_have_text("Incorrect password")

def test_EmptyUsername(page):
    page.goto(baseUrl)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("admin")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("User not found"), "Success login with empty username")\
        .to_have_text("User not found")