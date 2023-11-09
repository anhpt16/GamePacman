import pygame
from board import boards
import math



pygame.init()



WIDTH = 600
HEIGHT = 710
color_grid = (255,255,255)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards
color = 'blue'
PI = math.pi
player_images = []
for i in range(1,5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (30, 30))) #
blinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/red.png'),(20, 20))
#Player Position Default
player_x = 435 #300 (X * 20 + 15) (X * 20 - 5)
player_y = 175 #475 (Y * 20 + 15) (Y * 20 - 5)
#Blinky Position Default
blinky_x = 40 # 10(default) + 20(size 1 ô)
blinky_y = 40


direction = 0
counter = 0
flicker = False
# R, L, U, D
turns_allowed = [False, False, False, False]
direction_command = 0
player_speed = 2
ghost_speed = 1
score = 0



def draw_board():
    num1 = ((HEIGHT - 50) // 33) #(=20)
    num2 = (WIDTH // 30)    #(=20)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
                #pygame.draw.rect(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 1)
            if level[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
                #pygame.draw.rect(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 1)
            if level[i][j] == 3:
                pygame.draw.line(screen, color,(j * num2 + (0.5 * num2), i * num1), (j * num2 + (0.5 * num2), i * num1 + (1 * num1)), 3)
                #pygame.draw.rect(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 1)
            if level[i][j] == 4:
                pygame.draw.line(screen, color,(j * num2, i * num1 + (0.5 * num1)), (j * num2 + (num2), i * num1 + (0.5 * num1)), 3)
                #pygame.draw.rect(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 1)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, (j * num2 - (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 0, PI / 2, 3)
                #pygame.draw.rect(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 1)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), PI /2, PI, 3)
                #pygame.draw.rect(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 1)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, (j * num2 + (0.5 * num2), i * num1 - (0.5 * num1), num2, num1), PI , (3 * PI) / 2, 3)
                #pygame.draw.rect(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 1)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color, (j * num2 - (0.5 * num2), i * num1 - (0.5 * num1), num2, num1), (3 * PI) / 2 , 0, 3)
                #pygame.draw.rect(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 1)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white',(j * num2, i * num1 + (0.5 * num1)), (j * num2 + (num2), i * num1 + (0.5 * num1)), 3)
                #pygame.draw.rect(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1), num2, num1), 1)



def draw_player():
    # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
    if direction == 0:
        screen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))

def draw_ghost():
    screen.blit(blinky_img, (blinky_x, blinky_y))

def check_position(centerx, centery):
    turns = [False, False, False, False]
    #R, L, U, D
    num1 = (HEIGHT - 50) // 33
    num2 = WIDTH // 30


    num3 = 10

    if centerx // 30 < 19:
        # Check go back
        if direction == 0:
            if level[centery // num1][(centerx - num3) // num2] < 3:
                turns[1] = True
        if direction == 1:
            if level[centery // num1][(centerx + num3) // num2] < 3:
                turns[0] = True
        if direction == 2:
            if level[(centery + num3) // num1][centerx // num2] < 3:
                turns[3] = True
        if direction == 3:
            if level[(centery - num3) // num1][centerx // num2] < 3:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 6 <= centerx % num2 <= 14:
                if level[(centery + num3) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num3) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 6 <= centery % num1 <= 14:
                if level[centery // num1][(centerx + num2) // num2] < 3:
                    turns[0] = True
                if level[centery // num1][(centerx - num2) // num2] < 3:
                    turns[1] = True
        
        if direction == 0 or direction == 1:
            if 6 <= centerx % num2 <= 14:
                if level[(centery + num1) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num1) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 6 <= centery % num1 <= 14:
                if level[centery // num1][(centerx + num3) // num2] < 3:
                    turns[0] = True
                if level[centery // num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
    
    else:
        turns[0] = True
        turns[1] = True

    return turns
    pass

def check_node_ghost_plus(pos_x, pos_y, pac_x, pac_y, g0):
    list_node = []
    if(level[pos_x + 1][pos_y] == 0 or level[pos_x + 1][pos_y] == 1 or level[pos_x + 1][pos_y] == 2):
        g = 1 + g0
        h = abs(pac_x - (pos_x + 1)) + abs(pac_y - pos_y)
        f = g + h
        list_node.append((pos_x + 1, pos_y, g, h, f, pos_x, pos_y))
    if(level[pos_x  - 1][pos_y] == 0 or level[pos_x - 1][pos_y] == 1 or level[pos_x - 1][pos_y] == 2):
        g = 1 + g0
        h = abs(pac_x - (pos_x - 1)) + abs(pac_y - pos_y)
        f = g + h
        list_node.append((pos_x - 1, pos_y, g, h, f, pos_x, pos_y))
    if(level[pos_x][pos_y + 1] == 0 or level[pos_x][pos_y + 1] == 1 or level[pos_x][pos_y + 1] == 2):
        g = 1 + g0
        h = abs(pac_x - (pos_x)) + abs(pac_y - (pos_y + 1))
        f = g + h
        list_node.append((pos_x, pos_y + 1, g, h, f, pos_x, pos_y))
    if(level[pos_x][pos_y - 1] == 0 or level[pos_x][pos_y - 1] == 1 or level[pos_x][pos_y - 1] == 2):
        g = 1 + g0
        h = abs(pac_x - (pos_x)) + abs(pac_y - (pos_y - 1))
        f = g + h
        list_node.append((pos_x, pos_y - 1, g, h, f, pos_x, pos_y))
    return list_node
    pass

def check_node_ghost(pos_x, pos_y, pac_x, pac_y, g0):
    list_node = []
    for i in range (pos_x - 1, -1, -1):
        if(level[i][pos_y] != 0 and level[i][pos_y] != 1 and level[i][pos_y] != 2):
            #print("WallTren" + str(i) + str(pos_y))
            break
        else:
            if(level[i][pos_y - 1] == 0 or level[i][pos_y - 1] == 1 or level[i][pos_y - 1] == 2 or level[i][pos_y + 1] == 0 or level[i][pos_y + 1] == 1 or level[i][pos_y + 1] == 2):
                #print("NodeTren" + str(i) + str(pos_y))
                #print("g(tren) = " + str(pos_x - i))
                g = pos_x - i + g0
                #print("h(tren) = " + str(abs(pac_x - i) + abs(pac_y - pos_y)))
                h = abs(pac_x - i) + abs(pac_y - pos_y)
                f = g + h
                list_node.append((i, pos_y, g, h, f, pos_x, pos_y))
                break
            else:
                continue
    for i in range (pos_x + 1, 31, 1):
        if(level[i][pos_y] != 0 and level[i][pos_y] != 1 and level[i][pos_y] != 2):
            #print("WallDuoi" + str(i) + str(pos_y))
            break
        else:
            if(level[i][pos_y - 1] == 0 or level[i][pos_y - 1] == 1 or level[i][pos_y - 1] == 2 or level[i][pos_y + 1] == 0 or level[i][pos_y + 1] == 1 or level[i][pos_y + 1] == 2):
                #print("NodeDuoi" + str(i) + str(pos_y))
                #print("g(duoi) = " + str(i - pos_x))
                g = i - pos_x + g0
                #print("h(duoi) = " + str(abs(pac_x - i) + abs(pac_y - pos_y)))
                h = abs(pac_x - i) + abs(pac_y - pos_y)
                f = g + h
                list_node.append((i, pos_y, g, h, f, pos_x, pos_y))
                break
            else:
                continue
    for i in range (pos_y - 1, -1, -1):
        if(level[pos_x][i] != 0 and level[pos_x][i] != 1 and level[pos_x][i] != 2):
            #print("WallPhai" + str(pos_x) + str(i))
            break
        else:
            if(level[pos_x - 1][i] == 0 or level[pos_x - 1][i] == 1 or level[pos_x - 1][i] == 2 or level[pos_x + 1][i] == 0 or level[pos_x + 1][i] == 1 or level[pos_x + 1][i] == 2):
                #print("NodePhai" + str(pos_x) + str(i))
                #print("g(phai) = " + str(pos_y - i))
                g = pos_y - i + g0
                #print("h(phai) = " + str(abs(pac_x - pos_x) + abs(pac_y - i)))
                h = abs(pac_x - pos_x) + abs(pac_y - i)
                f = g + h
                list_node.append((pos_x, i, g, h, f, pos_x, pos_y))
                break
            else:
                continue
    for i in range (pos_y + 1, 33, 1):
        if(level[pos_x][i] != 0 and level[pos_x][i] != 1 and level[pos_x][i] != 2):
            #print("WallTrai" + str(pos_x) + str(i))
            break
        else:
            if(level[pos_x - 1][i] == 0 or level[pos_x - 1][i] == 1 or level[pos_x - 1][i] == 2 or level[pos_x + 1][i] == 0 or level[pos_x + 1][i] == 1 or level[pos_x + 1][i] == 2):
                #print("NodeTrai" + str(pos_x) + str(i))
                #print("g(trai) = " + str(i - pos_y))
                g = i - pos_y + g0
                #print("h(trai) = " + str(abs(pac_x - pos_x) + abs(pac_y - i)))
                h = abs(pac_x - pos_x) + abs(pac_y - i)
                f = g + h
                list_node.append((pos_x, i, g, h, f, pos_x, pos_y))
                break
            else:
                continue
    return list_node
    pass

def check_path_ghost(ghost_x, ghost_y, pac_x, pac_y):
    best_path = []
    dong = []
    mo = []
    g0 = 0
    h0 = abs(ghost_x - pac_x) + abs(ghost_y - pac_y)
    f0 = h0
    mo.append((ghost_x, ghost_y, g0, h0, f0, ghost_x, ghost_y))
    while(len(mo) != 0):
        set_f = [row[4] for row in mo]
        min_f = min(set_f)
        min_index = set_f.index(min_f)
        if(mo[min_index][0] == pac_x and mo[min_index][1] == pac_y):
            print("Search Completed")
            dong.append(mo[min_index])
            #print(dong)
            break
        else:
            g0 = mo[min_index][2]
            nodes = check_node_ghost_plus(mo[min_index][0], mo[min_index][1], pac_x, pac_y, g0)
            #print(nodes)
            dong.append(mo[min_index])
            for i in range(len(nodes)):
                count_m = 0
                count_d = 0
                for j in range(len(mo)):
                    if(nodes[i][0] == mo[j][0]):
                        if(nodes[i][1] == mo[j][1]):
                            if(nodes[i][2] < mo[j][2]):
                                mo[j] = nodes[i]
                        else:
                            count_m += 1
                    else:
                        count_m += 1
                for k in range(len(dong)):
                    if(len(dong) != 0):
                        if(nodes[i][0] == dong[k][0]):
                            if(nodes[i][1] == dong[k][1]):
                                count_d += 1
                if(count_m == len(mo) and len(dong) != 0 and count_d == 0):
                    mo.append(nodes[i])
                #print("cm:" + str(count_m) + "cd" + str(count_d))
            del mo[min_index]
            #print("Mo")
            #print(mo)
            #print("Dong")
            #print(dong)
    best_path.append(dong[len(dong) - 1])
    x = 0
    for i in range(len(dong) - 1, -1, -1):
        if(dong[i][0] == best_path[x][5] and dong[i][1] == best_path[x][6]):
            best_path.append(dong[i])
            x += 1
    print("BP")
    best_path.reverse()
    '''
    for i in range(len(best_path) - 1):
        fst = best_path[i]
        sed = best_path[i + 1]
        if(fst[0] == sed[0]):
            pygame.draw.line(screen, "red", (sed[0],sed[1]), (fst[0],fst[1]), 1)
        if(fst[1] == sed[1]):
            pygame.draw.line(screen, "red", (sed[1],sed[0]), (fst[1],fst[1]), 1)
    '''
    for i in range(len(best_path) - 1):
        current_cell = best_path[i]
        next_cell = best_path[i + 1]
    
        start_position = (current_cell[1] * 20 + 20 // 2, current_cell[0] * 20 + 20 // 2)
        end_position = (next_cell[1] * 20 + 20 // 2, next_cell[0] * 20 + 20 // 2)  
        pygame.draw.line(screen, "red", start_position, end_position, 2)
    print(best_path)
    return best_path
    pass

def move_player(play_x, play_y):
    # R, L, U, D
    if direction == 0 and turns_allowed[0]:
        play_x += player_speed
    elif direction == 1 and turns_allowed[1]:
        play_x -= player_speed
    elif direction == 2 and turns_allowed[2]:
        play_y -= player_speed
    elif direction == 3 and turns_allowed[3]:
        play_y += player_speed
    return play_x, play_y

def move_ghost(ghost_x,ghost_y, pacman_x, pacman_y):
    blinky_x = (ghost_y ) // 20
    blinky_y = (ghost_x ) // 20
    pac_x = (pacman_y + 15) // 20
    pac_y = (pacman_x + 15) // 20
    path = check_path_ghost(blinky_x, blinky_y, pac_x, pac_y)
    if(path[0][0] == path[1][0]):
        if((path[0][1] - path[1][1]) <= 0):
            if(ghost_x <= (path[1][1] * 20 + 10)):
                ghost_x += ghost_speed
        else:
            if((path[1][1] * 20 + 10)<= ghost_x):
                ghost_x -= ghost_speed
    if(path[0][1] == path[1][1]):
        if((path[0][0] - path[1][0]) <= 0):
            d = path[1][0] * 20 + 10
            if(ghost_y <= (path[1][0] * 20 + 10)):
                #print(d)
                #print(ghost_y)
                ghost_y += ghost_speed
        else:
            if((path[1][0] * 20 + 10)<= ghost_y):
                ghost_y -= ghost_speed
    #print(ghost_x)
    #print(ghost_y)
    return ghost_x, ghost_y
    pass



def check_collisions(scor):
    num2 = WIDTH // 30
    num1 = (HEIGHT - 50) // 33
    if 0 < player_x < 570:
        if level[center_y // num1][center_x // num2] == 1:
            level[center_y // num1][center_x // num2] = 0
            scor += 10
        if level[center_y // num1][center_x // num2] == 2:
            level[center_y // num1][center_x // num2] = 0
            scor += 50
    
    return scor

def draw_misc():
    score_text = font.render(f'Score: {score}', True, 'White')
    screen.blit(score_text, (10, 670))




run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True

    screen.fill('black')

    draw_board()
    draw_player()
    draw_ghost()
    draw_misc()
    center_x = player_x + 15
    center_y = player_y + 15
    turns_allowed = check_position(center_x, center_y)
    player_x, player_y = move_player(player_x, player_y)
    blinky_x, blinky_y = move_ghost(blinky_x, blinky_y, player_x, player_y)
    score = check_collisions(score)
    #print("ABC")
    #print(check_node_ghost(9, 7, 2, 13))
    #check_node_ghost(9, 7, 2, 13,0)
    #check_path_ghost(9,2,2,27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction


    if direction_command == 0 and turns_allowed[0]:
        direction = 0
    if direction_command == 1 and turns_allowed[1]:
        direction = 1
    if direction_command == 2 and turns_allowed[2]:
        direction = 2
    if direction_command == 3 and turns_allowed[3]:
        direction = 3

    if player_x > 600:
        player_x = -50
    elif player_x < -50:
        player_x = 597
    #pygame.draw.circle(screen, 'red', (50,50), 4)
    #screen.blit(player_images[1], (35,35))
    pygame.display.flip()
pygame.quit()
