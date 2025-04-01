import heapq
from collections import deque
from Sorting_Algorithms.bubblesort import *
from Sorting_Algorithms.insertionsort import *
from Sorting_Algorithms.selectionsort import *
from Sorting_Algorithms.mergesort import *
from Sorting_Algorithms.rects import Rect as CustomRect
from Graphing_Algorithms.placer import *

import pygame
import pygame_menu
import math
from pygame.locals import *
import random

pygame.init()
width = 1520
height = 860
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Main Menu')
clock = pygame.time.Clock()

# Define a custom black theme
black_theme = pygame_menu.themes.Theme(
    background_color=(0, 0, 0),   # Black background
    title_background_color=(0, 0, 0),  # Black title background
    title_font_color=(255, 255, 255),  # White title font
    widget_font_color=(255, 255, 255),  # White widget font
    widget_background_color=(0, 0, 0),  # Black widget background
    selection_color=(255, 255, 255),   # White selection color
    scrollbar_color=(255, 255, 255),    # White scrollbar
)


def choose_sorting_algorithm(value, rects, order_state):
    global sorting_generator
    print(f"Selected Algorithm: {value}")  # Debugging output
    if value == 1:
        print("Initializing Bubble Sort...")
        sorting_generator = bubble_sort(
            rects, ascending=order_state["is_ascending"])
    elif value == 2:
        print("Initializing Insertion Sort...")
        sorting_generator = insertion_sort(
            rects, ascending=order_state["is_ascending"])
    elif value == 3:
        print("Initializing Selection Sort...")
        sorting_generator = selection_sort(
            rects, ascending=order_state["is_ascending"])
    elif value == 4:
        print("Initializing Merge Sort...")
        sorting_generator = merge_sort(
            rects, ascending=order_state["is_ascending"])


def toggle_order(button, order_state):
    """Toggle between ascending and descending order."""
    order_state["is_ascending"] = not order_state["is_ascending"]  # Update the mutable state
    button.set_title(
        f'Toggle Order: {"Ascending" if order_state["is_ascending"] else "Descending"}')


def start_sorting():
    """Start the sorting process."""
    global is_sorting
    is_sorting = True


def toggle_pause(button):
    """Toggle between pause and resume."""
    global is_paused_sorting
    is_paused_sorting = not is_paused_sorting
    button.set_title("Resume" if is_paused_sorting else "Pause")


main_menu = None


def initialize_main_menu():
    """Initialize the main main_menu."""
    global main_menu
    main_menu = pygame_menu.Menu(width=width, height=height,
                                 title='', theme=black_theme)
    main_menu.add.button('Sorting Mode', Sorting_mode)
    main_menu.add.button('Graphing Mode', Graphing_mode)
    pygame.display.set_caption('Main Menu')


def return_to_main_menu():
    """Return to the main main_menu."""
    initialize_main_menu()
    main_menu.mainloop(screen)


sorting_generator = None
is_sorting = False  # Track if sorting is in progress
is_paused_sorting = False   # Track if sorting is paused


def choose_sorting_algorithm(value, rects, order_state):
    global sorting_generator
    print(f"Selected Algorithm: {value}")  # Debugging output
    if value == 1:
        print("Initializing Bubble Sort...")
        sorting_generator = bubble_sort(
            rects, ascending=order_state["is_ascending"])
    elif value == 2:
        print("Initializing Insertion Sort...")
        sorting_generator = insertion_sort(
            rects, ascending=order_state["is_ascending"])
    elif value == 3:
        print("Initializing Selection Sort...")
        sorting_generator = selection_sort(
            rects, ascending=order_state["is_ascending"])
    elif value == 4:
        print("Initializing Merge Sort...")
        sorting_generator = merge_sort(
            rects, ascending=order_state["is_ascending"])


def toggle_order(button, order_state):
    """Toggle between ascending and descending order."""
    order_state["is_ascending"] = not order_state["is_ascending"]  # Update the mutable state
    button.set_title(
        f'Toggle Order: {"Ascending" if order_state["is_ascending"] else "Descending"}')


def start_sorting():
    """Start the sorting process."""
    global is_sorting
    is_sorting = True


def toggle_pause(button):
    """Toggle between pause and resume."""
    global is_paused_sorting
    is_paused_sorting = not is_paused_sorting
    button.set_title("Resume" if is_paused_sorting else "Pause")


