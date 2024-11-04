# Program Name: ASCII Squares
# Name: Cadman Warren
# Date Modified: 10/31/24

def main():
    # Get inuput
    twoByN = int(input("What is 'n' value for 2byN?: "))
    fourByN = int(input("What is 'n' value for 4byN?: "))
    m = int(input("What is 'm' value for MbyN?: "))
    n = int(input("What is 'n' value for MbyN?: "))  

    # Draw squares based on input
    displayTwoByN(twoByN)
    displayFourByN(fourByN)
    displayMByN(m, n)


# Call display squares per what the project requests
def displayTwoByN(n):
    displaySquares(2, n)    

def displayFourByN(n):
    displaySquares(4, n)    

def displayMByN(m, n):
    displaySquares(m, n)

# Draw squares in an (m, n) grid
def displaySquares(m, n):
    for _ in range(n):
        print("+" + " - - - - +" * m)

        for _ in range(4):
            print("|" + "         |" * m)

    print("+" + " - - - - +" * m)
    



# Call main
if __name__ == "__main__":
    main()