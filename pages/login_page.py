from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login'not in current url"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOG_USERNAME), "Login username form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOG_PASS), "Login password form is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Reg email form is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "Reg pass1 form is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "Reg pass2 form is not presented"
        assert True