import pygame
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