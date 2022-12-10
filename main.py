import random
import time  # module imports need dependencies, check install script before running
from termcolor import colored

"""
Program Name: M1 and M2 Cracked
Program Purpose: Algorythmic Local Bruteforcer meant for the testing and studying of the law of random
Program Author: Coulter C. Stutz
Date Written: 8-22-22 -- 12-8-22 [STILL IN PROGRESS]

Bugs Right Now:
    Has issues pushing non-alphanumeric characters like punctuation through the ML Process
    Sometimes spotty error messages
"""



def get_key(val):  # checks keys
    for key, value in m2usedRand.items():
        if val == value:
            return key


"""
#####################################################################################################
#                                                                                                   #
#    Configuration                                                                                  #   # dat wide body tho 
#                                                                                                   #
#####################################################################################################
"""
enterIntoConsole = True  # configures if string is inputted through console
sleeptimes = 0.0000000  # How much sleep/delay time inbetween requests
selectedMethod = "all".upper()  # selects method
stringToCrack = [*"helloworld"]     # string to crack | only reads value if enterIntoConsole =! True
logall = True   # decides if stats and logging should be outputted to raw_out.txt and out.txt
demostrationTimes = 0  # will sleep for demonstration
"""####################################"""

"""
#########################################################################
#                                                                       #
#       Skinning                                                        #
#                                                                       #
#########################################################################
"""
configurationColors = 'red'  # Color shown in configuration print
successColors = 'green'  # Color shown in success messages and word color
dataColors = 'red'  # color shown in data
triedColors = 'red'  # Tried Color
failedColors = 'red'  # Color shown in error messages
"""####################################"""

# Predefined funcs
def nap(st):  # Nap function, made to catch quit exceptions
    try:
        time.sleep(st)
    except KeyboardInterrupt:  # if player quits during delay... then pop up with interuption errors
        print(
            f'{colored("Operation Interrupted!", failedColors)}: Attempted Times | M1:{colored(attempts, successColors)} M2:{colored(m2attempts, successColors)} | Total: {colored(attempts + m2attempts, successColors)} in {colored(str(time.time() - sTime), failedColors)} For: {colored("".join(stringToCrack), successColors)}')
        print(
            f'{colored("Operation Interrupted!", failedColors)}: Attempted Times | M2: {colored(m1ETime - m1STime, failedColors)} | M2: {colored(m2End - m2Start, failedColors)} For: {colored("".join(stringToCrack), successColors)}')
        print("")  # Whitespace


print(f'M{colored("CRACKED", "green")} Started!')  # notify that operation has started
nap(1)

char = [
    *"qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM<>?,./;'[]\-= |{}:!@#$%^&*()_+-=`~1234567890"]  # initiate a split by character list of
# all the chars that show up on a qwerty keeb

char_alpha = [*'qwertyuiopasdfghjklzxcvbnm']  # make a split list of all alpha characters

non_alphanumeric_stringables = [*"'~`!@#$%^&*()_+{}|:<>?-=[]\|;',./"]  # make a list of non alpha stringables

char_int = [*'1234567890']  # make a list of numerical characters to iterate through in the ML Solving Process

charDict = {}
offset = []

m1Used = []
m2Used = []  # initate varibles for Method 1: Char By Char
m2Close = []

m1ETime = 0
m1STime = 0

sTime = 0
eTime = 0

m2usedRandoms = []
m2usedRand = {}  # initate varibles for Method 2: String By String

contains = []  # contains varible for later processing

dictST = time.time()  # start the stopwatch for dictonary appending

for x in range(len(char)):  # Character initualization in a dictionary
    charDict[x] = char[x]  # appends character to dictonary
    print(f"Initualized {char[x]} at: {x}")  # notify

dictET = time.time()
print(f'Initialization took {colored(dictET - dictST, successColors)} seconds')
# nap(1)

cracked = []
m2Cracked = []  # Base save and refrence points
attempts = 0

total = 1

if enterIntoConsole:  # if userInput mode is enabled
    stringToCrack = [*input("String To Crack>>>>")]  # allow users to make input
    try:
        assert len(stringToCrack) != 0  # end program if len(stringToCrack) == 0
    except AssertionError:
        print("Cannot Be Zero!")  # error if the length of string == 0
