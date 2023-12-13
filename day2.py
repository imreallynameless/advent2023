f = open("day2.txt", "r")
sum = 0
total = 0
array = []
for line in f:
    line = line.strip()
    # get the id 
    line = line.split(":")
    id = line[0]
    id = id.split(" ")
    # split line by game
    # print (id)
    toadd = id[1]
    toAddInt = int(toadd)
    # print (line[1])
    games = line[1].split(";")
    # print (games)
    for game in games:
        game = game.split (",")
        for score in game:
            score = score.split(" ")
            # print (score)
            check = score[1]
            checkint = int(check)
            colour = score[2]
            if colour == "red":
                if checkint > 12:
                    if (toAddInt not in array):
                        array.append(toAddInt)
                        sum += toAddInt
                    # print(game)
                    # print(id)
                    break
            elif colour == "green":
                if checkint > 13:
                    if (toAddInt not in array):
                        array.append(toAddInt)
                        sum += toAddInt
                    # print(game)
                    # print(id)                    
                    break
            elif colour == "blue":
                if checkint > 14:
                    if (toAddInt not  in array):
                        sum += toAddInt
                        array.append(toAddInt)
                    # print(game)
                    # print(id)
                    break

        # cubes = score[0]
        # if score[1] == "red" and cubes > red:
        #     sum += id
        # elif score[1] == "green" and cubes > green:
        #     sum += id
        # elif score[1] == "blue" and cubes > blue:
        #     sum += id
print(sum)
        

    
