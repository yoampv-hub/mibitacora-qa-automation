import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    # Configuramos Chrome para que corra de forma invisible (Headless)
    opciones = Options()
    opciones.add_argument("--headless")
    opciones.add_argument("--window-size=1920,1080") # Le damos un tamaño virtual para que no falle la web
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opciones)
    
    yield driver 
    
    driver.quit()