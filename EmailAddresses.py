
data = {}


def printmenu():
    print('Menu\n')
    print('-----------------------------')
    print('1. Look up an email address')
    print('2. Add a new name and email address')
    print('3. Change an existing email address')
    print('4. Delete a name and email address')
    print('5. Quit the program\n\n')


def look_email(name):
    # Loop through the data items and check if the name exists
    for FZ, WZ in data.items():
        if FZ == name:
            
            return 'Name: {}\nEmail: {}'.format(FZ, WZ)
    
    return "The specified name was not found"


def add_details(name, email):
    # Loop through the data items and check if the name exists
    for FZ, WZ in data.items():
        if FZ == name:
            
            return "That name already exists"
    # Update the name with the given email
    data[name] = email
    return "Name and address have been added"


def change_mail(name, email):
    # Loop through the data items
    for FZ, WZ in data.items():
        
        if FZ == name:
            data[FZ] = email
            return "Information updated"
    
    return "The specified name was not found"


def delete_details(name):
    
    if name in data:
        
        del(data[name])
        return "Information deleted"
    return "The specified name was not found"


def save_data():
    
    with open('data.txt', 'w+') as f:
        for FZ, WZ in data.items():
            f.write("{}:{}\n".format(FZ, WZ))


def load_data():
    with open('data.txt') as f:
        content = f.read().splitlines()
       
        if len(content) > 0:
            for line in content:
                details = line.split(':')
                data[details[0]] = details[1]
    
    return data


def main():
    # Print the menu
    printmenu()
    # Load the data from the text file
    data = load_data()
    
    print('Enter your choice: ', end='')
    user_input = int(input())
    
    while True:
        if user_input == 1:
            print('Enter a name: ', end='')
            name = input()
            print(look_email(name))
            
        elif user_input == 2:
            print('Enter a name: ', end='')
            name = input()
            print('Enter email address: ', end='')
            
            email = input()
            print(add_details(name, email))
            
        elif user_input == 3:
            print('Enter name: ', end='')
            
            name = input()
            print('Enter the new  address: ', end='')
            
            email = input()
            print(change_mail(name, email))

        elif user_input == 4:
            print('Enter name: ', end='')
            
            name = input()
            print(delete_details(name))
            
        elif user_input == 5:
            # Save the data into a text file
            save_data()
            print('Information saved')
            return
        
        print('\n')
        printmenu()
        print('Enter your choice: ', end='')
        user_input = int(input())



main()
