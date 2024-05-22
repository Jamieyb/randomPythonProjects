# Contact Management Program

# Functions
def inside_menu():
    global Main
    print('9. Back')
    print("0. Exit")
    menu1 = input("Choose menu : ")
    print(" ")
    if menu1 == '9':
        Main='menu'
    elif menu1 == '0':
        Main=0
    else:
        print("Input is invalid")
        Main=0

def contact_list(contacts):
    for i in contacts:
        print(f'\nName   : {i["name"]}')
        print(f'Email  : {i["mail"]}')
        print(f'Number : {i["num"]}\n')
        print("="*5)

def add_contact():
    name = input('Name : ')
    mail = input('Email : ')
    num = input('Number : ')
    new_contact = {
        "name" : name,
        "mail" : mail,
        "num" : num
    }
    contacts.append(new_contact)
    print('\n')
    print('='*20)
    print('Contact successfully added')
    print("Name = "+name)
    print("Name = "+mail)
    print("Name = "+num)
    print('\n')

def del_contact():
    Name = input('Input contact name : ')
    index = -1
    for i in range(0,len(contacts)):
        if Name == contacts[i]['name']:
            index = i
    if index == -1:
        print('Contact is unavailable')
    else:
        del contacts[i]
        print('Contact successfully deleted\n')

def find_contact():
    find = input("Input contact information : ")
    print("="*10)
    print(f'Contacts with \'{find}\'')
    for i in contacts:
        if i['name'].lower().find(find) != -1:
            print(f'\nName   : {i["name"]}')
            print(f'Email  : {i["mail"]}')
            print(f'Number : {i["num"]}\n')
            print("="*5)



# List of contact dictionaries
contacts = [{
    "name" : "Jimi",
    "mail" : "Jimi@gmail.com",
    "num" : "08666"
}]

# Menu program
Main ='menu'
while Main != 0:
    print("\n# Menu")
    print("1. Contact list")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Find")
    print("0. Exit")

    menu = input("Choose menu : ")
    print(" ")

    if menu == '0':
        Main=0
    elif menu == '1':
        print("="*5+'CONTACT LIST'+"="*5)
        contact_list(contacts)
        # INSIDE MENU NAVIGATION
        inside_menu()
    elif menu == '2':
        print("Input contact information")
        add_contact()
        # INSIDE MENU NAVIGATION
        inside_menu()
    elif menu == '3':
        del_contact()
        # INSIDE MENU NAVIGATION
        inside_menu()
    elif menu == '4':
        find_contact()
        # INSIDE MENU NAVIGATION
        inside_menu()