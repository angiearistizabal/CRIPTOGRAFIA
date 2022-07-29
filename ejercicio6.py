from Crypto.Hash import HMAC, SHA256

secret = bytes.fromhex('2712A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')
msg0= bytes('Siempre existe más de una forma de hacerlo, y más de una solución válida.', 'utf-8')

h = HMAC.new(secret, msg=msg0, digestmod=SHA256)
print(h.hexdigest())





