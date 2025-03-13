import pygame
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

            rect = Rect(x=x, y=screen_height,
                        height=rect_height, width=rect_width)
            rects.add(rect)
            x += rect.image.get_width() + spacing  # Spacing

        print(len(rects))
        return rects
