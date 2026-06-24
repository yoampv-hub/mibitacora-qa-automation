import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

# Cargamos los secretos
load_dotenv()

def test_agregar_producto_al_carrito(browser):
    # 1. Preparar: Hacemos el Login rápido (Precondición para entrar al dashboard)
    browser.get(os.getenv("SAUCE_URL"))
    browser.find_element(By.ID, "user-name").send_keys(os.getenv("SAUCE_USERNAME"))
    browser.find_element(By.ID, "password").send_keys(os.getenv("SAUCE_PASSWORD"))
    browser.find_element(By.ID, "login-button").click()

    # 2. Interactuar: Hacemos clic en el botón de agregar la mochila Sauce Labs
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # 3. Validar (Assert): Buscamos la burbuja roja del carrito y comprobamos que dice "1"
    carrito_badge = browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    
    assert carrito_badge == "1"