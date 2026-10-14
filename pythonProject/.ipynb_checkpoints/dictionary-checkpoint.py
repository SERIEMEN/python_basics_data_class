'''users = {'user1' : 'Daniel', 'user2' : 'John'}
print(users['user1'])

users

stuffs = {'sk-01' : 'Water', 'sk-02' : 'Yogurt', 'sk-03' : 'Meat pie'}
for i in range(3):
    purchase = input("Item_ID: ")
    if purchase in stuffs.keys():
        print(stuffs.values())


    purchase = input("Item_ID: ")
    for keys, values in stuffs.items():
        if purchase == keys:
            print(values)
        else:
            print('Update the inventory list')
            break'''



''' def greet_user(user):
   # user = 'henry'
    print(f'Hello {user}')
greet_user('henry')

def greet_user(username):
    """Greet user with a message"""
    print(f"Hello {username.title()}!")
greet_user('i_human')

def get_full_name(first_name,last_name):
    return a full name
    full_name = f"{first_name.title()} {last_name.title()}"
    print(f"Your full name is {full_name} right?")

get_full_name('I.','Person') '''


def cake(flavour,message):
    """Greet user with a message"""
    print(f"I bought a {flavour.lower()} cake that has {message}.")

cake('starwberry' ,'happy birthday message written on it')


'''def get_cake(first_name,last_name):
    return a full name
    full_name = f"{first_name.title()} {last_name.title()}"
    print(f"Your full name is {full_name} right?")
get_full_name('I.','Person')'''

'''def phoneModel(brand,model,year,special=''):
    a funtion that saves information about a phone to a dictionary
    phone = {'Brand':brand,'Model':model,'Special Edition':special,'Year':year}
    return phone
phone1 = phoneModel('Apple','iPhone 13',2019,'Pro Max')
phone2 = phoneModel('Samsung','Galaxy S24',2024)
print(phone1)
print(phone2)

randos = ['Cyril', 'Emma', 'John', 'Daniel', 'Cole', 'Theophlius']
def greet_people():
    print() '''

arise = ["Emmanuel",'Rachel','Daniel','Victor','Chigozirim']
def greet_people(people):
  for person in people:
      msg = f"Good day {person}!"
      print(msg)

greet_people(arise)

def get_full_name(first_name,last_name):
    '''return a full name'''
    full_name = f"{first_name.title()} {last_name.title()}"
    print(f"Your full name is {full_name} right?")

def animalsNearMe(*animal):
    '''collects info on animals around you'''
    return animal
observation1 = animalsNearMe('dog')
observation2 = animalsNearMe('dog','cricket')

print(observation1)
print(observation2)