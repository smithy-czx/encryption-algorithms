#use of libraries, regular expression
import random, base64, re, secrets #built in files for certain functions.
import tkinter as tk # for gui
from  Modular_Arithmetic import modinv, egcd #file i made myself, it contains my implementation of the Euclidean's algorithm for prime numbers, and modular inverse.
from tkinter import ttk, WORD, messagebox

#-------------------------------------------------------------------------------------------utility functions-------------------------------------------------------------------------------------------------------------------------------
#database
import db #creates the database file if it is not already created
db.initialise()


#CONSTANTS 
NUMBER_OF_LETTERS_IN_ALPHABET = 26 #quick access to letters of the alphabet for encryptions
ENCRYPT = True #quick access to toggle mode
DECRYPT = False #quick access to toggle mode


def str_to_list(string, separator = ' '):
    str_list = []
    string = string.split(separator)
    for item in string:
        str_list.append((item))
    return str_list

def str_to_list_of_ints(string, separator=' '): #this is a utility function that takes a string and a type of separator you want to split the string by, it then splits it into lists
    int_list = []
    string = string.split(separator)
    for item in string:
        int_list.append(int(item))
    return int_list
    
#--------------------------------------------------------------------------------super classes and subclasses for composition-----------------------------------------------------------------------------------------------------------------------------------------------------

#super class, this is the base class where all classes are inherited from. THIS ALSO USES POLYMORPHISM AS ENCRYPTION CLASSES USE THE METHODS DIFFERENTLY
class encryption_algorithm: 
    def __init__(self):
        self.error = error_handling() # composition - this take the sub class of error_handling and now has all its function. this will be inherited by the encryption classes to handle any user errors

#error handling

    def error_checking(self):
        raise NotImplementedError("Subclasses must implement the error checking method.")
    
    def encrypt(self, message, key):
        raise NotImplementedError("Subclasses must implement the encrypt method.")

    def decrypt(self, message, key):
        raise NotImplementedError("Subclasses must implement the decrypt method")
    
    def get_summary(self):
        raise NotImplementedError("Subclasses must implement the summary method.")
    
#implementation of a stack data structure
class stack:
    def __init__(self): #instantiates the class
        self.items = []

    def is_empty(self): #it checks if the stack is empty and returns true or false if not
        return len(self.items) == 0

    def push(self, item): #this pushes an item on top of the stack
        self.items.append(item)

    def pop(self): # this pops an item off of the stack
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("this stack is empty, you can not pop from an empty stack") # if the stack is empty, it will return an error

    def peek(self):
        if not self.is_empty():
            return self.items[-1] # this allows the user to see the top of the stack
        else:
            raise IndexError("this stack is empty, you can not peek from an empty stack") # if the stack is empty, it will return an error

    def size(self):
        return len(self.items) # this returns the size of the stack

#searching algorithm    
class binary_search:        #implementation of the binary search algorithm
    def search(self, List, Target): # this is the search function
        Lower_Bound = 0 # setting the lower bound
        Upper_Bound = len(List) - 1 #setting the upperbound
        Amount_Of_Searches = 0 #this records the amount of searches it takes
        Found = False # set the 'found' as false

        while Lower_Bound <= Upper_Bound: #this makes a loop until the indexes of the lower and the upper bound are at the same position
            Midpoint = (Lower_Bound + Upper_Bound) // 2 # this finds the midpoint of the list

            if List[Midpoint] == Target: # if the target is at the midpoint, it sets found as true and breaks out of the loop
                Found = True
                break
            elif Target > List[Midpoint]: #if the target is larger than the midpoint that means that the target is found in the section above the midpoint of the list not below
                Lower_Bound = Midpoint + 1 #the lower bound then becomes the midpoint +1 because its not the mid point or below it

            else: #else, the target is in the lower part of the list, below the midpoint
                Upper_Bound = Midpoint - 1 # the midpoint becomes the upper bound minus 1
            
            Amount_Of_Searches += 1 # imcrement by search by 1
                
        if Found == True: # once found, found is set to true
            print(f'{Target} was found at index {Midpoint} in {Amount_Of_Searches} searches.') # the target was found and it shows when
            return Found
        else:
            return False

#sorting algorithm, recursion    
class quick_sort:
    def quicksort(self, array, left, right):
        if left < right:
            partition_index = self.partition(array, left, right) #recursion
            self.quicksort(array, left, partition_index - 1)
            self.quicksort(array, partition_index + 1, right)

    def partition(self, array, left, right):
        i = left
        j = right - 1
        pivot = array[right]

        while i < j:
            while i < right and self.compare_strings(array[i], pivot) < 0:
                i += 1
            while j > left and self.compare_strings(array[j], pivot) >= 0:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]

        if self.compare_strings(array[i], pivot) > 0:
            array[i], array[right] = array[right], array[i]

        return i

    def compare_strings(self, string1, string2):
        # used to compare alphanumeric strings, as the original implementation didn't work with alphanumeric strings
        def natural_keys(s):
            
            return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)] # regular expression, list comphrehension

        key1 = natural_keys(string1)
        key2 = natural_keys(string2)

        return (key1 > key2) - (key1 < key2)

#------------------------------------------------------------------------------------------------------error handling------------------------------------------------------------------------------------------------------------------------
    
#error handling - this checks whether the user hasn't made any errors when trying to execute the encryption/decryption
class error_handling(): 
    def empty_key_checker(self, key): # checks if key is empty
        if not key:
            messagebox.showerror('key Error', 'Error: The key can not be empty! please enter a valid key.')
            raise Exception('Please try again.') #kills currents encryption/decryption
        
    def empty_message_checker(self, message): # checks if message box is empty
        if not message:
            messagebox.showerror('Input Error', 'Error: The message can not be empty! please enter a valid message.')
            raise Exception('Please try again.') #kills currents encryption/decryption
        
    def key_value_checker_int(self, key): # checks if the value of the key is correct for the certain encryption for example railfence needs numbers
        try:
            int(key)
        except:
            messagebox.showerror('Input Error', 'Error: The key must be a integer! please enter a valid key.')
            raise Exception('Please try again.') #kills currents encryption/decryption
        
    def key_value_checker_str(self,key): #checks if the value of the key is correct for the certain encryption for example vigenere needs letters
        try:
            int(key)
            messagebox.showerror('Input Error', 'Error: The key must be a string! please enter a valid key.')
            raise Exception('Please try again.') #kills currents encryption/decryption
        except:
            pass

    def message_and_key_length(self, message, key): # checks if the length of the key and the message are the same, for example, the vigenere needs the same length
        if len(key) != len(message):
            messagebox.showerror('key Error', 'Error: For Maximum protection, this algorithm requires they key and message to be the same length, please do this.')
            raise Exception('Please try again.') #kills currents encryption/decryption
        
    def key_not_coprime(self,key): # checks if the key is coprime with the size of the alphabet, in the case of the affine cipher, this is a requirement for the encryption to work.
        gcd, _ , _ = egcd(key[0], NUMBER_OF_LETTERS_IN_ALPHABET)
        if gcd != 1:
            messagebox.showerror('key Error', "Error: part 'a' (the first integer) of the key is not co-prime with the size of the alphabet, please choose a different integer i.e. 17")
            raise Exception('Please try again.') #kills currents encryption/decryption
        

    def wrong_format(self,key): # for the affine cipher you will need to input a key separating the integer with a single comma, this makes sure it is in that format
        character_count = 0
        for character in key:
            if character == ',':
                character_count += 1
        if character_count != 1:
            messagebox.showerror('key Error', 'the integers must be seperated by a single comma')
            raise Exception('Please try again.') #kills currents encryption/decryption
    
    def empty_bitsize_checker(self, bit_size): #checks if no bitsize has been entered
        if not bit_size:
            messagebox.showerror('bit size Error', 'please enter a bit size!')
            raise Exception('Please try again.') #kills currents encryption/decryption
    def small_bitsize_checker(self, bit_size):
        if int(bit_size) <= 5:
            messagebox.showerror('WARNING', 'Warning: The bit must be more than 5! please enter a valid bit size.')
            raise Exception('Please try again.') #kills currents encryption/decryption

    
    def bit_size_value_checker_int(self, bit_size): # checks if the value of the bit size is correct for RSA
        try:
            int(bit_size)
        except:
            messagebox.showerror('Input Error', 'Error: The bit must be a integer! please enter a valid bit size.')
            raise Exception('Please try again.') #kills currents encryption/decryption
                  
#--------------------------------------------------------------------------------------encryption classes-------------------------------------------------------------------------------------------------------------------------------------------
        
#loops, if statements, lists        
class caesar_cipher(encryption_algorithm):
    def error_checking(self, message, key): # this is a wrapper function that calls all the error_handling functions from the error_handling class that is needed in the caesar cipher class
        self.error.empty_key_checker(key)
        self.error.empty_message_checker(message)
        self.error.key_value_checker_int(key) 

    def encrypt(self, message, key):    #encrypt method    
        self.error_checking(message,key)

        encrypted_message_list = [] 
        for message_letter in message.upper():
            if message_letter.isalpha(): #checks if it's in alphabet   
                message_value = ord(message_letter) - ord('A')
                encrypted_value = (int(key) + message_value) % NUMBER_OF_LETTERS_IN_ALPHABET
                encrypted_letter = encrypted_value + ord('A')

                encrypted_message_list.append(chr(encrypted_letter))
            else:
                encrypted_message_list.append(message_letter)

        return ''.join(encrypted_message_list)
    
    def decrypt(self, message, key):
        self.error_checking(message,key)

        decrypted_message_List = []
        for letter in message.upper():
            if letter.isalpha(): #checks if it's in alphabet    
                message_value = ord(letter) - ord('A')
                decrypted_value = (message_value - int(key)) % NUMBER_OF_LETTERS_IN_ALPHABET
                decrypted_letter = decrypted_value + ord('A') 

                decrypted_message_List.append(chr(decrypted_letter))
            else:
                decrypted_message_List.append(letter)
        return ''.join(decrypted_message_List)

    def get_summary(self):
        return '''The Caesar cipher is a simple substitution cipher used in ancient Rome created by Julius Caesar. Due to its simple implementation, it is a commonly used cipher to introduce
 students into the world of encryption. It works by shifting the alphabet by a number specified in the key. It is a Symmetric Cipher, that can easily be broken by methods such as
 brute force and frequency analysis. The Caesar cipher is a simple encryption which applies a mathematical function to each letter position to change the output. Choose
 a number to be the key shift. Choose a word to be the plain text.  '''

#multi-dimensional arrays, 
class rail_fence(encryption_algorithm):    
    def error_checking(self, message, key):
        self.error.empty_key_checker(key)
        self.error.empty_message_checker(message)
        self.error.key_value_checker_int(key)

    def encrypt(self, message, key):
        self.error_checking(message,key)
        key = int(key)
        rails = []
        for _ in range(key):  
            rails.append([])

        position = 0 #determines which rail is currently being manipulated
        ascension = True # determines where the the loop is ascending or descending
        for letter in message: #loops through each character in the message
            rails[position].append(letter) # this appends the letter in the rail specified by the position variable
            if position == (key - 1): # if the position is the last rail 
                ascension = False  # it is no longer ascending and the rail position begins to decrease by 1
            if position <= (key - 1) and ascension == False: #if the position is less than or equal to the index of the last rail, and it is in descending mode. 
                position -= 1 #this means that the rail position begins to decrease by 1
            elif position < (key - 1) and ascension: # if the position is less than the last rail index, and it is in ascending mode.
                position += 1 # this means that the rail position begins to increase by 1
            if position == 0: #if the rail position is back at the beginning index. 
                ascension = True  #it is in ascending mode

        list_of_rails = []

        for i in range(0, key):
            test = ''.join(rails[i])
            list_of_rails.append(test)
        

        encrypted_text = ''.join(list_of_rails) 

        return encrypted_text 
    
    def decrypt(self, message, key):
        self.error_checking(message,key)
        key = int(key)
        rails = []
        for _ in range(key):
            rails.append([])

        rails = []
        for _ in range(key):  
            rails.append([])

        position = 0 #determines which rail is currently being manipulated
        ascension = True # determines where the the loop is ascending or descending
        for _ in message:  #loops through each character in the message
            rails[position].append("*") # this appends a placeholder value in the rail specified by the position variable
            if position == (key - 1): # if the position is the last rail
                ascension = False # it is no longer ascending and the rail position begins to decrease by 1
            if position <= (key - 1) and ascension == False: #if the position is less than or equal to the index of the last rail, and it is in descending mode. 
                position -= 1 #this means that the rail position begins to decrease by 1
            elif position < (key - 1) and ascension: # if the position is less than the last rail index, and it is in ascending mode.
                position += 1 # this means that the rail position begins to increase by 1
            if position == 0: #if the rail position is back at the beginning index. 
                ascension = True #it is in ascending mode
        
        message_pos = 0
        for rail in rails:
            for i in range(len(rail)):
                rail[i] = message[message_pos]
                message_pos += 1        
        
        rail_indexes = []
        for _ in range(key): # index for each rail
            rail_indexes.append(0)
        
        decrypted_message = "" #contains string of decrypted message
        current_rail_position = 0 #determines which rail is being manipulated
        
        for _ in range(len(message)): #loops through code for the length of the message
        
            current_rail = rails[current_rail_position]
            rail_index = rail_indexes[current_rail_position] #rail index contains the index for the current rail.
            decrypted_message += current_rail[rail_index] #takes the character at the index of the current rail
            rail_indexes[current_rail_position] += 1 #increasing the index of the current rail position by 1
            
            if current_rail_position == 0: # start
                ascension = True  # if rail position is the first rail, it is no longer descending and the rail position begins to increase by 1
            elif current_rail_position == (key - 1): # end 
                ascension = False  # if rail position is the furthermost rail, it is no longer ascending and the rail position begins to decrease by 1
                             
            if ascension == False:
                current_rail_position -= 1 # ascension is false, so the rail position is decreasing
            else: 
                current_rail_position += 1  # ascension is true, so the rail position is increasing        
            
            
        return decrypted_message

    def get_summary(self):
        return '''The railfence cipher is a fun cipher. it was used by the ancient greeks in the scytle, a mechanical system used to produce ciphers. it consisted of a cylinder with a ribbon wrapped around it, the plaintext was wrote down onto the ribbon. The ciphertext was easily encrypted using a scytale of the same diameter. The modern method is to use 'rails', press the 'how does it work' button to find out more. 

'''



