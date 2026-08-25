print(" Hello Everyone!....")
print("Welcome to the Patter Generator and Number")
print("Analyzer")

print("Select an option:")
print("\n1. Generate a pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

print("\nEnter your choice: 1 ")
print("Enter the number of rows for the pattern: 5 ")

print("Pattern..1")
for i in range(1,5,1):
    print(i*"*")
    

    
print("Pattern.2")
for i in range(4,0,-1):
    print(i*"*")
    
    

print("Pattern..3")
n = int(input("Enter number of n:"))

for i in range(1,n + 1):
    b = " "*(n - i)
    s = "*"  * (2*i-1)
    print(b + s)

print("Select an option:")
print("\n1. Generate a pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

choice = int(input("Enter your choice: "))

match choice:
        case 1:
            rows = int(input("Enter number of rows: "))
            for i in range(1, rows + 1):
                print("*" * i)

        case 2:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            total = 0

            for num in range(start, end + 1):
                if num % 2 == 0:
                    print("Number", num, "is Even")
                else:
                    print("Number", num, "is Odd")

                total = total + num

            print("Sum of all numbers from", start, "to", end, "is:", total)
            
            print("Select an option:")
            print("\n1. Generate a pattern")
            print("2. Analyze a Range of Numbers")
            print("3. Exit")
            
            print("Enter your choice : 3 ")
            print("Exiting the program....")
           
            print("....Goodbye....")

print("Thank you all of you!")
