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
        arr = [random.randint(75, 500) for i in range(100)]
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

    @staticmethod
    def bubble_sort_asc(rects: pygame.sprite.Group):
        sprite_list = rects.sprites()
        n = len(sprite_list)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                sp1 = sprite_list[j].image.get_height()
                sp2 = sprite_list[j + 1].image.get_height()
                if sp1 > sp2:
                    swapped = True
                    # Swap the sprites in the list
                    sprite_list[j], sprite_list[j +
                                                1] = sprite_list[j + 1], sprite_list[j]

                    # Swap the x positions of the sprites
                    temp_x = sprite_list[j].rect.x
                    sprite_list[j].rect.x = sprite_list[j + 1].rect.x
                    sprite_list[j + 1].rect.x = temp_x

                    # Yield control back to the main loop to update the display
                    yield

            if not swapped:
                break

        # Final yield to indicate sorting is complete
        yield

    @staticmethod
    def bubble_sort_desc(rects: pygame.sprite.Group):
        sprite_list = rects.sprites()
        n = len(sprite_list)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                sp1 = sprite_list[j].image.get_height()
                sp2 = sprite_list[j + 1].image.get_height()
                if sp1 < sp2:
                    swapped = True
                    # Swap the sprites in the list
                    sprite_list[j], sprite_list[j +
                                                1] = sprite_list[j + 1], sprite_list[j]

                    # Swap the x positions of the sprites
                    temp_x = sprite_list[j].rect.x
                    sprite_list[j].rect.x = sprite_list[j + 1].rect.x
                    sprite_list[j + 1].rect.x = temp_x

                    # Yield control back to the main loop to update the display
                    yield

            if not swapped:
                break

        # Final yield to indicate sorting is complete
        yield


def main():
    pygame.init()
    screen = pygame.display.set_mode((1520, 860), flags=DOUBLEBUF)
    clock = pygame.time.Clock()
    running = True

    rect = Rect()
    rects = pygame.sprite.Group()
    rects = rect.randomize(rects)
    
    sort_generator = rect.bubble_sort_asc(rects)
    sort_generator_2 = rect.bubble_sort_desc(rects)
    
    sorting = False
    sorting_desc = False
    sorted_asc = False
    sorted_desc = True
    
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press r to randomize
                    rects = rect.randomize(rects)
                    sort_generator = rect.bubble_sort_asc(
                        rects)  # Reset the generator
                    sort_generator_2 = rect.bubble_sort_desc(
                        rects)  # Reset the generator
                    
                    sorting = False  # Stop sorting when randomizing
                    sorting_desc = False 

                elif event.key == pygame.K_b:  # Press 'b' to toggle ascending sort
                    if sorting_desc:  # Stop ascending sort before starting descending sort
                        sorting_desc = False
                        sort_generator_2 = None  # Clear the generator

                    sorting = not sorting  # Toggle sorting on/off
                    sorting_desc = False  # Ensure descending sort is off
                    
                    if sorted_desc: # Re randomize it, temp fix
                        rects = rect.randomize(rects)
                    
                    if sorting:
                        sort_generator = rect.bubble_sort_asc(
                            rects)  # Reset the generator

                elif event.key == pygame.K_n:  # Press 'n' to toggle descending sort
                    if sorting:  # Stop ascending sort before starting descending sort
                        sorting = False
                        sort_generator = None  # Clear the generator

                    sorting_desc = not sorting_desc  # Toggle descending sort
                    
                    if sorted_asc: # Re randomize it, temp fix
                        rects = rect.randomize(rects)
                    
                    if sorting_desc:
                        sort_generator_2 = rect.bubble_sort_desc(
                            rects)  # Reset the generator

        # Sorting logic (runs continuously when sorting is True)
        if sorting:
            try:
                next(sort_generator)  # Advance the sorting algorithm
            except StopIteration:
                sorting = False  # Sorting is complete
                sorted_asc = True

        if sorting_desc:
            try:
                next(sort_generator_2)  # Advance the sorting algorithm
            except StopIteration:
                sorting = False  # Sorting is complete
                sorted_desc = True

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        rects.draw(screen)  # Draw rectangles onto screen

        pygame.display.flip()  # flip() the display to put your work on screen
        clock.tick(600)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
