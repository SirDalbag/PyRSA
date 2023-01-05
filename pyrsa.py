import rsa
import base64

print('[ 1 - Зашифровать сообщение ] [ 2 - Расшифровать сообщение ]')
task = int(input('Какую задачу выполнить? - '))

match task:
    case 1:
        publicKey, privateKey = rsa.newkeys(512)
        message = input('Какое сообщение зашифровать? - ').encode('utf8')
        crypto = rsa.encrypt(message, publicKey)
        crypto = base64.b64encode(crypto)
        privateKeyPEM = privateKey.save_pkcs1().decode('utf8')
        print('Зашифрованное сообщение -', crypto.decode())
    case 2:
        message = input('Какое сообщение расшифровать? - ')
        privateKeyPEM = input('Ключ? - ')
        pemPrefix = '-----BEGIN RSA PRIVATE KEY-----\n'
        pemSuffix = '\n-----END RSA PRIVATE KEY-----'
        privateKeyPEM = '{}{}{}'.format(pemPrefix, privateKeyPEM, pemSuffix)
        privateKeyReloaded = rsa.PrivateKey.load_pkcs1(privateKeyPEM.encode('utf8')) 
        message = base64.b64decode(message)
        message = rsa.decrypt(message, privateKeyReloaded)
        print('Расшифрованное сообщение -', message.decode())
    case _:
        print('Ошибка! Такой задачи нет.')