def Sorting_mode():
    global sorting_generator, is_sorting, is_paused_sorting
    sorting_generator = None
    is_sorting = False
    is_paused_sorting = False
    pygame.display.set_caption('Sorting Visualizer')

    sorting_menu = pygame_menu.Menu(width=width, height=height, title='',
                                    theme=black_theme, center_content=False)

    # Create and randomize rectangles for sorting visualization
    rect = CustomRect()
    rects = pygame.sprite.Group()
    rects = rect.randomize(rects)

    # Add and position the 'Back' button
    back = sorting_menu.add.button('Back', return_to_main_menu)
    back.set_alignment(pygame_menu.locals.ALIGN_LEFT)  # Force alignment

    # Add and position the sorting algorithm dropdown
    order_state = {"is_ascending": True}  # Use a dictionary to track the state
    sorting_algorithms = sorting_menu.add.dropselect(
        'Sorting Algorithm: ',
        items=[
            ('Bubble Sort', 1),
            ('Insertion Sort', 2),
            ('Selection Sort', 3),
            ('Merge Sort', 4)
        ],
        onchange=lambda value, _: choose_sorting_algorithm(
            value[0][1], rects, order_state),  # Extract identifier
        open_middle=False
    )
    sorting_algorithms.set_alignment(pygame_menu.locals.ALIGN_LEFT)

    # Add and position the 'Randomize' button
    randomize = sorting_menu.add.button(
        'Randomize', lambda: rect.randomize(rects) if not is_sorting else None)
    randomize.set_alignment(pygame_menu.locals.ALIGN_LEFT)

    # Add a toggle button for ascending/descending order
    toggle_order_button = sorting_menu.add.button(
        'Toggle Order: Ascending', lambda: toggle_order(toggle_order_button, order_state))
    toggle_order_button.set_alignment(pygame_menu.locals.ALIGN_LEFT)

    # Add a 'Start' button
    start_button = sorting_menu.add.button('Start', start_sorting)
    start_button.set_alignment(pygame_menu.locals.ALIGN_LEFT)

    # Add a 'Pause' button
    pause_button = sorting_menu.add.button(
        'Pause', lambda: toggle_pause(pause_button))
    pause_button.set_alignment(pygame_menu.locals.ALIGN_LEFT)

    fps = 60
    sorting_fps = 10
    while True:
        events = pygame.event.get()  # Retrieve all events from Pygame's event queue

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Fill the screen with black
        screen.fill("black")
        sorting_menu.update(events)
        sorting_menu.draw(screen)
        rects.draw(screen)

        # If sorting is in progress and not paused, step through the generator
        if is_sorting and not is_paused_sorting and sorting_generator is not None:
            randomize.enabled = False  # Disable the 'Randomize' button
            try:
                next(sorting_generator)  # Advance the sorting algorithm
                fps = sorting_fps  # Set the FPS to the sorting FPS
            except StopIteration:
                sorting_generator = None  # Sorting is complete
                randomize.enabled = True  # Enable the 'Randomize' button
                is_sorting = False  # Reset sorting state
                fps = 60  # Reset FPS

        # Update the display and control FPS
        pygame.display.flip()
        clock.tick(fps)


graphing_generator = None
is_paused_graphing = False
is_graphing = False
graph = {}  # Dictionary to store adjacency list
selected_algorithm = None  # Store selected algorithm
start_node = None
goal_node = None


def build_graph(lines):
    global graph
    graph = {}

    for start, end, length in lines:
        graph.setdefault(start, []).append((end, length))
        graph.setdefault(end, []).append((start, length))  # Undirected graph


def bfs(start_node):
    visited = set()
    queue = deque([start_node])
    parent = {start_node: None}  # Store parent nodes for path reconstruction

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        yield node, parent  # Return the node and the parent dictionary

        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = node  # Track the path


def dfs(start_node):
    visited = set()
    stack = [start_node]
    parent = {start_node: None}  # Store parent nodes for path reconstruction

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        yield node, parent  # Return the node and the parent dictionary

        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = node  # Track the path


def dijkstra(start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    visited = set()
    parent = {start_node: None}  # Store parent nodes for path reconstruction

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)

        if node in visited:
            continue
        visited.add(node)

        yield node, parent  # Return the node and the parent dictionary

        for neighbor, weight in graph.get(node, []):
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
                parent[neighbor] = node  # Track the path


def choose_graphing_algorithm(value, circles, lines):
    """Store selected algorithm but do not start until 'Start' is pressed."""
    global selected_algorithm, graphing_generator
    build_graph(lines)  # Build graph from lines
    selected_algorithm = value  # Store selection for later


def start_graphing():
    global is_graphing, graphing_generator, start_node, goal_node
    if not selected_algorithm:
        print("No algorithm selected!")
        return
    if not graph:
        print("Graph is empty! Add nodes and edges first.")
        return
    # Select random start and goal nodes
    nodes = list(graph.keys())
    if len(nodes) < 2:
        print("Not enough nodes to select start and goal.")
        return
    start_node, goal_node = random.sample(
        nodes, 2)  # Ensure they are different
    is_graphing = True  # Enable graphing
    if selected_algorithm == 1:
        graphing_generator = bfs(start_node)
    elif selected_algorithm == 2:
        graphing_generator = dfs(start_node)
    elif selected_algorithm == 3:
        graphing_generator = dijkstra(start_node)


def toggle_pause_graphing(button):
    """Toggle between pause and resume."""
    global is_paused_graphing
    is_paused_graphing = not is_paused_graphing
    button.set_title("Resume" if is_paused_graphing else "Pause")


