import hashlib

# Calcular el hash del archivo para detectar si ya ha sido cargado antes
def compute_file_hash(file_bytes):
    return hashlib.md5(file_bytes).hexdigest()
