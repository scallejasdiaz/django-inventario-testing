# 🧪 Sistema de Inventario con Testing - Ejercicio Guiado

Este repositorio contiene una aplicación Django simple para la gestión de inventario. Está diseñada **con errores intencionales** para ser usada como base de un ejercicio guiado sobre **certificación y aseguramiento de calidad** en software.

## 🎯 Objetivo del ejercicio

El objetivo es que el estudiante:
- Identifique y documente errores en el sistema (tanto funcionales como de calidad).
- Ejecute pruebas automatizadas con `pytest` y `unittest`.
- Corrija errores básicos y registre evidencia en la tabla incluida más abajo.
- Reflexione sobre los criterios de aceptación, adaptabilidad y escalabilidad de la solución.

---

## ⚙️ Requisitos

- Python 3.10+
- Django 4.2+
- pipenv o virtualenv
- pytest y herramientas adicionales (ver más abajo)
- Navegador web

---

## 🚀 Instalación del proyecto

```bash
# 1. Clonar el repositorio
git clone https://github.com/scallejasdiaz/django-inventario-testing.git
cd django-inventario-testing

# 2. Crear entorno virtual
python3 -m venv env
source env/bin/activate   # En Windows: env\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Migraciones iniciales
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser
# Usuario: admin
# Contraseña: 4dm1n

# 6. Ejecutar servidor
python manage.py runserver
```

---

## 🧪 Ejecutar pruebas

```bash
pytest
# o también
python manage.py test
```

---

## 🔬 Herramientas de Testing Incluidas

| Herramienta      | Descripción                                            |
|------------------|--------------------------------------------------------|
| `pytest`         | Motor de pruebas liviano y eficiente                   |
| `pytest-django`  | Integración con proyectos Django                       |
| `coverage`       | Medición de cobertura de código                        |
| `pytest-cov`     | Cobertura directamente integrada con `pytest`         |
| `factory_boy`    | Generador de datos de prueba con objetos de fábrica   |
| `Faker`          | Generador de datos falsos (nombres, emails, etc.)     |

---

## 📋 Actividad guiada

1. Navega por la aplicación y detecta errores visuales o lógicos.
2. Ejecuta los tests y analiza los resultados.
3. Documenta cada error en la tabla de evidencias.
4. Propon soluciones o corrige directamente el código.
5. Comenta tu análisis.

---

## 📊 Tabla de Evidencias

| N° | Evidencia encontrada | Tipo de error | Ubicación | Acción realizada | Estado (pendiente/resuelto) |
|----|-----------------------|----------------|-----------|-------------------|------------------------------|
| 1  |                       |                |           |                   |                              |
| 2  |                       |                |           |                   |                              |
| 3  |                       |                |           |                   |                              |

---

## 🔍 Sugerencias de verificación

- Revisa si los enlaces de navegación funcionan correctamente.
- Verifica que los mensajes de éxito/error aparecen en las acciones CRUD.
- Comprueba si los tests cubren todos los casos esperados.
- Evalúa la legibilidad del código (nombres, comentarios, estructura).
- Reflexiona sobre la escalabilidad del sistema si se agregan nuevos modelos.

---

## 🧠 Recursos de apoyo

Puedes apoyarte en los siguientes materiales:
- [Video: Writing Your First Unit Tests in Django (YouTube)](https://www.youtube.com/watch?v=0MrgsYswT1c)
- Documentación oficial de Django: https://docs.djangoproject.com/
- Documentación de Pytest: https://docs.pytest.org/

---

## 🛡️ Nota para estudiantes

Este ejercicio no solo busca encontrar errores, sino también fomentar una actitud de mejora continua, análisis crítico y buenas prácticas de desarrollo en línea con un plan de certificación de calidad.
