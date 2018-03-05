#! /usr/bin/env python3.4
def find(pattern):
    with open('sequence2.txt', 'r') as myFile:
        content = myFile.read()
   # content = "138389"
    str_len = len(content)
    patt_len = len(pattern)
    digit = 0
    match = 0
    short_str_len = (str_len - patt_len + 1)
    num = ""
    list = []
    for i in range(short_str_len):
        #print("\nIn i loop. i = %d" % i)
        #print(" ")
        num = ""
        match = 0
        for j in range(patt_len):
            #print("\nIn j loop. j = %d" % j)
            #print("\npattern[%d]" % j)
            #print(pattern[j])
            digit = sum(c.isdigit() for c in pattern)
            #print("\nDigit: ")
            #print(digit)
            if content[j+i] == pattern[j]:
                match = match + 1
                #print("\nMatch: ")
                #print(match)
        if digit == match:
            for k in range(patt_len):
                #print("\nContent:")
                num = num + content[k+i]
            list.append(num)
    return list


        #Add else for empty list here!!!!!!!!!!
    #print("\n")
    #print("%d" % str_len)
    #print("%s" % content)

def getStreakProduct(sequence, maxSize, product):
    m = 0
    temp_prod = 1
    flag = 0
    num = ""
    list = []
    seq_len = len(sequence)
    #seqleniloop = (seq_len - maxSize + 1)
    for i in range(seq_len):        #seqleniloop
        #print(" ")
        num = ""
        flag = 0
        temp_prod = 1
        for j in range(maxSize):
            if flag == 0:
                #print("i= %d" % i)
                #print(sequence[i])
                if (i + j) < seq_len:
                    temp_prod = (temp_prod * ((ord(sequence[i + j])) - 48))
                    #print("Temp prod = %d" % temp_prod)
                    #print(ord(sequence[i + j]) - 48)
                    #print(temp_prod)
                if temp_prod == product:
                    #print(temp_prod) .....works
                    m = j
                    flag = 1
                    for k in range(i, (m + i + 1)):
                        #print(sequence[k], end='')
                        num = num + sequence[k]
                    list.append(num)
    return list
    #print(list)

def writePyramids(filePath, baseSize, count, char):
    half_base = int(baseSize / 2)
    f = open(filePath, "a")
    for i in range(half_base + 1):
        gap_count = half_base - i
        star = ""
        star_line = ""
        space = " "
        spacestr = ""
        group = ""
        for j in range(gap_count):
            spacestr = space*(j + 1)
        star = char*((2 * i) + 1)
        #print(star)
        group = spacestr+star+spacestr+space

        star_line = group*count

        f.write(star_line)
        f.write("\n")
    f.close()
        #print(star_line)

def getStreaks(sequence, letters):
    flag = 0
    count = 0
    list = []
    string = ""
    #group = ""
    sequence_length = len(sequence)
    letters_length = len(letters)
    for i in range(1, (sequence_length + 1)):
        if i < sequence_length:
            k = i - 1
            if letters.find(sequence[k]) == -1:
                #k = k + 1
                continue
            #print(sequence[k])
            if sequence[k] == sequence[i]:
                flag = 1
                count = count + 1
            else:
                flag = 0
                string = ""
                if (k - count) == 0:
                    string = sequence[:(k + 1)]
                else:
                    string = sequence[(k - count):(k + 1)]
                count = 0
                list.append(string)
        elif i == sequence_length:
            k = i - 1
            m = i - 2
            #print(sequence[k])
            if letters.find(sequence[k]) == -1:
                #k = k + 1
                #break
                #print(list)
                return list
                #return
            if sequence[k] == sequence[m]:
                flag = 1
                count = count + 1

            else:
                flag = 0
                string = ""
                count = 0
            string = string + sequence[k]
            list.append(string)

    #print(list)
    return list

def findNames(nameList, part, name):
    outputlist = []
    listlen = len(nameList)
    for i in range(listlen):
        list_elem = nameList[i]
        fname,lname = list_elem.split(" ")
        if part == "L":
            if lname.lower() == name.lower():
                outputlist.append(list_elem)
            else:
                continue
        elif part == "F":
            if fname.lower() == name.lower():
                outputlist.append(list_elem)
            else:
                continue
        elif part == "FL":
            if (fname.lower() == name.lower()) or (lname.lower() == name.lower()):
                outputlist.append(list_elem)
            else:
                continue
    #print(outputlist)
    return outputlist

def convertToBoolean(num, size):
    if isinstance(num, int) == False:
        jazz = []
        return jazz
    if isinstance(size, int) == False:
        jazz = []
        return jazz

    
    converted = bin(num)
    extraaa,binerdy = converted.split("b")
    jazz = []
    bin_len = len(binerdy)
    if bin_len >= num:
        for i in range(bin_len):
            if binerdy[i] == '0':
                jazz.append("False")
            else:
                jazz.append("True")
    else:
        for i in range((size - bin_len)):
            jazz.append("False")
        for z in range(bin_len):
            if binerdy[z] == '0':
                jazz.append("False")
            else:
                jazz.append("True")

    #print(jazz)
    return jazz

def convertToInteger(boolList):
    if isinstance(boolList, list) == True:
        if not boolList:
            return None
        else:
            bool_len = len(boolList)
            number = ""
            one = "1"
            zero = "0"

            for i in range(bool_len):
                if isinstance(boolList[i], bool) == False:
                    return None
                else:
                    if boolList[i] == True:
                        number = number + one
                    else:
                        number = number + zero
                output_num = int(number, 2)
            #print(output_num)
            return output_num

    else:
        return None









#if __name__ == "__main__":

    #find("1XX7")
    #getStreakProduct("54789654321687984", 5, 288)
    #getStreakProduct("14822", 3, 32)
    #writePyramids('py17.txt', 17, 6, '*')
    #getStreaks("SAAASSSSSSAPPPSSPPBBCCCSSSZZZZ", "SAQT")
    #names = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    #findNames(names, "F", "JOHNSON")
    #convertToBoolean(135, 2)
    #bList = [True, False, False, False, False, True, True]
    #convertToInteger(bList)
