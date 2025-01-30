from Sorting_Algorithms.bubblesort import *
from Sorting_Algorithms.quicksort import *
from Sorting_Algorithms.insertionsort import *
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
    
    def randomize(self,rect:Rect,rects:pygame.sprite.Group,arr:list):
        screen_width,screen_height = pygame.display.get_window_size()
        rect_width = 10  # Fixed width for rectangles
        spacing = 5  # Space between rectangles 
        height = 0
        x = 10
        print(screen_width)
        print(screen_height) 
        for i in range(len(arr)):
            if x + rect_width > screen_width:  # Width Check
                break
            
            height = arr[i]  # Height Check

            rect = Rect(x=x, y=screen_height, height=height)
            rects.add(rect)
            x += rect.image.get_width()+spacing #Spacing
            
        return rects

def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (1280, 720), flags=DOUBLEBUF)
    clock = pygame.time.Clock()
    running = True
    
    rect = Rect()
    rects = pygame.sprite.Group()
    arr = [random.randint(0, 500) for i in range(100)]
    rects = rect.randomize(rect,rects,arr)
    
    #arr = [random.randint(0, 500) for i in range(100)]
    #srt_arr = arr
    """
    for i in range(len(srt_arr)):
        if x + rect_width > screen_width:  # Width Check
            break

        height = srt_arr[i]  # Height Check

        rect = Rect(x=x, y=screen_height, height=height)
        rects.add(rect)
        
        x += rect.image.get_width()+spacing #Spacing
    """

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        rects.draw(screen)
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
