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
    global is_paused
    is_paused = not is_paused
    button.set_title("Resume" if is_paused else "Pause")

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
is_paused = False   # Track if sorting is paused


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
    global is_paused
    is_paused = not is_paused
    button.set_title("Resume" if is_paused else "Pause")


def Sorting_mode():
    global sorting_generator, is_sorting, is_paused
    sorting_generator = None
    is_sorting = False
    is_paused = False
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
        if is_sorting and not is_paused and sorting_generator is not None:
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


def Graphing_mode():
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

    fps = 60
    graphing_fps = 10

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
                        if mouse_pos[1] >= 300:
                            circles.append(mouse_pos)

                    elif current_component[0] == "Line":
                        if mouse_pos[1] >= 300:
                            hovered_circle = near_circle(mouse_pos, circles)
                            if hovered_circle:
                                if start_hovered_circle:
                                    lines.append(
                                        (start_hovered_circle, hovered_circle))
                                    start_hovered_circle = None  # Reset after drawing the line
                                else:
                                    # Set this circle as the start for the line
                                    start_hovered_circle = hovered_circle

                elif event.button == 3:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[1] >= 300:
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
        for pos in circles:
            pygame.draw.circle(screen, (255, 255, 255), pos,
                               10)  # Draw white circles

        for start_pos, end_pos in lines:
            pygame.draw.line(screen, (255, 255, 255), start_pos,
                             end_pos, 2)  # Draw white lines

        # Refresh the screen and tick the clock
        pygame.display.flip()
        clock.tick(fps)


initialize_main_menu()
main_menu.mainloop(screen)