else:  # if no userinput
    try:
        assert len(stringToCrack) != 0
    except AssertionError:
        print("Cannot Be Zero!")

print(len(stringToCrack))  # general debugging

'''
try:
    int(stringToCrack)
    contains.append("int")
except:
    if non_alphanumeric_stringables not in stringToCrack:
        contains.append("alpha")
    else:
        contains.append("all")
'''

#   print(colored()("".join(cracked), successColors"))

if selectedMethod != 'M2':
    cracked = []

    # init time var
    sTime = time.time()
    m1STime = time.time()  # init an start time

    for x in range(len(stringToCrack)):  # Random Char by Char brute-force
        for y in char:  # iterates through char
            attempts = attempts + 1  # starts an attempt
            print(
                f"{colored(''.join(cracked), successColors)}:{colored(y, dataColors)} attempts:{attempts}")  # print attempts work
            if y == stringToCrack[x]:  # if matches, appent to list
                cracked.append(y)
                break
            nap(sleeptimes)
    m1ETime = time.time()  # init a end time
    print(colored("".join(cracked), successColors))
    cracked = []


"""attempts = 0
for x in range(len(stringToCrack)):
    while True:
        randChar = random.choice(char)
        print(f"{colored()(''.join(cracked),successColors')}{colored()(randChar,'red')}")
        nap(sleeptimes)
        if randChar == stringToCrack[x]:
            cracked.append(randChar)
            break
        sys("cls")
nap(1)"""

print(colored("".join(cracked), successColors))  # prove success

m2attempts = 0  # initualize m2 variable for statistics
m2Start = time.time()  # start timer for m2Cracked

if selectedMethod != 'M1':
    while ''.join(stringToCrack).lower() != ''.join(m2Cracked).lower():
        m2Cracked.clear()

        try:
            int(''.join(stringToCrack))     # checks if string is all integer, if so then run only in integer mode
            for x in range(len(stringToCrack)):
                m2Cracked.append(random.choice(char_int))
        except:
            if char_int not in stringToCrack and non_alphanumeric_stringables not in stringToCrack:
                for x in range(len(stringToCrack)):
                    m2Cracked.append(random.choice(char_alpha))
            else:
                m2Cracked.append(random.choice(char))

        m2sorted = sorted(''.join(m2Cracked))
        stcSorted = sorted(''.join(stringToCrack))

        m2attempts = m2attempts + 1
        print(
            f"m2Cracked: Tried {colored(''.join(m2Cracked), triedColors)}:{colored(''.join(stringToCrack), successColors)} attempts:{m2attempts}")  # Thread 1
        m2usedRandoms.append(''.join(m2Cracked))

        if ''.join(m2Cracked) == ''.join(stringToCrack).lower():
            print(
                f'M2Cracked: {colored("".join(m2Cracked), successColors)}:{colored("".join(stringToCrack), successColors)}')
            m2End = time.time()
        elif m2sorted == stcSorted:
            m2Close.append(''.join(m2Cracked))

print(
    f"                                              {colored('Post Evaluation Statistics', configurationColors)}                                                            ")
print(colored(
    "--------------------------------------------------------------------------------------------------------------------",
    configurationColors))  # Whitespace

if selectedMethod == 'M1':
    print(f'{colored("Operation Completed!", successColors)}: Attempted Times | M1:{colored(attempts, successColors)} in {colored(str(time.time() - m1STime), dataColors)} For: {colored("".join(stringToCrack), successColors)}')
    print(f'{colored("Operation Completed!", successColors)}: Attempted Times | M1: {colored(m1ETime - m1STime, dataColors)}')
elif selectedMethod == 'M2':
    print(f'{colored("Operation Completed!", successColors)}: Attempted Times | M2:{colored(attempts, successColors)} in {colored(str(time.time() - m2Start), dataColors)} For: {colored("".join(stringToCrack), successColors)}')
    print(f'{colored("Operation Completed!", successColors)}: Attempted Times | M2: {colored(eTime - sTime, dataColors)}')
