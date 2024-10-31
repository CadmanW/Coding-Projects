# Program Name: ASCII Squares
# Name: Cadman Warren
# Date Modified: 10/31/2024

def main():
    # Get input
    twoByN = int(input("What is 'n' value for 2byN?: "))
    fourByN = int(input("What is 'n' value for 4byN?: "))
    m = int(input("What is 'm' value for MbyN?: "))
    n = int(input("What is 'n' value for MbyN?: "))

    # Display squares based on input
    displaySqaures(2, twoByN)    
    displaySqaures(4, fourByN)
    displaySqaures(m, n)    

# Function for displaying squares
def displaySqaures(m, n):
    for _ in range(n):
        print("+" + " - - - - +" * m)

        for _ in range(4):
            print("|" + "         |" * m)

    print("+" + " - - - - +" * m)
    



# Call main
if __name__ == "__main__":
    main()