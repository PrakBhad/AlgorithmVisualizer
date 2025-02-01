from Sorting_Algorithms.bubblesort import *
from Sorting_Algorithms.insertionsort import *
from Sorting_Algorithms.selectionsort import *

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

    @staticmethod
    def randomize(rects: pygame.sprite.Group):
        screen_width, screen_height = pygame.display.get_window_size()
        rect_width = 10  # Fixed width for rectangles
        spacing = 5  # Space between rectangles
        height = 0
        x = 20
        rects.empty()
        count = 0
        arr = [random.randint(120, 500) for i in range(100)]
        for i in range(len(arr)):
            if x + rect_width > screen_width:  # Width Check
                break
            count = i + 1
            height = abs(arr[i])  # Height Check

            rect = Rect(x=x, y=screen_height, height=height, width=rect_width)
            rects.add(rect)
            x += rect.image.get_width() + spacing  # Spacing
        print(count)
        return rects


class SortingAlgorithm:
    """"""

class Displayer:
    @staticmethod
    def fps_toggler(cmpmode:bool):
        if cmpmode:
            return 15
        else:
            return 600


def main():
    pygame.init()
    screen = pygame.display.set_mode((1520, 860), flags=DOUBLEBUF)
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
    sort_ascending = True  # True for ascending, False for descending
    
    cmpmode = False
    fps = Displayer.fps_toggler(cmpmode)
    
    paused = False

    while running:
        # Poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press 'r' to randomize
                    rects = rect.randomize(rects)
                    sort_generator = None
                    sorting_bubble = False
                    sorting_insertion = False
                    sorting_selection = False
                    paused = False

                elif event.key == pygame.K_b:  # Toggle bubble sort
                    sorting_insertion = False
                    sorting_selection = False
                    sorting_bubble = not sorting_bubble
                    if sorting_bubble:
                        rects = rect.randomize(rects)
                        sort_generator = bubble_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_i:  # Toggle insertion sort
                    sorting_bubble = False
                    sorting_selection = False
                    sorting_insertion = not sorting_insertion
                    if sorting_insertion:
                        rects = rect.randomize(rects)
                        sort_generator = insertion_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_s:  # Toggle insertion sort
                    sorting_bubble = False
                    sorting_insertion = False
                    sorting_selection = not sorting_selection
                    if sorting_selection:
                        rects = rect.randomize(rects)
                        sort_generator = selection_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_d:  # Toggle between ascending and descending
                    sort_ascending = not sort_ascending
                    if sorting_bubble or sorting_insertion:
                        rects = rect.randomize(rects)
                        if sorting_bubble:
                            sort_generator = bubble_sort(
                                rects, sort_ascending,cmpmode)
                        elif sorting_insertion:
                            sort_generator = insertion_sort(
                                rects, sort_ascending,cmpmode)
                        elif sorting_selection:
                            sort_generator = selection_sort(
                                rects, sort_ascending,cmpmode)

                elif event.key == pygame.K_c:
                    if not (sorting_bubble or sorting_insertion or sorting_selection):
                        cmpmode = not cmpmode
                        fps = Displayer.fps_toggler(cmpmode)

                elif event.key == pygame.K_SPACE:  # Press SPACE to pause/unpause
                    paused = not paused

        # Sorting logic (runs continuously when sorting is True and not paused)
        if not paused:
            if (sorting_bubble or sorting_insertion or sorting_selection) and sort_generator is not None:
                try:
                    next(sort_generator)
                except StopIteration:
                    sorting_bubble = sorting_insertion = sorting_selection = False
                    sort_generator = None

        # Fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        rects.draw(screen)  # Draw rectangles onto screen

        pygame.display.flip()  # Flip the display to put your work on screen
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
