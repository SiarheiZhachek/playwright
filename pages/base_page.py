from playwright.sync_api import Page, expect, Dialog
from pages.locators.base_page_locators import BasePageLocators as loc


class BasePage:
    url = None

    def __init__(self, page: Page, alert: Dialog = None):
        self.alert = alert
        self.page = page

    def open(self):
        if self.url:
            self.page.goto(self.url)
        else:
            print('Not possible to open page without url')

    def alerta(self):
        print(self.alert.message)
        self.alert.accept()



    def alert_text_is(self, text):
        expect(self.alert.message).to_have_text(text)

    def title_page_is(self, title):
        expect(self.page).to_have_title(title)

    def url_page_is_(self, url_page):
        expect(self.page).to_have_url(url_page)

    def logo_site_visible(self):
        logo = self.page.locator(loc.logo)
        expect(logo).to_be_visible()

    def home_link(self):
        link = self.page.get_by_role(loc.home_link[0], name=loc.home_link[1])
        return link

    def home_link_visible(self):
        expect(self.home_link()).to_be_visible()

    def home_link_text_is_(self, text):
        expect(self.home_link()).to_have_text(text)

    def home_link_click(self):
        self.home_link().click()

    def contact_link(self):
        link = self.page.get_by_role(loc.contact_link[0], name=loc.contact_link[1])
        return link

    def contact_linc_visible(self):
        expect(self.contact_link()).to_be_visible()

    def contact_lint_text_is_(self, text):
        expect(self.contact_link()).to_have_text(text)

    def contact_link_click(self):
        self.contact_link().click()

    def contact_field_is_visible(self):
        expect(self.page.locator(loc.contact_field)).to_be_visible()

    def about_us_link(self):
        link = self.page.locator(loc.about_us_link)
        return link

    def about_us_link_visible(self):
        expect(self.about_us_link()).to_be_visible()

    def about_us_link_text_is_(self, text):
        expect(self.about_us_link()).to_have_text(text)

    def about_us_link_click(self):
        return self.about_us_link().click()

    def abut_us_link_is_visible(self):
        expect(self.page.locator(loc.about_us_field).first.get_attribute('style')).to_have_text('display: block;')

    def cart_link(self):
        return self.page.locator(loc.cart_link)

    def cart_link_is_visible(self):
        expect(self.cart_link()).to_be_visible()

    def cart_link_text_is_(self, text):
        expect(self.cart_link()).to_have_text(text)

    def cart_link_click(self):
        self.cart_link().click()

    def log_in_link(self):
        return self.page.locator(loc.log_in_link)

    def log_in_link_is_visible(self):
        expect(self.log_in_link()).to_be_visible()

    def log_in_link_text_is_(self, text):
        expect(self.log_in_link()).to_have_text(text)

    def log_in_link_click(self):
        self.log_in_link().click()

    def sing_up_link(self):
        return self.page.locator(loc.sing_up_link)

    def sing_up_link_visible(self):
        expect(self.sing_up_link()).to_be_visible()

    def sing_up_link_text_is_(self, text):
        expect(self.sing_up_link()).to_have_text(text)

    def sing_up_link_click(self):
        self.sing_up_link().click()



    def enter_username(self, username):
        self.page.locator(loc.username_field_in_sing_up).fill(username)


