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


class SoringAlgorithm:
    @staticmethod
    def bubble_sort(rects: pygame.sprite.Group, ascending: bool = True, cmpmode: bool = False):
        sprite_list = rects.sprites()
        n = len(sprite_list)

        for sprite in sprite_list:
            sprite.image.fill((0, 255, 0))

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                sp1 = sprite_list[j].image.get_height()
                sp2 = sprite_list[j + 1].image.get_height()

                if cmpmode:
                    sprite_list[j].image.fill((255, 0, 0))
                    sprite_list[j+1].image.fill((255, 0, 0))

                if (sp1 > sp2) if ascending else (sp1 < sp2):
                    swapped = True
                    sprite_list[j], sprite_list[j +
                                                1] = sprite_list[j + 1], sprite_list[j]
                    sprite_list[j].rect.x, sprite_list[j +
                                                       1].rect.x = sprite_list[j + 1].rect.x, sprite_list[j].rect.x
                    yield

                if cmpmode:
                    for sprite in sprite_list:
                        sprite.image.fill((0, 255, 0))
            if not swapped:
                break
        yield

    @staticmethod
    def insertion_sort(rects: pygame.sprite.Group, ascending: bool = True, cmpmode: bool = False):
        sprite_list = rects.sprites()
        n = len(sprite_list)
        left_padding = 10
        spacing = 5

        for i in range(1, n):
            key_sprite = sprite_list[i]
            key_height = key_sprite.image.get_height()
            j = i - 1

            if cmpmode:
                key_sprite.image.fill((255, 0, 0))  # Red color
                yield

            while j >= 0 and ((sprite_list[j].image.get_height() > key_height) if ascending else (sprite_list[j].image.get_height() < key_height)):
                if cmpmode:
                    sprite_list[j].image.fill((255, 0, 0))  # Red color
                    yield
                    sprite_list[j].image.fill((0, 255, 0))  # Green color

                sprite_list[j + 1] = sprite_list[j]
                j -= 1
                yield

            sprite_list[j + 1] = key_sprite

            # Update positions of all sprites
            for index, sprite in enumerate(sprite_list):
                sprite.rect.x = left_padding + index * \
                    (sprite.rect.width + spacing)

            if cmpmode:
                key_sprite.image.fill((255, 0, 0))  # Red color
                yield
                key_sprite.image.fill((0, 255, 0))  # Green color

            yield

        yield

    @staticmethod
    def selection_sort(rects: pygame.sprite.Group, ascending: bool = True, cmpmode: bool = False):
        sprite_list = rects.sprites()
        n = len(sprite_list)
        left_padding = 10
        spacing = 5
        
        if cmpmode:
            original_colors = [sprite.image.get_at((0, 0)) for sprite in sprite_list]
            
        for i in range(n-1):
            min_idx = i
            if cmpmode:
                sprite_list[min_idx].image.fill((255, 0, 0))  # Red for current minimum
                yield
            
            for j in range(i+1, n):
                sp1 = sprite_list[j].image.get_height()
                sp2 = sprite_list[min_idx].image.get_height()
                
                if cmpmode:
                    sprite_list[j].image.fill((255, 0, 0))  # Red for comparison
                    yield
                    sprite_list[j].image.fill(original_colors[j])
                
                if (sp1 < sp2) if ascending else (sp1 > sp2):
                    if cmpmode:
                        sprite_list[min_idx].image.fill(original_colors[min_idx])
                    min_idx = j
                    if cmpmode:
                        sprite_list[min_idx].image.fill((255, 0, 0))  # Red for new minimum
                        yield
                
            if min_idx != i:
                sprite_list[i], sprite_list[min_idx] = sprite_list[min_idx], sprite_list[i]
                if cmpmode:
                    original_colors[i], original_colors[min_idx] = original_colors[min_idx], original_colors[i]
            
            if cmpmode:
                sprite_list[i].image.fill((0, 255, 0))  # Green for sorted position
                yield
            
            # Update positions of all sprites
            for index, sprite in enumerate(sprite_list):
                sprite.rect.x = left_padding + index * (sprite.rect.width + spacing)
            yield
        
        # Ensure the last element is also colored green
        if cmpmode:
            sprite_list[-1].image.fill((0, 255, 0))
            yield

class Renderer:
    def fps_toggler(self,cmpmode:bool):
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
    sorter = SoringAlgorithm()
    rects = pygame.sprite.Group()
    rects = rect.randomize(rects)

    sort_generator = None
    sorting_bubble = False
    sorting_insertion = False
    sorting_selection = False
    sort_ascending = True  # True for ascending, False for descending
    
    cmpmode = False
    displayer = Renderer()
    fps = displayer.fps_toggler(cmpmode)
    
    paused = False

    while running:
        # Poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press 'r' to randomize
                    rects = rect.randomize(rects)
                    paused = False

                elif event.key == pygame.K_b:  # Toggle bubble sort
                    sorting_insertion = False
                    sorting_selection = False
                    sorting_bubble = not sorting_bubble
                    if sorting_bubble:
                        rects = rect.randomize(rects)
                        sort_generator = sorter.bubble_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_i:  # Toggle insertion sort
                    sorting_bubble = False
                    sorting_selection = False
                    sorting_insertion = not sorting_insertion
                    if sorting_insertion:
                        rects = rect.randomize(rects)
                        sort_generator = sorter.insertion_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_s:  # Toggle insertion sort
                    sorting_bubble = False
                    sorting_insertion = False
                    sorting_selection = not sorting_selection
                    if sorting_selection:
                        rects = rect.randomize(rects)
                        sort_generator = sorter.selection_sort(
                            rects, sort_ascending, cmpmode)

                elif event.key == pygame.K_d:  # Toggle between ascending and descending
                    sort_ascending = not sort_ascending
                    if sorting_bubble or sorting_insertion:
                        rects = rect.randomize(rects)
                        if sorting_bubble:
                            sort_generator = sorter.bubble_sort(
                                rects, sort_ascending,cmpmode)
                        elif sorting_insertion:
                            sort_generator = sorter.insertion_sort(
                                rects, sort_ascending,cmpmode)
                        elif sorting_selection:
                            sort_generator = sorter.selection_sort(
                                rects, sort_ascending,cmpmode)

                elif event.key == pygame.K_c:
                    cmpmode = not cmpmode
                    fps = displayer.fps_toggler(cmpmode)

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
