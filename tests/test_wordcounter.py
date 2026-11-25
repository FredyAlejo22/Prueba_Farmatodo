import allure
import pytest

from data.test_data import (
    TEXTO_PRUEBA,
    PALABRAS_ESPERADAS,
    CARACTERES_ESPERADOS,
    TOP_3_KEYWORDS_ESPERADAS,
)


@pytest.mark.smoke
@allure.epic("Farmatodo - Prueba técnica QA")
@allure.feature("Suite automatizada WordCounter")
class TestWordCounter:

    @allure.story("Validar número de palabras")
    def test_cantidad_palabras(self, wordcounter):

        with allure.step("Ingresar texto de prueba"):
            wordcounter.escribir_texto(TEXTO_PRUEBA)
            wordcounter.tomar_captura("01 - Texto ingresado")
        with allure.step("Validar contador de palabras"):
            actual = wordcounter.obtener_cantidad_palabras()
            wordcounter.tomar_captura("02 - Contador de palabras")
            assert actual == PALABRAS_ESPERADAS, (
                f"Esperado: {PALABRAS_ESPERADAS}; obtenido: {actual}"
            )

    @allure.story("Validar número de caracteres")
    def test_cantidad_caracteres(self, wordcounter):
        with allure.step("Ingresar texto de prueba"):
            wordcounter.escribir_texto(TEXTO_PRUEBA)
            wordcounter.tomar_captura("01 - Texto ingresado")

        with allure.step("Validar contador de caracteres incluyendo espacios"):
            actual = wordcounter.obtener_cantidad_caracteres()
            wordcounter.tomar_captura("02 - Contador de caracteres")
            assert actual == CARACTERES_ESPERADOS, (
                f"Esperado: {CARACTERES_ESPERADOS}; obtenido: {actual}"
            )

    @allure.story("Validar las tres palabras más repetidas")
    def test_top_3_keyword_density(self, wordcounter):

        with allure.step("Ingresar texto de prueba"):
            wordcounter.escribir_texto(TEXTO_PRUEBA)
            wordcounter.tomar_captura("01 - Texto ingresado")

        with allure.step("Consultar las tres palabras más repetidas"):
            actual = wordcounter.obtener_tres_keywords_mas_repetidas()
            wordcounter.tomar_captura("02 - Keyword Density")

        with allure.step("Validar palabras y frecuencias"):
            wordcounter.tomar_captura("03 - Validación Top 3")
            assert actual == TOP_3_KEYWORDS_ESPERADAS, (
                f"Esperado: {TOP_3_KEYWORDS_ESPERADAS}; "
                f"obtenido: {actual}"
            )