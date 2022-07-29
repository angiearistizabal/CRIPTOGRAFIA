import jwt

#Descifro el jwt
decode_jwt = jwt.decode ('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRmVsaXBlIFJvZHJcdTAwZWRndWV6Iiwicm9sIjoiaXNBZG1pbiJ9.-KiAA8cjkamjwRUiNVHgGeJU8k2wiErdxQP_iFXumM8',"KeepCoding", algorithms="HS256")

#Hago un print de lo anterior

print(decode_jwt)


