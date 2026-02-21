from os.path import join
from constants import SPRITE_SHEET_WINDOW, SPRITE_WINDOW
import pygame


class ResourceLoader:

    def load_images(image_path: str):
        sprite_sheet_dict = {
            'imgs.png': pygame.image.load('imgs.png').convert_alpha()
        }
        img_meta_data = join(image_path, 'imgs.txt')
        sprite_dict = {}
        with open(img_meta_data) as file:
            for line in file.readlines():
                index, sprite_name, resource_name = line.split(',')
                try:
                    sprite = ResourceLoader.get_sprite(
                        sprite_sheet_dict[resource_name], index, SPRITE_SHEET_WINDOW, SPRITE_WINDOW
                    )
                    sprite_dict[sprite_name] = sprite
                except KeyError:
                    raise Exception(f'No such sprite sheet "{resource_name}". Check the resource name.')
        return sprite_dict

    def get_sprite(
        sprite_sheet: pygame.Surface,
        index: int,
        sprite_sheet_window: tuple,
        sprite_window: tuple
    ) -> pygame.Surface:
        sprite = pygame.Surface(sprite_window, pygame.SRCALPHA)
        # 
        i = (index * sprite_window[0])
        x = (i % sprite_sheet_window[0]) // sprite_window[0]
        y = i // sprite_sheet_window[0]
        sprite.blit(sprite_sheet, (0, 0), (x, y, *sprite_window))
        return sprite

    def load_audios(audio_path: str):
        pass
