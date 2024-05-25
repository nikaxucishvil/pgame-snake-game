import pygame
import random
import time

# Pygame-ის ინიციალიზაცია
pygame.init()

# შეკითხვა
print("(play / setting)")
question = input("enter one: ").lower().strip()

# ეკრანის ზომები
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# ეკრანის შექმნა
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# ფერების განსაზღვრა
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)

# გველის სისწრაფე და კუბის ზომა
snake_speed = 20
snake_block = 10

# გველის საწყისი პოზიცია
x1 = SCREEN_WIDTH / 2
y1 = SCREEN_HEIGHT / 2

# გველის პოზიციები
x1_change = 0
y1_change = 0

# საჭმლის პარამეტრები
food_width = 10
food_height = 10
foodx = random.randint(0, 795)
foody = random.randint(0, 595)
food_constructor = pygame.rect.Rect(foodx, foody, food_width, food_height)

# გველის სხეული
snake_body = []

# საათი
clock = pygame.time.Clock()

def snake_block_add(x, y):
    snake_body.append((x, y))
snake_block_add(x1, y1)

# თამაშის დასრულების ფუნქცია
def game_over():
    game_close = True
    while game_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        screen.fill(BLACK)
        font_style = pygame.font.SysFont(None, 50)
        message = font_style.render("Game Over! Do you want to play again?", True, RED)
        screen.blit(message, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])
    
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    game_loop()

def game_loop():
    global x1, y1, x1_change, y1_change, snake_block, snake_speed, GREEN, SCREEN_WIDTH, SCREEN_HEIGHT, screen, RED, BLACK, clock, snake_body

    game_over = True

    sound = pygame.mixer.music.load('8bit-music-for-game-68698.mp3')
    pygame.mixer.music.play(-1)
    # საჭმლის კოორდინატების გენერაცია
    foodx = int(random.randint(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    foody = int(random.randint(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
    data_text_font = pygame.font.SysFont('verdana', 30)


    snake_color = GREEN
    # ქულები
    score = 0
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        x1 += x1_change
        y1 += y1_change

        # ეკრანის შევსება ფონური გამოსახულებით
        screen.fill(BLACK)
        
        # საჭმლის დახატვა
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])

        # ამოწმებს თუ გველი შეეხო საჭმელს
        if x1 == foodx and y1 == foody:
            foodx = random.randint(0, (SCREEN_WIDTH - snake_block) // 10) * 10
            foody = random.randint(0, (SCREEN_HEIGHT - snake_block) // 10) * 10
            snake_speed += 1
            snake_body.append([x1, y1])
            score += 1

        # ამოწმებს ქულა თუ არის 100        
        if score == 100:
            screen.fill(GREEN)
            vin_text = data_text_font.render("YOU WIN", True, RED)
            screen.blit(vin_text, (325, 300))
            pygame.display.update()
            time.sleep(5)
            game_over = False

        #  ქულების გამოტანა ეკრანზე 
        score_text = data_text_font.render("Score:" + str(score), True, RED)
        screen.blit(score_text, (10,10))

        # განაახლეთ გველის სხეულის პოზიციები
        for i in range(len(snake_body) - 1, 0, -1):
            snake_body[i] = snake_body[i - 1]
        snake_body[0] = [x1, y1]

        # დახატეთ გველის სხეული
        for block in snake_body:
            pygame.draw.rect(screen, snake_color, [block[0], block[1], snake_block, snake_block])

        pygame.display.update()
        
        clock.tick(snake_speed)

        # ამოწმებს თუ გველი დაეჯახა კედელს
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_over = False  # დაასრულეთ თამაშის ციკლი

if question == "play":
    
    game_loop()
elif question == "setting":
    print("""
controls: LEFT, RIGHT, DOWN, UP |
screen size: 800px/600px        |
snake color: GREEN              |
food color: RED                 |
Rules of the game:{
You win the game if the snake touches the wall.
If the snake's points reach 100, the game is over pending a win
And "YOU WIN" text will be displayed on the screen.
good luck!
    }
        """)