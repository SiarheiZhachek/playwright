from playwright.sync_api import Page


class BasePageLocators:

    logo = 'a.navbar-brand'
    home_link = ('link', 'Home')
    contact_link = ('link', 'Contact')
    contact_field = '//div[@id="exampleModal"]/div/div'
    about_us_link = '//a[@data-target="#videoModal"]'
    about_us_field = '#videoModal'
    cart_link = '#cartur'
    log_in_link = '#login2'
    sing_up_link = '#signin2'


    username_field_in_sing_up = '#sign-username'
    password_field_in_sing_up = '#sign-password'

