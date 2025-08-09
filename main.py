from connection import add_task, view_tasks, update_task, delete_task
import os



def main():
    print("Starting the application...")
    os.system("cls")
    print("""
        Welcome to TODO List Cli developed in Python!
                    😀😀😀😀😀😀😀😀😀
        This CLI was developed by Gleizits. The source code can be found on his GitHub. Thank you for downloading it.
        Loading Tasks...
          """)
    a = input("Press Enter to continue...")
    if a == "":
        os.system("cls")

        while True:
            print("""
            TODO List Menu:
            1. Add Task
            2. View Tasks
            3. Update Task
            4. Delete Task
            5. Exit
            """)
            choice = int(input("Choose an option (1-5): "))

            if choice == 1:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                status = input("Enter task status (pending/completed): ")
                add_task(title, description, status)
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                task_id = int(input("Enter task ID to update: "))
                title = input("Enter new task title: ")
                description = input("Enter new task description: ")
                status = input("Enter new task status (pending/completed): ")
                update_task(task_id, title, description, status)
            elif choice == 4:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            elif choice == 5:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

            input("Press Enter to continue...")
            os.system("cls")

if __name__ == "__main__":
    main()
