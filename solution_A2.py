# --------------------------
# Name: Jiayao Pang ID: 194174300
# CP460 (Fall 2019)
# Assignment 2
# --------------------------

import math
import string
import utilities_A2


# ---------------------------------
# Q1: Vigenere Cipher (Version 2) #
# ---------------------------------
# -------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): string of any length
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call e_vigenere1
#               else --> call e_vigenere2
#               If invalid key (not string or empty string or non-alpha string) -->
#                   print error and return '',''
# ---------------------------------------------------------------------------------------
def e_vigenere(plaintext, key):
    if not isinstance(key, str) or key == '' or not key.isalpha():
        print('Error (e_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return e_vigenere1(plaintext, key)
    else:
        return e_vigenere2(plaintext, key)


# -------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): string of anylength
# Return:       ciphertext (string)
# Description:  Genereic Encryption scheme using Vigenere Cipher
#               calls proper function depending on key length
#               if len(key) == 1 --> call d_vigenere1
#               else --> call d_vigenere2
#               If invalid key (not string or empty string or contains no alpha char) -->
#                   print error and return '',''
# ---------------------------------------------------------------------------------------
def d_vigenere(ciphertext, key):
    if not isinstance(key, str) or key == '' or not key.isalpha():
        print('Error (d_vigenere): invalid key!')
        return ''
    key = key.lower()
    if len(key) == 1:
        return d_vigenere1(ciphertext, key)
    else:
        return d_vigenere2(ciphertext, key)


# -------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
# ---------------------------------------------------------------------------------------
def e_vigenere1(plaintext, key):
    # your code here
    ciphertext = ''
    square = utilities_A2.get_vigenereSquare()

    for char in plaintext:
        if char.lower() in square[0]:
            plainIndex = square[0].index(char.lower())
            keyIndex = square[0].index(key.lower())
            cipherChar = square[keyIndex][plainIndex]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
            key = char.lower()
        else:
            ciphertext += char

    return ciphertext

    return ciphertext


# -------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Encryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
# ---------------------------------------------------------------------------------------
def e_vigenere2(plaintext, key):
    # your code here
    ciphertext = ''
    square = utilities_A2.get_vigenereSquare()
    length = len(key)
    counter = 0

    # use the letter from key to encrypt not the plaintext itself
    # use mod function to make it recursive
    for char in plaintext:
        if char.lower() in square[0]:
            plainIndex = square[0].index(char.lower())
            keyIndex = square[0].index(key[counter % length].lower())
            cipherChar = square[keyIndex][plainIndex]
            ciphertext += cipherChar.upper() if char.isupper() else cipherChar
            counter += 1
            counter %= length
        else:
            ciphertext += char

    return ciphertext


# -------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): single character
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
# ---------------------------------------------------------------------------------------
def d_vigenere1(ciphertext, key):
    # your code here
    plaintext = ''
    square = utilities_A2.get_vigenereSquare()

    for char in ciphertext:
        if char.lower() in square[0]:
            keyIndex = square[0].index(key.lower())
            plainIndex = 0
            for i in range(26):
                if square[i][keyIndex] == char.lower():
                    plainIndex = i
                    break

            plainChar = square[0][plainIndex]
            key = plainChar
            plaintext += plainChar.upper() if char.isupper() else plainChar

        else:
            plaintext += char

    return plaintext


# -------------------------------------------------------------------------------------
# Parameters:   ciphertext(string)
#               key (str): a phrase
# Return:       ciphertext (string)
# Description:  Decryption using Vigenere Cipher (Polyalphabetic Substitituion)
#               Non alpha characters --> no substitution
#               Algorithm preserves case of the characters
# ---------------------------------------------------------------------------------------
def d_vigenere2(ciphertext, key):
    # your code here
    plaintext = ''
    square = utilities_A2.get_vigenereSquare()
    length = len(key)

    # use the letter from key to decrypt
    # use mod function to make it recursive
    counter = 0
    for char in ciphertext:
        if char.lower() in square[0]:
            keyIndex = square[0].index(key[counter % length].lower())
            counter += 1
            counter %= length
            plainIndex = 0
            for i in range(26):
                if square[i][keyIndex] == char.lower():
                    plainIndex = i
                    break

            plainChar = square[0][plainIndex]

            plaintext += plainChar.upper() if char.isupper() else plainChar

        else:
            plaintext += char

    return plaintext


# -------------------------------------
# Q2: Vigenere Crytanalysis Utilities #
# -------------------------------------

# -----------------------------------------------------------------------------
# Parameters:   text (string)
#               size (int)
# Return:       list of strings
# Description:  Break a given string into strings of given size
#               Result is provided in a list
# ------------------------------------------------------------------------------
def text_to_blocks(text, size):
    # your code here
    blocks = list()
    element = ''
    for char in text:
        if len(element) == size:
            blocks.append(element)
            element = ''
        element += char
    # do not forget the last block whose size is not equal to 'size'
    if len(element) != 0:
        blocks.append(element)

    return blocks


# -----------------------------------
# Parameters:   text (string)
# Return:       modifiedText (string)
# Description:  Removes all non-alpha characters from the given string
#               Returns a string of only alpha characters upper case
# -----------------------------------
def remove_nonalpha(text):
    # your code here
    modifiedText = ''
    for char in text:
        if char.isalpha():
            modifiedText += char

    return modifiedText


# -------------------------------------------------------------------------------------
# Parameters:   blocks: list of strings
# Return:       baskets: list of strings
# Description:  Assume all blocks have same size = n (other than last block)
#               Create n baskets
#               In basket[i] put character #i from each block
# ---------------------------------------------------------------------------------------
def blocks_to_baskets(blocks):
    # your code here
    # init the list to store string types
    empty = ''
    baskets = [empty] * len(blocks[0])

    for c in range(len(blocks[0])):
        for element in blocks:
            if c < len(element):
                baskets[c] += element[c]

    return baskets


# ----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       I (float): Index of Coincidence
# Description:  Computes and returns the index of coincidence 
#               for a given text
# ----------------------------------------------------------------
def get_indexOfCoin(ciphertext):
    # your code here
    ciphertext = remove_nonalpha(ciphertext)
    length = len(ciphertext)
    # make sure 'divided by 0' error would not occur
    if length < 2:
        return 0
    countList = utilities_A2.get_charCount(ciphertext)

    # calculate the sum
    sum = 0
    for charCount in countList:
        sum += charCount * (charCount - 1)
    # use the formula to get the final result
    I = sum / (length * (length - 1))

    return I


# ----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses Friedman's test to compute key length
#               returns key length rounded to nearest integer
# ---------------------------------------------------------------
def getKeyL_friedman(ciphertext):
    # your code here
    I = get_indexOfCoin(ciphertext)
    k = round((0.0633511 - 1 / 26) / (I - 1 / 26))
    return k


# ----------------------------------------------------------------
# Parameters:   ciphertext(string)
# Return:       key length (int)
# Description:  Uses the Ciphertext Shift method to compute key length
#               Attempts key lengths 1 to 20
# ---------------------------------------------------------------
def getKeyL_shift(ciphertext):
    # your code here
    resultList = list()

    for i in range(1, 21):
        sum = 0
        counter = 0
        for char in ciphertext[i:]:
            # add 1 if it matches
            if char == ciphertext[counter]:
                sum += 1
            counter += 1
        resultList.append(sum)

    # get the index and add 1
    k = resultList.index(max(resultList)) + 1

    return k


# ---------------------------------
#   Q3:  Block Rotate Cipher     #
# ---------------------------------
# -----------------------------------------------------------
# Parameters:   key (b,r)
# Return:       updatedKey (b,r)
# Description:  Assumes given key is in the format of (b(int),r(int))
#               Updates the key in three scenarios:
#               1- The key is too big (use modulo)
#               2- The key is negative
#               if an invalid key is given print error message and return (0,0)
# -----------------------------------------------------------
def adjustKey_blockRotate(key):
    # your code here
    # if key is a number(int)
    if isinstance(key, int):
        print('Error (adjustKey_blockRotate): Invalid key', end='')
        return (0, 0)
    # if there are more than two many elements in key
    if len(key) != 2:
        print('Error (adjustKey_blockRotate): Invalid key', end='')
        return (0, 0)
    # if either one in key is not type int
    if isinstance(key[0], int) is False or isinstance(key[1], int) is False:
        print('Error (adjustKey_blockRotate): Invalid key', end='')
        return (0, 0)
    # if the type of key is not tuple
    if type(key) is not tuple:
        print('Error (adjustKey_blockRotate): Invalid key', end='')
        return (0, 0)
    # if the first element of key is negative
    if key[0] <= 0:
        print('Error (adjustKey_blockRotate): Invalid key', end='')
        return (0, 0)
    # else: use the mode function to make the 2nd element smaller
    updatedKey = (key[0], key[1] % key[0])
    return updatedKey


# -----------------------------------
# Parameters:   text (string)
# Return:       nonalphaList (2D List)
# Description:  Analyzes a given string
#               Returns a list of non-alpha characters along with their positions
#               Format: [[char1, pos1],[char2,post2],...]
#               Example: get_nonalpha('I have 3 cents.') -->
#                   [[' ', 1], [' ', 6], ['3', 7], [' ', 8], ['.', 14]]
# -----------------------------------
def get_nonalpha(text):
    # your code here
    nonalphaList = list()
    counter = 0
    for char in text:
        if char.isalpha() is False:
            nonalphaList.append((char, counter))
        counter += 1

    return nonalphaList


# -----------------------------------
# Parameters:   text (str)
#               2D list: [[char1,pos1], [char2,pos2],...]
# Return:       modifiedText (string)
# Description:  inserts a list of nonalpha characters in the positions
# -----------------------------------
def insert_nonalpha(text, nonAlpha):
    # your code here
    modifiedText = text

    counter = 0
    for l in nonAlpha:
        # using [:] to handle strings
        temp1 = modifiedText[:l[1]]
        temp2 = modifiedText[l[1]:]
        modifiedText = temp1 + l[0] + temp2
        counter += 1

    return modifiedText


# -----------------------------------------------------------
# Parameters:   plaintext (string)
#               key (b,r): (int,int)
# Return:       ciphertext (string)
# Description:  break plaintext into blocks of size b
#               rotate each block r times to the left
# -----------------------------------------------------------
def e_blockRotate(plaintext, key):
    # your code here
    ciphertext = ''
    # adjust the key first
    updatedKey = adjustKey_blockRotate(key)
    # remove the non-alpha characters
    newText = remove_nonalpha(plaintext)
    # store the non-alpha characters previously
    nonalphaList = get_nonalpha(plaintext)

    # divide the text to blocks
    blocks = text_to_blocks(newText, updatedKey[0])

    # add 'q' behind the last block
    # cause no English word ends with 'q'
    while len(blocks[-1]) != updatedKey[0]:
        blocks[-1] += 'q'

    # shift every block
    for element in blocks:
        ciphertext += utilities_A2.shift_string(element, updatedKey[1], 'l')

    # do not forget to insert the non-alpha characters finally
    ciphertext = insert_nonalpha(ciphertext, nonalphaList)

    return ciphertext


# -----------------------------------------------------------
# Parameters:   ciphertext (string)
#               key (b,r): (int,int)
# Return:       plaintext (string)
# Description:  Decryption using Block Rotate Cipher
# -----------------------------------------------------------
def d_blockRotate(ciphertext, key):
    # your code here
    plaintext = ''

    updatedKey = adjustKey_blockRotate(key)

    newText = remove_nonalpha(ciphertext)
    nonalphaList = get_nonalpha(ciphertext)

    blocks = text_to_blocks(newText, updatedKey[0])

    for element in blocks:
        plaintext += utilities_A2.shift_string(element, updatedKey[1], 'r')
    plaintext = insert_nonalpha(plaintext, nonalphaList)

    # delete the 'q's in the last block
    while plaintext[-1] is 'q':
        plaintext = plaintext[:-1]

    return plaintext


# -----------------------------------------------------------
# Parameters:   ciphertext (string)
#               b1 (int): starting block size
#               b2 (int): end block size
# Return:       plaintext,key
# Description:  Cryptanalysis of Block Rotate Cipher
#               Returns plaintext and key (r,b)
#               Attempts block sizes from b1 to b2 (inclusive)
#               Prints number of attempts
# -----------------------------------------------------------
def cryptanalysis_blockRotate(ciphertext, b1, b2):
    # your code here
    plaintext = ''
    num_attempts = 0
    found = False

    # try every block size among the range and decrypt it
    # see if it's plaintext
    for i in range(b1, b2 + 1):
        for j in range(1, i):
            num_attempts += 1
            plaintext = d_blockRotate(ciphertext, (i, j))
            if utilities_A2.is_plaintext(plaintext, "engmix.txt", 0.8):
                found = True
                break
        if found:
            break

    # print the results and set the values to the key
    if found:
        key = (i, j)
        print('Key found after ' + str(num_attempts) + ' attempts')
        print('Key = (' + str(key[0]) + ', ' + str(key[1]) + ')')
        print('Plaintext: ' + plaintext)
    else:
        key = (0, 0)
        print('Block Rotate Cryptanalysis Failed. No Key was found')

    return plaintext, key


# ---------------------------------
#       Q4: Cipher Detector     #
# ---------------------------------
# -----------------------------------------------------------
# Parameters:   ciphertext (string)
# Return:       cipherType (string)
# Description:  Detects the type of a given ciphertext
#               Categories: "Atbash Cipher, Spartan Scytale Cipher,
#                   Polybius Square Cipher, Shfit Cipher, Vigenere Cipher
#                   All other ciphers are classified as Unknown. 
#               If the given ciphertext is empty return 'Empty Ciphertext'
# -----------------------------------------------------------
def get_cipherType(ciphertext):
    # your code here

    # empty string
    if len(ciphertext) == 0:
        return 'Empty Ciphertext'

    # ------------------------------------------------------------
    # the detecting sequence is:
    # Polybius Square Cipher -> Atbash Cipher -> Shfit Cipher ->
    # Spartan Scytale Cipher -> Vigenere Cipher
    # ------------------------------------------------------------

    # Polybius Square Cipher---------------------------------------------------------------------------
    polybius_square = ciphertext.replace('\n', '')
    # if all numbers and the length is even
    if len(polybius_square) % 2 == 0 and polybius_square.isnumeric():
        return 'Polybius Square Cipher'

    # Atbash Cipher-----------------------------------------------------------------------------------
    # step back to the origin text
    atbash = ''
    lowerChars = utilities_A2.get_lower()
    upperChars = lowerChars.upper()
    for c in ciphertext:
        if c.isalpha():
            atbash += upperChars[ord('Z') - ord(c)] if c.isupper() else lowerChars[ord('z') - ord(c)]
        else:
            atbash += c
    # get the I and chi_squared first
    I = get_indexOfCoin(atbash)
    chi = utilities_A2.get_chiSquared(atbash)
    if abs(0.065 - I) <= 0.003 and chi < 150:
        return 'Atbash Cipher'
    # sometimes we need to use the is_plaintext method
    if utilities_A2.is_plaintext(atbash, 'engmix.txt', 0.8):
        return 'Atbash Cipher'

    # Shfit Cipher------------------------------------------------------------------------------------
    # use cryptanalysis to get the 'best' plaintext
    tempKey, shift = utilities_A2.cryptanalysis_shift(ciphertext)
    # see if the so called 'best' plaintext is real according to I and the chi_square
    I = get_indexOfCoin(shift)
    chi = utilities_A2.get_chiSquared(shift)
    # if the key is one, then it not a ciphertext
    if tempKey != 1:
        if abs(0.065 - I) <= 0.003 and chi < 150:
            return 'Shfit Cipher'
        if utilities_A2.is_plaintext(shift, 'engmix.txt', 0.8):
            return 'Shfit Cipher'
    else:
        return 'Unknown'

    # Spartan Scytale Cipher---------------------------------------------------------------------------
    # if the type of this ciphertext is not one of the 3 types above
    # then we can get the I and chi_square directly
    I = get_indexOfCoin(remove_nonalpha(ciphertext))
    chi = utilities_A2.get_chiSquared(remove_nonalpha(ciphertext))
    if abs(0.065 - I) <= 0.003 and chi < 150:
        return 'Spartan Scytable Cipher'

    # sometimes the 'I & chi' method didn't work
    # then wen use frequency analysis since it's mono-alphabetical
    freqTable = utilities_A2.get_freqTable()
    charCount = utilities_A2.get_charCount(remove_nonalpha(ciphertext))
    textMax = freqTable.index(max(freqTable))
    textMin = freqTable.index(min(freqTable))
    charMax = charCount.index(max(charCount))
    charMin = charCount.index(min(charCount))
    # see if the frequency matches
    if charCount[25] == 0 or charMin == textMin:
        if charMax == textMax:
            return 'Spartan Scytable Cipher'

    # Vigenere Cipher---------------------------------------------------------------------------------
    # theoretically, the average word length is 4.7
    # and 'sub' is approximately equal to #words in the ciphertext
    # if it's not Vegenere Cipher, 4.7 * sub will be much larger than normal
    sub = len(ciphertext) - len(remove_nonalpha(ciphertext))
    # but unfortunately, the average word length in ciphertext6.txt is about 3.74
    # so I changed the parameter
    if 3.7 * sub > len(remove_nonalpha(ciphertext)):
        return 'Unknown'

    # get the possible key length
    FriedmanL = getKeyL_friedman(ciphertext)
    ShiftL = getKeyL_shift(ciphertext)

    no_found = False
    final_found = False
    if ShiftL != 1:
        # try every possible size
        for size in range(min(FriedmanL, ShiftL), max(FriedmanL, ShiftL) + 1):
            blocks = text_to_blocks(remove_nonalpha(ciphertext), size)
            baskets = blocks_to_baskets(blocks)

            for element in baskets:
                # get the list of chi_squared for every shift
                chiList = [round(utilities_A2.get_chiSquared(utilities_A2.d_shift(element, (i, 'l'))), 4)
                           for i in range(26)]
                # judge if the chi value is normal
                if min(chiList) >= 150:
                    no_found = True
                    break

            if no_found:
                no_found = False
            else:
                final_found = True
                break

        if final_found:
            return 'Vigenere Cipher'

    cipherType = 'Unknown'
    return cipherType


# -------------------------------------
#  Q5: Wheastone Playfair Cipher     #
# -------------------------------------
# -----------------------------------------------------------
# Parameters:   plaintext (string)
# Return:       modifiedPlain (string)
# Description:  Modify a plaintext through the following criteria
#               1- All non-alpha characters are removed
#               2- Every 'W' is translsated into 'VV' double V
#               3- Convert every double character ## to #X
#               4- if the length of text is odd, add X
#               5- Output is formatted as pairs, separated by space
#                   all upper case
# -----------------------------------------------------------
def formatInput_playfair(plaintext):
    # your code here
    modifiedPlain = ''

    plaintext = remove_nonalpha(plaintext).upper()
    # replace all 'W' to 'VV'
    plaintext = plaintext.replace('W', 'VV')
    # add 'X' if the length is odd
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    # replace every ## to #X
    modPlainList = text_to_blocks(plaintext, 2)
    for element in modPlainList:
        if element[0] == element[1]:
            element = element[:-1] + 'X'

        modifiedPlain = modifiedPlain + element + ' '

    modifiedPlain = modifiedPlain.strip()

    return modifiedPlain


# -------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Encryption using Wheatstone Playfair Cipher
# ---------------------------------------------------------------------------------------
def e_playfair(plaintext, key):
    # your code here
    ciphertext = ''
    plaintextList = formatInput_playfair(plaintext).split(' ')

    row = len(key)
    column = len(key[0])

    for element in plaintextList:
        (indexF_r, indexF_c) = get_index(element[0], key)
        (indexS_r, indexS_c) = get_index(element[1], key)

        # rule 1
        if indexF_r == indexS_r and indexF_c != indexS_c:
            ciphertext += key[indexF_r][(indexF_c + 1) % column]
            ciphertext += key[indexF_r][(indexS_c + 1) % column]
            ciphertext += ' '
        # rule 2
        elif indexF_r != indexS_r and indexF_c == indexS_c:
            ciphertext += key[(indexF_r + 1) % row][indexF_c]
            ciphertext += key[(indexS_r + 1) % row][indexF_c]
            ciphertext += ' '
        # rule 3
        else:
            ciphertext += key[indexF_r][indexS_c]
            ciphertext += key[indexS_r][indexF_c]
            ciphertext += ' '
    # delete the last ' '
    ciphertext = ciphertext.strip()

    return ciphertext


# -------------------------------------------------------------------------------------
# Parameters:   plaintext(string)
#               key: playfair Square (2D List)
# Return:       ciphertext (string)
# Description:  Decryption using Wheatstone Playfair Cipher
# -------------------------------------------------------------------------------
def d_playfair(ciphertext, key):
    # your code here
    plaintext = ''
    ciphertextList = ciphertext.split(' ')

    row = len(key)
    column = len(key[0])

    for element in ciphertextList:
        (indexF_r, indexF_c) = get_index(element[0], key)
        (indexS_r, indexS_c) = get_index(element[1], key)

        # rule 1
        if indexF_r == indexS_r and indexF_c != indexS_c:
            plaintext += key[indexF_r][(indexF_c - 1) % column]
            plaintext += key[indexF_r][(indexS_c - 1) % column]
            plaintext += ' '
        # rule 2
        elif indexF_r != indexS_r and indexF_c == indexS_c:
            plaintext += key[(indexF_r - 1) % row][indexF_c]
            plaintext += key[(indexS_r - 1) % row][indexF_c]
            plaintext += ' '
        # rule 3
        else:
            plaintext += key[indexF_r][indexS_c]
            plaintext += key[indexS_r][indexF_c]
            plaintext += ' '
    # delete the last ' '
    plaintext = plaintext.strip()

    return plaintext


# -------------------------------------------------------------------------------------
# Parameters:   char (string)
#               square: playfair Square (2D List)
# Return:       (i, j) : (row, column) which is the index for the input char
# Description:  Find the index of the char in the playfair Square
# -------------------------------------------------------------------------------
def get_index(char, square):
    for i in range(len(square)):
        for j in range(len(square[i])):
            if char == square[i][j]:
                return (i, j)

