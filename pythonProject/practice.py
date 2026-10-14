numbers = []
num2=[]

for i in range(1,51):
    # a loop that adds numbers from 1 to 50 to the list named numbers
    print(i)
    numbers.append(i)
print(f"The total number of items in the numbers list is:\n\t{len(numbers)}")
print(f"The smallest number in the list numbers is: \n\t{min(numbers)}")
print(f"The largest number in the list numbers is: \n\t{max(numbers)}")
print(f"The total sum of numbers in the list numbers is: \n\t{sum(numbers)}")
for i in range(20):
    num2.append(i)
numbers = []
num2=[]

for i in range(1,1_000_001):
    # a loop that adds numbers from 1 to 50 to the list named numbers
    #print(i)
    numbers.append(i)
print(f"The total number of items in the numbers list is:\n\t{len(numbers)}")
print(f"The smallest number in the list numbers is: \n\t{min(numbers)}")
print(f"The largest number in the list numbers is: \n\t{max(numbers)}")
print(f"The total sum of numbers in the list numbers is: \n\t{sum(numbers)}")
for i in range(20):
    num2.append(i)

first500 = numbers[2:50:3]
print(min(first500))
print(max(first500))
print(first500)

names = ["John","Bull","My","Son"]
real_name = names[:2]
names.append("I sent you")
real_name.append("is a name")
print(names)
print(real_name)

passwords = ('123456monkeys','10gr33nbottles','twol1ttledicky')

cars = ['porsche','mercedes',"ferrari",'volvo','jeep','toyota']


if 'porsche' in cars:
    print("My favourite car is a Porsche 911")
else:
    print("I'll find a good one one day.")

username = "GoldenL10n"
password = "Tr3@sure123"

user = input("Username: ")
if user == username:
    for i in range(3):
        pwd = input("Password: ")
        if pwd == password:
            print(f"Welcome {username}!")
            break# to end the loop ahead of time
        else:
            print("wrong password")
else:
    print("Goodbye!")

friends = ['Victory', 'Chiamaka', 'Kamsi', 'Emmanuel', 'Goodluck']

girls = friends[:2]  # a slice is one of the ways you can make a copy of the list
print(girls)
boys = friends[2:]
print(boys)

print(friends)

for i in range(5):
    person = friends[i]
    if person in girls:
        print(f"Good morning {person}~, how are you doing today?")
    elif person in boys:
        print(f"Good morning {person}, how has life been treating you?")
    else:
        print("It was nice to meet you")

# a tuple is a list that cannot be modified

restaurant = ['genesis', 'sammies', 'chicken republic', 'dominoes', 'mr biggs']
if 'genesis' in restaurant:
    print(f"I saw some nice cakes at Genesis yesterday")
elif 'sammies' in restaurant:
    print(f"I saw my friend at Sammies last night")
elif 'chicken republic' in restaurant:
    print(f"I saw my friend at Chicken Republic last night")
elif 'dominoes' in restaurant:
    print(f"I saw my friend at Dominoes last week")
elif 'mr biggs' in restaurant:
    print(f"I saw my friend at Mr. Biggs last night")
else:
    print("I couldn't guess which one.")

username = "Ghost Rider"
password = "_@55h013_"
print("Log in")
for i in range(5):
    User = input("\tUsername: ")
    if User == username:
        Pwd = input("\tPassword: ")
        if Pwd == password:
            print("Welcome back!")
            break
        else:
            print("Wrong password!")
    else:
        print("Wrong Username!")

# creating a list with even numbers
even_num = []
for i in range(2, 30, 2):
    even_num.append(i)
print(even_num)