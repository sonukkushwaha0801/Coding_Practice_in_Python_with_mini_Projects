import pygame

pygame.init()

#Initial Values
win_width = 750
win_height = 450
rows = 3
columns = 3
pad = 10

#Calculations
t_width = (win_width - ((rows + 1) * pad)) // rows
t_height = (win_height - ((columns + 1) * pad)) // columns

win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('Tic Tac Toe')

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([t_width, t_height])
        self.image.fill(white)
        self.rect = self.image.get_rect()
    
tile_list = pygame.sprite.Group()
taken_list = pygame.sprite.Group()
    
for row in range(rows):
    for column in range(columns):
        tile = Tile()
        tile.rect.x = pad + ((t_width + pad) * row)
        tile.rect.y = pad + ((t_height + pad) * column)
        tile_list.add(tile)
tile_list.draw(win)
    
def redraw():
    pygame.display.update()
    
draw_object = 'rect'

run = True

while run:
    
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tile_list.draw(win)
                taken_list = pygame.sprite.Group()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i in tile_list:
                if i.rect.collidepoint(pos) and i not in taken_list:
                    taken_list.add(i)
                    if draw_object == 'rect':
                        pygame.draw.rect(win, red, (i.rect.x + pad, i.rect.y + pad, t_width - (2 * pad), t_height - (2 * pad)))
                        draw_object = 'circle'
                    else:
                        if t_width < t_height:
                            pygame.draw.circle(win, green, (i.rect.center), (t_width - 2 * pad) // 2)
                        else:
                            pygame.draw.circle(win, green, (i.rect.center), (t_height - 2 * pad) // 2)
                        draw_object = 'rect'
    redraw()

pygame.quit()
