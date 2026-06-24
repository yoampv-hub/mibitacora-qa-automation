import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

# Cargar las variables secretas del archivo .env

load_dotenv

def test_login_exitoso(browser):
# 1. Preparar
    url = os.getenv("SAUCE_URL") 
    usuario = os.getenv("SAUCE_USERNAME")
    password = os.getenv("SAUCE_PASSWORD")
# 2. Navegar e Interactuar
    browser.get(url)
    browser.find_element(By.ID, "user-name").send_keys(usuario)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

# 3. Validar (Assert): Comprobamos que la URL cambió al inventario
    assert "inventory.html" in browser.current_url

def test_login_fallido(browser):
# 1. Preparar
   url = os.getenv("SAUCE_URL")

# 2. Navegar e Interactuar con datos falsos
   browser.get(url)
   browser.find_element(By.ID, "user-name").send_keys("usuario_falso")
   browser.find_element(By.ID, "password").send_keys("clave_mala")
   browser.find_element(By.ID, "login-button").click()

    # 3. Validar (Assert): Comprobamos que sale el mensaje de error rojo
   mensaje_error = browser.find_element(By.CSS_SELECTOR, "[data-test='error']").text
   assert "Epic sadface" in mensaje_error



 