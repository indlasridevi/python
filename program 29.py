class simpleGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = set()
    def insert_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()
            print(f"Node {node} inserted.")
        else:
            print(f"Node {node} already exists.")
        def insert_edge(self, node1, node2):
            if node1 in self.nodes and node2 in self.nodes:
                edge =(node1, node2) if node1<node2 else(node,node1)
                if edge not in self.edges:
                    self.edges.add(edge)
                    self.nodes[node1].add(node2)
                    self.nodes[node2].add(node1)
                    print(f"Edge ({node1},{node2}) inserted.")
                else:
                    print(f"Edge({node1}, {node2}) already exists. ")
            else:
                print("One or both nodes do not exist.")
        def display_graph(self):
            print("Nodes:", list(self.nodes.keys()))
            print("Edges;:", list(self.edges))
my_graph = simpleGraph()
while True:
    print("\nGraph Operations:")
    print("1. Insert Node")
    print("2. Insert Edge")
    print("3. Display Graph")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        node = input("Enter the node: ")
        my_graph.insert_node(node)
    elif choice == 2:
        node1 = input("Enter the first node: ")
        node2 = input("Enter the secondnode: ")
        my_graph.insert_edge(node1, node)
    elif choice == 3:
        my_graph.display_graph()
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")