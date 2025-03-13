import pygame
def insertion_sort(rects: pygame.sprite.Group, ascending: bool = True):
        sprite_list = rects.sprites()
        n = len(sprite_list)
        left_padding = 10
        spacing = 5

        for i in range(1, n):
            key_sprite = sprite_list[i]
            key_height = key_sprite.image.get_height()
            j = i - 1

            
            key_sprite.image.fill((255, 0, 0))  # Red color
            yield

            while j >= 0 and ((sprite_list[j].image.get_height() > key_height) if ascending else (sprite_list[j].image.get_height() < key_height)):
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

            
            key_sprite.image.fill((255, 0, 0))  # Red color
            yield
            key_sprite.image.fill((0, 255, 0))  # Green color

            yield

        yield