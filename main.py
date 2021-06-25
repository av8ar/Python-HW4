import random

#Does the conversions
class IPAddressConverter:
   
    #converts number to its equivalent IP Address
    @staticmethod
    def numToIpAddress(num):
        address = ''
        if num == 0 and address == '': 
            return '0.0.0.0'
        while num > 0:
            address = str(num mod 256) + '.' + address
            num /= 256
        return address

    #converts ipAddress to its equivalent number form
    @staticmethod
    def ipAddressToNum(address):
        num = 0
        exp = 3
        intList = address.split('.')
        for i in intList:
            num += int(i) * (256 ** exp)
            exp -= 1   
        return num

#Generates key, encrypts, decrypts messages
class MonoAlphabeticCipher:

    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    char_str = upper_alphabet + lower_alphabet + digits

    #Instantiation
    def __init__(self):
        self.key = self.generateKey()

    #Generates key
    def generateKey(self):
        global char_str
        key = ''
        for i in range(62):
            c = char_str[random.randint(0, 61)]
            if c not in key:
                key.append(c)
        self.key = key
        return key
    
    #Encrypts message
    def encrypt(self, msg):
        global char_str
        encrypted_msg = ''
        for c in msg:
            encrypted_msg.append(self.key[char_str.index(c)])
        return encrypted_msg

    #Decrypts encrypted message
    def decrypt(self, encrypted_msg):
        global char_str
        decrypted_msg = ''
        for c in encrypted_msg:
            decrypted_msg.append(char_str[self.key.index(c)])
        return decrypted_msg

#Main function
def main():
    print('Hello World')
    converter = IPAddressConverter()
    address1 = '127.0.0.1'
    num1 = 2130706433
    address2 = '0.0.0.0'
    num2 = 0

    print(address1, '=', converter.ipAddressToNum(address1))
    print(num1, '=', converter.numToIpAddress(num1))
    print(address2, '=', converter.ipAddressToNum(address2))
    print(num2, '=', converter.numToIpAddress(num2))

#Executes main method
if __name__ == '__main__':
    main()