"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Pavel Both
email: pavelboth@gmail.com
discord: conjuctor Pavel Both
"""
import os
import sys 

def clear_terminal():
    # Podmínka pro různé operační systémy
    if os.name == 'nt':  # Pro Windows
        os.system('cls')
    else:  # Pro ostatní operační systémy (Linux, MacOS)
        os.system('clear')

userlist = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

clear_terminal()

username = input("Enter username: ")
if username in userlist:
    password = input("Enter heslo: ")  
    passwordlist = userlist[username]
    if password == passwordlist:
        print("\nLogin successful")
        print("\n-----------------------------------------------------------------\n")  
        print("Hello " + username, "Welcome in our program")       
        print("\n-----------------------------------------------------------------\n")     
    else:
        print("Wrong password")
        sys.exit()      
else:
    print("User is not registred")
    sys.exit()       

text_variant = input("Choose option 1, 2 or 3 of the text you want to analyze: ")
if text_variant.isdigit():
    text_variant = int(text_variant)
    print("\n-----------------------------------------------------------------\n")
    if text_variant in [1, 2, 3]:
        text = TEXTS[text_variant - 1].split()
        print(f"{username}, you chose text option number >>> {text_variant} <<< great choice :-)")
    else:
        print("Wrong input\n")
        sys.exit()
else:
    print("wrong input.\n")
    sys.exit()
                  
capital_letter_A = 0
capital_letters = 0
lower_letter = 0
numeric = 0
total = 0
record = {}

for x in text:
        if x[0].isupper(): 
            capital_letter_A += 1    # počet slov začínajících velkým písmenem
        if x.isalpha() and x.isupper(): 
            capital_letters += 1     # počet slov psaných velkými písmeny 
        if x.islower(): 
            lower_letter += 1        # počet slov psaných malými písmeny
        if x.isnumeric(): 
            numeric += 1             # počet čísel (ne cifer)
        if x.isnumeric(): 
            total += int(x)          # suma všech čísel (ne cifer) v textu.
        length = len(x)
        if length in record:
            record[length] += 1
        else:
            record[length] = 1
            
print("\n-----------------------------------------------------------------\n")
print("There are", len(text), "words in the selected text.")         
print("There are", capital_letter_A , "words in the selected text.")
print("There are", capital_letters, "titlecase words.")   
print("There are", lower_letter, "lowercase words.")
print("There are", numeric ,"numeric strings.")
print("The sum of all the numbers is", total)

sorted_words = sorted(record.items(), key=lambda x: x[0])
print("\nNumber of words with a given length:")
print("---------------------------------")
print("Length | Frequency        ")
print("---------------------------------")
for length, number in sorted_words:
    if length < 10:
        print ( " ", length , "   ", "#" * number, " " * (17-number), "|", number)
    else:
        print ( " ", length , "  ", "#" * number, " " * (17-number), "|", number)               
print("\n-----------------------------------------------------------------")


 

        

        
