## wednesday's class (16/09/26) TOPIC - dictionary/while loop/functions


products = {'Sk-01': 'Bottle Water',
            'Sk-02': 'Yoghurt',
            'Sk-03': 'Meat pie',
            'Sk-04': 'Cake',
            'Sk-05': 'Sausage Roll'}

purchase = input("Item ID: ")
for keys, values in products.items():
    if purchase == keys:
        print(values)
    else:
        print("Update the inventory list.")
        break

# A while loop will run indefinitely for as long as the conditions are met

''' operation = "Y"
print("A simple calculator!")
while operation.lower() != 'stop':
    print("Operations:\n\tsum\n\tmin\n\tmul\n\tdiv\n\tstop")
    operation = input("Operation: ")
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))
    if operation.lower() == 'sum':
        print(a + b)
    elif operation.lower() == 'min':
        print(a - b)
    elif operation.lower() == 'mul':
        print(a * b)
    elif operation.lower() == 'div':
        print(a / b)
    else:
        print("Enter a valid operation.")

print(num) '''

details = {"Ghost rider": "12345aprilf00",
           "JoggerBoi": "jeeeeery678",
           "Emmanuel123456": "st@rlink"}
tries = 6

while tries > 0:
    tries -= 1
    User = input("Username: ")
    Pwd = input("Password: ")
    for keys, values in details.items():
        if User in keys and Pwd in values:
            print(f"Welcome {User}")
            tries = 0
            break
        else:
            print("Wrong details")
            print(f"You have {tries} attempts left")


# functions
def greeting():
    """a standard message"""
    print("Hello World!")

greeting()

def add(a=0, b=0):
    """adding all the given values"""
    print(a + b)

add()
friends = []

def af(a):
    """add name to list"""
    friends.append(a)

def send_regards():
    """send message to names on list"""
    for friend in friends:
        print(f"Good afternoon {friend}!")


af("Jonathan")
af("Francis")
af("Chisom")
af("Samson")
af("Christabel")
send_regards()


'''users = {'user1' : 'Daniel', 'user2' : 'John'}
print(users['user1'])'''


### monday's class (21/09/26). TOPIC - functions/positional arguments/keyword arguments

def greet_user(username):
    """Greet user with a message"""
    print(f"Hello {username.title()}!")
greet_user('i_human')

def get_full_name(first_name,last_name,middle_name=''):
    '''return a full name'''
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


user1 = get_full_name('I.','Person')#positional argument
user2 = get_full_name(first_name='John',last_name='Cena')#keyword argument
user3 = get_full_name('G.','D.','Roger')

print(user1)
print(user2)
print(user3)

def cake(flavour,message):
    ''''a function that prints a message about the cake you bought'''
    print(f"I bought a {flavour.lower()} cake that has {message}.")
cake('starwberry' ,'happy birthday message written on it')



def phoneModel(brand,model,year,special=''):
    '''a funtion that saves information about a phone to a dictionary'''
    phone = {'Brand':brand,'Model':model,'Special Edition':special,'Year':year}
    return phone
phone1 = phoneModel('Apple','iPhone 13',2019,'Pro Max')
phone2 = phoneModel('Samsung','Galaxy S24',2024)
print(phone1)
print(phone2)


names = ["Emmanuel",'Rachel','Daniel','Victor','Chigozirim']
def greet_people(people):
    '''greet everyone on list'''
    for person in names:
        msg = f"Good day {person}!"
        print(msg)

#ose
greet_people(names)

def get_full_name(first_name,last_name):
    '''return a full name'''
    full_name = f"{first_name.title()} {last_name.title()}"
    print(f"Your full name is {full_name} right?")
#stop

def animalsNearMe(*animal):
    '''collects info on animals around you'''
    return animal
observation1 = animalsNearMe('dog')
observation2 = animalsNearMe('dog','cricket')

print(observation1)
print(observation2)