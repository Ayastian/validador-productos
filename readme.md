# 🛒 Validador de Productos: Líder vs Canónico

Esta aplicación permite comparar productos entre una fuente **Líder** y su versión **Canónica**, visualizando datos clave como nombre, marca, cantidad, unidad, precio e imagen. Fue desarrollada en **Python** usando **Streamlit**, y está pensada para facilitar el etiquetado manual de coincidencias entre productos.

---

## 🚀 Cómo iniciar la app

### 1. Clona este repositorio

```bash
git clone https://github.com/Ayastian/validador-productos.git
cd validador-productos
```

### 2. Crea y activa un entorno virtual

#### En Windows (cmd o PowerShell)

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### En macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación

```bash
streamlit run app.py
```

---

## 📂 Tipos de archivos soportados

Puedes cargar cualquiera de los siguientes formatos:

- `.xlsx` (Excel)
- `.csv` (CSV)
- `.parquet` (Parquet)

---

## ✅ ¿Qué puedes hacer con esta app?

- Visualizar productos lado a lado (Líder vs Canónico)
- Ver imágenes, nombres, marcas, unidades, cantidades y precios
- Clasificar productos como:
  - ✅ Igual
  - ❌ Distinto
  - ❓ Dudoso
- Descargar un archivo actualizado con tus etiquetas

---

## 📄 ¿Quieres modificar la lógica o estructura?

Revisa el archivo [`estructura_logica.md`](estructura_logica.md) donde se explica cómo está organizado el código y qué hace cada parte, para facilitar cualquier personalización o extensión.

---
