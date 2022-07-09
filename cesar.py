import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ROTATION = 3
MSGERRO = 'Escreve direito ai, tanso'
STUDENTNAME = 'Student name: Vinicius Silveira de Melo'
CRYPTMESSAGE = 'Message crypt: '
DECRYPTMESSAGE = 'Message decrypt: '

def cryptOrDecryptBusinessService(message, rotation):
    returnMessage = '';
    for i in message:
        if(i in ALPHABET):
            returnMessage += ALPHABET[(ALPHABET.index(i) + (rotation * ROTATION)) % len(ALPHABET)]
        else:
            returnMessage += i
    return returnMessage

def crypt(message):
    return cryptOrDecryptBusinessService(message, 1)
    
def decrypt(message):
    return cryptOrDecryptBusinessService(message, -1)

def main():
    print(STUDENTNAME)
    try:
        command = sys.argv[1].lower()
        message = sys.argv[2].lower()
        
        if command == 'crypt':
            print(CRYPTMESSAGE + crypt(message))
        elif command == 'decrypt':
            print(DECRYPTMESSAGE + decrypt(message))
        else:
            print(MSGERRO)
    except:
        print(MSGERRO)

if __name__ == '__main__':
    main()