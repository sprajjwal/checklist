checklist = list()

# CREATE
def create(item):
    checklist.append('Blue')

# READ
def read(index):
    item = checklist[index]
    return item

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# TEST
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    #print(read(1))

test()