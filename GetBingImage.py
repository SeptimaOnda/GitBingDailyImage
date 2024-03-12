import requests
import json
import urllib.request


def descargar_y_decodificar_json(url):
    # Realizar la solicitud GET para descargar el archivo JSON
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Decodificar el contenido JSON
        data = response.json()
        return data
    else:
        return None

# URL del archivo JSON a descargar
url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

# Llamar a la función con la URL del archivo JSON
json_data = descargar_y_decodificar_json(url)

# Obtén la URL de la imagen
url_imagen = "https://www.bing.com" + json_data["images"][0]["url"]
print("URL de la imagen:", url_imagen)

# Descarga la imagen
urllib.request.urlretrieve(url_imagen, "BingDailyImage.jpg")
# urllib.request.urlretrieve(url_imagen, "/var/www/snaps2u-web/web/img/home_background.jpg")