from pages.base_page import BasePage
from pages.locators.home_page_locators import HomePageLocators as loc
from playwright.sync_api import expect


class HomePage(BasePage):

    url = 'https://www.demoblaze.com/index.html'

    def categories_link(self):
        return self.page.locator(loc.categories_link)

    def categories_link_is_visible(self):
        expect(self.categories_link()).to_be_visible()

    def categories_link_text_is(self, text):
        expect(self.categories_link()).to_have_text(text)

    def categories_link_click(self):
        self.categories_link().click()

    def phones_link(self):
        return self.page.locator(loc.phones_link)

    def phones_link_is_visible(self):
        expect(self.phones_link()).to_be_visible()

    def phones_link_text_is_(self, text):
        expect(self.phones_link()).to_have_text(text)

    def phones_link_click(self):
        self.phones_link().click()

    def laptops_link(self):
        return self.page.locator(loc.laptops_link)

    def laptops_link_is_visible(self):
        expect(self.laptops_link()).to_be_visible()

    def laptops_link_text_is_(self, text):
        expect(self.laptops_link()).to_have_text(text)

    def laptops_link_click(self):
        self.laptops_link().click()

    def monitors_link(self):
        return self.page.locator(loc.monitors_link)

    def monitors_link_is_visible(self):
        expect(self.monitors_link()).to_be_visible()

    def monitors_link_text_is_(self, text):
        expect(self.monitors_link()).to_have_text(text)

    def monitors_link_click(self):
        self.monitors_link().click()

    def samsung_galaxy_s6(self):
         return self.page.get_by_role(
             loc.samsung_galaxy_s6[0], name=loc.samsung_galaxy_s6[1]
         )

    def samsung_galaxy_s6_link_is_visible(self):
        expect(self.samsung_galaxy_s6()).to_be_visible()

    def samsung_galaxy_s6_text_is_(self, text):
        expect(self.samsung_galaxy_s6()).to_have_text(text)

    def samsung_galaxy_s6_click(self):
        self.samsung_galaxy_s6().click()

    def add_to_cart(self):
        return self.page.locator(loc.add_to_cart)

    def add_to_cart_click(self):
        self.add_to_cart().click()



