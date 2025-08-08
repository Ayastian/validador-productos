import streamlit as st
from .normalization import format_price, normalize_unit

# Muestra la imagen del producto o advertencia si no hay URL
def display_image_or_warning(image_url, warning_text):
    if isinstance(image_url, str) and image_url.startswith("http"):
        st.image(image_url, width=250)
    else:
        st.warning(warning_text)

# Muestra los detalles del producto Líder
def display_lider_product(row, clean_name, formatted_price):
    st.subheader("🟡 Producto Líder")
    display_image_or_warning(row.get("menu_item_image_lider"), "⚠️ Imagen de Líder no disponible")
    st.markdown(f"**Nombre:** {clean_name}")
    st.markdown(f"**Marca:** {row.get('product_brand_lider', '')}")
    st.markdown(f"**Unidad:** {row.get('net_qty_unit_lider', '')}")
    st.markdown(f"**Cantidad:** {row.get('net_qty_lider', '')}")
    st.markdown(f"**Precio:** {formatted_price}")

# Muestra los detalles del producto Canónico
def display_canonical_product(row, quantity, unit, formatted_price):
    st.subheader("🔵 Producto Canónico")
    display_image_or_warning(row.get("img_url"), "⚠️ Imagen del Canónico no disponible")
    st.markdown(f"**Nombre:** {row.get('product_name', '')}")
    st.markdown(f"**Marca:** {row.get('canonical_brand', '')}")
    raw_unit = row.get('net_qty_unit_lider', '')
    unit = normalize_unit(raw_unit)
    st.markdown(f"**Unidad:** {unit}")
    st.markdown(f"**Cantidad:** {quantity or ''}")
    st.markdown(f"**Precio:** {formatted_price}")
