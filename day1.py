
f = open("day1.txt", "r")
sum = 0
toAdd = ""
last = ""
first = True
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
for line in f:
    line = line.strip()
    for i in range(len(line)):
        if line[i].isalpha():
            for j in range(len(digits)):
                if digits[j] in line[i:i+len(digits[j])]:
                    if first:
                        toAdd += str(j+1)
                        last = str(j+1)
                        first = False
                    else:
                        last = str(j+1)
            # if "one" in line[i:i+3]:
            #     if first:
            #         toAdd += "1"
            #         last = "1"
            #         first = False
            #     else:
            #         last = "1"
            # if "two" in line[i:i+3]:
            #     if first:
            #         toAdd += "2"
            #         last = "2"
            #         first = False
            #     else:
            #         last = "2"
            # if "three" in line[i:i+5]:
            #     if first:
            #         toAdd += "3"
            #         last = "3"
            #         first = False
            #     else:
            #         last = "3"
            # if "four" in line[i:i+4]:
            #     if first:
            #         toAdd += "4"
            #         last = "4"
            #         first = False
            #     else:
            #         last = "4"
            # if "five" in line[i:i+4]:
            #     if first:
            #         toAdd += "5"
            #         last = "5"
            #         first = False
            #     else:
            #         last = "5"
            # if "six" in line[i:i+3]:
            #     if first:
            #         toAdd += "6"
            #         last = "6"
            #         first = False
            #     else:
            #         last = "6"
            # if "seven" in line[i:i+5]:
            #     if first:
            #         toAdd += "7"
            #         last = "7"
            #         first = False
            #     else:
            #         last = "7"
            # if "eight" in line[i:i+5]:
            #     if first:
            #         toAdd += "8"
            #         last = "8"
            #         first = False
            #     else:
            #         last = "8"
            # if "nine" in line[i:i+4]:
            #     if first:
            #         toAdd += "9"
            #         last = "9"
            #         first = False
            #     else:
            #         last = "9"
            # if "zero" in line[i:i+4]:
            #     if first:
            #         toAdd += "0"
            #         last = "0"
            #         first = False
            #     else:
            #         last = "0"
        if line[i].isdigit():
            if first:
                toAdd += line[i]
                last = line[i]
                first = False
            else:
                last = line[i]
    toAdd += last
    sum += int(toAdd)
    toAdd = ""
    first = True
print(sum)
f.close()