message=str(input("Enter the message:"))
key=str(input("Enter the key word:"))
def encrypt(encrpt_message,key_word):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    encryption_message=""
    for char in encrpt_message:
        if not char.isalpha():
            encryption_message+=char
        else:
            value_1=alphabet.index(char)
            value_2=len(key_word)
            value_3=value_1*value_2
            val=value_3//10
            val_1=value_3%10
            offset=(val+val_1)%26
            encryption_message+=alphabet[offset]
    print('the encrpted message is:',encryption_message)
encrption=encrypt(message,key)





    







