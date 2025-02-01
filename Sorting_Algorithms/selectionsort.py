import pygame
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