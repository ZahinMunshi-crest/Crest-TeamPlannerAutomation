from playwright.sync_api import expect


def test_valid_user_credentials(login_page):
    login_page.open()
    login_page.login("zahin.munshi", "12345")
    expect(login_page.timesheet_header).to_be_visible()
    assert login_page.timesheet_header.inner_text() == "My Timesheet"


def test_invalid_user_credentials(login_page):
    login_page.open()
    login_page.login("zahin", "12345")
    expect(login_page.timesheet_header).not_to_be_visible()


def test_username_password_required(login_page):
    login_page.open()
    login_page.login("", "")
    expect(login_page.login_error_message).to_be_visible()
    assert login_page.login_error_message.inner_text() == "Username is required."
    login_page.login("test", "")
    assert login_page.login_error_message.inner_text() == "Password is required."
