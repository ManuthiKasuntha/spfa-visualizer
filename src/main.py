import pygame
from visualizer import Visualizer
from algorithms import SPFA_Algorithms

# ---------- CONFIG ----------
ROWS = 10
COLS = 10
CELL_SIZE = 40
GRID_ORIGIN = (50, 50)

# Initialize maze and demo walls (0 = path, 1 = wall)
maze = [[0 for _ in range(COLS)] for _ in range(ROWS)]
maze[1][1] = 1
maze[2][1] = 1
maze[3][1] = 1
maze[1][3] = 1
maze[2][3] = 1
maze[3][3] = 1
maze[4][2] = 1
maze[5][2] = 1
maze[6][2] = 1
maze[4][9] = 1
maze[5][9] = 1
maze[6][9] = 1

# Specify start & end
start = (0, 0)  # (row, col)
end   = (9, 9)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("SPFA Visualizer")

    # Create Visualizer (holds maze, drawing and helpers)
    viz = Visualizer(rows=ROWS, cols=COLS, cell_size=CELL_SIZE,
                     grid_origin=GRID_ORIGIN, maze=maze, start=start, end=end)

    # Create graph from maze
    graph = viz.maze_to_graph()
    graph.start = start
    graph.goal = end

    print(f"Graph has {len(graph.nodes)} nodes")
    print(f"Start node {start} neighbors: {graph.neighbors(start)}")
    print(f"End node {end} neighbors: {graph.neighbors(end)}")

    # -------- Convert graph to Dijkstra edges --------
    edges = []   # (u,v,w)

    for (r, c) in graph.nodes:
        u = viz.id_from_coord(r, c)
        for (nr, nc) in graph.neighbors((r, c)):
            v = viz.id_from_coord(nr, nc)
            edges.append((u, v, 1))

    src_id = viz.id_from_coord(*start)
    dst_id = viz.id_from_coord(*end)

    # IMPORTANT: n must match numeric ID range (0..ROWS*COLS-1)
    n = ROWS * COLS

    path_ids = SPFA_Algorithms.dijkstras(
        n=n,
        edges=edges,
        src=src_id,
        dst=dst_id
    )

    # Convert node IDs → (r,c)
    shortest_path = [viz.coord_from_id(pid) for pid in path_ids]

    # -------- Main Loop --------
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((50, 50, 50))
        viz.draw_grid(screen, path=shortest_path)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()