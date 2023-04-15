''' 
Name: Ryan Campbell
Date: 4/15/2023
Description: This code allows the user to encode a string
'''

class cyberSecurity:
    def __init__(self, shift):
        self._encryptedMessage = ''
        self._decryptedMessage = ''
        self._shift = shift

    # Main encryption method. Planninng on adding a random number generator along with other things. This system
    # Would be easy to break into as of now, but in future installments the main ecrypt and decrypt class
    # Will constantly be changing their shift key along with its other features

    def encrypt(self, message):
        # Basic encryption method
        scrambleText = ""
        for char in message:
            if ord(char) >= 65 and ord(char) <= 90:
                shiftChar = chr((ord(char) + self._shift - 65) % 26 + 65)
                scrambleText += shiftChar
            elif ord(char) >= 97 and ord(char) <= 122:
                shiftChar = chr((ord(char) + self._shift - 97) % 26 + 97)
                scrambleText += shiftChar
            else:
                scrambleText += char
        self._encryptedMessage = scrambleText
        return scrambleText

    # Main decryption method. Same as encryption ,very basic but efficient and works. Will be updated
    # later with the random number generator. As of right now, I only changed the numbers within the
    # actual encrpt and decrypt functions
    def decrypt(self, message):
        # Basic decryption method
        emptyText = ""
        for char in message:
            if ord(char) >= 65 and ord(char) <= 90:
                shiftChar = chr((ord(char) - self._shift - 65) % 26 + 65)
                emptyText += shiftChar
            elif ord(char) >= 97 and ord(char) <= 122:
                shiftChar = chr((ord(char) - self._shift - 97) % 26 + 97)
                emptyText += shiftChar
            else:
                emptyText += char
        self._decryptedMessage = emptyText
        return emptyText

    # Getters
    def getEncryptedMessage(self):
        return self._encryptedMessage

    def getDecryptedMessage(self):
        return self._decryptedMessage

    # Setters
    def setEncryptedMessage(self, message):
        self._encryptedMessage = message

    def setDecryptedMessage(self, message):
        self._decryptedMessage = message

    def setShift(self, shift):
        self._shift = shift

    def getShift(self):
        return self._shift
    # This is one of the options that the user will be able to access in later installments of this code
class AdvancedEncryption(cyberSecurity):
    def __init__(self, shift=3):
        super().__init__(shift)
        self.shift = shift

    def encrypt(self, message):
        # Basic encryption method
        scrambleText = ""
        for char in message:
            if ord(char) >= 65 and ord(char) <= 90:
                shiftChar = chr((ord(char) + self.shift - 6) % 226 + 653)
                scrambleText += shiftChar
            elif ord(char) >= 97 and ord(char) <= 122:
                shiftChar = chr((ord(char) + self.shift - 9) % 24 + 970)
                scrambleText += shiftChar
            else:
                scrambleText += char
        return scrambleText

    def decrypt(self, message):
        # Basic decryption method
        emptyText = ""
        for char in message:
            if ord(char) >= 65 and ord(char) <= 90:
                shiftChar = chr((ord(char) - self.shift - 65) % 26 + 65)
                emptyText += shiftChar
            elif ord(char) >= 97 and ord(char) <= 122:
                shiftChar = chr((ord(char) - self.shift - 97) % 26 + 97)
                emptyText += shiftChar
            else:
                emptyText += char
        return emptyText

def menu():

    print("Welcome to Ryan's Cyber Security Software (Version 1.3.6)")
    print("1. Administrator")
    print("2. Normal User")
    userChoice = input("Enter 1 for Administrator or 2 for Normal User: ")
    if userChoice == "1":
        shiftChoice = int(input("Enter the new shift value: "))
        security = cyberSecurity(shiftChoice)
        security.setShift(shiftChoice)

        adminChoice = input("Enter E to encrypt or D to decrypt: ")
        message = input("Enter the message: ")
        if adminChoice.upper() == "E":
            security.encrypt(message)
            print("Encrypted message:", security.getEncryptedMessage())
        elif adminChoice.upper() == "D":
            security.decrypt(message)
            print("Decrypted message:", security.getEncryptedMessage())
        else:
            print("Invalid choice. Exiting program.")
    elif userChoice == "2":
        security = cyberSecurity(3)
    print("1. Encryption")
    print("2. Decryption")
    print("3. Other Security Options")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Please choose a number 1-4:"))

            if choice == 1:
                print("You chose Encryption")
                # Get user input
                message = input("Enter the message to encrypt: ")
                # Encrypt message using the specified shift value
                encryptedMessage = security.encrypt(message)
                print("Encrypted message: ", encryptedMessage)

            elif choice == 2:
                print("You chose Decryption")
                # Get user input
                message = input("Enter the message to decrypt: ")
                # Decrypt message using the specified shift value
                decryptedMessage = security.decrypt(message)
                print("Decrypted message: ", decryptedMessage)

            elif choice == 3:
                print("You chose Other methods of Cyber Security")
                # Not implemented yet

            elif choice == 4:
                print("Thank you for using Ryan's Encryption, Decryption, and Cyber Security Programs!")
                break
            else:
                print("An unexpected error has occurred, please try again.")
        except ValueError:
            print("Invalid choice, please only enter one number between 1 and 4")
    else:
        print("Invalid choice. Exiting program.")

menu()
