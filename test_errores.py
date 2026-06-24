import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
# cargamos los secretos 
load_dotenv ()

@pytest.mark.skip(reason="Fallo intencional omitido en la nube")


def test_falla_a_proposito_con_captura (browser):

    browser.get(os.getenv("SAUCE_URL"))

    try:
# 2. Interactuar: Intentamos hacer clic en un botón que NO EXISTE  
        browser.find_element(By.ID, "boton-fantasma-que-no-existe").click()

    except Exception as e:
# 3. La trampa: Si el código falla al no encontrar el botón, entra aquí
# Tomamos la fotografía de la pantalla en ese exacto segundo
      browser.save_screenshot("evidencia_error.png")



# Le decimos a Pytest que marque la prueba como FAILED oficialmente

    pytest.fail("Fallo provocado exitosamente para probar la captura de pantalla.")