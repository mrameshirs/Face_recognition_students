from cryptography.fernet import Fernet


kbyte = b'wYZiHRIKIzWAAOa4J8-UNbq9Blj5IfKY6SRvDxIYnJ0='
encmsg = b'gAAAAABmHDtNQ7Z-6DmU8XIYGzSCof3DYHLLvWzuBNDzwXTBeWA7E65iTWXv0s_IFwGko7NP9GTreuTN5VpSazUod5wcYxzvyA=='

def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

def encdec():
    decrypted = decrypt_message(kbyte, encmsg)
    return decrypted