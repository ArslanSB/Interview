# Prueba Técnica - Backend Engineer

## ¡Gracias por tu tiempo! 🙌

Antes que nada, queremos agradecerte por dedicar tu tiempo a esta prueba técnica. Sabemos que tu tiempo es valioso, y apreciamos mucho tu interés en formar parte de nuestro equipo.

## Configuración del Entorno en GitHub Codespaces

Este proyecto está configurado para funcionar directamente en GitHub Codespaces, lo que te permitirá comenzar a trabajar sin necesidad de configurar tu máquina local.

### Pasos para iniciar el entorno:

1. **Abrir en Codespaces:**
   - Haz clic en el botón "Code" en el repositorio
   - Selecciona la pestaña "Codespaces"
   - Crea un nuevo Codespace o abre uno existente

2. **El entorno ya incluye:**
   - Python y `uv` como package manager
   - Docker para ejecutar PostgreSQL
   - Todas las herramientas necesarias preconfiguradas

## Instalación de Dependencias

Este proyecto utiliza **`uv`** como package manager para Python, que es mucho más rápido que pip tradicional.

### Instalar dependencias:

```bash
uv sync
```

O si prefieres instalarlas manualmente:

```bash
uv pip install -e .
```

## Configuración de la Base de Datos

El proyecto utiliza PostgreSQL en Docker. Para iniciar la base de datos:

```bash
docker-compose up -d
```

Esto levantará una instancia de PostgreSQL en segundo plano.

### Aplicar migraciones:

```bash
alembic upgrade head
```

> ⚠️ **Nota:** Este proceso puede tardar varios minutos ya que genera datos de prueba durante la migración. Aunque esto no es una práctica recomendada en producción, lo hacemos aquí para agilizar la prueba técnica y que no tengas que crear datos manualmente.

### Acceder a PostgreSQL (opcional):

Si necesitas acceder directamente a la base de datos para inspeccionar datos o ejecutar queries:

```bash
docker-compose exec postgres psql -U postgres -d app_db
```

## Ejecutar la Aplicación

Una vez instaladas las dependencias y con la base de datos corriendo, puedes ejecutar la aplicación FastAPI:

```bash
uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

La aplicación estará disponible en:
- API: `http://localhost:8000`
- Documentación interactiva (Swagger): `http://localhost:8000/docs`
- Documentación alternativa (ReDoc): `http://localhost:8000/redoc`

---

## 🎯 Problema a Resolver

### Contexto del Negocio

Nuestro equipo de producto ha identificado un problema crítico que está afectando la experiencia de usuario en nuestra plataforma. Los usuarios del sistema, específicamente los agentes de ventas y el equipo de soporte, han reportado que **la carga de la lista de clientes está tomando más de 60 segundos**, lo cual es inaceptable desde el punto de vista de UX.

### Impacto

- **Productividad:** Los agentes pierden tiempo valioso esperando que cargue la información
- **Experiencia de Usuario:** Frustración y percepción de que el sistema es lento
- **Escalabilidad:** Si ya tenemos problemas con el volumen actual, esto solo empeorará al crecer

### Tu Tarea

Como Backend Engineer, durante esta sesión de live coding necesitamos que:

1. **Identifiques** la causa raíz del problema de rendimiento
2. **Propongas** las soluciones que encuentres durante el análisis
3. **Implementes** las soluciones que consideres más adecuadas

### Criterios de Evaluación

- Capacidad de análisis y diagnóstico en tiempo real
- Conocimiento de optimización de bases de datos y APIs
- Proceso de pensamiento y resolución de problemas
- Calidad del código implementado
- Consideración de trade-offs y alternativas

---

## Recursos Útiles

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de uv](https://github.com/astral-sh/uv)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

---

¡Buena suerte! 🚀
