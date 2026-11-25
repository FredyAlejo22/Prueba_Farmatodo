import allure

class BasePage:
    def __init__(self, page):
        self._page = page

    def open_url(self, url):
        self._page.goto(url, wait_until="domcontentloaded")

    def tomar_captura(self, nombre):
        captura = self._page.screenshot(full_page=True)

        allure.attach(
            captura,
            name=nombre,
            attachment_type=allure.attachment_type.PNG
        )
