import pygame as py, constants, colors

py.init()

screen = py.display.set_mode(size=constants.SCREEN_SIZE)
screen_width, screen_height = py.display.get_surface().get_size()
clock = py.time.Clock()

def get_rect_pos(mouse_pos):
    return (mouse_pos[0] - constants.RADIUS, mouse_pos[1] - constants.RADIUS)

def insert_city(cities, mouse_pos):
    if cities.get(mouse_pos) == None:
        rect_pos = get_rect_pos(mouse_pos)
        width = constants.RADIUS*2
        city_rect = py.Rect(rect_pos[0], rect_pos[1], width, width)
        cities[mouse_pos] = city_rect

def delete_city(cities, mouse_rect):
    for city in list(cities.keys()):
        if py.Rect.colliderect(cities[city], mouse_rect):
            del cities[city]

def main():
    run = True
    mouse_pos = ()
    cities = {}
    left_click = 0
    right_click = 0
    while run:
        clock.tick(constants.FPS)
        screen.fill(colors.LIGHT_PURPLE)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            elif event.type == py.MOUSEBUTTONDOWN:
                pass
            elif event.type == py.MOUSEBUTTONUP:
                mouse_pos = py.mouse.get_pos()
                if left_click:
                    insert_city(cities, mouse_pos)
                else:
                    mouse_rect = py.Rect(mouse_pos[0], mouse_pos[1], 1,1)
                    delete_city(cities, mouse_rect)


        mouse_state = py.mouse.get_pressed()
        left_click = mouse_state[0]
        right_click = mouse_state[2]

        for city in cities:
            py.draw.circle(screen, colors.RED, city, constants.RADIUS, 2)
        
        py.display.update()

if __name__ == "__main__":
    main()