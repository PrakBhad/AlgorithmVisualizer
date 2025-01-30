from Sorting_Algorithms.bubblesort import *
from Sorting_Algorithms.quicksort import *
from Sorting_Algorithms.insertionsort import *
from Sorting_Algorithms.mergesort import *
import pygame
from pygame.locals import *
import random

class Rect(pygame.sprite.Sprite):
    def __init__(self, x=100, y=0, width=100, height=500, color=(0, 255, 0), value=10):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.value = value
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect(center=(x, y))
def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (1280, 720), flags=DOUBLEBUF)
    clock = pygame.time.Clock()
    running = True
    
    rects = pygame.sprite.Group()
    x=50
    height = 500
    arr= [random.randint(-200,200) for i in range(100)]
    
    for i in range(len(arr)):
            rect = Rect(x=x,y=screen.get_height(),height=height) #Centered the rectangles
            rects.add(rect)
            x+=rect.image.get_width()+20
            height=max(100,rect.image.get_height()+arr[i])
    
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
