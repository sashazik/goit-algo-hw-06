import networkx as nx
import matplotlib.pyplot as plt

# --- ЗАВДАННЯ 1: Створення графа ---

G = nx.Graph()

# Розширений список ребер
edges = [
    ("Центр", "Північ", 5),
    ("Центр", "Схід", 8),
    ("Центр", "Захід", 6),
    ("Північ", "Вокзал", 3),
    ("Північ", "Промзона", 7),
    ("Схід", "Промзона", 4),
    ("Схід", "Аеропорт", 10),
    ("Захід", "Парк", 4),
    ("Захід", "Вокзал", 5),
    ("Вокзал", "Університет", 2),
    ("Парк", "Університет", 3),
    ("Промзона", "Аеропорт", 6),
    ("Парк", "Центр", 7),
    ("Північ", "Захід", 4),
    ("Схід", "Вокзал", 12),
    ("Аеропорт", "Університет", 20),
    ("Промзона", "Центр", 9)
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Візуалізація (за бажанням можна закоментувати, щоб не вискакувало вікно)
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=2500, node_color="lightgreen", 
        font_size=10, font_weight="bold", edge_color="gray", width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа міста")
plt.show()

# --- ЗАВДАННЯ 2: DFS і BFS (ВИПРАВЛЕНО) ---

start_node = "Аеропорт"
end_node = "Університет"

print(f"\n--- Порівняння шляхів ({start_node} -> {end_node}) ---")

# 1. DFS (Пошук у глибину)
# Логіка: будуємо дерево DFS і шукаємо шлях у ньому
try:
    dfs_tree = nx.dfs_tree(G, source=start_node)
    dfs_path = nx.shortest_path(dfs_tree, source=start_node, target=end_node)
    print(f"DFS (глибина): {dfs_path}")
except Exception as e:
    print(f"DFS не знайшов шлях: {e}")

# 2. BFS (Пошук у ширину)
# Логіка: shortest_path у незваженому графі працює як BFS
try:
    bfs_path = nx.shortest_path(G, source=start_node, target=end_node)
    print(f"BFS (ширина):  {bfs_path}")
except nx.NetworkXNoPath:
    print("BFS не знайшов шлях")


# --- ЗАВДАННЯ 3: Алгоритм Дейкстри ---

print(f"\n--- Найкоротший шлях (Дейкстра) ---")

try:
    # Тут ми обов'язково вказуємо weight='weight', щоб врахувати відстань
    dijkstra_path = nx.dijkstra_path(G, source=start_node, target=end_node, weight='weight')
    dijkstra_length = nx.dijkstra_path_length(G, source=start_node, target=end_node, weight='weight')
    
    print(f"Маршрут: {dijkstra_path}")
    print(f"Загальна довжина (вага): {dijkstra_length}")
except nx.NetworkXNoPath:
    print("Шлях не знайдено")