#Does the conversions
import random
#import debugpy


class IPAddressConverter:
    def numToIpAddress(num):
        address = ''
        while num > 0:
            address = str(num % 256) + '.' + address
            num /= 256
        return address

    def ipAddressToNum(address):
        num = 0
        exp = 3
        intList = address.split('.')
        for i in intList:
            num += i * (256**exp)
            exp -= 1
        return num


class MonoAlphabeticCipher:

    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    char_str = upper_alphabet + lower_alphabet + digits

    def __init__(self):
        self.key = self.generateKey()

    def generateKey(self):
        key = ''
        for i in range(62):
            c = self.char_str[random.randint(0, 61)]
            if c not in key:
                key += c
        self.key = key
        return key

    def encrypt(self, msg):
        encrypted_msg = ''
        for c in msg:
            encrypted_msg += self.key[self.char_str.index(c)]
        return encrypted_msg

    def decrypt(self, encrypted_msg):
        decrypted_msg = ''
        for c in encrypted_msg:
            decrypted_msg += self.char_str[self.key.index(c)]
        return decrypted_msg


def main():
    print('Hello World')
    converter = IPAddressConverter()
    address1 = '127.0.0.1'
    num1 = 2130706433
    print(address1, '=', converter.ipAddressToNum(address1))
    print(num1, '=', converter.numToIpAddress(num1))
