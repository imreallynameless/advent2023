f = open("day2.txt", "r")
total = 0
for line in f:
    product = 1
    dict = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    line = line.strip()
    # get the id 
    line = line.split(":")
    id = line[0]
    id = id.split(" ")
    # split line by game
    # print (id)
    # print (line[1])
    games = line[1].split(";")
    # print (games)
    for game in games:
        game = game.split (",")
        for score in game:
            score = score.split(" ")
            check = score[1]
            checkint = int(check)
            colour = score[2]
            if colour == "red":
                if checkint > dict["red"]:
                    dict["red"] = checkint
            elif colour == "green":
                if checkint > dict["green"]:
                    dict["green"] = checkint
            elif colour == "blue":
                if checkint > dict["blue"]:
                    dict["blue"] = checkint
    for key in dict:
        product *= dict[key]
    total += product
print(total)

    