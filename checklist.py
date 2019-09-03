checklist = list()

# [{'color': 'blue', 'completed': False}, {'color': 'red', 'completed': False}]

# CREATE
def create(item):
    if item.split(' ', 1)[0].lower() in checklist:
        return True
    else: 
        checklist.append({'color': item.split(' ', 1)[0].lower(), 
        'item': item, 'completed': True})
        return False

# READ
def read(index):
    print(checklist[index]['item'])
    

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
            status = create(input("Add to list: "))
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
    if checklist[index]:
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
while running:
    selection = user_input(
        '''\nEnter
A to add to list
R to read from list
P to display list
D to delete 
Q to quit
-> ''')
    running = select(selection.upper())