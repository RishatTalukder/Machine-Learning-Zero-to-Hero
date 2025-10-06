import os
import sqlite3

DB_NAME = "todo.db"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_connection():
    return sqlite3.connect(DB_NAME)

def setup_database():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_task(description):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        conn.commit()

def list_tasks():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT id, description FROM tasks")
        return c.fetchall()

def delete_task(task_id):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

def edit_task(task_id, new_description):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_description, task_id))
        conn.commit()

def show_menu():
    print("=== TO-DO APP (SQLite) ===")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Delete a task")
    print("4. Edit a task")
    print("5. Exit")
    print("=============================")

def show_tasks():
    tasks = list_tasks()
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour tasks:")
        for task in tasks:
            print(f"{task[0]}. {task[1]}")
    print()

# ------------------ Main App ------------------

def main():
    setup_database()

    while True:
        clear_screen()
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            clear_screen()
            task = input("Enter new task: ").strip()
            if task:
                add_task(task)
                print("✅ Task added!")
            else:
                print("⚠️ Task cannot be empty.")
            input("\nPress Enter to continue...")

        elif choice == "2":
            clear_screen()
            show_tasks()
            input("Press Enter to continue...")

        elif choice == "3":
            clear_screen()
            show_tasks()
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                delete_task(task_id)
                print("✅ Task deleted!")
            except ValueError:
                print("⚠️  Please enter a valid ID.")
            input("\nPress Enter to continue...")

        elif choice == "4":
            clear_screen()
            show_tasks()
            try:
                task_id = int(input("Enter task ID to edit: ").strip())
                new_desc = input("Enter new description: ").strip()
                if new_desc:
                    edit_task(task_id, new_desc)
                    print("✏️  Task updated!")
                else:
                    print("⚠️  Task cannot be empty.")
            except ValueError:
                print("⚠️  Please enter a valid ID.")
            input("\nPress Enter to continue...")

        elif choice == "5":
            clear_screen()
            print("Exiting To-Do App")
            break

        else:
            print("Invalid choice. Please select 1–5.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
