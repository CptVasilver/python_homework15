import pytest
from selene import browser, be


def test_github_desktop_skip(browser_management):
    if browser_management == 'mobile':
        pytest.skip(reason='Wrong screen resolution')

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('#login_field').should(be.visible)


def test_github_mobile_skip(browser_management):
    if browser_management == 'desktop':
        pytest.skip(reason='Wrong screen resolution')

    browser.open('/')
    browser.element(".HeaderMenu-toggle-bar").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("#login_field").should(be.visible)