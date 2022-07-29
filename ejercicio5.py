import hashlib


s = hashlib.sha3_256()

s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.","UTF-8"))

print(s.hexdigest()) 