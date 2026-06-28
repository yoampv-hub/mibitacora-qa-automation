# Mi Bitácora Béisbol - QA Automation Suite

Proyecto de automatización QA con **Python, Selenium WebDriver y Pytest** para validar los flujos críticos de la aplicación web **Mi Bitácora Béisbol / PitchTracker Pro**.

La suite automatiza escenarios reales de usuario sobre una aplicación desplegada en producción, incluyendo autenticación, navegación interna, selección de contexto deportivo, acceso a perfiles de jugadores y generación de reportes mediante Inteligencia Artificial.

---

## Resumen del proyecto

Este repositorio contiene una suite de pruebas End-to-End desarrollada para validar la estabilidad funcional de **Mi Bitácora Béisbol**, una aplicación orientada al scouting, análisis y toma de decisiones en béisbol base.

El objetivo principal de las pruebas es verificar que los flujos críticos de la aplicación funcionen correctamente desde la perspectiva de un usuario real.

---

## Stack tecnológico

| Tecnología         | Uso dentro del proyecto                               |
| ------------------ | ----------------------------------------------------- |
| Python 3.12        | Lenguaje principal para los scripts de prueba         |
| Selenium WebDriver | Automatización del navegador e interacción con el DOM |
| Pytest             | Ejecución, organización y validación de pruebas       |
| python-dotenv      | Gestión segura de variables de entorno                |
| Chrome WebDriver   | Ejecución de pruebas en navegador Chrome              |
| React App          | Aplicación objetivo probada por la suite              |

---

## Estrategia de automatización

La suite fue diseñada aplicando buenas prácticas de QA Automation:

### Sincronización dinámica

Se reemplazaron esperas rígidas con `time.sleep()` por esperas explícitas usando `WebDriverWait` y `Expected Conditions`.

Se utilizan condiciones como:

* `visibility_of_element_located`
* `element_to_be_clickable`
* `invisibility_of_element_located`
* `presence_of_element_located`

Esto permite sincronizar las pruebas con los tiempos reales de renderizado de React, modales dinámicos y respuestas asíncronas.

### Validaciones intermedias

El flujo E2E no valida únicamente el resultado final. Incluye puntos de control durante el recorrido para detectar en qué parte específica puede fallar el proceso.

Ejemplos:

* Validación de login exitoso.
* Validación de acceso al Dashboard.
* Confirmación de carga de la lista de bateadores.
* Confirmación de acceso al perfil de jugador.
* Validación de disponibilidad del módulo PDF.
* Validación de generación de reporte IA.
* Verificación de logout correcto.

### Trazabilidad visual

La suite genera capturas de pantalla durante puntos clave del flujo. Estas capturas se almacenan en el directorio `/screenshots` para facilitar la revisión y depuración.

---

## Casos de prueba cubiertos

### `test_login_fallido_mi_app`

Valida que el sistema rechace credenciales incorrectas y muestre el mensaje de error correspondiente.

### `test_login_exitoso_mi_app`

Valida que un usuario con credenciales válidas pueda iniciar sesión y acceder correctamente al Dashboard.

### `test_flujo_completo_e2e`

Ejecuta un flujo completo de usuario:

1. Login exitoso.
2. Selección de contexto de juego.
3. Selección de categoría.
4. Configuración inicial de sesión.
5. Navegación al módulo de bateadores.
6. Acceso al perfil de un jugador.
7. Validación del módulo PDF.
8. Navegación al módulo de video.
9. Generación de reporte mediante IA.
10. Logout.
11. Verificación de retorno a la pantalla de login.

---

## Estructura recomendada del proyecto

```text
mibitacora-qa-automation/
├── tests/
│   └── test_mi_app.py
├── screenshots/
├── conftest.py
├── requirements.txt
├── pytest.ini
├── .env.example
├── .gitignore
└── README.md
```

---

## Instalación local

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd mibitacora-qa-automation
```

### 2. Crear entorno virtual

En macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Variables de entorno

Crear un archivo `.env` en la raíz del proyecto con la siguiente estructura:

```env
APP_URL=https://su-dominio-de-prueba.com
APP_MANAGER_EMAIL=usuario_demo@ejemplo.com
APP_MANAGER_PASSWORD=password_demo
```

Por seguridad, el archivo `.env` no debe subirse al repositorio.

Se recomienda incluir un archivo `.env.example` con valores de ejemplo.

---

## Ejecución de pruebas

Para ejecutar la suite completa:

```bash
pytest -v
```

Para ejecutar solamente el archivo principal:

```bash
pytest -v tests/test_mi_app.py
```

Si el archivo está en la raíz del proyecto:

```bash
pytest -v test_mi_app.py
```

---

## Artefactos generados

Durante la ejecución, la suite puede generar capturas de pantalla en:

```text
/screenshots
```

Estas capturas ayudan a analizar el estado visual de la aplicación durante puntos críticos del flujo.

---

## Próximas mejoras

* Incorporar atributos `data-testid` en los componentes React para reforzar la estabilidad de los selectores.
* Separar los flujos en Page Object Model.
* Añadir reportes HTML con `pytest-html`.
* Integrar ejecución automática con GitHub Actions.
* Añadir pruebas específicas para validación de errores en formularios.
* Añadir pruebas de regresión para módulos de lanzadores y bateadores.

---

## Autor

**Yoam Perez Vega**
Junior QA Automation / Developer
Ponferrada, España
