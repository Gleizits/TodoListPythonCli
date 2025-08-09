import sqlite3 as sql
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db", "TODO_CliPy.db")
conn = None

try:
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    conn.commit()
    
    # crear tareas
    def add_task(title, description, status):
        # insertar los datos en la tabla
        cursor.execute(f"INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)", (title, description, status))
        # guardar los cambios
        conn.commit()


    # visualizar tareas
    def view_tasks():
        # seleccionar todas las tareas
        view = cursor.execute("SELECT * FROM tasks")
        
        # mostrar las tareas
        for todos in view:
            print(todos)

    # actualizar tareas
    def update_task(task_id, title, description, status):
        # actualizar la tarea
        cursor.execute(f"UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?", (title, description, status, task_id))
        # guardar los cambios
        conn.commit()
    
    # eliminar tareas
    def delete_task(task_id):
        # eliminar la tarea
        cursor.execute(f"DELETE FROM tasks WHERE id = ?", (task_id,))
        # guardar los cambios
        conn.commit()

except sql.Error as e:
    # mostrar el errorm si ocurre
    print(f"An error occurred: {e}")