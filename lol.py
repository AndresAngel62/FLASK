import requests

# 1. Hacemos la petición a la API
respuesta = requests.get("https://api.github.com/users/octocat")

# 2. Convertimos el formato JSON a un diccionario de Python
datos = respuesta.json()

# 3. Accedemos a la información fácilmente
print(datos["name"])  # Imprime el nombre obtenido