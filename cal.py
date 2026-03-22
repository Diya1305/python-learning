print("A simple Calculator")

num1=float(input("Enter a number: "))
num2=float(input("Enter another number:  "))

print("""Choose a number: 
      1: Add
      2: Subtract
      3: multiply
      4: divide
      """)

choice =input("1/2/3/4")

if choice=="1":
    print(num1+num2)
