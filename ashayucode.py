import base64

stringg = input("Please Enter Sky Key: ")
KEYLOG = base64.b64decode(stringg).decode('utf-8')

print(KEYLOG)
createfile = open('.env', 'w')
createfile.writelines(KEYLOG)
createfile.close()