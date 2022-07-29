import jks
import os
#CON ESTO CONSEGUIMOS LA CLAVE
path=os.path.dirname(__file__)
print(path)

keystore=path + "/KeyStorePracticas/"
ks = jks.KeyStore.load(keystore, "123456")

for alias, sk in ks.secret_keys.items():
    print("Secret key: %s" % sk.alias)
    print("  Algorithm: %s" % sk.algorithm)
    print("  Key size: %d bits" % sk.key_size)
    print("  Key: %s" % "".join("{:02x}".format(b) for b in bytearray(sk.key)))