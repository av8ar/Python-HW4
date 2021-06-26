import random
import unittest

#Does the conversions
class IPAddressConverter:
   
    #converts number to its equivalent IP Address
    @staticmethod
    def numToIpAddress(num):
        address = ''
        counter = 0
        if num == 0 and address == '': 
            return '0.0.0.0'
        while num > 0:
            if counter == 0:
                address = str(num%256)
            else:
                address = str(num%256) + '.' + address
            num = int(num/256)
            counter += 1
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

class IPAddressConverterTest(unittest.TestCase):
    
    def test_IPAddressConverterTest(self):        
        self.assertEqual(IPAddressConverter.ipAddressToNum('127.0.0.1'), 2130706433)
        self.assertEqual(IPAddressConverter.ipAddressToNum('0.0.0.0'), 0)
        self.assertEqual(IPAddressConverter.ipAddressToNum('101.0.78.13'), 1694518797)
        self.assertEqual(IPAddressConverter.ipAddressToNum('9.9.9.10'), 151587082)
        self.assertEqual(IPAddressConverter.ipAddressToNum('10.6.8.130'), 168167554)
        self.assertEqual(IPAddressConverter.ipAddressToNum('255.255.255.255'), 4294967295)
        self.assertEqual(IPAddressConverter.ipAddressToNum('6.6.6.6'), 101058054)
        self.assertEqual(IPAddressConverter.ipAddressToNum('220.36.180.140'), 3693393036)
        self.assertEqual(IPAddressConverter.ipAddressToNum('0.0.250.4'), 64004)
        self.assertEqual(IPAddressConverter.ipAddressToNum('9.207.201.0'), 164612352)
        
        


#Generates key, encrypts, decrypts messages
class MonoAlphabeticCipher:

    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = lower_alphabet.upper()
    digits = '0123456789'
    char_str = upper_alphabet + lower_alphabet + digits

    #Instantiation
    def __init__(self):
        self.key = self.generateKey()

    #Generates key
    def generateKey(self):
        key = ''
        for i in range(62):
            c = self.char_str[random.randint(0, 61)]
            while c in key:
                c = self.char_str[random.randint(0, 61)]
            key += c
        self.key = key
        return key
    
    #Encrypts message
    def encrypt(self, msg):
        encrypted_msg = ''
        for c in msg:
            encrypted_msg += self.key[self.char_str.index(c)]
        return encrypted_msg

    #Decrypts encrypted message
    def decrypt(self, encrypted_msg):
        decrypted_msg = ''
        for c in encrypted_msg:
            decrypted_msg += self.char_str[self.key.index(c)]
        return decrypted_msg

class MonoalphabeticCipherTest(unittest.TestCase):
    def test_MonoalphabeticCipherTest(self):
        c = MonoAlphabeticCipher()
        keyList = []
        encList = []
        decList = []
        msgList = ['Mario123', 'CelSius23', 'COVID19', 'Murica99', 'StephCurry22', 'dreamD4', '420blazeit', 'amogus1', 'todoslosdias', 'stevesuptic', 'McKillaGorilla', 'mainpy', 'korewapendesu', 'KFC', 'kurama', 'story1', '909485', '01racecar10', 'parabellum', '8bit', 'CPU', 'ValoStatsFails', 'StatenIsland', 'disconnect', 'kettle7', '70and7d', 'YouTube', 'ChesterAruthru', 'geometry3', 'jujutsu']
        for i in range(30):
            k = c.generateKey()
            e = c.encrypt(msgList[i])
            d = c.decrypt(e)
            keyList.append(k)
            encList.append(e)
            decList.append(d)
        for i in range(30):
            c.key = keyList[i]
            self.assertEqual(c.encrypt(msgList[i]), encList[i])
            self.assertEqual(c.decrypt(encList[i]), decList[i])

#Main function
def main():
    print('Hello World')
    converter = IPAddressConverter()
    cipher = MonoAlphabeticCipher()
    address1 = '127.0.0.1'
    num1 = 2130706433
    address2 = '0.0.0.0'
    num2 = 0
    msg = 'Pyth0n15Super10r'
    encrypted_msg = cipher.encrypt(msg)
    print(address1, '=', converter.ipAddressToNum(address1))
    print(num1, '=', converter.numToIpAddress(num1))
    print(address2, '=', converter.ipAddressToNum(address2))
    print(num2, '=', converter.numToIpAddress(num2))
    print('key1:', cipher.key)
    print('msg:', msg)
    print('encrypted msg:', encrypted_msg)
    print('decrypted msg:', cipher.decrypt(encrypted_msg))

#Executes main method
if __name__ == '__main__':
   #unittest.main(verbosity = 2)
   main()