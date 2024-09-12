# Get ordinal from cardinal



def getOrdinal(cardinal):
    # Handle the hundreds place for 11th, 12th, 13th
    if cardinal % 100 in range(11, 14):
        return (str(cardinal) + "th")
    else:
        # Handle the tens place for 0th, 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th
        match cardinal % 10:
            case 1:
                return f"{str(cardinal)}st"
            case 2:
                return f"{str(cardinal)}nd"
            case 3:
                return f"{str(cardinal)}rd"
            case _:
                return f"{str(cardinal)}th"


# Get the range for the for loop 
input = input("Range? (num num)\n").split(" ")

for i in range(int(input[0]), int(input[1])):
    print(getOrdinal(i))