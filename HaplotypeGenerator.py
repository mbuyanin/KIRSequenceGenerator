# Created for use of testing whether a concept for a KIR sequencer would work.
import sys
import random as rand

genes = {"g3DL3" : [], "g2DS2" : [], "g2DL2_3" : [], "g2DL5B" : [], "g2DS3_5" : [], "g2DP1" : [], "g2DL1" : [], "g3DP1" : [], "g2DL4" : [], "g3DP1" : [], "g2DL4" : [], "g3DL1_S1" : [], "g2DL5A" : [], "g2DS3_5a" : [], "g2DS1" : [], "g2DS4" : [], "g3DL2" : []}

def getRandHaplotype(randInt):
    file = open("HAPLOTYPE_GENETIC_INFO.txt")
    for i, line in enumerate(file):
        if i == randInt:
            (g3DL3, g2DS2, g2DL2, g2DL3, g2DL5B, g2DS3, g2DS5, g2DP1, g2DL1, g3DP1, g2DL4, g3DL1, g3DS1, g2DL5A, g2DS3a, g2DS5a, g2DS1, g2DS4, g3DL2) = line.split()
    return (g3DL3, g2DS2, g2DL2, g2DL3, g2DL5B, g2DS3, g2DS5, g2DP1, g2DL1, g3DP1, g2DL4, g3DL1, g3DS1, g2DL5A, g2DS3a, g2DS5a, g2DS1, g2DS4, g3DL2)

def readHaplotype(sequence):
    failedString = ""
    for i in range(1020):
        failedString += "N"

    if sequence[0] == '1': #3DL3
        genes["g3DL3"] = fileReader("./FASTA Files/KIR3DL3_gen.fasta")
    else:
        genes["g3DL3"] = failedString
            

    if sequence[1] == '1': #2DS2
       genes["g2DS2"] = fileReader("./FASTA Files/KIR2DS2_gen.fasta")
    else:
        genes["g2DS2"] = failedString
    
    if sequence[2] == '1': #2DL2
        genes["g2DL2_3"] = fileReader("./FASTA Files/KIR2DL2_gen.fasta")
    elif sequence[3] == '0':
        genes["g2DL2_3"] = failedString
   
    if sequence[3] == '1': #2DL3
        genes["g2DL2_3"] = fileReader("./FASTA Files/KIR2DL3_gen.fasta")
    
    print("2DL5B")
    if sequence[4] == '1': #2DL5B
        file = open("./FASTA Files/KIR2DL5_gen.fasta")
        outputString = ""
        lines = file.readlines()
        randomLine = rand.randint(0,len(lines))

        for i, line in enumerate(lines): # Focus area for changing
            if randomLine == i:
                j = typeChecker(lines, i, "B")
                break
        
        line = lines[j]
        print(line)
        line = lines[j + 1]
        
        while (not line.startswith(">")) and j != len(lines) - 2:
            outputString += line[:len(line) - 1] #Change this to :60 - len(line) in the future
            j += 1
            line = lines[j]
        genes["g2DL5B"] = outputString
    else:
        genes["g2DL5B"] = failedString
    
    if sequence[5] == '1': #2DS3
        genes["g2DS3_5"] = fileReader("./FASTA Files/KIR2DS3_gen.fasta")
    elif sequence[6] == '0':
        genes["g2DS3_5"] = failedString
   
    if sequence[6] == '1': #2DS5
        genes["g2DS3_5"] = fileReader("./FASTA Files/KIR2DS5_gen.fasta")
    
    if sequence[7] == '1': #2DP1
        genes["g2DP1"] = fileReader("./FASTA Files/KIR2DP1_gen.fasta")
    else:
        genes["g2DP1"] = failedString

    if sequence[8] == '1': #2DL1
        genes["g2DL1"] = fileReader("./FASTA Files/KIR2DL1_gen.fasta")
    else:
        genes["g2DL1"] = failedString

    if sequence[9] == '1': #3DP1
        genes["g3DP1"] = fileReader("./FASTA Files/KIR3DP1_gen.fasta")
    else:
        genes["g3DP1"] = failedString

    if sequence[10] == '1': #2DL4
        genes["g2DL4"] = fileReader("./FASTA Files/KIR2DL4_gen.fasta")
    else:
        genes["g2DL4"] = failedString
    
    if sequence[11] == '1': #3DL1
        genes["g3DL1_S1"] = fileReader("./FASTA Files/KIR3DL1_gen.fasta")
    elif sequence[12] == '0':
        genes["g3DL1_S1"] = failedString
    
    if sequence[12] == '1': #3DS1
        genes["g3DL1_S1"] = fileReader("./FASTA Files/KIR3DS1_gen.fasta")
    
    print("2DL5A")
    if sequence[13] == '1': #2DL5A
        file = open("./FASTA Files/KIR2DL5_gen.fasta")
        lines = file.readlines()
        randomLine = rand.randint(0,len(lines))
        outputString = ""

        for i, line in enumerate(lines): # Focus area for changing
            if randomLine == i:
                j = typeChecker(lines, i, "A")
                break

        line = lines[j]
        print(line)
        line = lines[j + 1]

        while (not line.startswith(">")) and j != len(lines) - 2:
            outputString += line[:len(line) - 1] #Change this to :60 - len(line) in the future
            j += 1
            line = lines[j]
        genes["g2DL5A"] = outputString
    else:
        genes["g2DL5A"] = failedString
    
    coinflip = 0
    if sequence[14] == sequence[15] and sequence[14] == '1':
        coinflip = rand.randint(1,2)

    if sequence[14] == '1' and (coinflip == 0 or coinflip == 1): #2DS3
        genes["g2DS3_5a"] = fileReader("./FASTA Files/KIR2DS3_gen.fasta")
    elif sequence[15] == '0':
        genes["g2DS3_5a"] = failedString
    
    if sequence[15] == '1' and (coinflip == 0 or coinflip == 2): #2DS5
        genes["g2DS3_5a"] = fileReader("./FASTA Files/KIR2DS5_gen.fasta")
    
    if sequence[16] == '1': #2DS1
        genes["g2DS1"] = fileReader("./FASTA Files/KIR2DS1_gen.fasta")
    else:
        genes["g2DS1"] = failedString
    
    if sequence[17] == '1': #2DS4
        genes["g2DS4"] = fileReader("./FASTA Files/KIR2DS4_gen.fasta")
    else:
        genes["g2DS4"] = failedString
    
    if sequence[18] == '1': #3DL2
        genes["g3DL2"] = fileReader("./FASTA Files/KIR3DL2_gen.fasta")
    else:
        genes["g3DL2"] = failedString

