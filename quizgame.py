import pygame
import random
import time

pygame.init()

# Set the dimensions of the window
width = 800
height = 600

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quiz Game")

# Set the font for the questions and answers
font = pygame.font.SysFont(None, 30)

# Set the questions and answers
questions = ["What is the capital of France?", "What is 2+2?", "What is the largest ocean?", "What is the currency of Japan?", "What is the highest mountain in the world?"]
answers = ["Paris", "4", "Pacific", "Yen", "Mount Everest"]

# Set the score
score = 0

# Set the timer
timer = 30

# Set the clock
clock = pygame.time.Clock()

# Set the game loop
game_over = False

# Define the function for drawing text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, False, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Define the function for displaying the questions and answers
def display_question(question, answers):
    global score
    global game_over

    # Shuffle the answers
    random.shuffle(answers)

    # Display the question
    draw_text(question, font, black, win, width // 2, height // 2 - 100)

    # Display the answers
    for i in range(len(answers)):
        draw_text(str(i + 1) + ". " + answers[i], font, black, win, width // 2, height // 2 - 50 + i * 50)

    # Check for the user's answer
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    user_answer = answers[int(event.unicode) - 1]
                    if user_answer == answers[0]:
                        score += 1
                    return  # exit the function and wait for the next question

        # check if the timer is up
        if timer == 0:
            game_over = True
            return  # exit the function and end the game loop

        # update the screen
        pygame.display.update()
        clock.tick(60)

# Start the game loop
while not game_over:
    # Set the background color
    win.fill(white)

    # Display the score
    draw_text("Score: " + str(score), font, black, win, 70, 20)

    # Display the timer
    draw_text("Time: " + str(timer), font, black, win, width-70, 20)

    # Decrease the timer by one second
    if timer > 0:
        timer -= 1

    # Check if the timer is over
    if timer == 0:
        game_over = True

    # Display the next question
    if not game_over:
        display_question(random.choice(questions), answers)

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Display the final score
win.fill(white)
draw_text("Final Score: " + str(score), font, black, win, width//2, height//2)
pygame.display.update()

# Wait for 3 seconds before closing the window
time.sleep(3)
pygame.quit()
