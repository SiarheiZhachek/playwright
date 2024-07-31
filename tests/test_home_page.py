from playwright.sync_api import Page, Dialog
from pages.home_page import HomePage
from pages.cart_page import CartPage
from time import sleep


def test_open_page(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.title_page_is('STORE')
    home_page.url_page_is_(home_page.url)


def test_logo_site_visible(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.logo_site_visible()


def test_home_link_is_visible(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.home_link_visible()


def test_home_link_text(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.home_link_text_is_('Home (current)')


def test_contact_link_is_visible_and_check_text(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.contact_linc_visible()
    home_page.contact_lint_text_is_('Contact')


def test_contact_link_click(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.contact_link_click()
    home_page.contact_field_is_visible()


def test_about_us_link_is_visible_and_check_text(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.about_us_link_visible()
    home_page.about_us_link_text_is_('About us')


def test_about_us_link_click(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.about_us_link_click()
    home_page.about_us_link_visible()


def cart_link_is_visible_and_check_text(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.cart_link_is_visible()
    home_page.cart_link_text_is_('Cart')


def test_cart_link_click(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.cart_link_click()
    cart_page = CartPage(page)
    cart_page.url_page_is_(cart_page.url)
    cart_page.check_cart_page_title_is_('STORE')


def test_log_in_link_is_visible_ahd_check_text(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.log_in_link_is_visible()
    home_page.log_in_link_text_is_('Log in')


def test_sing_up_link_is_visible_and_check_text(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.sing_up_link_visible()
    home_page.sing_up_link_text_is_('Sign up')


def test_categories_link_is_visible_and_check_text(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.categories_link_is_visible()
    home_page.categories_link_text_is('CATEGORIES')


def test_phones_link_is_visible_and_check_text(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.phones_link_is_visible()
    home_page.phones_link_text_is_('Phones')


def test_samsung_galaxy_s6_is_visible_and_check_text(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.samsung_galaxy_s6_link_is_visible()
    home_page.samsung_galaxy_s6_text_is_('Samsung galaxy s6')


def test_test_samsung_galaxy_s6_click(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.samsung_galaxy_s6_click()
    home_page.url_page_is_('https://www.demoblaze.com/prod.html?idp_=1')


def test_add_to_cart(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.samsung_galaxy_s6_click()
    home_page.add_to_cart_click()
    sleep(5)






def test_enter_username(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.sing_up_link_click()
    home_page.enter_username('user123')
    sleep(3)


def test_attribute(page: Page):
    page.goto('https://www.lambdatest.com/selenium-playground/javascript-alert-box-demo')

    # def accept_alert(alert: Dialog):
    #     print(alert.message)
    #     alert.accept()
    #
    # page.on('dialog', accept_alert)
    page.on("dialog", lambda dialog: dialog.accept())
    button = page.get_by_role('button', name='Click Me').first
    button.click()
    sleep(5)