def fileReader(nameOfFile):
    file = open(nameOfFile)
    lines = file.readlines()
    random = rand.randint(0,len(lines))
    startOfString = False
    outputString = ""

    for i, line in enumerate(lines):
        if random == i:
            if line.startswith(">"):
                startOfString = True
            else:
                while not line.startswith(">"):
                    if i == len(lines) - 2:
                        i = 0
                        break
                    i += 1
                    line = lines[i]
            break
    
    print(line)
    i += 1
    line = lines[i]

    while (not line.startswith(">")) and i != len(lines) - 2:
        outputString += line[:len(line) - 1] #Change this to :60 - len(line) in the future
        i += 1
        line = lines[i]
    return outputString

def typeChecker(lines, j, character):
    rightType = False
    outputString = ""

    if lines[j][0] == ">": # Add on condition to see if it is a B or an A
        print(lines[j])
        (garbage, useful, garbage1, garbage2) = lines[j].split()
        if useful[7] == character:
            rightType = True
    else:
        while not lines[j].startswith(">"): # Add on condition to see if it is a B or an A
            if j == len(lines) - 1:
                j = 0
                break
            j += 1

        (garbage, useful, garbage1, garbage2) = lines[j].split()

        if useful[7] == character:
            rightType = True
    
    if not rightType:
        j = typeChecker(lines, j + 1, character)
    return j

def createFile(numOfIterations):
    for num in range(numOfIterations):
        fileString = "./output/output_%d.fasta" % (num + 1)
        outputFile = open(fileString, "w")
        for a in range(2):
            randInt = rand.randint(1,26)
            split = getRandHaplotype(randInt)
            print(split)
            readHaplotype(split)
            outputString = genes["g3DL3"] + genes["g2DS2"] + genes["g2DL5B"] + genes["g2DS3_5"] + genes["g2DP1"] + genes["g2DL1"] + genes["g3DP1"] + genes["g2DL4"] + genes["g3DL1_S1"] + genes["g2DL5A"] + genes["g2DS3_5a"] + genes["g2DS1"] + genes["g2DS4"] + genes["g3DL2"]
            length = len(outputString)
            i = 0
            while i < length:
                if i % 60 == 0:
                    outputString = outputString[:i] + "\n" + outputString[i:]
                    length = len(outputString)
                i += 1

            file = open("HAPLOTYPES.txt")
            for i, line in enumerate(file):
                if i == randInt:
                    header = ">" + line

            outputFile.write(header)
            outputFile.write(outputString)
            outputFile.write("\n")


if __name__ == "__main__":
    print("This script will run %d times" % int(sys.argv[1]))
    createFile(int(sys.argv[1]))