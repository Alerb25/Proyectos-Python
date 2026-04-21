#para este proyecto el usuario introduce un listado de tareas y el programa los pasa a un txt
# hacer un menu en el cual se elijan el numero total de tareas, y que se digan el nombre y el estado
#luego que el programa los pase a un txt

class Chore: 
    def __init__(self, title, status):
        self.title = title
        self.status = status

    def __str__(self):
        # Esto define cómo se verá la tarea cuando la guardemos o imprimamos
        return f"Título: {self.title} | Estado: {self.status}"


lista_tareas = []
total = int(input("Introduzca el número de tareas que tiene: "))

# Recogida de datos
for i in range(total):
    print(f"\nTarea {i+1}:")
    titulo = input("Introduzca el título: ")
    estado = input("Introduzca el estado: ")
    
    # Creamos el objeto y lo guardamos en la lista
    nueva_tarea = Chore(titulo, estado)
    lista_tareas.append(nueva_tarea)

#Guardar en el archivo TXT
with open("mis_tareas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("--- LISTADO DE TAREAS ---\n")
    for t in lista_tareas:
        archivo.write(str(t) + "\n") # Usamos el método __str__ de la clase

print("\n¡Hecho! Las tareas se han guardado en 'mis_tareas.txt'.")