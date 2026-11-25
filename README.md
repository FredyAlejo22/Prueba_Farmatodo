# Farmatodo QA - Punto 1: WordCounter

Proyecto base con Python + Playwright + Pytest + POM.

## Abrir en Visual Studio Code
Descomprime el ZIP y abre la carpeta `farmatodo_qa_wordcounter` con File > Open Folder.

## Preparar entorno (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

## Ejecutar
```powershell
pytest -v
```
Navegador visible:
```powershell
pytest -v --headed
```
Un escenario:
```powershell
pytest -v tests/test_wordcounter.py -k "cantidad_palabras"
```
Allure:
```powershell
pytest -v --alluredir=allure-results
allure serve allure-results
```
(El comando `allure serve` requiere tener Allure Commandline instalado.)

## Estructura
- `pages/`: Page Objects y clase base.
- `tests/`: escenarios automatizados.
- `data/`: datos y resultados esperados.
- `conftest.py`: fixtures de navegador.
- `pytest.ini`: configuración de Pytest.

## Nota sobre selectores
Los selectores están centralizados en `pages/wordcounter_page.py`. WordCounter puede cambiar su HTML;
si un locator no coincide con el DOM actual, ajustaremos ese Page Object sin modificar los tests.
El método de Keyword Density está aislado para facilitar esa inspección.
