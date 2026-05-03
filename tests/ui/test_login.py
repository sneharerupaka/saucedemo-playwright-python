import pytest
from pages.login_page import LoginPage

class TestLogin:

    def test_valid_login(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")
        assert "inventory" in page.url

    def test_invalid_login(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("invalid_user", "wrong_password")
        assert "Epic sadface" in login.get_error_message()

    def test_empty_username(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("", "secret_sauce")
        assert "Username is required" in login.get_error_message()

    def test_empty_password(self, page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "")
        assert "Password is required" in login.get_error_message()