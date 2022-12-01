import pygame as py, constants, colors, math

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
        
def get_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def update_weights(cities):
    adj = []
    for city_1 in cities.keys():
        temp = []
        for city_2 in cities.keys():
            temp.append(get_distance(city_1, city_2))
        adj.append(temp)
    return adj

def update_city_state(city , city_states, color):
    city_states[city] = color

def draw_cities(cities, city_states):
    for i, city in enumerate(list(cities.keys())):
        py.draw.circle(screen, city_states[i], city, constants.RADIUS)

def main():
    run = True
    mouse_pos = ()
    cities = {}
    adj = []
    left_click = 0
    right_click = 0
    city_states = {}
    while run:
        clock.tick(constants.FPS)
        screen.fill(colors.BLACK)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            elif event.type == py.MOUSEBUTTONDOWN:
                pass
            elif event.type == py.MOUSEBUTTONUP:
                mouse_pos = py.mouse.get_pos()
                if left_click:
                    insert_city(cities, mouse_pos)
                    adj = update_weights(cities)
                else:
                    mouse_rect = py.Rect(mouse_pos[0], mouse_pos[1], 1,1)
                    delete_city(cities, mouse_rect)
                    adj = update_weights(cities)

        mouse_state = py.mouse.get_pressed()
        left_click = mouse_state[0]
        right_click = mouse_state[2]

        for i in range(len(adj)):
            update_city_state(i, city_states, colors.RED)

        draw_cities(cities, city_states)

        for city_1 in cities.keys():
            for city_2 in cities.keys():
                py.draw.line(screen,colors.WHITE, city_1, city_2, 2)

        #call rec
        
        py.display.update()

if __name__ == "__main__":
    main()