class vigenere_cipher(encryption_algorithm):    
    def error_checking(self, message, key): #error handling
        self.error.empty_key_checker(key)
        self.error.empty_message_checker(message)
        self.error.key_value_checker_str(key)
        self.error.message_and_key_length(message, key)
    
    
    def encrypt(self, message, key):
        encrypted_message_list = [] 

        self.error_checking(message,key)

        for message_letter, key_letter in zip(message.upper(), key.upper()): #this loops through both message and key letters using zip function
            if message_letter.isalpha() == True and key_letter.isalpha() == True: #working only on alphabetic characters
                message_value = ord(message_letter) - ord('A') #vigenere implementation
                key_value = ord(key_letter) - ord ('A')
                encrypted_value = key_value + message_value
                encrypted_value = encrypted_value % NUMBER_OF_LETTERS_IN_ALPHABET

                encrypted_letter = chr(encrypted_value + ord('A'))

                encrypted_message_list.append(encrypted_letter)
                
            else:
                encrypted_message_list.append(message_letter)            

        encrypted_text = ''.join(encrypted_message_list)
    
        return encrypted_text
    
    def decrypt(self, message, key):
        self.error_checking(message,key)

        decrypted_message_List = []
        for message_letter, key_letter in zip(message.upper(), key.upper()): #loops through both ciphertext and key letters uing zip function
            if message_letter.isalpha() == True and key_letter.isalpha() == True: #only applying to alphabetic characters
                message_value = ord(message_letter) - ord('A') #implementation of vigenere decrypt  
                key_value = ord(key_letter) - ord('A')
                decrypted_value = message_value - key_value 
                decrypted_value = decrypted_value % NUMBER_OF_LETTERS_IN_ALPHABET

                decrypted_letter = chr(decrypted_value + ord('A'))

                decrypted_message_List.append(decrypted_letter)
            else:
                decrypted_message_List.append(message_letter)

        decrypted_text = ''.join(decrypted_message_List)

        return decrypted_text #returns decrypted message

    def get_summary(self): #returns the summary of the encryption
        return '''The vigenere cipher is known as the two-time pad. It was invented in 1553 by an italian cryptographer names Giovan Battista Bellaso. is a type of substitution cipher used for data encryption in which several monoalphabetic substitutions happen rather than one. Click the 'how does it work' for more information!
    ''' 
    

class vernam_cipher(encryption_algorithm):
        
    def error_checking(self, message, key): #error handling
        self.error.empty_key_checker(key)
        self.error.empty_message_checker(message)
        self.error.key_value_checker_str(key)
        self.error.message_and_key_length(message, key)

    def generate_key(self, message): #gemerates a random key
        one_time_key = ''
        characters = message.replace(" ", "") #removes all whitespace in message
        message = ''
        for letter in characters:
            message += letter
            

        for i in range(len(message)): #loops for the size of the message 
            one_time_key +=secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') #generates a random combination of letters using secrets library for the size of the message
            
        return one_time_key


    def encrypt(self,message,key):
        
        self.error_checking(message,key)

        encrypted_message = ''

        
        characters = message.replace(" ", "") #removes all whitespace
        message = ''
        for letter in characters:
            message += letter
        


        for index, letter in enumerate(message.lower()):


            encrypted_letter = (ord(key[index])^ord(letter)) #applies xor to each of the characters by turning it into its ascii characters first then xor'ing
            encrypted_message += chr(encrypted_letter) #turns it back into characters and initialises the encrypted message

       

        return encrypted_message #returns encrypted message




    
    def decrypt(self, message, key):
        
        self.error_checking(message,key)

        decrypted_message = ''

        
        message = message.replace(" ", "") #removes all whitespace


        for index, letter in enumerate(message.lower()):


            decrypted_letter = (ord(key[index])^ord(letter)) #use of xor to decrypt message
            decrypted_message += chr(decrypted_letter)
            

        return decrypted_message #returns decrypted message

    
    def get_summary(self): #returns summary of encryption
        return 'the vernam cipher - named after Gilbert Vernam who co-founded the one-time pad cipher in 1917, it is said to be one of the most important ciphers in cryptograph history!'

class affine_cipher(encryption_algorithm):

    def error_checking(self, message, key):#errorhandling
        self.error.empty_key_checker(key)
        self.error.wrong_format(key)
        try:
            key = str_to_list_of_ints(key, separator=",") #calling utility function
        except:
            messagebox.showerror('key Error', 'The key needs to be fully integer.')
        self.error.key_not_coprime(key)
        self.error.empty_message_checker(message)
        return key
    
    def encrypt(self, message, key):        
        key = self.error_checking(message,key)
        encrypted_message_list = [] #list
        for letter in message.upper(): 
            if letter.isalpha(): #executing of alphabetic characters
                encrypted_letter = (chr(((key[0]*(ord(letter) - ord('A'))+ key[1]) % NUMBER_OF_LETTERS_IN_ALPHABET) + ord('A'))) #coded format of the encryption formula: E(x) = (ax + b) mod m
                
                encrypted_message_list.append(encrypted_letter)
            else:
                encrypted_message_list.append(letter)
        return ''.join(encrypted_message_list)      

    def decrypt(self, message, key):
        key = self.error_checking(message, key)
        decrypted_message_list = [] #list
        for letter in message.upper():
            if letter.isalpha():
                decrypted_letter = (chr(((modinv(key[0], NUMBER_OF_LETTERS_IN_ALPHABET)*(ord(letter) - ord('A') - key[1]))% NUMBER_OF_LETTERS_IN_ALPHABET) +ord('A'))) #coded format of the decryption formula: D(y) = a⁻¹ ⋅ (y-b) mod m, i use high level mathematics with my modular inverse library function called here
                
                decrypted_message_list.append(decrypted_letter)
            else:
                decrypted_message_list.append(letter)
        return ''.join(decrypted_message_list)

    def get_summary(self): #returning summary
        return "Affine Cipher's origin is not precisely known, as it is a type of substitution cipher that has been found throughout history by various cultures, by using similar methods. This is a great starter for encryptions using Modular inverse. it would be beneficial to understand this before attempting to understand the RSA Algorithm. "



