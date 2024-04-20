from selene import browser
import pytest


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 1024),(480, 800), (540, 960)])
def browser_management(request):
    width, height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height
    if width > height:
        yield 'desktop'
    else:
        yield 'mobile'
    browser.quit()


@pytest.fixture(scope='function', params=[(480, 800), (540, 960)])
def browser_mobile(request):
    width, height = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(scope='function', params=[(1920, 1080), (1280, 1024)])
def browser_desktop(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()
