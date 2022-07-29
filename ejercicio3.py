from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

try:

    textoPlano_bytes = bytes('Este curso es de lo mejor que podemos encontrar en el mercado', 'UTF-8')
    clave_bytes = bytes.fromhex('979DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
    nonce_mensaje_bytes = b64decode('9Yccn/f5nJJhAt2S')
    datos_asociados_bytes = bytes('Datos no cifrados sólo autenticados', 'utf-8')
    cipher = ChaCha20_Poly1305.new(key=clave_bytes, nonce=nonce_mensaje_bytes)
    cipher.update(datos_asociados_bytes)
    texto_cifrado_bytes, tag_bytes = cipher.encrypt_and_digest(textoPlano_bytes)
    mensaje_enviado = { "nonce": b64encode(nonce_mensaje_bytes).decode(),"datos asociados": b64encode(datos_asociados_bytes).decode(), "texto cifrado": b64encode(texto_cifrado_bytes).decode(), "tag": b64encode(tag_bytes).decode()}
    json_mensaje = json.dumps(mensaje_enviado)
    print("Mensaje: ", json_mensaje)
    
except (ValueError, KeyError) as error: 
    print("Problemas al cifrar....")
    print("El motivo del error es: ", error)