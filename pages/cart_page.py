from pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):

    url = 'https://www.demoblaze.com/cart.html'

    def check_cart_page_title_is_(self, title):
        expect(self.page.title()).to_have_title(title)
