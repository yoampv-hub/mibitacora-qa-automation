import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Cargamos los secretos
load_dotenv()

def test_login_fallido_mi_app(browser):
    # 1. Preparar: Navegamos a tu dominio oficial
    browser.get(os.getenv("APP_URL"))
    
    # 2. Interactuar: Usamos WebDriverWait porque React puede tardar medio segundo en pintar los campos
    wait = WebDriverWait(browser, 10) # Esperará máximo 10 segundos
    
    # Buscamos el campo de email (ajustaremos el selector si Lovable le puso otro nombre)
    campo_email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    campo_email.send_keys("hacker@falso.com")
    
    # Buscamos el campo de contraseña
    campo_password = browser.find_element(By.CSS_SELECTOR, "input[type='password']")
    campo_password.send_keys("clave_inventada")
    
    # Buscamos el botón de entrar (por lo general es tipo submit)
    boton_login = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    boton_login.click()
    
    # 3. Validar: Esperamos a ver si aparece algún mensaje de error en la pantalla
    # Como cerramos el registro, un usuario falso debería ser rechazado
    # Esta línea busca cualquier elemento que contenga la palabra "Invalid" o el mensaje que dé Supabase
    # 3. Validar: Esperamos a que la notificación Toast de React sea visible con el texto exacto
    mensaje_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid login credentials')]")))
    
    assert mensaje_error.is_displayed()

def test_login_exitoso_mi_app(browser):
    # 1. Preparar: Navegamos a tu dominio oficial
    browser.get(os.getenv("APP_URL"))
    wait = WebDriverWait(browser, 10)
    
    # 2. Interactuar: Ingresamos tus credenciales reales desde el .env
    campo_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    campo_email.send_keys(os.getenv("APP_MANAGER_EMAIL"))
    
    campo_password = browser.find_element(By.CSS_SELECTOR, "input[type='password']")
    campo_password.send_keys(os.getenv("APP_MANAGER_PASSWORD"))
    
    boton_login = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    boton_login.click()
    
    # 3. Validar: Esperamos a que cargue el menú inferior buscando el texto "Dashboard"
    # Esto confirma que el login fue exitoso y estamos dentro de la app
    ancla_dashboard = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Dashboard')]")))
    
    assert ancla_dashboard.is_displayed()