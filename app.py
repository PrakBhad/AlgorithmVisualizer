from Sorting_Algorithms.bubblesort import *
from Sorting_Algorithms.insertionsort import *
from Sorting_Algorithms.selectionsort import *
from Sorting_Algorithms.mergesort import *
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

    def maze(self,rects:pygame.sprite.Group):
        screen_width, screen_height = pygame.display.get_window_size()
        rects.empty()
        y = screen_height // 2
        count = 0
        rect_height = 10
        rect_width = 10

        #Left End
        for x in range(0,screen_width+rect_width,10):
            rect = Rect(x=x, y=y, height=rect_height, width=rect_width, color=(255,255,255))
            rects.add(rect)

        #Right End
        for x in range(0,screen_width+rect_width,10):
            rect = Rect(x=x, y=screen_height, height=rect_height, width=rect_width, color=(255,255,255))
            rects.add(rect)

        #Left Vertical Line
        for y1 in range(y,screen_height,10):
            rect = Rect(x=rect_width//2, y=y1, height=rect_height, width=rect_width, color=(255,255,255))
            rects.add(rect)

        #Right Vertical Line
        for y1 in range(y,screen_height+rect_height,10):
            rect = Rect(x=(screen_width-rect_width//2), y=y1, height=rect_height, width=rect_width, color=(255,255,255))
            rects.add(rect)

        isAlternate = 0
        for x in range(30, screen_width, 20):  # Iterate over columns with spacing of 20
            if isAlternate % 2 == 0:  # "Up" line
                for y1 in range(y, y + y // 2, 10):  # Create rectangles going upwards
                    rect = Rect(x=x, y=y1, height=rect_height, width=rect_width, color=(255, 255, 255))
                    if not pygame.sprite.spritecollideany(rect, rects):  # Check for intersection
                        rects.add(rect)  # Add only if no collision
            else:  # "Down" line
                for y1 in range(screen_height - (y // 2), screen_height + rect_height, 10):  
                    # Create rectangles going downwards
                    rect = Rect(x=x, y=y1, height=rect_height, width=rect_width, color=(255, 255, 255))
                    if not pygame.sprite.spritecollideany(rect, rects):  # Check for intersection
                        rects.add(rect)  # Add only if no collision
            isAlternate += 1


        print(len(rects))
        return rects


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

            elif event.type == VIDEORESIZE and graphing_mode:
                rects = rect.maze(rects)
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

                elif event.key == pygame.K_r and graphing_mode:  # Press 'r' to randomize
                    rects = rect.maze(rects)
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
                    else:
                        rects = rect.maze(rects)

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
                        rects = rect.maze(rects)
                    else:
                        screen = pygame.display.set_mode(
                            (1520, 860), flags=DOUBLEBUF | RESIZABLE)
                        rects = rect.maze(rects)
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
        else:
            screen.fill("black")
            rects.draw(screen)
        
        pygame.display.flip()  # Flip the display to put your work on screen
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
