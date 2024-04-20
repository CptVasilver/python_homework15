import pytest
from selene import browser, be

only_desktop = pytest.mark.parametrize("browser_management", [(1920, 1080)], indirect=True)
only_mobile = pytest.mark.parametrize("browser_management", [(480, 800)], indirect=True)

@only_desktop
def test_github_desktop_param(browser_management):
    browser.open('/')
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("#login_field").should(be.visible)

@only_mobile
def test_github_mobile_param(browser_management):
    browser.open('/')
    browser.element(".HeaderMenu-toggle-bar").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("#login_field").should(be.visible)
