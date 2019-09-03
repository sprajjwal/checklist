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
    item = checklist[index]['item']
    print(item)

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
    print('\n')

# MARK COMPLETION
def mark_completed(index):
    checklist[index]['completed'] = True
    

# USER INPUT
def user_input(prompt):
    return input(prompt)

# SELECT
def select(function_code):
    if function_code == "A":
        status = True
        while status:
            status = create(input("Add to list: "))
    elif function_code == "R":
        read(input("Item to read: "))
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
        '''\nPress A to add to list
R to read from list
P to display list
D to delete 
Q to quit: ''')
    running = select(selection.upper())