shoping_list = []
def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items
Enter 'SHOW' to stop adding items
Enter 'HELP' to stop adding items
""")

show_help()
def show_list():
    print("Here's your list:")
    for item in shoping_list:
        #print out the list
        print(item)
        
def show_add_list(newlist):
    shoping_list.append(newlist)
    print("this item {} is ur {} number bying".format(newlist, len(shoping_list)))



while True:
    newlist = input(">> ")
    

    if newlist == "DONE":
        
        break
    elif newlist == "HELP":
        show_help()
        continue
    elif newlist == "SHOW" :
        show_list()
        continue 
    elif newlist == "COUNT":
    
        print(len(shoping_list))
        continue
    show_add_list(newlist)

show_list()