else:
    print(f'{colored("Operation Completed!", successColors)}: Attempted Times | M1:{colored(attempts, successColors)} M2:{colored(m2attempts, successColors)} | Total: {colored(attempts + m2attempts, successColors)} in {colored(str(time.time() - sTime), dataColors)} For: {colored("".join(stringToCrack), successColors)}')
    print(f'{colored("Operation Completed!", successColors)}: Attempted Times | M1: {colored(m1ETime - m1STime, dataColors)} | M2: {colored(m2End - m2Start, dataColors)} For: {colored("".join(stringToCrack), successColors)}')

print(colored(
    "--------------------------------------------------------------------------------------------------------------------",
    configurationColors))  # Whitespace

print("")  # Whitespace
print(
    f"                                                {colored('Post Analysis', configurationColors)}                                              ")
print(colored(
    "--------------------------------------------------------------------------------------------------------------------",
    configurationColors))  # Whitespace

for x in range(len(stringToCrack)):
    total = total * 96

if selectedMethod == 'M1' or selectedMethod == 'ALL':
    print()
    print(f"[M1CRACKED] {colored('Attempts:', configurationColors)}: {attempts}")
    print(f"[M1CRACKED] {colored('Possible Attempts', configurationColors)}: {total}")

if sleeptimes != 0.0 and selectedMethod != 'M2':
    print(f"[M1CRACKED] {colored('Delay Times:', configurationColors)}: {sleeptimes}")

if selectedMethod == 'M2' or selectedMethod == 'ALL':
    print()
    print(f"[M2CRACKED] {colored('Attempts:', configurationColors)}: {m2attempts}")
    print(f"[M2CRACKED] {colored('Possible Attempts', configurationColors)}: {total ^ 2}")
    print()

print(f"[ALL] {colored('Total Attempts:', configurationColors)}: {attempts + m2attempts}")
print()

if len(m2Close) > 0:
    print(f"{colored('Close Hits:', configurationColors)} {len(m2Close)}")
else:
    print(f"{colored('Close Hits:', configurationColors)} None")

try:
    int(''.join(stringToCrack))
    print(f"{colored('Ran IN:', configurationColors)} Integer Mode")
except:
    print(f"{colored('Ran IN:', configurationColors)} String Mode")


print(f"{colored('ConsoleInput?:', configurationColors)}: {enterIntoConsole}")
print(f"{colored('Selected Method:', configurationColors)}: {selectedMethod}")
print(f"{colored('Output All Attempts?:', configurationColors)}: {logall}")

if demostrationTimes == 0:
    print(f"{colored('Demonstration Mode:', configurationColors)}: {False}")
else:
    print(f"{colored('Demonstration Mode:', configurationColors)}: {True} with a time of {demostrationTimes}")

if len(m2Close) > 0:
    print(
        f"                                            {colored('Close Hits', configurationColors)}                                              ")
    print(colored(
        "--------------------------------------------------------------------------------------------------------------------",
        configurationColors))  # Whitespace
    print()

    print(m2Close)

    print()
    print(colored(
        "--------------------------------------------------------------------------------------------------------------------",
        configurationColors))  # Whitespace
    print()

if logall:

    for x in m2usedRandoms:  # iterate through used

        if x not in m2usedRand:  # if it isn't already in the numerated dictionary...
            m2usedRand[x] = 1  # Add it to the dictionary

        else:
            m2usedRand[x] = m2usedRand[x] + 1  # if it is, change the numerical value in dictionary
            # of the value to show that it came up again

    f = open('raw_out.txt', 'w+')
    for x in range(len(m2usedRandoms)):
        f.writelines(f'{m2usedRandoms[x]}\n')  # Output the raw output

    f = open('out.txt', 'w+')
    for x in reversed(sorted(m2usedRand.values())):  # Sort the list
        f.writelines(f'{get_key(x)}:{x}\n')  # Output the numerated list
        del m2usedRand[get_key(x)]  # Delete the key from dictionary to prevent nonnumerical sorting

"""
    Dev ChecklistS
    
    Fix NonAlphaNumericCharacters not showing up in M2Cracked!  [still hella broken lol]
    Make M2Cracked Faster with AlphaNumeric Characters  [hecc my man 45% slower for fucking punctuation]
    Fix The 'intresting' console output system

"""

print()