def Graphing_mode():
    global is_graphing, graphing_generator, start_node, goal_node
    pygame.display.set_caption('Graphing Visualizer')
    graphing_menu = pygame_menu.Menu(width=width, height=height, title='',
                                     theme=black_theme, center_content=False)

    back = graphing_menu.add.button('Back', return_to_main_menu)
    back.set_alignment(pygame_menu.locals.ALIGN_LEFT)  # Force alignment

    current_component = ["Node"]
    adder = graphing_menu.add.dropselect(
        'Component', items=[('Node', 1), ('Line', 2)],
        onchange=lambda component, _: choose_component(
            component[0][1], current_component),
        open_middle=False)  # Adding Component Selector
    adder.set_alignment(pygame_menu.locals.ALIGN_LEFT)  # Force alignment

    circles = []
    lines = []
    start_hovered_circle = None
    reset = graphing_menu.add.button(
        'Reset', lambda: remove_components(circles, lines))
    reset.set_alignment(pygame_menu.locals.ALIGN_LEFT)  # Force alignment

    graphing_algorithms = graphing_menu.add.dropselect(
        'Sorting Algorithm: ',
        items=[
            ('BFS', 1),
            ('DFS', 2),
            ('Dijstra', 3)
        ],
        onchange=lambda value, _: choose_graphing_algorithm(
            value[0][1], circles, lines),  # Extract identifier
        open_middle=False
    )
    graphing_algorithms.set_alignment(pygame_menu.locals.ALIGN_LEFT)

    start_button = graphing_menu.add.button('Start', start_graphing)
    start_button.set_alignment(pygame_menu.locals.ALIGN_LEFT)

    # Add a 'Pause' button
    pause_button = graphing_menu.add.button(
        'Pause', lambda: toggle_pause_graphing(pause_button))
    pause_button.set_alignment(pygame_menu.locals.ALIGN_LEFT)

    fps = 60
    graphing_fps = 3
    
    explored_edges = set()
    final_path_edges = set()
    
    while True:
        events = pygame.event.get()  # Retrieve all events from Pygame's event queue

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    # Add mouse position to circles list
                    mouse_pos = pygame.mouse.get_pos()
                    if current_component[0] == "Node":
                        if mouse_pos[1] >= 420:
                            circles.append(mouse_pos)

                    elif current_component[0] == "Line":
                        if mouse_pos[1] >= 420:
                            hovered_circle = near_circle(mouse_pos, circles)
                            if hovered_circle:
                                if start_hovered_circle:
                                    length = math.ceil(math.hypot(start_hovered_circle[0] - hovered_circle[0],
                                                                  start_hovered_circle[1] - hovered_circle[1]))
                                    lines.append(
                                        (start_hovered_circle, hovered_circle, length))
                                    start_hovered_circle = None  # Reset after drawing the line
                                else:
                                    # Set this circle as the start for the line
                                    start_hovered_circle = hovered_circle

                elif event.button == 3:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[1] >= 420:
                        # Check for node removal
                        hovered_circle = near_circle(mouse_pos, circles)
                        if hovered_circle:
                            circles.remove(hovered_circle)

                        # Check for line removal
                        hovered_line = near_line(mouse_pos, lines)
                        if hovered_line:
                            lines.remove(hovered_line)

        # Fill the screen with black
        screen.fill("black")

        # Update and draw the menu
        graphing_menu.update(events)
        graphing_menu.draw(screen)

        # Draw all circles
        for start_pos, end_pos, length in lines:
            color = (255, 255, 255)  # Default white

            if (start_pos, end_pos) in explored_edges or (end_pos, start_pos) in explored_edges:
                color = (255, 255, 0)  # Yellow for explored edges

            if (start_pos, end_pos) in final_path_edges or (end_pos, start_pos) in final_path_edges:
                color = (255, 0, 0)  # Red for the final path

            pygame.draw.line(screen, color, start_pos, end_pos, 2)

        # Draw nodes (circles)
        for pos in circles:
            color = (255, 255, 255)  # Default white
            if pos == start_node:
                color = (0, 255, 0)  # Green for start
            elif pos == goal_node:
                color = (128, 0, 128)  # Purple for goal

            pygame.draw.circle(screen, color, pos, 10)
        
        pygame.draw.line(screen, color=(255, 255, 255), start_pos=(
            0, 380), end_pos=(1520, 380), width=10)

        # Run graphing algorithm step-by-step
        if is_graphing and graphing_generator:
            try:
                # Get node and parent dictionary
                current_node, parent = next(graphing_generator)

                # Add edges to explored_edges
                if parent[current_node] is not None:
                    explored_edges.add((parent[current_node], current_node))

                # Highlight current node
                pygame.draw.circle(screen, (0, 255, 0), current_node, 12)

            except StopIteration:
                # After algorithm finishes, reconstruct final path
                node = goal_node
                while node is not None and node in parent:
                    prev_node = parent[node]
                    if prev_node is not None:
                        final_path_edges.add((prev_node, node))
                    node = prev_node

                is_graphing = False  # Stop graphing
        

        # Refresh the screen and tick the clock
        pygame.display.flip()
        clock.tick(fps)


initialize_main_menu()
main_menu.mainloop(screen)
