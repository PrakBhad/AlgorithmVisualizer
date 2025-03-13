import pygame

def merge_sort(rects: pygame.sprite.Group, ascending: bool = True):
    sprite_list = rects.sprites()
    n = len(sprite_list)
    width = 1
    left_padding = 10
    spacing = 5

    while width < n:
        for l in range(0, n, width * 2):
            r = min(l + (width * 2 - 1), n - 1)
            m = min(l + width - 1, n - 1)

            L = sprite_list[l:m+1]
            R = sprite_list[m+1:r+1]
            i = j = 0
            k = l

            while i < len(L) and j < len(R):
                # Highlight comparison
                
                L[i].image.fill((255, 0, 0))
                R[j].image.fill((255, 0, 0))
                yield

                # Compare values
                if (L[i].image.get_height() <= R[j].image.get_height()) if ascending else \
                   (L[i].image.get_height() >= R[j].image.get_height()):
                    sprite_list[k] = L[i]
                    # Reset colors before moving index
                    
                    L[i].image.fill((0, 255, 0))
                    R[j].image.fill((0, 255, 0))
                    i += 1
                else:
                    sprite_list[k] = R[j]
                    # Reset colors before moving index
                    L[i].image.fill((0, 255, 0))
                    R[j].image.fill((0, 255, 0))
                    j += 1
                k += 1
                yield

            # Handle remaining elements
            while i < len(L):
                sprite_list[k] = L[i]
                
                L[i].image.fill((0, 255, 0))
                i += 1
                k += 1
                yield

            while j < len(R):
                sprite_list[k] = R[j]
                R[j].image.fill((0, 255, 0))
                j += 1
                k += 1
                yield

            # Update positions
            for idx, sprite in enumerate(sprite_list):
                sprite.rect.x = left_padding + idx * (sprite.rect.width + spacing)
            yield

        width *= 2
    yield
