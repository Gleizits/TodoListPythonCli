import sqlite3 as sql
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db", "TODO_CliPy.db")
conn = None

try:
    
    # Crea la base de datos y la tabla si no existen
    with sql.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT CHECK(status IN ('pending', 'completed')) DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")
    
    conn.commit()
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

if __name__ == "__main__":
    # cerrar la conexión si se ejecuta directamente
    if conn:
        conn.close()
        print("Open main.py please.")