def append_task(tasks,task, limit_date, priority):
    new_task = {"Tarea" : task, "Fecha_Limite" : limit_date, "Prioridad" : priority}
    tasks.append(new_task)

def show_task(tasks):
    if not tasks:
        print("No hay tareas")
    else:
        for i, task in enumerate(tasks,1):
            print(f"\nTarea {i}:")
            for clave, value in task.items():
                print(f"{clave} : {value}")

if __name__ == "__main__":
    task_list = []
    while True:
        print("\n1. Agregar Tarea")
        print("2. Mostrar Tarea")
        print("3. Salir")
        
        choice = input("Seleccione opcion: ")
        
        if choice == "1":
            new2_task = input("Ingrese la descripcion de la tarea:")
            new_limit_task = input("Ingrese fecha limite:")
            new_priority = input("Ingrese prioridad:")
            append_task(task_list,new2_task,new_limit_task,new_priority)
            
        elif choice == "2":
            show_task(task_list)
            
        elif choice == "3":
            break
    
        else:
            print("Opcion no valida, intente nuevamente")