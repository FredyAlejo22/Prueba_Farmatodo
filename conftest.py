
from playwright.sync_api import sync_playwright
import pytest

from pages.wordcounter_page import WordCounterPage


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Ejecutar pruebas mostrando el navegador"
    )


@pytest.fixture
def browser_page(request):
    headed = request.config.getoption("--headed")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not headed)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900}
        )
        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.fixture
def wordcounter(browser_page):
    page_object = WordCounterPage(browser_page)
    page_object.open()
    return page_object
