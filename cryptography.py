"""""""""""""""""""""""""""""""""""""""""""""""""""
A library containing multiple classes and functions
related to cryptography 
"""""""""""""""""""""""""""""""""""""""""""""""""""
#Function to convert a string to a list of characters
def split(string):
    return [char for char in string]
    
class encrypt:
    #Only lowercase characters
    def shift(message,key):
        ciphertext = ""
        cipherlist = []
        mlist = split(message)
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        for i in range(len(alphabets)):
            if key == alphabets[i]:
                key_no = i
        
        for i in range(len(alphabets)):
            shift_value = (i + key_no)%(len(alphabets)-1)
            cipherlist.append(alphabets[shift_value])
        
        for x in mlist:
            index = alphabets.index(x)
            ciphertext = ciphertext+cipherlist[index]
            
        print(ciphertext)
        
    
    
    
    
    
    
    def vigenere(message,key):
        #Only lowercase characters
        y = 0
        z = 0
        main = True
        ciphertext = ""
        shiftlist = []
        mlist = split(message)
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        keylist = split(key)
        
        for i in keylist:
            for x in range (len(alphabets)):
                if i == alphabets[x]:
                    shiftlist.append(x)
          
        keylength = len(keylist)
        keylength2 = keylength
        mlength = len(mlist)
        
        while(mlength != 0):
            
            x = alphabets.index(mlist[y])
            shift_value = (x + shiftlist[z])%(len(alphabets)-1)
            ciphertext = ciphertext+alphabets[shift_value]
            y+=1
            z+=1
            keylength-=1
            mlength-=1
            if(keylength == 0):
                z = 0
                keylength = keylength2
            
        print(ciphertext)
        
        
        
        
        
    def one_time_pad(message,key):
        #Only lowercase characters
        y = 0
        z = 0
        main = True
        ciphertext = ""
        shiftlist = []
        mlist = split(message)
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        keylist = split(key)
        keylength = len(keylist)
        keylength2 = keylength
        mlength = len(mlist)
        
        if keylength != mlength:
            print("Invalid key: Length of key is not equal to length of message")
            main = False
        
        
        if(main == True):
            for i in keylist:
                for x in range (len(alphabets)):
                    if i == alphabets[x]:
                        shiftlist.append(x)
              
           
            while(mlength != 0):
                x = alphabets.index(mlist[y])
                shift_value = (x + shiftlist[z])%(len(alphabets)-1)
                ciphertext = ciphertext+alphabets[shift_value]
                y+=1
                z+=1
                mlength-=1
               
        print(ciphertext)
    
       
        

                
                
                
                
                

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""        







class decrypt:
    #Only lowercase characters
    def shift(message,key):
        ciphertext = ""
        cipherlist = []
        mlist1 = split(message)
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        for i in range(len(alphabets)):
            if key == alphabets[i]:
                key_no = i
        
        for i in range(len(alphabets)):
            shift_value = (i - key_no)%(len(alphabest)-1)
            cipherlist.append(alphabets[shift_value])
        
        for x in mlist1:
            index = alphabets.index(x)
            ciphertext = ciphertext+cipherlist[index]
            
        print(ciphertext)
        
        
    
    
    
    
    def vigenere(message,key):
        #Only lowercase characters
        y = 0
        z = 0
        main = True
        ciphertext = ""
        shiftlist = []
        mlist = split(message)
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        keylist = split(key)
        
        for i in keylist:
            for x in range (len(alphabets)):
                if i == alphabets[x]:
                    shiftlist.append(x)
          
        keylength = len(keylist)
        keylength2 = keylength
        mlength = len(mlist)
        
        while(mlength != 0):
            
            x = alphabets.index(mlist[y])
            shift_value = (x - shiftlist[z])%(len(alphabets)-1)
            ciphertext = ciphertext+alphabets[shift_value]
            y+=1
            z+=1
            keylength-=1
            mlength-=1
            if(keylength == 0):
                z = 0
                keylength = keylength2
            
        print(ciphertext)
        
        
        
        
        
        
        
    def one_time_pad(message,key):
        #Only lowercase characters
        y = 0
        z = 0
        main = True
        ciphertext = ""
        shiftlist = []
        mlist = split(message)
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        keylist = split(key)
        keylength = len(keylist)
        keylength2 = keylength
        mlength = len(mlist)
        
        if keylength != mlength:
            print("Invalid key: Length of key is not equal to length of message")
            main = False
        
        
        if(main == True):
            for i in keylist:
                for x in range (len(alphabets)):
                    if i == alphabets[x]:
                        shiftlist.append(x)
              
           
            while(mlength != 0):
                x = alphabets.index(mlist[y])
                shift_value = (x - shiftlist[z])%(len(alphabets)-1)
                ciphertext = ciphertext+alphabets[shift_value]
                y+=1
                z+=1
                mlength-=1
               
        print(ciphertext)
            
    
