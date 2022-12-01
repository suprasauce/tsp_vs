import pygame as py, constants, colors, math, algo, time, sys

py.init()

screen = py.display.set_mode(size=constants.SCREEN_SIZE)
screen_width, screen_height = py.display.get_surface().get_size()
clock = py.time.Clock()

# globals
city_states = {}
cities = {}
adj = []

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
            temp.append(int(get_distance(city_1, city_2)))
        adj.append(temp)
    return adj

def update_city_state(city , city_states, color):
    city_states[city] = color

def draw_cities(cities, city_states):
    for i, city in enumerate(list(cities.keys())):
        py.draw.circle(screen, city_states[i], city, constants.RADIUS)

def init_globals():
    global city_states
    global cities
    global adj
    city_states = {}
    cities = {}
    adj = []

def update_screen(cities, city_states, call):
    screen.fill(colors.BLACK)
    draw_cities(cities, city_states)

    # cities_pos_list = list(cities.keys())
    # for i in len(edges):
    #     for j in len(edges):
    #         if edges[i][j] == 1:
    #             py.draw.line(screen,colors.WHITE, cities_pos_list[i], cities_pos_list[j], 2)


    for city_1 in cities.keys():
        for city_2 in cities.keys():
            py.draw.line(screen,colors.WHITE, city_1, city_2, 2)
    py.display.update()
    if call:
        py.time.delay(constants.WAIT)

def main():
    global city_states
    global cities
    global adj
    run = True
    mouse_pos = ()
    left_click = 0
    right_click = 0
    init_globals()
    permute_call = False
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

            elif event.type == py.KEYDOWN:
                if event.key == py.K_d:
                    permute_call = True

        mouse_state = py.mouse.get_pressed()
        left_click = mouse_state[0]
        right_click = mouse_state[2]

        for i in range(len(adj)):
            update_city_state(i, city_states, colors.RED)

        update_screen(cities, city_states, permute_call)

        #call permute if len >= 5
        if permute_call:
            n = len(adj)
            nodes = [x for x in range(n)]
            algo.init_globals(city_states, cities, adj)
            algo.permute(0, n, nodes, adj)
            run = False
            print(algo.mini)
        
        
if __name__ == "__main__":
    main()
    # unvisited = red
    # visited = green
    # current = purple