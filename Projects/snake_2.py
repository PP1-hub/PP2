import pygame
import time 
import random


pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption("My Snake Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRASS = (37, 232, 102)


clock = pygame.time.Clock() # to track time 

snake_size = 10

apple = pygame.image.load("images/apple_small.png").convert_alpha()

message_font = pygame.font.SysFont('qwerty', 30) # messages-> Game over 
score_font = pygame.font.SysFont('qwerty', 25) # score 

FPS = 10 # snake speed 

def draw_score(score):
    text = score_font.render("Score: " + str(score), True, BLACK) 
    screen.blit(text, [0, 0]) #position 

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(screen, ORANGE, [pixel[0], pixel[1], snake_size, snake_size]) #pass a list, position of individuals block.
        #on the position 0 1 we have this pixel and it has x/y coordinate, we draw a pixel of snake size

def run_game():

    game_over = False # use in while loop
    game_close = False

    x = SCREEN_WIDTH / 2  # define starting position 
    y = SCREEN_HEIGHT / 2

    x_speed = 0  # define a default speed of snake 
    y_speed = 0

    snake_pixels = [] # snake is going to grow in size we need to add more blocks to it
    snake_length = 1  

    target_x = round(random.randrange(0, SCREEN_WIDTH-snake_size) / 10.0) *10.0 #for food 
    target_y = round(random.randrange(0, SCREEN_HEIGHT-snake_size) / 10.0) *10.0

# MAIN GAME LOOP
    while not game_over:

        while game_close:
            screen.fill(BLACK)
            game_over_message = message_font.render("Game Over!", True, RED) 
            screen.blit(game_over_message, [SCREEN_WIDTH/3, SCREEN_HEIGHT/2]) #position of message 
            draw_score(snake_length - 1) #update 
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1: # if we press 1, game quit 
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2: # if we press 2, we restart the game 
                        run_game()  
                if event.type == pygame.QUIT: 
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               game_over = True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT:  # if we press left, we want the snake to go to the left and change the speed
                    x_speed =- snake_size     #movement 
                    y_speed = 0 # as we cant move dioganally 
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed =- snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if  x >= SCREEN_WIDTH  or x < 0 or  y>= SCREEN_HEIGHT or y < 0: # boundary-> right/left limit
            game_close = True

        x += x_speed   #the position of the head is going to be increasedby the speed 
        y += y_speed   # MOVEMENT change the position based on the speed 

        screen.fill(GRASS) #background 
        #pygame.draw.rect(screen, RED, [target_x, target_y, snake_size, snake_size])
        fruit_rect = pygame.Rect( [target_x, target_y, snake_size, snake_size]) #drawing apple 
        screen.blit(apple, fruit_rect)

        snake_pixels.append([x,y]) 

        if len(snake_pixels) > snake_length:
            del snake_pixels[0] #delete the tail

        for pixel in snake_pixels[:-1]:   # if one of those pixels is in the same position as the current posiyion of the head, running into himself 
            if pixel == [x,y]: # CRASH HIMSELF 
                game_close = True

        draw_snake(snake_size, snake_pixels) 
        draw_score(snake_length - 1)       #we have the length of one but we still want to have a score of 0 cause we havent done anything, when we got 1 food we want to have score 1

        pygame.display.update() #update the changes 

        if x == target_x and y == target_y: # if  the head of snake in the same position as food, then we will eat it
            target_x = round(random.randrange(0, SCREEN_WIDTH-snake_size) / 10.0) *10.0
            target_y = round(random.randrange(0, SCREEN_HEIGHT-snake_size) / 10.0) *10.0

            snake_length +=1


        clock.tick(FPS)

    pygame.quit() 
    quit() #quit in general 

run_game()
