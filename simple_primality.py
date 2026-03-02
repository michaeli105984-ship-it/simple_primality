"""
Filename: simple_primality.py
Author: <Fontaine, Michael>
Created: <3/2/2026>
Instructor: Holtslander
"""
def prime():
    print("Enter a non-negative whole number greater than 1 on the line below.")
    
    user_input = input()
    number = int(user_input)
    
    if number < 2:
        print(number, "is NOT a prime number.")
        return
    
    for i in range(2, number):
        if number % i == 0:
            print(number, "is NOT a prime number.")
            return
    
    print(number, "is a prime number.")
# You should not need to change any code below this point
def main():
    print("This program will determine the primality of a number.")
    running = "y"
    while running == "y":
        prime()
        running = input("Check another number? (y/N)\n").lower()
    print("Thank you for using this primality program!")

if __name__ == "__main__":

    main()

