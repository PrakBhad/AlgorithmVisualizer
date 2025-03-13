from Sorting_Algorithms.bubblesort import *
from Sorting_Algorithms.insertionsort import *
from Sorting_Algorithms.selectionsort import *
from Sorting_Algorithms.mergesort import *
from Sorting_Algorithms.rects import Rect as CustomRect

import pygame
from pygame.locals import *

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

    rect = CustomRect()
    rects = pygame.sprite.Group()
    rects = rect.randomize(rects)

    sort_generator = None
    sorting_bubble = False
    sorting_insertion = False
    sorting_selection = False
    sorting_merge = False
    sort_ascending = True  # True for ascending, False for descending

    graphing_mode = False

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
                
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and not graphing_mode:  # Press 'r' to randomize
                    rects = rect.randomize(rects)
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
                    sorting_bubble = not sorting_bubble
                    if sorting_bubble:
                        rects = rect.randomize(rects)
                        sort_generator = bubble_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_i and not graphing_mode:  # Toggle insertion sort
                    sorting_bubble = False
                    sorting_selection = False
                    sorting_merge = False
                    sorting_insertion = not sorting_insertion
                    if sorting_insertion:
                        rects = rect.randomize(rects)
                        sort_generator = insertion_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_s and not graphing_mode:  # Toggle selection sort
                    sorting_bubble = False
                    sorting_insertion = False
                    sorting_merge = False
                    sorting_selection = not sorting_selection
                    if sorting_selection:
                        rects = rect.randomize(rects)
                        sort_generator = selection_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_m and not graphing_mode:  # Toggle merge sort
                    sorting_bubble = False
                    sorting_insertion = False
                    sorting_selection = False
                    sorting_merge = not sorting_merge
                    if sorting_merge:
                        rects = rect.randomize(rects)
                        sort_generator = merge_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_d and not graphing_mode:  # Toggle between ascending and descending
                    sort_ascending = not sort_ascending
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

                elif event.key == pygame.K_c and not graphing_mode:
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

        # Sorting logic (runs continuously when sorting is True and not paused)
        if not paused:
            if (sorting_bubble or sorting_insertion or sorting_selection or sorting_merge) and sort_generator is not None and not graphing_mode:
                try:
                    next(sort_generator)
                except StopIteration:
                    sorting_bubble = sorting_insertion = sorting_merge = sorting_selection = False
                    sort_generator = None

        if not graphing_mode:
            screen.fill("black")
            rects.draw(screen)  # Draw rectangles onto screen

        pygame.display.flip()  # Flip the display to put your work on screen
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
