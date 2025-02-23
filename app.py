from Sorting_Algorithms.bubblesort import *
from Sorting_Algorithms.insertionsort import *
from Sorting_Algorithms.selectionsort import *
from Sorting_Algorithms.mergesort import *
from Graphing_Algorithms.bfs import *
from Graphing_Algorithms.dfs import *
from Graphing_Algorithms.dijkstra import *

import pygame
from pygame.locals import *
import random


class Rect(pygame.sprite.Sprite):
    def __init__(self, height=0, x=0, y=0, width=10, color=(0, 255, 0), value=10):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.value = value
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(midbottom=(x, y))
        return None
        
    def randomize(self, rects: pygame.sprite.Group):
        screen_width, screen_height = pygame.display.get_window_size()
        rect_width = 10  # Fixed width for rectangles
        spacing = 5  # Space between rectangles
        rect_height = 0
        x = 10
        rects.empty()
        arr = [random.randint(120, 500) for i in range(screen_width)]
        for i in range(len(arr)):
            if x + rect_width > screen_width:  # Width Check
                break
            rect_height = abs(arr[i])  # Height Check

            rect = Rect(x=x, y=screen_height, height=rect_height, width=rect_width)
            rects.add(rect)
            x += rect.image.get_width() + spacing  # Spacing

        print(len(rects))
        return rects

