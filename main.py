from collections import deque

def agregar_grafo():
    grafo = {}
    num_nodos = int(input("¿Cuántos nodos tiene el grafo? "))
    grafo['nodos'] = []
    grafo['adyacencias'] = {}
    
    for i in range(num_nodos):
        nodo = input(f"Introduce el nombre del nodo {i+1}: ")
        grafo['nodos'].append(nodo)
        grafo['adyacencias'][nodo] = []  # Inicializar la lista de adyacencias para cada nodo
    
    num_aristas = int(input("¿Cuántas aristas tiene el grafo? "))
    
    for i in range(num_aristas):
        nodo1 = input(f"Introduce el nodo de origen de la arista {i+1}: ")
        nodo2 = input(f"Introduce el nodo de destino de la arista {i+1}: ")
        # Agregar las conexiones bidireccionales (suponiendo que el grafo es no dirigido)
        grafo['adyacencias'][nodo1].append(nodo2)
        grafo['adyacencias'][nodo2].append(nodo1)
    
    return grafo

def bfs(grafo, inicio, fin):
    # Usamos un BFS para encontrar la distancia más corta en un grafo no ponderado
    visitados = {nodo: False for nodo in grafo['nodos']}
    distancias = {nodo: float('inf') for nodo in grafo['nodos']}
    
    # Cola para el BFS
    cola = deque([inicio])
    visitados[inicio] = True
    distancias[inicio] = 0
    
    while cola:
        nodo_actual = cola.popleft()
        
        # Si llegamos al nodo final, devolvemos la distancia
        if nodo_actual == fin:
            return distancias[nodo_actual]
        
        # Recorremos los nodos vecinos (adyacentes)
        for vecino in grafo['adyacencias'][nodo_actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                distancias[vecino] = distancias[nodo_actual] + 1
                cola.append(vecino)
    
    # Si no se encuentra el camino, devolvemos None
    return None

def main():
    # Agregar un solo grafo
    grafo = agregar_grafo()
    
    print("\nGrafo agregado:")
    print("Nodos:", grafo['nodos'])
    print("Adyacencias:", grafo['adyacencias'])
    
    # Preguntar por el nodo de inicio y el nodo final
    inicio = input("Introduce el nodo de inicio: ")
    fin = input("Introduce el nodo de destino: ")
    
    # Calcular la distancia más corta usando BFS
    distancia = bfs(grafo, inicio, fin)
    
    if distancia is not None:
        print(f"La distancia más corta entre {inicio} y {fin} es {distancia}")
    else:
        print(f"No hay camino entre {inicio} y {fin}")

if __name__ == "__main__":
    main()
