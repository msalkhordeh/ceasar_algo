class caesar :
   
        def Encrypt(self,input:str,key:int):
            try :
                print('Encrypt : ' + input +' with : '+ key)
                result= ''.join([ chr(ord(x)+int(key)) for x in input ])
                print(result)
            except :
                    print("Wrong Input...!!!")

        def Decrypt(self,input,key):
            try :
                print('Decrypt : ' + input +' with : '+ key)
                result= ''.join([ chr(ord(x)-int(key)) for x in input ])
                print(result)
            except :
                    print("Wrong Input...!!!")
  
_caesar = caesar()
op=input("Enter 1 for Encrypt and 2 for Decrypt :")
if op=='1' :
    value=input("Enter a text to encrypt/Decrypt : ")
    key=input("Enter a key to encrypt/Decrypt : ")
    _caesar.Encrypt(value,key)
elif op=='2' :
    value=input("Enter a text to encrypt/Decrypt : ")
    key=input("Enter a key to encrypt/Decrypt : ")
    _caesar.Decrypt(value,key)
else :
    print("Wrong Operation...!!!")


