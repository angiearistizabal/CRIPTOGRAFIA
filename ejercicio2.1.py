
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

#Paso todos la información a Bytes 

texto_cifrado_bytes=b64decode('zcFJxR1fzaBj+gVWFRAah1N2wv+G2P01ifrKejICaGpQkPnZMiexn3WXlGYX5WnNIosyKfkNKG9GGSgG1awaZg==')
clave = bytes.fromhex('e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72')
iv_bytes = bytes.fromhex('00000000000000000000000000000000')
#Ahora a cifrar
try:
    cipher = AES.new(clave, AES.MODE_CBC, iv_bytes)
    mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="pkcs7") 
    print("En hex: ", mensaje_des_bytes.hex())
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error)