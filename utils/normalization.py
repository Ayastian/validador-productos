import re

# Extrae el nombre del producto sin la marca (para Líder)
def extract_clean_name(full_name, brand):
    if isinstance(full_name, str) and "·" in full_name:
        return full_name.split("·", 1)[-1].strip()
    return full_name

# Extrae la cantidad y la unidad desde el campo package del producto canónico
def extract_quantity_and_unit(package):
    if isinstance(package, str):
        match = re.search(r"(\d+(?:[.,]\d+)?)\s*([a-zA-Z]+)", package)
        if match:
            quantity = match.group(1).replace(",", ".")
            unit = match.group(2).lower()
            return float(quantity), unit
    return None, None

# Normaliza el precio de Líder (algunos vienen en centavos)
def normalize_lider_price(price):
    try:
        price = float(price)
    except:
        return 0
    return price / 100 if price > 10000 else price

# Da formato al precio para mostrarlo con símbolo $
def format_price(value):
    try:
        return f"${int(float(value)):,}"
    except:
        return "$0"

# Diccionario para normalizar las unidades más comunes
UNIT_MAPPING = {
    "g": "g", "gr": "g", "gramos": "g",
    "kg": "kg", "kgr": "kg", "kilos": "kg",
    "ml": "ml", "cc": "ml", "mililitros": "ml",
    "l": "l", "lt": "l", "litros": "l",
    "un": "un", "u": "un", "unidad": "un", "und": "un"
}

# Normaliza la unidad usando el diccionario anterior
def normalize_unit(unit: str) -> str:
    if not isinstance(unit, str):
        return ""
    unit = unit.strip().lower()
    return UNIT_MAPPING.get(unit, unit)
