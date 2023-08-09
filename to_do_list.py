#create a list to hold to-do tasks

to_do_list = []
finished = False
while not finished:
    task = input("Enter a task for your to-do list.  Press <enter> when done. ")

    if len(task) == 0:
        finished = True
    else:
        to_do_list.append(task)
        print("task added.")