class RSA_Algorithm(encryption_algorithm):
#researched on rabin millers primality test and incorporated it into code
    @staticmethod #use of static methods 
    def primality_test(num, num_of_rounds): #miller rabin's test algorithm to test if a number if prime or not.

        if num == 2: #if the number is equal to 2, it is a prime number.
            return True

        if num % 2 == 0: #if the number is even, it is not a prime
            return False

        power_of_two_exponent, odd_num = 0, num - 1
        while odd_num % 2 == 0:
            power_of_two_exponent += 1 #power_of_two_exponent = power_of_two_exponent +1
            odd_num = odd_num//2 
        for _ in range(num_of_rounds): #loops
            rand_num = random.randrange(2, num - 1)
            result_of_mod = pow(rand_num, odd_num, num) #use of pow 
            if result_of_mod == 1 or result_of_mod == num - 1:
                continue
            for _ in range(power_of_two_exponent - 1):
                result_of_mod = pow(result_of_mod, 2, num)
                if result_of_mod == num - 1:
                    break
            else:
                return False
        return True
    
    @staticmethod #static method
    def is_prime(PrimeNumber):
        return RSA_Algorithm.primality_test(PrimeNumber, 64)#function wrapper, called
    
    @staticmethod #static methods
    def prime_number_generation(Bits): #generates a random number and then callsis_prime function to check primality
        while True:
            num = random.randrange(2**(Bits-1), (2**Bits)-1)
            if RSA_Algorithm.is_prime(num):
                return num   

    def key_generation(self, nbits):
        print(nbits, "bits")
        p = RSA_Algorithm.prime_number_generation(nbits) #this generates a certain amount of bit specified by the user.
        print(p, "is prime")
        q = RSA_Algorithm.prime_number_generation(nbits) #this generates a certain amount of bit specified by the user.
        print(q, "is prime")

        n = p*q

        phi = (p-1)*(q-1) #generating phi 

        e =  65537 #universal value of public exponent

        d = modinv(e,phi) #use of highlevel maths in modular inverse


        public_key = (e, n) #sets up public key 
        private_key = (d, n) #sets up private key

        return public_key, private_key
    

    def error_checking(self, message, key):
        self.error.empty_message_checker(message)
        self.error.empty_key_checker(key)
    
    def encrypt(self, message, public_key): # key is public key: e, n
        
        self.error_checking(message, public_key)

        public_key = str_to_list_of_ints(public_key) #utility function


        e, n = public_key[0], public_key[1]        
        

        encrypted_message_list = []
        for char in message: #looping and encrypting
            encrypted_number = (ord(char) ** e) % n
            encrypted_message_list.append(encrypted_number)

        for index, bits in enumerate(encrypted_message_list): #use of enum

            encrypted_message_list[index] = encrypted_message_list[index].to_bytes((encrypted_message_list[index].bit_length() + 7) // 8, 'big')
            encrypted_message_list[index] = base64.b64encode(encrypted_message_list[index]) #using base64 encoding to encode the integers into random ascii value

        
        return encrypted_message_list

    def decrypt(self, encrypted_message, private_key):


        private_key = str_to_list_of_ints(private_key)
        encrypted_message = str_to_list(encrypted_message)
        
        for index, bits in enumerate(encrypted_message):
            
            encrypted_message[index] = base64.b64decode(encrypted_message[index])
            encrypted_message[index] = int.from_bytes(encrypted_message[index], 'big') #using base64 encoding to decode the ascii values back into integers


        d, n = private_key[0], private_key[1]
        decrypted_message = ""
        for encrypted_number in encrypted_message: #decrypting
            decrypted_char = chr(pow(encrypted_number, d, n)) #use of pow
            decrypted_message += decrypted_char
        
        return decrypted_message

    def get_summary(self): #research was done to find how the euclidean algorithm works. 
        return '''RSA algorthm is an asymmetric encryption algorithm, named after the three creators - Rivest, Shamir and Adlemen. Created in 1977, it remains crucial for protected communication of data over the internet. a key role is euclidean's algorithm, used to find modular inverse. The steps are shown below.    
        \n1. Initialization:
    • Choose your e and phi values.
    • Start with the coefficients x1 = 1, y1 = 0, x2 = 0, y2 = 1.
2. Applying the Extended Euclidean Algorithm:
    • make a loop using the formula below until the remainder becomes 0:
        remainder = e - e - [phi/e] · (n)
    • Swap coefficients: x1 ↔ X2, Y1 ↔ Y2.
    • Update e to phi and phi to the remainder.
3. Finding Coefficients:
    • We continue the loop until the remainder becomes 0.
    • The last non-zero remainder's coefficients x2 and y2 are the coefficients for the linear
      equation ex + ϕ(n)y = 1. where ϕ(n) = phi 
      
BONUS: if x2 is a negative number, we add phi so it becomes positive '''
    
#-----------------------------------------------------------------------------------------------------------frames initialisation for encryption explanations---------------------------------------------------------------------------------------------------
class encryption_explanation:
    def __init__(self, algorithm_name, window):
        self.algorithm_name = algorithm_name
        self.window = window
        self.encrypt_explanation_frame = tk.Frame(self.window, bg='#383444')
        self.encrypt_explanation_frame2 = tk.Frame(self.window, bg='#383444')
        self.decrypt_explanation_frame = tk.Frame(self.window, bg='#383444')
        self.decrypt_explanation_frame2 = tk.Frame(self.window, bg='#383444')
        self.frames = [self.encrypt_explanation_frame, 
                      self.encrypt_explanation_frame2,
                      self.decrypt_explanation_frame,
                      self.decrypt_explanation_frame2,
                       ] #list of frames, this is to implementing a sort of paging window
        
        self.current_frame = self.encrypt_explanation_frame

        self.setup_frames()

    def showframe(self, frame):
        frame.tkraise()

    def information(self): #texts for widgets
        if self.algorithm_name == 'Caesar Cipher':
            texts = {'caesar page 1':'''The Caesar cipher is a simple substitution cipher, it works by shifting the alphabet by a number specified in the key. It is a Symmetric Cipher, that can easily be broken by methods such as brute force and frequency analysis. Lets do an example, lets encrypt the message, 'HELLO' by a key shift of '3'! 'H' is the 8th letter of the alphabet. 

If we shift it by 3, the encrypted letter would be K! if we apply it to 'E' we get 'H', If we continue, the final output will be 'KHOOR'. However as you can see, its only a substitution, both 'L's have been encrypted to O - showing the weakness of the Caesar cipher.
 
                     ''',

    'caesar page 1 conclusion': '''Lets draw a diagram of this example, click on the next page to see it!''',
    'caesar alphabet': '''A B C D E F G H I J K L M N O P Q R S T U V W X Y Z''',
    'caesar page 2 conclusion': '''As you can see, the encryption is fairly simple, the diagram depicts an encryption with key shift 3 to the plaintext HELLO. refer to the alphabet above and move three to the right! 

To see the decryption process, go to the next page!''',

    'caesar page 3': '''For the decryption process, its essentially the same thing, just in reverse. This time, the key shift moves backwards with the alphabet. so
if the key was 4 and we wanted to decrypt B. We would move back four positions in the alphabet. B > X. When dealing with a shift that
takes the letter to after the end, or before the start of the alphabet, we loop around the alphabet. As seen here. In code, we can do this
by applying a modulo of the length of the alphabet (26) to the result of the decryption.''',

    'caesar page 3 conclusion': '''Lets draw a diagram of this! Lets try decrypting the message NYPMYW with a key shift 4. click on the next page to see it!''',
    'caesar page 4 conclusion': '''As you can see, the decryption is quite simple too! Now it's your turn, enter a message into the message box as well as a key shift. then, press encrypt! to decrypt it, switch modes then press 'previous encrypted message' to retrieve the last encrypted message (this works for encrypt mode too), then just press decrypt! what's the encryption of 'hello world' with a key of 5? test it out!'''
                    }
        
        elif self.algorithm_name == 'Rail Fence Cipher':
            texts= {'Rail Fence page 1':'''The Rail Fence Cipher is a transposition cipher. As seen in the summary, the original method was to use a mechanic system called a
scytale. But today, the modern method uses rails to depict the encryption of a plain text. The encryption works by writing the plain text
downwards and diagonally on successive rails, with the amount of rails in the imaginary fence dictated by the key. once the bottom rail is
reached, You start moving up. once the top rail is reached the message is written downwards. This process repeats until the whole
plain text is written out.''',

'Rail Fence page 1 new line': '''With this, we can break down this algorithm into its key steps, it works something like this: ''',

'Rail Fence page 1 directions': '''

    1.it take a given plain text from the user.
    2. the key decides how many 'rails' the algorithm has (in this case 3)
    3. the algorithm loops through the text, with every letter going onto the next 'rail line'.
    4. once the bottom most rail has been filled by a letter, the letters are placed on the next
        rail above, and so on and so forth until the top rail has been filled by a letter.
    5. this cycle is repeated until all letters have been place on a rail.
    6. the letters on each rail become one word to create the cipher text 
    with the top rail being the first word and the bottom rail being the last word. ''',

'Rail Fence page 1 conclusion': '''With this in mind, how about we try encrypting the phrase "WE ARE DISCOVERED RUN AT ONCE" with a key of 3 on the next page! ''',

'Rail Fence diagram': '''W . . . R . . . I . . . V . . . D . . . N . . .   . . . E
. E . A . E . D . S . O . E . E .   . U .   . T . O . C .
. .   . . .   . . . C . . . R . . . R . . . A . . . N . .
''',

'Rail Fence diagram explanation': '''As you can see the phrase has been encrypted with three rails. each letter is being placed using the 'diagonally down, diagonally up'
method. Now, to get the final cipher text, we make each rail into a word starting with the first rail, then the next, then the next, then the
next... and they you join each word to form the ciphertext! a diagram is down below:
''',

'Rail Fence diagram title': 'Keys (number of rails): 3       message: WE ARE DISCOVERED RUN AT ONCE',

'Rail Fence page 2 conclusion': '''Once we collect each of the rails, we get the ciphertext - "WRIVDN EEAEDSOEE U TOC  CRRAN"! It's as simple as that. 

To see the decryption process, click on the next page!''',

'Rail Fence page 3': '''The decryption process is a bit more complicated, but if we know the key, we can decrypt it! first, we need to form the 'rail' used to encrypt the plain text, because if we have this, we can form the original text. to pick the original characters of the message in order, we must make a 'placeholder rail' - with length of the message. lets use the example of "SEPTEYD.UST AN H K NIONSITSIG" with a key of 3:''',

'Rail Fence placeholder diagram': '''* . . . * . . . * . . . * . . . * . . . * . . . * . . . *
. * . * . * . * . * . * . * . * . * . * . * . * . * . * .
. . * . . . * . . . * . . . * . . . * . . . * . . . * . .
''',

'Rail Fence decryption diagram explanation': '''Once you have built the place holder rail fence, we can start the decryption proccess by filling up the placeholder with the encrypted message letters. this time, instead of going up and down, we fill the lines left to right. press the next page to see it step by step. ''',
'First Rail': ' S . . . E . . . P . . . T . . . E . . . Y . . . D . . . •',
'Second Rail':  '. U . S . T .   . A . N .   . H .   . K .   . N . I . O .',
'Third Rail': '. . N . . . S . . . I . . . T . . . S . . . I . . . G . .',

'Rail Fence decryption diagram':''' S . . . E . . . P . . . T . . . E . . . Y . . . D . . . •
 . U . S . T .   . A . N .   . H .   . K .   . N . I . O .
 . . N . . . S . . . I . . . T . . . S . . . I . . . G . .''',

'Rail Fence decryption diagram title': '''Now we have all the rails, if we combine them we get something like this!''',

'Rail Fence page 4 conclusion': '''Now, after we have made the rails, You just have to do the same process as the encryption:  collect each letter by going diagonally down until reaching the bottom rail, then diagonally up until reaching the top rail - and repeat! If we do it to this message, we get: SUNSETS PAINT THE SKY INDIGO. Now it's your turn, enter a message into the message box as well as a rail number. then, press encrypt! to decrypt it, switch modes then press 'previous encrypted message' to retrieve the last encrypted message (this works for encrypt mode too), then just press decrypt! whats the encryption of 'hello world' with a key of 4? test it out!'''
                   }
        elif self.algorithm_name == 'Vigenere Cipher':
            texts = {'Vigenere Cipher page 1': 'The Vigenere Cipher is a simple polyalphabetic substitution in which text (alphabetic) is encrypted using series of Caesar ciphers (refer to the caesar cipher explanation for more information) with different shifts based on key. Instead of using a number for the key, the Vigenere uses a key the same length as the message. This way you can use the vigenere table to encrypt and decrypt the message. It works like this: ',
                     'Vigenere page 1 directions': '''
1. generate the vigenere table

2. loop through each letter of plaintext and the key from beginnning to end

3. for each step, look at the letter from the plaintext and the letter from the key

4. we use those letters as co-ordinates on the vigenere table
with the plaintext letter being the Y Co-ordinate
and the key being the X co-ordinate.

5. the letter found from the co-ordinates becomes the letter
in our encrypted message.

6. this is done with each letters in the plaintext and key until the loop is finished.
''',

'Vigenere Cipher page 1 conclusion': '''With this method we can use the vigenere table to encrypt a message. How about we try encryption 'HELLO' with the key 'COINS'. Go onto the next page to see it!''',

'vigenere table': '''      A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z
    +------------------------------------------------------------------------------------------------------+
  A | A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z|
  B | B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A|
  C | C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B|
  D | D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C|
  E | E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D|
  F | F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E|
  G | G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F|
  H | H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G|
  I | I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H|
  J | J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I|
  L | L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K|
  M | M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L|
  N | N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M|
  O | O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N|
  P | P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O|
  Q | Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P|
  R | R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q|
  S | S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R|
  T | T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S|
  U | U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T|
  V | V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U|
  W | W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V|
  X | X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W|
  Y | Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X|
  Z | Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y|
    +------------------------------------------------------------------------------------------------------+''',

    'table explanation': '''using the steps we talked about before we get the cipher text 'JSTYG'. It's as simple as that! Click on the next page for the decryption explanation''',

    'decryption title': '''For the decryption, the process is exactly the same! we follow the same steps: ''',

    'decryption directions': '''1. generate the vigenere table

2. loop through each letter of ciphertext and the key from beginning to end

3. for each step, look at the letter from the ciphertext and the letter from the key

4. we use those letters. The key is the X co-rdinate at the top. we go to the key letter, 
and look through the letters in its column until we find the ciphertext letter. 
we then look at the Y co-ordinate value that the cipher text letter holds.

5. the letter found from the Y co-ordinate becomes the letter
in our decrypted message.

6. this is done with each letters in the ciphertext and key until the loop is finished.''',

'decryption page 1 conclusion': '''It's as simple as that, lets try decrypting the word 'YOTXIR' with the key, monkey. click on the next page to see. ''',

'decryption page 2 conclusion': '''Using the steps we talked about before we get the plaintext 'MAGNET'. It's as simple as that! Now it's your turn, enter a message into the message box as well as a key. then, press encrypt! to decrypt it, switch modes then press 'previous encrypted message' to retrieve the last encrypted message (this works for encrypt mode too), then just press decrypt! whats the encryption of 'HELLO WORLD' with a key 'COINS BOILS'? test it out!'''
                     }
            
        elif self.algorithm_name == 'Vernam Cipher':
            texts = {'Vernam Cipher page 1': '''The Vernam Cipher is a peculiar cipher - it's different from the rest. Normally, encryptions are seen as computationally secure. This means that the encryption's can't be cracked in a reasonable amount of time using a reasonable amount of computing power. However - they are STILL breakable. These are encryptions like the RSA (Rivest-Shamir-Adleman), AES (Advanced Encryption Standard) and ecetera. On the otherhand is considered unbreakable if certain conditions are met. The conditions are as follows:
\n1. The key must be truly random. 
\n2. The key must be the same length as the message or longer.
\n3. The key must can't be shared and must be one time use.
\nThe encryption technique is quite simple, yet, very effective. It works something like this:''',

'Vernam Cipher encrypt directions': '''1. iterate through the plaintext and pair each letter of the plaintext with the corresponding letter of the key (matching by index)
\n2.starting from the first pair apply a bit wise XOR to the ascii code of the key and plaintext characters. 
For example, a plaintext of 'HELLO' and key of 'COINS'.  Bitwising 'H' and 'C' would be equivalent of Bitwising their ASCII codes: 72 ^ 67. 
\n3. An XOR is an exclusive OR. Unlike, OR which outputs a 1 if there is atleast one 1, an XOR only outputs a 1 if one input bit is 0 and the other is 1, the XOR output is 1.
however if both input bits are 0 or both are 1, the XOR output is 0.
\n4. So in the case of 72 ^ 67, we turn them into there binary components. '1001000' and '1000011' and apply an XOR to get '0001011'. 
if we convert this back we get 11 which we can convert back to ASCII.
\n5. We then do this for every pair. 

\nWe can better explain this through a diagram explanation. click the next page to see!
''',

'ascii table':'''+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
|  a   |  b   |  c   |  d   |  e   |  f   |  g   |  h   |  i   |  j   |  k   |  l   |  m   |  n   |
+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
| 97   | 98   | 99   | 100  | 101  | 102  | 103  | 104  | 105  | 106  | 107  | 108  | 109  | 110  |
+------+------+------+------+------+------+------+------+------+------+------+------+------+------+
|  o   |  p   |  q   |  r   |  s   |  t   |  u   |  v   |  w   |  x   |  y   |  z   |
+------+------+------+------+------+------+------+------+------+------+------+------+
| 111  | 112  | 113  | 114  | 115  | 116  | 117  | 118  | 119  | 120  | 121  | 122  |
+------+------+------+------+------+------+------+------+------+------+------+------+
''',

'letter 1 encryption':'''h = 104, C = 67. 104 = 1101000 and 67 = 1000011. 1101000 ^ 1000011 = 101011. 101011 = 43''',
'letter 2 encryption': '''e = 101, T = 84. 101 = 1100101 and 84 = 1010100. 1100101 ^ 1010100 = 110001. 110001 = 49''',
'encryption conclusion': '''You then convert each of the ascii code into it's corresponding characters - combine them and get your new encrypted message - +1! To see the decryption process, click the next page!''',

'Vernam Cipher page 1 decryption': '''The Vernam Cipher decryption works exactly like the encryption process. This means that the decryption works as follows:''',


'Vernam Cipher decrypt directions': '''1. iterate through the ciphertext and pair each letter of the ciphertext with the corresponding letter of the key (matching by index)
\n2.starting from the first pair apply a bit wise XOR to the ascii code of the key and ciphertext characters. 
For example, a ciphertext of '+*%"<' and key of 'COINS'.  Bitwising '+' and 'C' would be equivalent of Bitwising their ASCII codes: 43 ^ 67. 
\n3. An XOR is an exclusive OR. Unlike, OR which outputs a 1 if there is atleast one 1, an XOR only outputs a 1 
if one input bit is 0 and the other is 1, the XOR output is 1.
however if both input bits are 0 or both are 1, the XOR output is 0.
\n4. So in the case of 43 ^ 67, we turn them into there binary components. '0101011' and '1000011' and apply an XOR to get '1101000'. 
if we convert this back we get 104 which we can convert back to ASCII to get the character 'h'.
\n5. We then do this for every pair. 

\nWe can better explain this through a diagram explanation. click the next page to see!
''',


'letter 1 decryption':'''? = 63, G = 71. 63 = 111111 and 71 = 1000111. 111111 ^ 1000111 = 1111000. 1111000 = 120''',
'letter 2 decryption': '''. = 46, V = 86. 46 = 101110 and 86 = 1010110. 101110 ^ 1010110 = 1111000. 1111000 = 120''',
'decryption conclusion': '''You then convert each of the ascii code into it's corresponding characters - combine them and get your encrypted message - xx! Now it's your turn, enter a message into the message box and then press 'generate key' to create a truly random key. then, press encrypt! to decrypt it, switch modes then press 'previous encrypted message' to retrieve the last encrypted message (this works for encrypt mode too), then just press decrypt! whats the encryption of 'HELLO WORLD' with a random key? test it out! '''


        }
        
        elif self.algorithm_name == 'Affine Cipher':
            texts = {'Affine page 1': '''The Affine cipher is a peculiar substitution cipher. It utilises mathematical concepts such as Modular Inverse. Therefore, this encryption is a great starter for cryptology that uses euclidean's algorithm and it's a great beginner for understanding the RSA algorithm. The letters in the alphabet is mapped to a numerical equivalent, for example - (a = 0, b = 1, c = 2, … z = 25). each letter is encrypted using a mathematical formula function with a key consisting of two integers, as parameters. The function is: ''',
                     
                    'Affine page 1 new line': 'E(x)=(ax+b) mod m',

                    'Affine page 1 new paragraph': '''a and b depict the first and second integer of the key. x is the plaintext letter numeric value, and m is a constant - the size of the alphabet.

                    
                    \nlet's give a step-by-step on how the encryption works:''',

                    'Affine page 1 directions': '''1. Choose your key - pick two integers; a and b, where a is coprime with the size of the alphabet (greatest common divisor = 1). \n2.Convert Letters to Numbers - Replace each letter of your message with its numeric equivalent using the alphabet encoding. \n3. encrypting - apply the encryption formula to produce the encrypted values. \n4. Convert Numbers to Letters - replace each number with the corresponding letter using the alphabet encoding.
\nYou now have your encrypted message. We can visualise this better using a diagram, click the next page to see.''',

'alphabet': 'A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z',
'numbers':  ' 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25',

'title': '''Lets encrypt 'HELLO' with the key '5, 8' ''',

'encryption1': ''''H - 7': E(7)=( 5 x 7 + 8) mod 26 = 17 ''', 
'encryption2': ''''E - 4': E(4)=( 5 x 4 + 8) mod 26 = 2 ''',
'encryption3/4': ''''L - 11': E(11)=( 5 x 11 + 8) mod 26 = 11''',
'encryption5': ''''O - 14': E(14)=( 5 x 14 + 8) mod 26 = 0''',

'conversions': '''These convert into 'R', 'C', 'L', 'L', 'A' ''',

'conclusion': '''The encrypted message is 'RCLLA', its as simple as that! Also, as you can see, both 'L's are mapped to the same encrypted letter, meaning that the cipher is subject to frequency analysis. To see the decryption process, go to the next page!''',

'Affine decryption page 1': '''The Affine cipher's decryption is complicated. As mentioned prior, it uses Modular inverse. this is the inverse of the function we used to encrypt the message. \nWhen we say a mod m, it means finding the remainder when a is divided by m. the modular inverse of a, in other words a⁻¹, is a number, that when multiplied by a, gives the remainder of 1 when divided by m. this can be shown as: 'a ⋅ a⁻¹ ≡ 1 mod m'. This allows us to 'undo' the affine cipher encryption. Using this concepts we can create the formula:''',

'Affine decryption page 1 new line': 'D(y) = a⁻¹ ⋅ (y-b) mod m',

'Affine decryption page 1 new paragraph': '''a and b depict the first and second integer of the key. y is the cipher letter numeric value, a⁻¹ is a number that when multiplied by a, and the modulus of m is applied, the remainder is 1. m is a constant - the size of the alphabet.''',

'Affine decryption page 1 directions': '''1. Choose your key - choose the two integers,  a and b, that were used to encrypt the message prior. \n2.Convert Letters to Numbers - Replace each letter of your ciphertext with its numeric equivalent using the alphabet encoding. \n3. decrypting - apply the decryption formula to produce the decrypted values. \n4. Convert Numbers to Letters - replace each number with the corresponding letter using the alphabet encoding.
\nYou now have your decrypted message. We can visualise this better using a diagram, click the next page to see.''',

'decryption1/4': ''''R - 17': D(17)= 7 ⋅ (17 - 18) mod 26 = 19 ''', 
'decryption2': ''''A - 0': D(0)= 7 ⋅ (0 - 18) mod 26 = 4 ''',
'decryption3': ''''Z - 25': D(25)= 7 ⋅ (25 - 18) mod 26 = 23''',
'decryption5': ''''C - 2': D(2)= 7 ⋅ (2 - 18) mod 26 = 18''',
'decrypt_conversions': '''These convert into 'T', 'E', 'X', 'T', 'S' ''',
'decrypt_conclusion': '''The decrypted message is 'TEXTS'. 'a⁻¹' was found using the EXTENDED EUCLIDEAN ALGORITHM (look at the RSA explanation to learn more). It's as simple as that! Now it's your turn, enter a message into the message box and then enter two integers, a and b, (with 'a' being coprime with the size of the alphabet) as the key. make sure the two integers are separated by a comma. then, press encrypt! to decrypt it, switch modes then press 'previous encrypted message' to retrieve the last encrypted message (this works for encrypt mode too), then just press decrypt! whats the encryption of 'HELLO WORLD' with a key of 57? test it out! '''




                     
                     }
        elif self.algorithm_name == 'RSA Algorithm':
            texts = {'RSA page 1': '''The RSA algorithm is a popular cipher in todays world of cryptology. It is used in protecting data across the internet through schemes such as digital signatures. unlike other encryptions in the program, the RSA algorithm is an asymmetric cipher - this means it consists of two keys - the public and private key. the public key is used to encrypt the message, while the private key, which is kept secret, is used to decrypt the message. Although it is not unbreakable like the Vernam cipher, its pretty close. The security relies on the difficulty of factoring two large prime numbers. 
\n                                                                                    The steps for creating the keys are as follows:''',
                     
                     'RSA key directions 1': '''1. Select 2 large prime numbers, p and q - lets say the bitsize is 2048, this means that you will randomly generate a number between 1 and (2²⁰⁴⁸ - 1). in code, you would randomly choose a number and then check its primality by using MILLER RABIN'S test for primality.
\n2. Phi Generation - After selecting two prime numbers, we multiply them together, denoted as n, it is a crucial part of the public key: ''',

'RSA key directions 2': '''we then calculate Euler's totient function: ϕ(n) = (p - 1)(q - 1). The Euler function finds the number of positive integers, less than a given number, that are coprime (refer to the affine explanation) to that number.
\n3. exponent generation - we then choose an integer for the 'public exponent', given by the restriction:  ''',
'RSA key directions 3': '''4. We then use an equation to encrypt the message using the public exponent and the product of two prime numbers, n. Note that in the RSA algorithm it is universal to set the public exponent to 65 5337 
\n The equation utilises modulus, the RSA algorithm denotes the equation as:  ''',

'conclusion': '''thats the key generation for the public key. In the encryption equation, 'e' denotes the public exponent, 'm' denotes the message, 'c' denotes the ciphertext, 'n' denotes the product of the two prime numbers. lets do a small example on the encryption process.''',

'alphabet': 'A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z',
'numbers':  ' 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25',
'n generation': 'n = (3) x (7)',
'encryption': 'c ≡ mᵉ mod n',
'letter encryption': '2 ≡ 11⁵ mod 21',
'encryption conclusion': '''For simplicity, i mapped each letter to a small value, in actual code, we use characters corresponding ASCII Values. in this case the encrypted message was 2, we can convert this into it's mapped letter, 'C'. And that's it, its as complicated as that!, click the next page for the decryption process''',

'RSA decrypt page 1': '''The decryption process utilises modular inverse in the private key generation. In theory, the decryption itself is simple, following the same process as the encryption, just with a different mathematical formula. However, obtaining the private key is a different story. it uses 'd', the private exponent, 'n', the result of Euler's totient function, and 'mod' which is modulus.
\n                                                                                    The steps for creating the keys are as follows:''',

'RSA private key direction 1': '''1. Please note, the private and the public key are generated at the same time. Follow the same steps as shown prior, calculate the totient function, and the public exponent.
\n2. we then use the modular inverse of the public exponent modulo ϕ(n) to create the private exponent - 'd' note that in the RSA algorithm it is universal to set the public exponent to 65 5337 
\nTo find the modular inverse, we use the extended euclidean algorithm. the algorithm denotes the equation: ''',
'RSA private key direction 2': '''We use the public exponent 'e' and 'ϕ(n)' so we can find the private key, where the coefficient 'x' becomes the modular inverse meaning the private exponent 'd' = x. This is crucial and now allows us to decrypt the message using the equation: ''',
'decrypt conclusion': '''thats the key generation for the private key. In the decryption equation 'd' denotes the private exponent, 'm' denotes the message, 'c' denotes the ciphertext, 'n' denotes the product of the two prime numbers. lets do a small example on the decryption process.''',
'phi decryption generation': 'ϕ(n) = (5 - 1)(11 - 1)',

'decryption': 'm ≡ cᵈ mod n',

'decrypting letter': '18 ≡ 2²⁷ mod 55',

'decryption conclusion 2': '''For simplicity, i mapped each letter to a small value, in actual code, we use characters corresponding ASCII Values. in this case the decrypted message was 18, we can convert this into it's mapped letter, 'S'. And that's it, its as complicated as that! Now it's your turn, enter a message into the message box, a bitsize, and then press 'generate key' to create the public and private keys. then, press encrypt! to decrypt it, switch modes then press 'previous encrypted message' to retrieve the last encrypted message (this works for encrypt mode too), then just press decrypt! whats the encryption of 'HELLO WORLD' with a bitsize of 150? test it out! Please note, in the program, base64 encoding is used to encode the integers into random ascii characters for security. '''


            
            
                    }
        return texts
    


    

    def setup_frames(self):
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        for frame in self.frames: #going through frames
            frame.grid(row=0, column=0, sticky='nsew')

        self.texts = self.information() #calling texts for specific algorithm

        self.screen_width = self.window.winfo_screenwidth()
        self.encrypt_explanation_title = tk.Label(self.encrypt_explanation_frame, text=f'How does the {self.algorithm_name}\'s encryption work?', bg='#383444', fg='white', font=("Helvetica", 12, "bold underline"))
        self.encrypt_explanation_title.pack(fill='x')

        self.encrypt_explanation_button = tk.Button(self.encrypt_explanation_frame, text='Next Page', command=lambda: self.showframe(self.encrypt_explanation_frame2), width = 20, height = 2) #use of lambda to delay function call
        self.encrypt_explanation_button.place(x=1700, y=960)

        self.encrypt_explanation_title2 = tk.Label(self.encrypt_explanation_frame2, text=f'How does the {self.algorithm_name}\'s encryption work?', bg='#383444', fg='white', font=("Helvetica", 12, "bold underline"))
        self.encrypt_explanation_title2.pack(fill='x')

        self.encrypt_explanation_button2 = tk.Button(self.encrypt_explanation_frame2, text='Next Page', command=lambda: self.showframe(self.decrypt_explanation_frame), width = 20, height = 2)
        self.encrypt_explanation_button2.place(x=1700, y=960)

        self.decrypt_explanation_title = tk.Label(self.decrypt_explanation_frame, text=f'How does the {self.algorithm_name}\'s decryption work?', bg='#383444', fg='white', font=("Helvetica", 12, "bold underline"))
        self.decrypt_explanation_title.pack(fill='x')

        self.decrypt_explanation_button = tk.Button(self.decrypt_explanation_frame, text='Next Page', command=lambda: self.showframe(self.decrypt_explanation_frame2), width = 20, height = 2)
        self.decrypt_explanation_button.place(x=1700, y=960)

        self.decrypt_explanation_title2 = tk.Label(self.decrypt_explanation_frame2, text=f'How does the {self.algorithm_name}\'s decryption work?', bg='#383444', fg='white', font=("Helvetica", 12, "bold underline"))
        self.decrypt_explanation_title2.pack(fill='x')

        self.decrypt_explanation_button2 = tk.Button(self.decrypt_explanation_frame2, text='close', command=self.close_window, width = 20, height = 2 )
        self.decrypt_explanation_button2.place(x=1700, y=960)

        
        

        self.encryption_widgets()
        self.decryption_widgets()
        self.showframe(self.encrypt_explanation_frame)

    
    def close_window(self): #destroys window
        self.window.destroy()
    
    def encryption_widgets(self): #widgets
        if self.algorithm_name == 'Caesar Cipher':
            
            
            self.encryption_explanation_text = tk.Label(self.encrypt_explanation_frame, text=self.texts['caesar page 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
            self.encryption_explanation_text2 = tk.Label(self.encrypt_explanation_frame, text=self.texts['caesar page 1 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
            self.caesar_alphabet = tk.Label(self.encrypt_explanation_frame2, text=self.texts['caesar alphabet'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 16))
            self.caesar_encryption_conclusion = tk.Label(self.encrypt_explanation_frame2, text=self.texts['caesar page 2 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 16))


            self.caesar_alphabet.place(relx = 0.5, rely= 0.1, anchor= 'center')
            self.encryption_explanation_text.place(relx=0.5, rely=0.4, anchor='center' )
            self.encryption_explanation_text2.place(relx=0.5, rely= 0.7, anchor = 'center')
            self.caesar_encryption_conclusion.place(relx=0.5, rely= 0.9, anchor = 'center')

            self.canvas = tk.Canvas(self.encrypt_explanation_frame2, width=1000, height =700, bg= '#383444')
            self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            rect_coords = (750, 300, 250, 200)
            self.rectangle = self.canvas.create_rectangle(rect_coords, fill='white', outline='black')
            
            self.plaintext = self.canvas.create_text(450,250, text="      H  E  L  L  O", fill="Black", font=("Arial", 30)  )

            
            new_rect_coords = (750, 600, 250, 500)
            self.new_rectangle = self.canvas.create_rectangle(new_rect_coords, fill='white', outline='black')

            self.ciphertext = self.canvas.create_text(450, 550, text="      K  H  O  O  R", fill="black", font=("Arial", 30))

            arrow_coords = (500, 300, 500, 500)
            self.arrow = self.canvas.create_line(arrow_coords, arrow=tk.LAST, width=2)
            self.key_shift = self.canvas.create_text(600, 400, text="key shift: 3", fill="black", font=("Arial", 20))



        if self.algorithm_name == 'Rail Fence Cipher':

            self.encryption_explanation_text = tk.Label(self.encrypt_explanation_frame, text=self.texts['Rail Fence page 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.encryption_explanation_text2 = tk.Label(self.encrypt_explanation_frame, text=self.texts['Rail Fence page 1 new line'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
            self.encryption_explanation_text3 = tk.Label(self.encrypt_explanation_frame, text=self.texts['Rail Fence page 1 directions'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, 'bold'))
            self.RailFence_encryption_conclusion = tk.Label(self.encrypt_explanation_frame, text=self.texts['Rail Fence page 1 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))

            self.encryption_diagram = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =200, bg= 'white')
            self.plaintext = self.encryption_diagram.create_text(605, 110, text=self.texts['Rail Fence diagram'], fill="Black",font=("Courier", 26, 'bold'))
            self.diagram_explanation = tk.Label(self.encrypt_explanation_frame2, text=self.texts['Rail Fence diagram explanation'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
            self.diagram_title = tk.Label(self.encrypt_explanation_frame2, text=self.texts['Rail Fence diagram title'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, 'bold'))
            self.RailFence_page2_conclusion = tk.Label(self.encrypt_explanation_frame2, text=self.texts['Rail Fence page 2 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))


            self.encryption_explanation_text.place(relx=0.5, rely=0.15, anchor='center' )
            self.encryption_explanation_text2.place(relx=0.4, rely= 0.34, anchor = 'center')
            self.encryption_explanation_text3.place(relx=0.5, rely= 0.545, anchor = 'center')
            self.RailFence_encryption_conclusion.place(relx=0.5, rely= 0.85, anchor = 'center')

            self.diagram_explanation.place(relx=0.5, rely= 0.25, anchor = 'center')
            self.diagram_title.place(relx=0.5, rely=0.375, anchor= 'center')
            self.RailFence_page2_conclusion.place(relx=0.5, rely= 0.85, anchor = 'center')
            
            self.encryption_diagram.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



           

        if self.algorithm_name == 'Vigenere Cipher':

            self.encryption_explanation_text = tk.Label(self.encrypt_explanation_frame, text=self.texts['Vigenere Cipher page 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.encryption_explanation_text2 = tk.Label(self.encrypt_explanation_frame, text=self.texts['Vigenere page 1 directions'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, 'bold'))
            self.vigenere_encryption_conclusion = tk.Label(self.encrypt_explanation_frame, text=self.texts['Vigenere Cipher page 1 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))

            
            self.encryption_explanation_text.place(relx=0.5, rely=0.15, anchor='center' )
            self.encryption_explanation_text2.place(relx=0.5, rely= 0.544, anchor = 'center')
            self.vigenere_encryption_conclusion.place(relx=0.5, rely= 0.88, anchor = 'center')

            self.table_title = tk.Label(self.encrypt_explanation_frame2, text="Vigenere lookup table: message - 'HELLO' key - 'COINS' ", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))
            self.vigenere_encryption_conclusion_page2 = tk.Label(self.encrypt_explanation_frame2, text=self.texts['table explanation'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))


            self.vigenere_table = tk.Canvas(self.encrypt_explanation_frame2, width=980, height =500, bg= 'white')
            self.vigenere_table_text = self.vigenere_table.create_text(490, 250, text=self.texts['vigenere table'], fill="Black",font=("Courier", 11, 'bold'))


            self.table_title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            self.vigenere_table.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.vigenere_encryption_conclusion_page2.place(relx=0.5, rely= 0.85, anchor = 'center')


        if self.algorithm_name == 'Vernam Cipher':
    
            self.encryption_explanation_text = tk.Label(self.encrypt_explanation_frame, text=self.texts['Vernam Cipher page 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.encryption_explanation_text2 = tk.Label(self.encrypt_explanation_frame, text=self.texts['Vernam Cipher encrypt directions'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 17, 'bold'))


            self.encryption_explanation_text2.place(relx=0.49, rely= 0.725, anchor = 'center')
            self.encryption_explanation_text.place(relx=0.5, rely=0.25, anchor='center' )


            self.table_title = tk.Label(self.encrypt_explanation_frame2, text="ASCII Table: ", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))  

            self.encryption_diagram = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =200, bg= 'white')
            self.ascii_text = self.encryption_diagram.create_text(605, 110, text=self.texts['ascii table'], fill="Black",font=("Courier", 14))

            self.encrypt_title = tk.Label(self.encrypt_explanation_frame2, text="Encrypting 'he' with key 'CT'", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))  
            self.first_letter = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.first_letter_text = self.first_letter.create_text(605, 35, text=self.texts['letter 1 encryption'], fill="Black",font=("Courier", 16, 'bold'))
            self.first_letter_explanation = tk.Label(self.encrypt_explanation_frame2, text = 'Returns ASCII\n character +!', bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))
            

            self.second_letter = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.second_letter_text = self.second_letter.create_text(605, 35, text=self.texts['letter 2 encryption'], fill="Black",font=("Courier", 16, 'bold'))
            self.second_letter_explanation = tk.Label(self.encrypt_explanation_frame2, text = 'Returns ASCII\n character 1!', bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))

            self.conclusion = tk.Label(self.encrypt_explanation_frame2, text=self.texts['encryption conclusion'],  bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20))

            
                    
            self.first_letter.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
            self.second_letter.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            self.first_letter_explanation.place(relx=0.865, rely=0.45, anchor='center')
            self.second_letter_explanation.place(relx=0.865, rely=0.6, anchor='center')
            self.conclusion.place(relx=0.5, rely=0.9, anchor= 'center')

            self.encrypt_title.place(relx=0.5, rely=0.39, anchor='center')
            self.table_title.place(relx=0.5, rely=0.05, anchor = 'center')
            self.encryption_diagram.place(relx=0.5, rely=0.18, anchor=tk.CENTER)
    



            

        if self.algorithm_name == 'Affine Cipher':
            
            self.encryption_explanation_text = tk.Label(self.encrypt_explanation_frame, text=self.texts['Affine page 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.encryption_explanation_text2 = tk.Label(self.encrypt_explanation_frame, text=self.texts['Affine page 1 new line'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Lucida Calligraphy", 24))
            self.encryption_explanation_text3 = tk.Label(self.encrypt_explanation_frame, text=self.texts['Affine page 1 new paragraph'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, 'bold'))
            self.encryption_directions = tk.Label(self.encrypt_explanation_frame, text=self.texts['Affine page 1 directions'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
          
            
            self.alphabet = tk.Label(self.encrypt_explanation_frame2, text=self.texts['alphabet'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Courier", 16))
            self.numbers = tk.Label(self.encrypt_explanation_frame2, text=self.texts['numbers'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Courier", 16))
            
            


            self.encryption_explanation_text.place(relx=0.5, rely=0.15, anchor='center' )
            self.encryption_explanation_text2.place(relx=0.5, rely= 0.3, anchor = 'center')
            self.encryption_explanation_text3.place(relx=0.5, rely= 0.5, anchor = 'center')
            self.encryption_directions.place(relx=0.5, rely= 0.8, anchor = 'center')


            self.alphabet.place(relx = 0.5, rely= 0.1, anchor= 'center')
            self.numbers.place(relx=0.5, rely= 0.12, anchor= 'center')

            self.table_title = tk.Label(self.encrypt_explanation_frame2, text="Encryting 'HELLO' with key '5, 8' ", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))

            self.first_encryption = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.first_encryption.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

            self.second_encryption = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.second_encryption.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

            self.third_encryption = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.third_encryption.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

            self.fourth_encryption = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.fourth_encryption.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
            
            self.fifth_encryption = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.fifth_encryption.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

            self.conversions = tk.Label(self.encrypt_explanation_frame2, text=self.texts['conversions'],  bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, 'bold'))
            self.conclusion = tk.Label(self.encrypt_explanation_frame2, text=self.texts['conclusion'],  bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20))

            self.table_title.place(relx=0.5, rely=0.2, anchor= 'center')
            self.first_encryption_text = self.first_encryption.create_text(605, 35, text=self.texts['encryption1'], fill="Black",font=("Palatino Linotype", 24, 'bold'))
            self.second_encryption_text = self.second_encryption.create_text(605, 35, text=self.texts['encryption2'], fill="Black",font=("Palatino Linotype", 24, 'bold'))
            self.third_encryption_text = self.third_encryption.create_text(605, 35, text=self.texts['encryption3/4'], fill="Black",font=("Palatino Linotype", 24, 'bold'))
            self.fourth_encryption_text = self.fourth_encryption.create_text(605, 35, text=self.texts['encryption3/4'], fill="Black",font=("Palatino Linotype", 24, 'bold'))
            self.fifth_encryption_text = self.fifth_encryption.create_text(605, 35, text=self.texts['encryption5'], fill="Black",font=("Palatino Linotype", 24, 'bold'))

            self.conversions.place(relx= 0.5, rely=0.72, anchor= 'center')
            self.conclusion.place(relx= 0.5, rely=0.87, anchor= 'center') 

        if self.algorithm_name == 'RSA Algorithm':
            
            self.encryption_explanation_text = tk.Label(self.encrypt_explanation_frame, text=self.texts['RSA page 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.encryption_explanation_text2 = tk.Label(self.encrypt_explanation_frame, text=self.texts['RSA key directions 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.encryption_explanation_text3 = tk.Label(self.encrypt_explanation_frame, text='n = pq', bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Lucida Calligraphy", 24))
            self.encryption_explanation_text4 = tk.Label(self.encrypt_explanation_frame, text=self.texts['RSA key directions 2'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.encryption_explanation_text5 = tk.Label(self.encrypt_explanation_frame, text='1 < exponent < ϕ(n) and the exponent and ϕ(n) are coprime.', bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Lucida Calligraphy", 24))
            self.encryption_explanation_text6 = tk.Label(self.encrypt_explanation_frame, text=self.texts['RSA key directions 3'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.encryption_explanation_text7 = tk.Label(self.encrypt_explanation_frame, text='c ≡ mᵉ mod n', bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Lucida Calligraphy", 24))
            self.encryption_page1_conclusion = tk.Label(self.encrypt_explanation_frame, text=self.texts['conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20)) 


            self.encryption_explanation_text.place(relx=0.5, rely=0.15, anchor='center' )
            self.encryption_explanation_text2.place(relx=0.5, rely=0.35, anchor='center')
            self.encryption_explanation_text3.place(relx=0.5, rely=0.45, anchor='center')
            self.encryption_explanation_text4.place(relx=0.49, rely=0.546, anchor='center')
            self.encryption_explanation_text5.place(relx=0.5, rely=0.64, anchor='center')
            self.encryption_explanation_text6.place(relx=0.49, rely= 0.74, anchor= 'center')
            self.encryption_explanation_text7.place(relx=0.5, rely= 0.84, anchor= 'center')
            self.encryption_page1_conclusion.place(relx=0.5, rely=0.91, anchor='center')

            self.alphabet = tk.Label(self.encrypt_explanation_frame2, text=self.texts['alphabet'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Courier", 16))
            self.numbers = tk.Label(self.encrypt_explanation_frame2, text=self.texts['numbers'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Courier", 16))

            self.encrypt_title = tk.Label(self.encrypt_explanation_frame2, text="Encrypting 'L' with prime numbers p = '3', q = '7', e = '5'", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))  
            
            self.n_generation = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.n_generation_text = self.n_generation.create_text(605, 35, text=self.texts['n generation'], fill="Black",font=("Courier", 26, 'bold'))
            self.n_generation_explanation = tk.Label(self.encrypt_explanation_frame2, text = "this means \n'n' is 21!", bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))
            

            self.encryption_template = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.encryption_template_text = self.encryption_template.create_text(605, 35, text=self.texts['encryption'], fill="Black",font=("Lucida Calligraphy", 26, 'bold'))
            
            self.encrypting_letter_diagram = tk.Canvas(self.encrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.encrypting_letter_text = self.encrypting_letter_diagram.create_text(605, 35, text=self.texts['letter encryption'], fill="Black",font=("Lucida Calligraphy", 26, 'bold'))
            self.encryption_explanation = tk.Label(self.encrypt_explanation_frame2, text = 'Returns the\n integer 2!', bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))

            self.alphabet.place(relx = 0.5, rely= 0.1, anchor= 'center')
            self.numbers.place(relx=0.5, rely= 0.12, anchor= 'center')
            self.encrypt_title.place(relx=0.5, rely=0.2, anchor= 'center')

            self.n_generation.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
            self.encryption_template.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

            self.n_generation_explanation.place(relx=0.865, rely=0.3, anchor='center')
            self.encryption_explanation.place(relx=0.865, rely=0.6, anchor='center')
            self.conclusion = tk.Label(self.encrypt_explanation_frame2, text=self.texts['encryption conclusion'],  bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20))

            self.encrypting_letter_diagram.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            self.conclusion.place(relx=0.5, rely=0.8, anchor='center')
             
            


            
            
    
    def decryption_widgets(self):
        if self.algorithm_name == 'Caesar Cipher':
            self.decryption_explanation_text = tk.Label(self.decrypt_explanation_frame, text=self.texts['caesar page 3'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
            self.decryption_conclusion_text = tk.Label(self.decrypt_explanation_frame, text=self.texts['caesar page 3 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
            self.caesar_alphabet = tk.Label(self.decrypt_explanation_frame2, text=self.texts['caesar alphabet'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 16))
            self.caesar_decryption_final_page = tk.Label(self.decrypt_explanation_frame2, text=self.texts['caesar page 4 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 14))

            
            self.decryption_explanation_text.place(relx=0.5, rely=0.4, anchor='center' )
            self.decryption_conclusion_text.place(relx=0.5, rely=0.7, anchor='center' )
            self.caesar_alphabet.place(relx = 0.5, rely= 0.1, anchor= 'center')
            self.caesar_decryption_final_page.place(relx=0.5, rely= 0.9, anchor = 'center')

            self.canvas = tk.Canvas(self.decrypt_explanation_frame2, width=1000, height =700, bg= '#383444')
            self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            rect_coords = (750, 300, 250, 200)
            self.rectangle = self.canvas.create_rectangle(rect_coords, fill='white', outline='black')
            
            self.ciphertext = self.canvas.create_text(450,250, text="      N  Y  P  M  Y  W", fill="Black", font=("Arial", 30)  )

            
            new_rect_coords = (750, 600, 250, 500)
            self.new_rectangle = self.canvas.create_rectangle(new_rect_coords, fill='white', outline='black')

            self.plaintext = self.canvas.create_text(450, 550, text="      J  U  L  I  U  S", fill="black", font=("Arial", 30))

            arrow_coords = (500, 300, 500, 500)
            self.arrow = self.canvas.create_line(arrow_coords, arrow=tk.LAST, width=2)
            self.key_shift = self.canvas.create_text(600, 400, text="key shift: 4", fill="black", font=("Arial", 20))

        if self.algorithm_name == 'Rail Fence Cipher':
    
            self.decryption_explanation_text = tk.Label(self.decrypt_explanation_frame, text=self.texts['Rail Fence page 3'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
            self.RailFence_decryption_conclusion = tk.Label(self.decrypt_explanation_frame, text=self.texts['Rail Fence decryption diagram explanation'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
            self.first_rail_title = tk.Label(self.decrypt_explanation_frame2, text= 'This is the first rail, the letters replace the available asterisks in the first rail:', bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.second_rail_title = tk.Label(self.decrypt_explanation_frame2, text= 'This is the second rail, the letters replace the available asterisks in the second rail:', bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.third_rail_title = tk.Label(self.decrypt_explanation_frame2, text= 'This is the third rail, the letters replace the available asterisks in the third rail:', bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.decryption_diagram_title = tk.Label(self.decrypt_explanation_frame2, text= self.texts['Rail Fence decryption diagram title'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.RailFence_decryption_final_page = tk.Label(self.decrypt_explanation_frame2, text=self.texts['Rail Fence page 4 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            
            
            self.decryption_explanation_text.place(relx=0.5, rely=0.35, anchor='center' )
            self.RailFence_decryption_conclusion.place(relx=0.5, rely= 0.85, anchor = 'center')


            self.first_rail_title.place(relx=0.5,rely=0.05, anchor = 'center')
            self.second_rail_title.place(relx=0.5,rely=0.2, anchor = 'center')
            self.third_rail_title.place(relx=0.5,rely=0.35, anchor='center')
            self.decryption_diagram_title.place(relx=0.5,rely=0.52, anchor= 'center' )
            self.RailFence_decryption_final_page.place(relx=0.5,rely=0.85, anchor= 'center' )

            self.decryption_rails = tk.Canvas(self.decrypt_explanation_frame, width=1200, height =200, bg= 'white')
            self.decryption_rails.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
            self.plaintext = self.decryption_rails.create_text(605, 110, text=self.texts['Rail Fence placeholder diagram'], fill="Black",font=("Courier", 26, 'bold'))

            self.first_rail = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.first_rail.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

            self.second_rail = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.second_rail.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

            self.third_rail = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.third_rail.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

            self.first_rail_text = self.first_rail.create_text(605, 35, text=self.texts['First Rail'], fill="Black",font=("Courier", 24, 'bold'))
            self.second_rail_text = self.second_rail.create_text(605, 35, text=self.texts['Second Rail'], fill="Black",font=("Courier", 24, 'bold'))
            self.third_rail_text = self.third_rail.create_text(605, 35, text=self.texts['Third Rail'], fill="Black",font=("Courier", 24, 'bold'))

            
            self.diagram = tk.Canvas(self.decrypt_explanation_frame2, width=1100, height =190, bg= 'white')
            self.ciphertext = self.diagram.create_text(545, 100, text=self.texts['Rail Fence decryption diagram'], fill="Black",font=("Courier", 24, 'bold'))

            self.diagram.place(relx=0.5, rely=0.65, anchor=tk.CENTER)



        if self.algorithm_name == 'Vigenere Cipher':

            self.decryption_explanation_text = tk.Label(self.decrypt_explanation_frame, text=self.texts['decryption title'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.decryption_explanation_text2 = tk.Label(self.decrypt_explanation_frame, text=self.texts['decryption directions'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, 'bold'))
            self.vigenere_decryption_conclusion = tk.Label(self.decrypt_explanation_frame, text=self.texts['decryption page 1 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))

            
            self.decryption_explanation_text.place(relx=0.5, rely=0.2, anchor='center' )
            self.decryption_explanation_text2.place(relx=0.5, rely= 0.544, anchor = 'center')
            self.vigenere_decryption_conclusion.place(relx=0.5, rely= 0.88, anchor = 'center')

            self.table_title = tk.Label(self.decrypt_explanation_frame2, text="Vigenere lookup table: message - 'YOTXIR' key - 'MONKEY' ", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))
            self.vigenere_decryption_conclusion_page2 = tk.Label(self.decrypt_explanation_frame2, text=self.texts['decryption page 2 conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))


            self.vigenere_table = tk.Canvas(self.decrypt_explanation_frame2, width=980, height =500, bg= 'white')
            self.vigenere_table_text = self.vigenere_table.create_text(490, 250, text=self.texts['vigenere table'], fill="Black",font=("Courier", 11, 'bold'))


            self.table_title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            self.vigenere_table.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.vigenere_decryption_conclusion_page2.place(relx=0.5, rely= 0.85, anchor = 'center')

        if self.algorithm_name == 'Vernam Cipher':
            
            self.decryption_explanation_text = tk.Label(self.decrypt_explanation_frame, text=self.texts['Vernam Cipher page 1 decryption'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.decryption_explanation_text2 = tk.Label(self.decrypt_explanation_frame, text=self.texts['Vernam Cipher decrypt directions'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 17, 'bold'))

            self.decryption_explanation_text.place(relx=0.5, rely=0.3, anchor='center' )
            self.decryption_explanation_text2.place(relx=0.55, rely= 0.7, anchor = 'center')



            self.table_title = tk.Label(self.decrypt_explanation_frame2, text="ASCII Table: ", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))  

            self.decryption_diagram = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =200, bg= 'white')
            self.plaintext = self.decryption_diagram.create_text(605, 110, text=self.texts['ascii table'], fill="Black",font=("Courier", 14))

            self.decrypt_title = tk.Label(self.decrypt_explanation_frame2, text="Decrypting '?.' with key 'GV'", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))  
            self.first_letter = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.first_letter_text = self.first_letter.create_text(605, 35, text=self.texts['letter 1 decryption'], fill="Black",font=("Courier", 16, 'bold'))
            self.first_letter_explanation = tk.Label(self.decrypt_explanation_frame2, text = 'Returns ASCII\n character x!', bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))
            

            self.second_letter = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.second_letter_text = self.second_letter.create_text(605, 35, text=self.texts['letter 2 decryption'], fill="Black",font=("Courier", 16, 'bold'))
            self.second_letter_explanation = tk.Label(self.decrypt_explanation_frame2, text = 'Returns ASCII\n character x!', bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))

            self.conclusion = tk.Label(self.decrypt_explanation_frame2, text=self.texts['decryption conclusion'],  bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20))

            
                    
            self.first_letter.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
            self.second_letter.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            self.first_letter_explanation.place(relx=0.865, rely=0.45, anchor='center')
            self.second_letter_explanation.place(relx=0.865, rely=0.6, anchor='center')
            self.conclusion.place(relx=0.5, rely=0.85, anchor= 'center')

            self.decrypt_title.place(relx=0.5, rely=0.39, anchor='center')
            self.table_title.place(relx=0.5, rely=0.05, anchor = 'center')
            self.decryption_diagram.place(relx=0.5, rely=0.18, anchor=tk.CENTER)
    


    

        if self.algorithm_name == 'Affine Cipher':
            
            self.decryption_explanation_text = tk.Label(self.decrypt_explanation_frame, text=self.texts['Affine decryption page 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.decryption_explanation_text2 = tk.Label(self.decrypt_explanation_frame, text=self.texts['Affine decryption page 1 new line'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Lucida Calligraphy", 24))
            self.decryption_explanation_text3 = tk.Label(self.decrypt_explanation_frame, text=self.texts['Affine decryption page 1 new paragraph'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, 'bold'))
            self.decryption_directions = tk.Label(self.decrypt_explanation_frame, text=self.texts['Affine decryption page 1 directions'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24))
          
            
            self.alphabet = tk.Label(self.decrypt_explanation_frame2, text=self.texts['alphabet'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Courier", 16))
            self.numbers = tk.Label(self.decrypt_explanation_frame2, text=self.texts['numbers'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Courier", 16))
            
            


            self.decryption_explanation_text.place(relx=0.5, rely=0.15, anchor='center' )
            self.decryption_explanation_text2.place(relx=0.5, rely= 0.3, anchor = 'center')
            self.decryption_explanation_text3.place(relx=0.5, rely= 0.5, anchor = 'center')
            self.decryption_directions.place(relx=0.5, rely= 0.8, anchor = 'center')


            self.alphabet.place(relx = 0.5, rely= 0.1, anchor= 'center')
            self.numbers.place(relx=0.5, rely= 0.12, anchor= 'center')

            self.table_title = tk.Label(self.decrypt_explanation_frame2, text="decryting 'RAZRC' with key '7, 13' ", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))

            self.first_decryption = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.first_decryption.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

            self.second_decryption = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.second_decryption.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

            self.third_decryption = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.third_decryption.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

            self.fourth_decryption = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.fourth_decryption.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
            
            self.fifth_decryption = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =50, bg= 'white')
            self.fifth_decryption.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

            self.conversions = tk.Label(self.decrypt_explanation_frame2, text=self.texts['decrypt_conversions'],  bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, 'bold'))
            self.conclusion = tk.Label(self.decrypt_explanation_frame2, text=self.texts['decrypt_conclusion'],  bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20))

            self.table_title.place(relx=0.5, rely=0.2, anchor= 'center')
            self.first_decryption_text = self.first_decryption.create_text(605, 35, text=self.texts['decryption1/4'], fill="Black",font=("Palatino Linotype", 24, 'bold'))
            self.second_decryption_text = self.second_decryption.create_text(605, 35, text=self.texts['decryption2'], fill="Black",font=("Palatino Linotype", 24, 'bold'))
            self.third_decryption_text = self.third_decryption.create_text(605, 35, text=self.texts['decryption3'], fill="Black",font=("Palatino Linotype", 24, 'bold'))
            self.fourth_decryption_text = self.fourth_decryption.create_text(605, 35, text=self.texts['decryption1/4'], fill="Black",font=("Palatino Linotype", 24, 'bold'))
            self.fifth_decryption_text = self.fifth_decryption.create_text(605, 35, text=self.texts['decryption5'], fill="Black",font=("Palatino Linotype", 24, 'bold'))

            self.conversions.place(relx= 0.5, rely=0.72, anchor= 'center')
            self.conclusion.place(relx= 0.5, rely=0.87, anchor= 'center') 

        if self.algorithm_name == 'RSA Algorithm':

            self.decryption_explanation_text = tk.Label(self.decrypt_explanation_frame, text=self.texts['RSA decrypt page 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.decryption_explanation_text2 = tk.Label(self.decrypt_explanation_frame, text=self.texts['RSA private key direction 1'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.decryption_explanation_text3 = tk.Label(self.decrypt_explanation_frame, text='ex + ϕ(n)y = 1', bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Lucida Calligraphy", 24))
            self.decryption_explanation_text4 = tk.Label(self.decrypt_explanation_frame, text=self.texts['RSA private key direction 2'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20))
            self.decryption_explanation_text5 = tk.Label(self.decrypt_explanation_frame, text='m ≡ cᵈ mod n', bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Lucida Calligraphy", 24))
            self.decryption_page1_conclusion = tk.Label(self.decrypt_explanation_frame, text=self.texts['decrypt conclusion'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 20)) 


            self.decryption_explanation_text.place(relx=0.5, rely=0.15, anchor='center' )
            self.decryption_explanation_text2.place(relx=0.5, rely=0.38, anchor='center')
            self.decryption_explanation_text3.place(relx=0.5, rely=0.53, anchor='center')
            self.decryption_explanation_text4.place(relx=0.49, rely=0.6, anchor='center')
            self.decryption_explanation_text5.place(relx=0.5, rely=0.73, anchor='center')
            self.decryption_page1_conclusion.place(relx=0.5, rely=0.85, anchor='center')

            self.alphabet = tk.Label(self.decrypt_explanation_frame2, text=self.texts['alphabet'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Courier", 16))
            self.numbers = tk.Label(self.decrypt_explanation_frame2, text=self.texts['numbers'], bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Courier", 16))

            self.decrypt_title = tk.Label(self.decrypt_explanation_frame2, text="Decrypting 'C' with prime numbers p = '5', q = '11', e = '3'", bg='#383444', fg='white', justify="left", anchor = 'w',  wraplength=self.screen_width, font=("Arial", 24, "bold underline"))  
            
            self.phi_generation = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.phi_generation_text = self.phi_generation.create_text(605, 35, text=self.texts['phi decryption generation'], fill="Black",font=("Courier", 26, 'bold'))
            self.phi_generation_explanation = tk.Label(self.decrypt_explanation_frame2, text = 'this means totient\n function is 40!', bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))
            

            self.euclidean_algorithm = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.euclidean_algorithm_text = self.euclidean_algorithm.create_text(605, 35, text='3x + 40y = 1', fill="Black",font=("Courier", 26, 'bold'))
            self.euclidean_algorithm_explanation = tk.Label(self.decrypt_explanation_frame2, text = " solving for x\n means d = '27'", bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))
            
            self.decrypting_template_diagram = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.decrypting_template_text = self.decrypting_template_diagram.create_text(605, 35, text=self.texts['decryption'], fill="Black",font=("Lucida Calligraphy", 26, 'bold'))
            self.decryption_explanation = tk.Label(self.decrypt_explanation_frame2, text = 'Returns the\n integer 2!', bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))

            self.decryption_diagram = tk.Canvas(self.decrypt_explanation_frame2, width=1200, height =60, bg= 'white')
            self.decryption_text = self.decryption_diagram.create_text(605, 35, text=self.texts['decrypting letter'], fill="Black",font=("Lucida Calligraphy", 26, 'bold'))
            self.decryption_explanation = tk.Label(self.decrypt_explanation_frame2, text = 'Returns the\n integer 18!', bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20, "bold"))

            self.alphabet.place(relx = 0.5, rely= 0.05, anchor= 'center')
            self.numbers.place(relx=0.5, rely= 0.07, anchor= 'center')
            self.decrypt_title.place(relx=0.5, rely=0.15, anchor= 'center')

            self.phi_generation.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
            self.phi_generation_explanation.place(relx=0.865, rely=0.25, anchor='center')

            self.euclidean_algorithm.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
            self.euclidean_algorithm_explanation.place(relx=0.865, rely=0.4, anchor='center')

            self.decrypting_template_diagram.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

            self.decryption_diagram.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
            self.decryption_explanation.place(relx=0.865, rely=0.7, anchor='center')

            self.conclusion = tk.Label(self.decrypt_explanation_frame2, text=self.texts['decryption conclusion 2'],  bg= '#383444' , fg='white', justify="left", anchor = 'w', wraplength=self.screen_width, font=("Arial", 20))
            self.conclusion.place(relx=0.5, rely=0.85, anchor='center')


    def show_frame(self):
        self.window.mainloop()




#--------------------------------------------------------------------------------------------------- login window-----------------------------------------------------------------------------------------------------------------------------------
 
class login_system: #login system
    def __init__(self, root):
        self.login_window = root
        self.login_window.title("Login")

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.login_window.state('zoomed')
        self.is_authenticated = False #boolean set up for authentication of user
        
        self.create_widgets()

    def create_widgets(self): #widgets
        username_label = tk.Label(self.login_window, text="Username:",  bg= '#383444', fg='white', font=('Segoe UI', '20'))
        username_label.place(relx=0.5, rely=0.3, anchor="center")

        username_entry = tk.Entry(self.login_window, textvariable=self.username_var,  bg= '#080404', fg='white', insertbackground='white', font=('Segoe UI', '20'))
        username_entry.place(relx=0.5, rely=0.35, anchor="center")

        password_label = tk.Label(self.login_window, text="Password:",  bg= '#383444', fg='white', font=('Segoe UI', '20'))
        password_label.place(relx=0.5, rely=0.4, anchor="center")

        self.password_entry = tk.Entry(self.login_window, textvariable=self.password_var, show="*",  bg= '#080404', fg='white', insertbackground='white', font=('Segoe UI', '20'))
        self.password_entry.place(relx=0.5, rely=0.45, anchor="center")

        show_password = tk.Checkbutton(self.login_window, text="show password", command=self.show_password, bg= '#383444', fg='white', font=('Segoe UI', '10'))
        show_password.place(relx=0.62, rely=0.45, anchor="center")

        login_button = tk.Button(self.login_window, text="Login", command=self.login, bg= '#282424', fg='white', font=('Segoe UI', '20'))
        login_button.place(relx=0.5, rely=0.51, anchor="center")

        self.login_window.bind("<Return>", lambda event: self.login())
        
        register_button = tk.Button(self.login_window, text="Register", command=self.register, bg= '#282424', fg='white', font=('Segoe UI', '20'))
        register_button.place(relx=0.64, rely=0.4, anchor="center")
    def show_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def login(self):        
        result = db.login(self.username_var.get(), self.password_var.get()) #calls database for login function, checks if its in the database
        
        if result: #if it is, user is authenticated
            self.is_authenticated = True
            self.login_window.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def register(self):  #if register button is pressed,  register window is opened
        register_window = tk.Tk()
        register_window.configure(bg='#383444')
        register_app = register_window_system(register_window)
        register_window.mainloop()

#----------------------------------------------------------------------------------------register window---------------------------------------------------------------------------------------------------------------------------------------------        
    
class register_window_system:
    def __init__(self, root):
        self.register_window = root
        self.register_window.title("Register")
        self.register_window.state('zoomed')
        self.list_sort = quick_sort() #composition
        self.list_search = binary_search() #composition

        self.create_widgets()
        
    def create_widgets(self): #widgets
        username_label = tk.Label(self.register_window, text="UserID:",  bg= '#383444', fg='white', font=('Segoe UI', '20'))
        username_label.place(relx=0.5, rely=0.2, anchor="center")

        self.username_entry = tk.Entry(self.register_window, text="",  bg= '#080404', fg='white', font=('Segoe UI', '20'), insertbackground='white')
        self.username_entry.place(relx=0.5, rely=0.25, anchor="center")

        password_label = tk.Label(self.register_window, text="Enter Password:",  bg= '#383444', fg='white', font=('Segoe UI', '20'))
        password_label.place(relx=0.5, rely=0.3, anchor="center")

        self.password_entry = tk.Entry(self.register_window, text="", show="*",  bg= '#080404', fg='white', font=('Segoe UI', '20'), insertbackground='white')
        self.password_entry.place(relx=0.5, rely=0.35, anchor="center")

        show_password = tk.Checkbutton(self.register_window, text="show password", command=self.show_password, bg= '#383444', fg='white', font=('Segoe UI', '10'))
        show_password.place(relx=0.62, rely=0.4, anchor="center")

        password_confirmation_Label = tk.Label(self.register_window, text="Confirm Password:",  bg= '#383444', fg='white', font=('Segoe UI', '20'))
        password_confirmation_Label.place(relx=0.5, rely=0.4, anchor="center")

        self.password_confirmation_entry = tk.Entry(self.register_window, text="", show="*",  bg= '#080404', fg='white', font=('Segoe UI', '20'), insertbackground='white')
        self.password_confirmation_entry.place(relx=0.5, rely=0.45, anchor="center")

        year_label = tk.Label(self.register_window, text="enter year group:",  bg= '#383444', fg='white', font=('Segoe UI', '20'))
        year_label.place(relx=0.5, rely=0.5, anchor="center")

        self.year_entry = tk.Entry(self.register_window, text="",  bg= '#080404', fg='white', font=('Segoe UI', '20'), insertbackground='white')
        self.year_entry.place(relx=0.5, rely=0.55, anchor="center")

        register_button = tk.Button(self.register_window, text="Register", command=self.register, bg= '#282424', fg='white', font=('Segoe UI', '20'))
        register_button.place(relx=0.484,rely=0.6)

        self.register_window.bind("<Return>", lambda event: self.register()) #lambda to delay function call
        
        self.back_button = tk.Button(self.register_window, text=" < ", command=self.back_to_login, bg= '#282424', fg='white', font=('Segoe UI', '20'))
        self.back_button.place(relx=0.455,rely=0.6)

    def back_to_login(self):
        self.register_window.destroy()
    
    def show_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
            self.password_confirmation_entry.config(show='')
        else:
            self.password_entry.config(show='*')
            self.password_confirmation_entry.config(show='*')

    def sort_database(self, names): #uses quicksort to sort database in alphabetical order
        sort = self.list_sort #renaming class 
        sort.quicksort(names, 0, len(names) -1)        
        return names #returns list of names

    def register(self):
        list_of_names = db.get_username() #queries database to get all usernames
        name_found = self.list_search #renames binary search
        username = self.username_entry.get() #gets username inputted
        username = username.strip()
        password = self.password_entry.get() #gets password inputted
        year = self.year_entry.get() #gets year inputted
        year = int(year)
        years = [7, 8, 9, 10, 11, 12, 13]
        password_confirmation = self.password_confirmation_entry.get() #gets confirmed password inputted by user       

        list_of_names = self.sort_database(list_of_names)

        if name_found.search(list_of_names, username.upper()) == True: #uses binary search to check if username is already in database
            messagebox.showerror("Registration Failed!", "This Username is already in use! Please register another.") #if it is in database, it returns an error
            self.register_window.destroy()
        else:
            #other errors by users are caught
            if len(username) < 3:
                messagebox.showerror('Register Error', 'Error: For Maximum protection, username length must be greater than 3 characters, please do this.')
                self.register_window.destroy()
            else:
                if password_confirmation == password and year in years:
                    db.register(username, password, year)
                    messagebox.showinfo("Registration Success!", "User registered successfully")
                    self.register_window.destroy()
                elif password_confirmation != password:
                    messagebox.showerror("Registration Failed!", "The passwords did not match")
                    self.register_window.destroy()
                elif year not in years:
                    messagebox.showerror("Registration Failed!", "Invalid year selected")
                    self.register_window.destroy()

#-----------------------------------------------------------------------------------------main window implementation ------------------------------------------------------------------------------------------------------------------------------------

class app_interface:
    def __init__(self, window, username):
        self.window = window
        self.window.title(f"{username}'s Cryptology Program")
        self.mode_var = tk.BooleanVar()
        self.algorithm_var = tk.StringVar()
        self.key_var = tk.StringVar()
        self.message_var = tk.StringVar()
        self.output_var = tk.StringVar()
        self.summary_var = tk.StringVar()
        self.bit_size_var = tk.IntVar()
        self.window.state('zoomed')



        #composition, the stack class being used in the Appinterface class
        self.encryption_history = stack()
        self.decryption_history = stack()
        self.error = error_handling()
        

        self.mode_var.set(ENCRYPT)
        year = db.get_year(username)

        self.encryption_methods = {
            "Caesar Cipher": caesar_cipher(),
            "Rail Fence Cipher": rail_fence(),
        }

        if year >= 10:
            self.encryption_methods["Vigenere Cipher"] = vigenere_cipher()

        if year >= 12:
            self.encryption_methods["Vernam Cipher"] = vernam_cipher()
            self.encryption_methods["Affine Cipher"] = affine_cipher()
        
        if year >= 13:
            self.encryption_methods["RSA Algorithm"] = RSA_Algorithm()
    #dynamic dictionary that is mapped to encryption classes
        self.create_widgets()


    def create_widgets(self): #widgets
        self.algorithm_label = tk.Label(self.window, text="Select Encryption:",  bg= '#383444', fg='white', font=('Segoe UI', '9', 'bold'))
        self.algorithm_label.pack()

        algorithms = list(self.encryption_methods.keys())

        algorithm_dropdown = ttk.Combobox(self.window, textvariable=self.algorithm_var, values=algorithms, state="readonly")
        algorithm_dropdown.pack()
        algorithm_dropdown.bind("<<ComboboxSelected>>", self.update_summary_and_gui_activation)

        self.toggle_button = tk.Button(self.window, text="Encrypt Mode", command=self.toggle_mode, bg= '#282424', fg='white')
        self.toggle_button.pack()
        self.key_label = tk.Label(self.window, text="Key/Public Key:",  bg= '#383444', fg='white', font=('Segoe UI', '9', 'bold'))
        self.key_label.pack()

        self.key_entry = tk.Entry(self.window, textvariable=self.key_var,  bg= '#080404', fg='white', insertbackground='white')
    
        self.key_entry.pack()

        self.message_label = tk.Label(self.window, text="Message:",  bg= '#383444', fg='white', font=('Segoe UI', '9', 'bold'))
        self.message_label.pack()

        self.message_entry = tk.Entry(self.window, textvariable=self.message_var, bg= '#080404', fg='white', insertbackground='white')
        self.message_entry.pack()

        self.encrypt_button = tk.Button(self.window, text="Encrypt", command=self.encrypt_or_decrypt,  bg= '#282424', fg='white')
        self.encrypt_button.pack()

        self.window.bind("<Return>", lambda event: self.encrypt_or_decrypt())

        self.output_label = tk.Label(self.window, text="Output:",  bg= '#383444', fg='white', font=('Segoe UI', '9', 'bold'))
        self.output_label.pack()

        self.output_entry = tk.Entry(self.window, textvariable=self.output_var, disabledforeground='white', insertbackground='white', disabledbackground='#080404', state='disabled')
        self.output_entry.pack()

        self.backward_button = tk.Button(self.window, text="previous decrypted message", command=self.navigate_history_backward,  bg= '#282424', fg='white')
        self.backward_button.pack(padx=2, pady=2)


        self.directions_label = tk.Label(self.window, text="Enter a message into the message box and enter a key depending\non the encryption chosen, then, press encrypt. to decrypt it, switch modes\nthen press 'previous encrypted message' to retrieve the last encrypted message\n(this works for encrypt mode too), then just press decrypt!  ",  bg= '#383444', fg='white', font=('Segoe UI', '10', 'bold'))
        self.directions_label.place(relx=0.7, rely=0.08)
        self.summary_label = tk.Label(self.window, text="Summary:",  bg= '#383444', fg='white', font=('Segoe UI', '9', 'bold'))
        self.summary_label.place(relx=0.485, rely=0.26)

        self.summary_text = tk.Text(self.window, height=20, width=150, wrap = WORD, bg= '#080404', fg='white', font=('Arial', 16, 'bold'))
        self.summary_text.pack(padx=10, pady=40)
        self.summary_text.config(state='disabled')

        self.generate_key_button = tk.Button(self.window, text="generate private and public key", command=self.generate_rsa_key,  bg= '#282424', fg='white', font=('Segoe UI', '9', 'bold'))
        self.generate_vernam_key_button = tk.Button(self.window, text="generate one time pad", command=self.generate_vernam_key,  bg= '#282424', fg='white', font=('Segoe UI', '9', 'bold'))

        self.bit_size_label = tk.Label(self.window, text="Enter Bit Size:",  bg= '#383444', fg='white', font=('Segoe UI', '9', 'bold'))
        self.bit_size_entry = tk.Entry(self.window, text= "",  bg= '#080404', fg='white', insertbackground='white', font=('Segoe UI', '9', 'bold'))

        self.expand_button = tk.Button(self.window, text= "Expand texts", command=self.expand,  width = 20, height = 2,  bg= '#282424', fg='white')
        self.explanation_button = tk.Button(self.window, text= 'How does this work?', command=self.explain_encryption_method, width = 20, height = 2,  bg= '#282424', fg='white')



#----------------------------------------------------------------------------------------------main window button commands----------------------------------------------------------------------------------------------------------------------------

    def bit_error_checking(self, bit_size): #bit error checking
            self.error.empty_bitsize_checker(bit_size)
            self.error.bit_size_value_checker_int(bit_size)
            self.error.small_bitsize_checker(bit_size)
    
    def generate_rsa_key(self): #generating rsa key button command
        current_mode = self.mode_var.get()
        selected_algorithm = self.encryption_methods.get("RSA Algorithm")
        bit_size = self.bit_size_entry.get()
        self.bit_error_checking(bit_size)
        bit_size = int(bit_size)
        self.public_key, self.private_key = selected_algorithm.key_generation(bit_size)
        
        if current_mode == ENCRYPT:
            current_key = self.public_key
            self.key_label.config(text='public key: ')
        elif current_mode == DECRYPT:
            current_key = self.private_key        
            self.key_label.config(text='public key: ')

        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, current_key)
        


        
    def generate_vernam_key(self): #generating random vernam key button commads
        current_mode = self.mode_var.get()
        message = self.message_entry.get()
        self.error.empty_message_checker(message) #checks if message is empty
        selected_algorithm = self.encryption_methods.get("Vernam Cipher")   
        self.key = selected_algorithm.generate_key(message)

        if current_mode == ENCRYPT:
            key = self.key
            self.key_label.config(text='encrypt key: ')
        elif current_mode == DECRYPT:
            key = self.key       
            self.key_label.config(text='decrypt key: ')
        
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, key)
        
        




    
    def gui_change(self, event): # this dynamically changes the widgets in the gui depending on encryption chosen
        selected_algorithm_name = self.algorithm_var.get()
        if selected_algorithm_name == "Caesar Cipher":
            self.bit_size_label.pack_forget()
            self.bit_size_entry.pack_forget()
            self.generate_key_button.pack_forget()
            self.generate_vernam_key_button.pack_forget()

            self.message_entry.delete(0, tk.END)
            self.key_entry.delete(0, tk.END)
            self.key_label.config(text='Enter number of Shifts (key):')
            self.explanation_button.place(x = 1100, y=100)
            self.expand_button.place(x = 680, y=100)

        elif selected_algorithm_name == "Rail Fence Cipher":
            self.bit_size_label.pack_forget()
            self.bit_size_entry.pack_forget()
            self.generate_key_button.pack_forget()
            self.generate_vernam_key_button.pack_forget()

            self.message_entry.delete(0, tk.END)
            self.key_entry.delete(0, tk.END)
            self.key_label.config(text='Enter number of rails (key):')
            self.explanation_button.place(x = 1100, y=100)
            self.expand_button.place(x = 680, y=100)

        elif selected_algorithm_name == "Vigenere Cipher":
            self.bit_size_label.pack_forget()
            self.bit_size_entry.pack_forget()
            self.generate_key_button.pack_forget()
            self.generate_vernam_key_button.pack_forget()

            self.message_entry.delete(0, tk.END)
            self.key_entry.delete(0, tk.END)
            self.key_label.config(text='Enter a key with the same amount of characters:')
            self.explanation_button.place(x = 1100, y=100)
            self.expand_button.place(x = 680, y=100)

        elif selected_algorithm_name == "Vernam Cipher":
            self.bit_size_label.pack_forget()
            self.bit_size_entry.pack_forget()
            self.generate_key_button.pack_forget()

            self.message_entry.delete(0, tk.END)
            self.key_entry.delete(0, tk.END)
            self.generate_vernam_key_button.pack()
            self.key_label.config(text='key: ')
            self.explanation_button.place(x = 1100, y=100)
            self.expand_button.place(x = 680, y=100)

        elif selected_algorithm_name == 'Affine Cipher':
            self.bit_size_label.pack_forget()
            self.bit_size_entry.pack_forget()
            self.generate_key_button.pack_forget()

            self.message_entry.delete(0, tk.END)
            self.key_entry.delete(0, tk.END)
            self.key_label.config(text='key - enter two integers separated with a comma:')
            self.explanation_button.place(x = 1100, y=100)   
            self.expand_button.place(x = 680, y=100) 

        elif selected_algorithm_name == 'RSA Algorithm':
            self.bit_size_label.pack()
            self.bit_size_entry.pack()
            self.generate_key_button.pack()

            self.message_entry.delete(0, tk.END)
            self.key_entry.delete(0, tk.END)
            self.generate_vernam_key_button.pack_forget()
            self.key_label.config(text='enter a bit size and press the generate key button down below!')
            self.explanation_button.place(x = 1100, y=100)
            self.expand_button.place(x = 680, y=100)

        


    def update_summary(self, event): #dynamically updates gui
        selected_algorithm_name = self.algorithm_var.get()
        selected_algorithm = self.encryption_methods.get(selected_algorithm_name)
        if selected_algorithm:
            summary_text = selected_algorithm.get_summary()
            self.summary_text.config(state="normal")
            self.summary_text.delete("1.0", tk.END)
            self.summary_text.insert("1.0", summary_text)
            self.summary_text.config(state="disabled")

    def update_summary_and_gui_activation(self, event): #wrapper function
        self.update_summary(event)
        self.gui_change(event)  

    
    def close_window(self): #closes window function
        self.explanation_window.destroy()
    
    def expand(self): #expand texts implementaion
        self.explanation_window = tk.Toplevel()
        self.explanation_window.title("")
        self.explanation_window.configure(bg='#383444')
        self.explanation_window.state("zoomed")
        self.key = self.key_var.get()
        self.message = self.message_var.get()
        try: #error handling
            self.output = self.result
        except AttributeError: #if the output is empty, it should except the attribute error and replace the output with an empty string so it can be shown on the screen
            self.output = ''
#widgets

        self.expanded_key_label = tk.Label(self.explanation_window, text="Key:",  bg= '#383444', fg='white', font=('Segoe UI', '11'))
        self.expanded_key_text = tk.Text(self.explanation_window, height=20, width=150, wrap = WORD, bg='#080404', fg='white')
        self.expanded_message_label = tk.Label(self.explanation_window, text="message:",  bg= '#383444', fg='white', font=('Segoe UI', '11'))
        self.expanded_message_text = tk.Text(self.explanation_window, height=10, width=150, wrap = WORD, bg='#080404', fg='white')
        self.expanded_output_label = tk.Label(self.explanation_window, text="output:",  bg= '#383444', fg='white', font=('Segoe UI', '11'))
        self.expanded_output_text = tk.Text(self.explanation_window, height=20, width=150, wrap = WORD, bg='#080404', fg='white')
        self.close_window_button = tk.Button(self.explanation_window, text='close', width = 10, height = 1, command= self.close_window,  bg= '#282424', fg='white', font=('Segoe UI', '11'))

        self.expanded_key_label.pack()
        self.expanded_key_text.pack()
        self.expanded_message_label.pack()
        self.expanded_message_text.pack(padx=10, pady=10)
        self.expanded_output_label.pack()
        self.expanded_output_text.pack(padx=10, pady=10)
        self.close_window_button.pack()
        
        self.expanded_key_text.config(state="normal")
        self.expanded_key_text.delete("1.0", tk.END)
        self.expanded_key_text.insert("1.0", self.key)
        self.expanded_key_text.config(state="disabled")

        self.expanded_message_text.config(state="normal")
        self.expanded_message_text.delete("1.0", tk.END)
        self.expanded_message_text.insert("1.0", self.message)
        self.expanded_message_text.config(state="disabled")

        self.expanded_output_text.config(state="normal")
        self.expanded_output_text.delete("1.0", tk.END)
        self.expanded_output_text.insert("1.0", self.output)
        self.expanded_output_text.config(state="disabled")
        

        

    def explain_encryption_method(self): #if expand texts button is pressed
        selected_algorithm_name = self.algorithm_var.get()
        window = tk.Toplevel(self.window)
        window.title(selected_algorithm_name)
        window.state("zoomed")

        self.encryption_explanation = encryption_explanation(selected_algorithm_name, window)
        self.encryption_explanation.show_frame()



    def navigate_history_backward(self): #buton for using the previous encrypted/decrypted message
        current_mode = self.mode_var.get()

        if current_mode == ENCRYPT: #uses decrypt stack if mode is in encrypt
            if not self.decryption_history.is_empty(): #chekcs if stack is empty
                latest_message = self.decryption_history.pop() #uses composition so it can pop the previous message into the message box
                self.message_entry.delete(0, tk.END)
                self.message_entry.insert(0, latest_message)
            else:
                pass 
        elif current_mode == DECRYPT: #uses encrypt stack if mode is in decrypt
            if not self.encryption_history.is_empty(): #checks the stack is empty
                latest_message = self.encryption_history.pop() #uses composition so it can pop the previous message into the message box
                self.message_entry.delete(0, tk.END)
                self.message_entry.insert(0, latest_message)
            else:
                pass

    def toggle_mode(self): #dynamic changes mode
        self.mode_var.set(not self.mode_var.get())
        current_mode = self.mode_var.get()
        selected_algorithm_name = self.algorithm_var.get()

        # Update the text of the toggle button based on the current mode

        if current_mode == ENCRYPT:
            backward_button_text = 'previous decrypted message'
            execution_button_text = "Encrypt"
            if selected_algorithm_name == "RSA Algorithm":
                current_key = self.public_key #gets public key
                self.key_label.config(text='public key: ')
            elif selected_algorithm_name == "Vernam Cipher":
                self.key_label.config(text='encrypt key: ')

        else:
            backward_button_text = 'previous encrypted message'
            execution_button_text = "Decrypt"
            if selected_algorithm_name == "RSA Algorithm":
                current_key = self.private_key #gets private key
                self.key_label.config(text='private key: ')
            elif selected_algorithm_name == "Vernam Cipher":     
                self.key_label.config(text='decrypt key: ')

        self.toggle_button.config(text=execution_button_text + " Mode")
        self.backward_button.config(text=backward_button_text)
        self.encrypt_button.config(text=execution_button_text)
        if selected_algorithm_name == "RSA Algorithm":
            self.key_entry.delete(0, tk.END)
            self.key_entry.insert(0,current_key)

    def encrypt_or_decrypt(self): #executes encryption
        selected_algorithm_name = self.algorithm_var.get()#gets name of current algorithm
        selected_algorithm = self.encryption_methods.get(selected_algorithm_name) #gets the encryption/decryption methods of the algorithm  mapped to the algorithm name

        message = self.message_var.get()
        key = self.key_var.get()
        current_mode = self.mode_var.get()
        if current_mode == ENCRYPT:
            self.result = selected_algorithm.encrypt(message, key) #stores result
            self.encryption_history.push(self.result) #this pushes the encrypted message onto the decrypt stack
        elif current_mode == DECRYPT:
            self.result = selected_algorithm.decrypt(message, key) #stores result
            self.decryption_history.push(self.result) #this pushes the decrypted message onto the encrypt stack

        self.output_var.set(self.result) #shows the result in the output box
        self.output_entry.delete(0, tk.END)  # Clear previous text
        self.output_entry.insert(0, self.result)
        


if __name__ == "__main__": #verifies file
    login_window = tk.Tk()
    login_window.configure(bg='#383444')
    login_system = login_system(login_window)

    login_window.mainloop() #starts gui

    if login_system.is_authenticated:
        # get the username of the authenticated user
        username = login_system.username_var.get()
        
        main_window = tk.Tk()
        main_window.configure(bg='#383444')
        app = app_interface(main_window, username)
         # pass in the username of the logged in user
        main_window.mainloop()

