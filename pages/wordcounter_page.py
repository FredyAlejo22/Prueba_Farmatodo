import re
from pages.base_page import BasePage


class WordCounterPage(BasePage):
    URL = "https://wordcounter.net/"
    TXT_EDITOR = "textarea"

    def open(self):
        self.open_url(self.URL)
        self._page.locator(self.TXT_EDITOR).first.wait_for(state="visible", timeout=15000)

    def escribir_texto(self, texto):
        self._page.locator(self.TXT_EDITOR).first.fill(texto)
        self._page.wait_for_timeout(500)

    def _texto_visible(self):
        return self._page.locator("body").inner_text()

    def obtener_cantidad_palabras(self):
        match = re.search(r"(\d+)\s+words?\b", self._texto_visible(), re.IGNORECASE)
        if not match:
            raise AssertionError("No se encontró el contador de palabras.")
        return int(match.group(1))

    def obtener_cantidad_caracteres(self):
        texto = self._texto_visible()
        match = re.search(r"(\d+)\s+characters?\b", texto, re.IGNORECASE)
        if not match:
            raise AssertionError("No se encontró el contador de caracteres.")
        return int(match.group(1))

    def obtener_keyword_density(self):

        acordeon = self._page.locator(
            "a.accordion-toggle[data-target='#kwd-accordion']"
        )

        acordeon.scroll_into_view_if_needed()

        if acordeon.get_attribute("aria-expanded") != "true":
            acordeon.click()

        contenedor = self._page.locator("#kwd-accordion-data")

        # Esperar a que existan los resultados
        self._page.wait_for_function("""
            () => {
                const panel = document.querySelector('#kwd-accordion-data');
                return panel &&
                    panel.querySelectorAll('span.word').length > 0;
            }
        """, timeout=15000)

        # Extraer directamente el contenido del HTML
        filas = contenedor.locator("a.list-group-item:has(span.word)")

        elementos = filas.evaluate_all("""
            filas => filas.map(fila => ({
                palabra: fila.querySelector('span.word')?.textContent?.trim(),
                frecuencia: fila.querySelector('span.badge')?.textContent?.trim()
            }))
        """)

        resultado = {}

        for elemento in elementos:
            palabra = elemento["palabra"] or ""
            frecuencia = elemento["frecuencia"] or ""

            coincidencia = re.search(r"(\d+)", frecuencia)

            if palabra and coincidencia:
                resultado[palabra.lower()] = int(coincidencia.group(1))

        print("Keyword Density:", resultado)

        if not resultado:
            raise AssertionError(
                "No se pudieron extraer los resultados de Keyword Density."
            )

        return resultado

    def obtener_tres_keywords_mas_repetidas(self):
        datos = self.obtener_keyword_density()

        return sorted(
            datos.items(),
            key=lambda item: (-item[1], item[0])
        )[:3]
