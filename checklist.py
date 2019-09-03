checklist = list()
# [{'color': 'blue', 'completed': False}, {'color': 'red', 'completed': False}]

rainbow = "violet indigo blue green yellow orange red"
# CREATE
def create(item):
    if check_color(item.split(' ', 1)[0].lower()):
        print("This color has already been worn! Wear a different color")
        return True
    elif item.split(' ', 1)[0].lower() in rainbow: 
        checklist.append({'color': item.split(' ', 1)[0].lower(), 
        'item': item, 'completed': True})
        return False
    elif item in 'q Q':
        return False
    else:
        print("This color doesn't belong in rainbow! Choose a different color!")
        return True

# Helper function to check if color exists:
def check_color(color):
    for items in checklist:
        if color == items['color']:
            return True
    return False
    
# READ
def read(index):
    print("Input " + str(index) +
    " is " + checklist[index]['item'])
    

# UPDATE
def update(index, item):
    checklist[index]['item'] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# LIST ALL ITEMS
def list_all_items():
    index = 0
    print("\n")
    for items in checklist:
        print(str(index) + " " + items['item'])
        index += 1

# MARK COMPLETION
def mark_completed(index):
    checklist[index]['completed'] = True

# UNCHECK COMPLETION
def uncheck_completed(index):
    checklist[index]['completed'] = False 

# USER INPUT
def user_input(prompt):
    return input(prompt)

# SELECT
def select(function_code):
    status = True
    if function_code == "A":
        while status:
            status = create(input("Add to list or Q to Quit: "))
    elif function_code == "R":
        user_input = int(input("Item to read: "))
        if check_index(user_input):
            read(user_input)
        else: 
            print("Invalid index!")
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False
    elif function_code == "D":
        list_all_items()
        destroy(int(input("Enter index to delete: ")))
    else:
        # Error catching
        print("Unknown option")
    return True

# Helper function to check index
def check_index(index):
    if index < len(checklist):
        return True
    else:
        return False

# Function to check if rainbow is complete
def check_rainbow():
    count = 0
    for color in checklist:
        if color['color'] in rainbow:
            count += 1
    if count == 7:
        return True
    else: 
        return False

# # TEST
# def test():
#     create("purple sox")
#     create("red cloak")

#     print(read(0))
#     print(read(1))

#     update(0, "purple socks")
#     destroy(1)

#     print(read(0))
#     #print(read(1))

# test()

running = True
rainbow_print = False
while running:
    selection = user_input(
        '''\nEnter:
A to add to list 
R to read from list
P to display list
D to delete 
Q to quit
-> ''')
    running = select(selection.upper())
    if check_rainbow() == True and rainbow_print == False: 
        print("Rainbow completed! Good job!")
        rainbow_print = True
    elif check_rainbow() == False:
        rainbow_print = False