import streamlit as st
import pandas as pd
from io import BytesIO

from utils.file_handling import compute_file_hash
from utils.normalization import (
    extract_clean_name, extract_quantity_and_unit,
    normalize_lider_price, format_price, normalize_unit
)
from utils.ui_helpers import (
    display_lider_product, display_canonical_product
)

st.title("Validador de Productos: Líder vs Canónico")

# Función para registrar la etiqueta seleccionada y avanzar
def save_label_and_advance(index, label):
    st.session_state.results[index] = label
    st.session_state.index += 1
    st.rerun()

uploaded_file = st.file_uploader("Sube tu archivo de productos", type=["xlsx", "csv", "parquet"])

if uploaded_file:
    file_bytes = uploaded_file.read()
    file_hash = compute_file_hash(file_bytes)
    uploaded_file.seek(0)

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith(".parquet"):
        df = pd.read_parquet(uploaded_file)
    else:
        st.error("Formato de archivo no soportado.")
        st.stop()

    if "etiqueta_manual" not in df.columns:
        df["etiqueta_manual"] = ""
    else:
        df["etiqueta_manual"] = df["etiqueta_manual"].fillna("").astype(str)

    # Si es un archivo nuevo, reiniciar estado
    if st.session_state.get("file_hash") != file_hash:
        st.session_state.results = {
            i: val for i, val in df["etiqueta_manual"].items()
            if val in ["Igual", "Distinto", "Dudoso"]
        }
        st.session_state.file_hash = file_hash
        try:
            st.session_state.index = df[df["etiqueta_manual"].str.strip() == ""].index[0]
        except IndexError:
            st.session_state.index = len(df)

    total = len(df)
    index = st.session_state.index

    if index < total:
        row = df.iloc[index]
        st.markdown(f"### Comparación {index + 1} de {total}")

        # Procesar campos de comparación
        clean_name = extract_clean_name(
            row.get("menu_item_name_lider", ""), row.get("product_brand_lider", "")
        )
        lider_price_str = format_price(normalize_lider_price(row.get("menu_item_price_lider", 0)))
        canonical_price_str = format_price(row.get("last_price", 0))
        quantity, raw_unit = extract_quantity_and_unit(row.get("package", ""))
        unit = normalize_unit(raw_unit)

        # Mostrar productos en columnas
        col1, col2 = st.columns(2)
        with col1:
            display_lider_product(row, clean_name, lider_price_str)
        with col2:
            display_canonical_product(row, quantity, unit, canonical_price_str)

        # Formulario con botones
        with st.form(key=f"form_{index}"):
            col_yes, col_no, col_maybe = st.columns(3)
            with col_yes:
                btn_yes = st.form_submit_button("✅ Sí es el mismo")
            with col_no:
                btn_no = st.form_submit_button("❌ No es el mismo")
            with col_maybe:
                btn_maybe = st.form_submit_button("❓Dudo")

            if btn_yes:
                save_label_and_advance(index, "Igual")
            elif btn_no:
                save_label_and_advance(index, "Distinto")
            elif btn_maybe:
                save_label_and_advance(index, "Dudoso")
    else:
        st.success("Todos los productos han sido validados")

    # Guardar etiquetas al DataFrame
    for i, label in st.session_state.results.items():
        df.at[i, "etiqueta_manual"] = label

    df_validated = df[df["etiqueta_manual"].isin(["Igual", "Distinto", "Dudoso"])]
    if not df_validated.empty:
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)
        st.download_button(
            label=" Descargar archivo con etiquetas",
            data=output.getvalue(),
            file_name="validated_products.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
