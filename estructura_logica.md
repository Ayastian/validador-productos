
# 🧠 Estructura y Lógica del Proyecto

Este archivo describe la estructura de carpetas y la lógica de los módulos del proyecto.

## 📁 Estructura de carpetas

```
.
├── app.py                  # Script principal de Streamlit
├── requirements.txt        # Dependencias del proyecto
├── README.md               # Guía de instalación y uso
├── estructura_logica.md    # (Este archivo)
└── utils/                  # Funciones auxiliares
    ├── __init__.py
    ├── file_handling.py    # Funciones para manejo de archivos y hash
    ├── normalization.py    # Funciones de normalización y formateo
    └── ui_helpers.py       # Funciones para mostrar productos en pantalla
```

## 🔍 Lógica de los módulos

### `app.py`
Contiene la lógica principal de la aplicación Streamlit:
- Subida de archivo (`.xlsx`, `.csv`, `.parquet`)
- Validación y comparación de productos Líder vs Canónico
- Visualización de productos en dos columnas
- Botones para etiquetar: "Igual", "Distinto", "Dudoso"
- Descarga del archivo validado

### `utils/file_handling.py`
Funciones relacionadas con:
- Obtención del hash del archivo para mantener el estado
- Identificación de si un archivo ha sido modificado

### `utils/normalization.py`
Funciones para:
- Extraer y limpiar nombre del producto
- Extraer cantidad y unidad desde `package`
- Normalizar precios
- Formatear precios para visualización
- Normalizar unidades de medida (g, gr, kg, etc.)

### `utils/ui_helpers.py`
Funciones auxiliares para:
- Mostrar imágenes con validación de URL
- Mostrar información del producto Líder
- Mostrar información del producto Canónico

---

💡 **Nota**: La lógica está modularizada para facilitar futuras modificaciones o integraciones con otros validadores o fuentes de datos.
