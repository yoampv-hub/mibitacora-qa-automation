import os
import pytest
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

def test_flujo_completo_e2e(browser):
    # --- 1. PREPARAR: INICIO DE SESIÓN ---
    browser.get(os.getenv("APP_URL"))
    wait = WebDriverWait(browser, 10)
    
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']"))).send_keys(os.getenv("APP_MANAGER_EMAIL"))
    browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(os.getenv("APP_MANAGER_PASSWORD"))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    time.sleep(2) 

    browser.save_screenshot("debug_1_menu_categorias.png")

    # --- 1.5 SELECCIONAR CONTEXTO Y ALINEACIÓN (El Modal) ---
    btn_juego_real = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Juego Real') or contains(text(), 'juego real')]")))
    browser.execute_script("arguments[0].click();", btn_juego_real)
    time.sleep(1) 
    
    btn_u14 = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'U-14') or contains(text(), 'U 14')]")))
    browser.execute_script("arguments[0].click();", btn_u14)
    time.sleep(1) 
    
    # 🌟 NUEVA JUGADA: Clonar la alineación usando el teclado
    dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Empezar vacío')]")))
    browser.execute_script("arguments[0].click();", dropdown)
    time.sleep(1) # Esperamos a que se abra la lista
    
    # Presionamos Abajo y Enter para seleccionar el primer juego guardado
    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    
    # --- 1.6 CERRAR EL MODAL PARA ENTRAR AL JUEGO ---
    btn_iniciar_modal = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Iniciar Sesión')]")))
    browser.execute_script("arguments[0].click();", btn_iniciar_modal)
    
    # Le damos 3 segundos para que el modal desaparezca y el estadio cargue por completo
    time.sleep(3)
    
    # --- 2. NAVEGAR A BATEADORES ---
    btn_bateadores = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Bateadores')]")))
    browser.execute_script("arguments[0].click();", btn_bateadores)
    
    time.sleep(2) 

    browser.save_screenshot("debug_2_menu_categorias.png")

    # --- 3. SELECCIONAR JUGADOR ---
    btn_manolo = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Manolo')]")))
    browser.execute_script("arguments[0].click();", btn_manolo)
    
    time.sleep(1) 

    browser.save_screenshot("debug_3_seleccionar_jugador.png")

    # --- 4. CLICK EN EL BOTÓN PDF ---
    btn_pdf = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'PDF')]")))
    browser.execute_script("arguments[0].click();", btn_pdf)
    
    # --- 5. NAVEGAR A VIDEO ---
    btn_video = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Video') or contains(text(), 'video')]")))
    browser.execute_script("arguments[0].click();", btn_video)
    
    # --- 6. GENERAR REPORTE (El elemento de IA) ---
    btn_reporte = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Generar Reporte')]")))
    browser.execute_script("arguments[0].click();", btn_reporte)
    
    time.sleep(2) 
    
    browser.save_screenshot("debug_4_menu_categorias.png") 

    # --- 7. CIERRE DE FLUJO: LOGOUT ---
    btn_logout = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Sign out') or contains(text(), 'Sign Out')]")))
    browser.execute_script("arguments[0].click();", btn_logout)
    
    # --- 8. VALIDACIÓN FINAL ---
    pantalla_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    assert pantalla_login.is_displayed()

