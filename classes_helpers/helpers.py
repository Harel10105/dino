import pygame


def add_image(screen, img_path, x_pos, y_pos, width, height, backgruond):
    if backgruond is not None:
        # Add the image to the screen
        img = pygame.image.load(img_path)
        img.set_colorkey(backgruond)
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (x_pos, y_pos))
    else:
        # Add the image to the screen
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (x_pos, y_pos))

def mouse_in_button(button, mouse_pos):
    """
    The function get button and mouse press position on screen and return True
    if mouse click on button
    :param button: Button object
        button on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """
    if  button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.height:
        return True
    return False