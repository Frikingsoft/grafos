def agregar_grafo():
    grafo = {}
    num_nodos = int(input("¿Cuántos nodos tiene el grafo? "))
    grafo['nodos'] = []
    
    for i in range(num_nodos):
        nodo = input(f"Introduce el nombre del nodo {i+1}: ")
        grafo['nodos'].append(nodo)
    
    num_aristas = int(input("¿Cuántas aristas tiene el grafo? "))
    grafo['aristas'] = []
    
    for i in range(num_aristas):
        nodo1 = input(f"Introduce el nodo de origen de la arista {i+1}: ")
        nodo2 = input(f"Introduce el nodo de destino de la arista {i+1}: ")
        grafo['aristas'].append((nodo1, nodo2))
    
    return grafo

def main():
    num_grafos = int(input("¿Cuántos grafos deseas agregar? "))
    lista_grafos = []
    
    for i in range(num_grafos):
        print(f"\nAgregando grafo {i+1}:")
        grafo = agregar_grafo()
        lista_grafos.append(grafo)
    
    print("\nLista de grafos agregados:")
    for i, grafo in enumerate(lista_grafos):
        print(f"\nGrafo {i+1}:")
        print("Nodos:", grafo['nodos'])
        print("Aristas:", grafo['aristas'])

agregar_grafo()