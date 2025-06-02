import os
import json

file="to_do.json"
def load_task():
    if not os.path.exists(file) or os.stat(file).st_size == 0:
        return []  # return empty list if file doesn't exist or is empty
    with open(file, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(file,"w") as f:
        json.dump(tasks,f,indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks")
        return
    for idx,task in enumerate(tasks,start=1):
        if task["done"]:
            status="DONE"
        else:
            status="NOT DONE"
        
        print(f"{idx}. [{status}] {task["task"]}")

def add_task(tasks):
    t=input("Enter task:")
    tasks.append({"task":t,"done":False})
    print("Task added!")

def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        idx=int(input("Enter the task number to be marked done:"))-1
        if 0<=idx<len(tasks):
            tasks[idx]["done"]=True
            print("Task marked as done!")
        else:
            print("invalid Task number")
    except ValueError:
        print("enter a number")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx=int(input("Enter the task number to be deleted:"))-1
        if 0<=idx<len(tasks):
            tasks.pop(idx)
            print("Task deleted")
        else:
            print("invalid Task number")
    except ValueError:
        print("enter a number")

def main():
    tasks=load_task()
    while True:
        print("Menu:\n")
        print("1.Add task")
        print("2.Show task")
        print("3.Mark task as done")
        print("4.Delete task")
        print("5.Save task and exit")

        ch=int(input("Enter choice:"))
        if ch==1:
            add_task(tasks)
        elif ch==2:
            show_tasks(tasks)
        elif ch==3:
            mark_task_done(tasks)
        elif ch==4:
            delete_task(tasks)
        elif ch==5:
            save_tasks(tasks)
            break
        else:
            print("Invalid choice!")
        print("\n");

if __name__=="__main__":
    main()






    
    