class Maze:
    @staticmethod
    def generate_maze(width, height, cell_size=10):
        """Generates a maze that occupies the bottom half of the screen."""
        half_height = height // 2
        cols, rows = width // cell_size, half_height // cell_size
        maze = [[1 for _ in range(cols)] for _ in range(rows)]

        start_x, start_y = random.randrange(
            1, cols, 2), random.randrange(1, rows, 2)
        maze[start_y][start_x] = 0

        walls = [(start_x + dx, start_y + dy) for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]
                 if 0 < start_x + dx < cols and 0 < start_y + dy < rows]

        while walls:
            wx, wy = random.choice(walls)
            walls.remove((wx, wy))

            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = wx + dx, wy + dy
                if 0 < nx < cols and 0 < ny < rows and maze[ny][nx] == 1:
                    maze[wy][wx] = 0
                    maze[(wy + ny) // 2][(wx + nx) // 2] = 0
                    maze[ny][nx] = 0

                    walls.extend([(nx + dx, ny + dy) for dx, dy in directions
                                  if 0 < nx + dx < cols and 0 < ny + dy < rows and maze[ny + dy][nx + dx] == 1])

                    yield maze  # Yield intermediate states for visualization

        yield maze  # Final maze state
        
    @staticmethod
    def draw_maze(screen, maze, cell_size):
        """Draws the maze only in the bottom half of the screen."""
        screen_width, screen_height = pygame.display.get_window_size()
        offset_y = screen_height // 2  # Start drawing from the middle

        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                color = (255, 255, 255) if cell == 1 else (0, 0, 0)
                pygame.draw.rect(
                    screen, color, (x * cell_size, offset_y + y * cell_size, cell_size, cell_size))

          

def fps_toggler(cmpmode: bool):
    if cmpmode:
        return 15
    else:
        return 600


def main():
    pygame.init()
    screen = pygame.display.set_mode((1520, 860), flags=DOUBLEBUF | RESIZABLE)
    pygame.display.set_caption("Algorithm Visualizer")
    clock = pygame.time.Clock()
    running = True

    rect = Rect()
    rects = pygame.sprite.Group()
    rects = rect.randomize(rects)

    sort_generator = None
    sorting_bubble = False
    sorting_insertion = False
    sorting_selection = False
    sorting_merge = False
    sort_ascending = True  # True for ascending, False for descending

    graphing_mode = False
    maze_generator = None
    
    cmpmode = False
    fullscreen = False
    fps = fps_toggler(cmpmode)

    paused = False

    while running:
        # Poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == VIDEORESIZE and not graphing_mode:
                rects = rect.randomize(rects)
                sort_generator = None
                sorting_bubble = False
                sorting_insertion = False
                sorting_selection = False
                sorting_merge = False
                paused = False
                maze_generator = None

            elif event.type == VIDEORESIZE and graphing_mode:
                screen_width, screen_height = pygame.display.get_window_size()
                maze_generator = Maze.generate_maze(
                    screen_width, screen_height)
                maze = [[1 for _ in range(screen_width)]
                        for _ in range(screen_height)]
                sort_generator = None
                sorting_bubble = False
                sorting_insertion = False
                sorting_selection = False
                sorting_merge = False
                paused = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and not graphing_mode:  # Press 'r' to randomize
                    rects = rect.randomize(rects)
                    sort_generator = None
                    sorting_bubble = False
                    sorting_insertion = False
                    sorting_selection = False
                    sorting_merge = False
                    paused = False
                    maze_generator = None

                elif event.key == pygame.K_r and graphing_mode:  # Press 'r' to randomize
                    maze_generator = Maze.generate_maze(
                        screen_width, screen_height)
                    maze = [[1 for _ in range(screen_width)]
                            for _ in range(screen_height)]
                    sort_generator = None
                    sorting_bubble = False
                    sorting_insertion = False
                    sorting_selection = False
                    sorting_merge = False
                    paused = False

                elif event.key == pygame.K_b and not graphing_mode:  # Toggle bubble sort
                    sorting_insertion = False
                    sorting_selection = False
                    sorting_merge = False
                    maze_generator = None
                    sorting_bubble = not sorting_bubble
                    if sorting_bubble:
                        rects = rect.randomize(rects)
                        sort_generator = bubble_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_i and not graphing_mode:  # Toggle insertion sort
                    sorting_bubble = False
                    sorting_selection = False
                    sorting_merge = False
                    maze_generator = None
                    sorting_insertion = not sorting_insertion
                    if sorting_insertion:
                        rects = rect.randomize(rects)
                        sort_generator = insertion_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_s and not graphing_mode:  # Toggle selection sort
                    sorting_bubble = False
                    sorting_insertion = False
                    sorting_merge = False
                    maze_generator = None
                    sorting_selection = not sorting_selection
                    if sorting_selection:
                        rects = rect.randomize(rects)
                        sort_generator = selection_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_m and not graphing_mode:  # Toggle merge sort
                    sorting_bubble = False
                    sorting_insertion = False
                    sorting_selection = False
                    maze_generator = None
                    sorting_merge = not sorting_merge
                    if sorting_merge:
                        rects = rect.randomize(rects)
                        sort_generator = merge_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_d and not graphing_mode:  # Toggle between ascending and descending
                    sort_ascending = not sort_ascending
                    maze_generator = None
                    if sorting_bubble or sorting_insertion or sorting_selection or sorting_merge:
                        rects = rect.randomize(rects)
                        if sorting_bubble:
                            sort_generator = bubble_sort(
                                rects, sort_ascending, cmpmode)
                        elif sorting_insertion:
                            sort_generator = insertion_sort(
                                rects, sort_ascending, cmpmode)
                        elif sorting_selection:
                            sort_generator = selection_sort(
                                rects, sort_ascending, cmpmode)
                        elif sorting_merge:
                            sort_generator = merge_sort(
                                rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_g:
                    graphing_mode = not graphing_mode
                    if not graphing_mode:
                        rects = rect.randomize(rects)
                    else:
                        screen_width, screen_height = pygame.display.get_window_size()
                        maze_generator = Maze.generate_maze(
                            screen_width, screen_height)
                        maze = [[1 for _ in range(screen_width)]
                                for _ in range(screen_height)]

                elif event.key == pygame.K_c:
                    if not (sorting_bubble or sorting_insertion or sorting_selection or sorting_merge):
                        cmpmode = not cmpmode
                        fps = fps_toggler(cmpmode)

                elif event.key == pygame.K_SPACE:  # Press SPACE to pause/unpause
                    paused = not paused

                elif event.key == pygame.K_f and not graphing_mode:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(
                            (1520, 860), flags=DOUBLEBUF | FULLSCREEN)
                        rects = rect.randomize(rects)
                    else:
                        screen = pygame.display.set_mode(
                            (1520, 860), flags=DOUBLEBUF | RESIZABLE)
                        rects = rect.randomize(rects)

                elif event.key == pygame.K_f and graphing_mode:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(
                            (1520, 860), flags=DOUBLEBUF | FULLSCREEN)
                        maze_generator = Maze.generate_maze(
                            screen_width, screen_height)
                        maze = [[1 for _ in range(screen_width)]
                                for _ in range(screen_height)]
                    else:
                        screen = pygame.display.set_mode(
                            (1520, 860), flags=DOUBLEBUF | RESIZABLE)
                        maze_generator = Maze.generate_maze(
                            screen_width, screen_height)
                        maze = [[1 for _ in range(screen_width)] for _ in range(screen_height)]
        # Sorting logic (runs continuously when sorting is True and not paused)
        if not paused:
            if (sorting_bubble or sorting_insertion or sorting_selection or sorting_merge) and sort_generator is not None and not graphing_mode:
                try:
                    next(sort_generator)
                except StopIteration:
                    sorting_bubble = sorting_insertion = sorting_merge = sorting_selection = False
                    sort_generator = None
        
        if not paused:
            if not(sorting_bubble or sorting_insertion or sorting_selection or sorting_merge) and sort_generator is None and graphing_mode:
                try:
                    maze = next(maze_generator)
                except StopIteration:
                    pass
        
        if not graphing_mode:
            screen.fill("black")
            rects.draw(screen)  # Draw rectangles onto screen
        else:
            screen.fill("black")
            Maze.draw_maze(screen,maze,10)
        
        pygame.display.flip()  # Flip the display to put your work on screen
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
