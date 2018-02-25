import pygame
import random
import os
import time

pygame.init()
screen = pygame.display.set_mode((800, 640))
person = pygame.image.load('person.png')
house = pygame.image.load('house.png')
clock = pygame.time.Clock()
pygame.display.set_caption('People counting game')

myfont = pygame.font.SysFont('comicsansms', 80)
smallfont = pygame.font.SysFont('comicsansms', 30)


ingoing_persons = 5
outgoing_persons = 3

def animate_person_going_inside_house(speed):
    
    running = True
    x = -200
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False

        x += speed
        screen.fill((255, 255, 255)) # fill the screen
        screen.blit(person, (int(x), 340))
        screen.blit(house, (200, 260))
        if x > 300:
            return
        pygame.display.update() # Just do one thing, update/flip.

        clock.tick(40) # This call will regulate your FPS (to be 40 or less)

def animate_person_going_outside_house(speed):
    
    running = True
    x = 300
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False

        x += speed
        screen.fill((255, 255, 255)) # fill the screen
        screen.blit(person, (int(x), 340))
        screen.blit(house, (200, 260))
        if x > 900:
            return
        pygame.display.update() # Just do one thing, update/flip.

        clock.tick(40) # This call will regulate your FPS (to be 40 or less)

def animate_all_people(ingoing, outgoing, difficulty):
    result = ingoing - outgoing
    ingoing_so_far = 0
    outgoing_so_far = 0
    people_inside = 0
    while True:
        if random.choice( (0, 1) ):
            if ingoing_so_far < ingoing:
                people_inside += 1
                animate_person_going_inside_house(difficulty)
                ingoing_so_far += 1
        else:
            if outgoing_so_far < outgoing and people_inside > 0: # People can only exit if people are inside!
                people_inside -= 1
                animate_person_going_outside_house(difficulty)
                outgoing_so_far += 1
        if ingoing_so_far == ingoing and outgoing_so_far == outgoing:
            break

    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_0 and people_inside == 0) or \
               (event.key == pygame.K_1 and people_inside == 1) or \
               (event.key == pygame.K_2 and people_inside == 2) or \
               (event.key == pygame.K_3 and people_inside == 3) or \
               (event.key == pygame.K_4 and people_inside == 4) or \
               (event.key == pygame.K_5 and people_inside == 5) or \
               (event.key == pygame.K_6 and people_inside == 6) or \
               (event.key == pygame.K_7 and people_inside == 7) or \
               (event.key == pygame.K_8 and people_inside == 8) or \
               (event.key == pygame.K_9 and people_inside == 9):
                for _ in range(40 * 2):
                    text = myfont.render('Correct! {}!'.format(str(result)), False, (255, 0, 0))
                    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))
                    pygame.display.flip()
                return 1
            
            else:
                for _ in range(40 * 2):
                    text = myfont.render('Wrong!, It was {}'.format(str(result)), False, (255, 0, 0))
                    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))
                    pygame.display.flip()
                return 0

def random_if_condition(minmax, condition):
    while True:
        r = random.randint(*minmax)
        if condition(r):
            return r

"""
def play_game(difficulty):
    ingoing, outgoing = random.randint(0, 9), random.randint(0, 9)
    animate_all_people(ingoing, outgoing, difficulty)
"""

def play_match(rounds, speed, max_people):
    while True:
        text = smallfont.render("Count the people inside the house.", False, (255, 0, 0))
        screen.blit(text,
        (380 - text.get_width() // 2, 140 - text.get_height() // 2))

        text = smallfont.render("When no more people are moving", False, (255, 0, 0))
        screen.blit(text,
        (380 - text.get_width() // 2, 240 - text.get_height() // 2))
        
        text = smallfont.render("press the number on the keyboard.", False, (255, 0, 0))
        screen.blit(text,
        (380 - text.get_width() // 2, 340 - text.get_height() // 2))

        text = smallfont.render("Press any key to start playing.", False, (255, 0, 0))
        screen.blit(text,
        (380 - text.get_width() // 2, 440 - text.get_height() // 2))
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
            break
        pygame.display.flip()


    points = 0
    for _ in range(rounds):
        ingoing = random.randint(0, max_people)        # Careful to avoid more outgoing than ingoing
        points += animate_all_people(ingoing , random_if_condition( (0, max_people), lambda r: r <= ingoing), speed)
    for _ in range(40 * 5): # 5 seconds
        text = myfont.render("You got {}/{} right".format(points, rounds), False, (255, 0, 0))
        screen.blit(text,
        (320 - text.get_width() // 2, 140 - text.get_height() // 2))

        pygame.display.flip()
    
    
#animate_all_people(random.randint(0, 9) , random.randint(0, 9), 30)


if __name__ == "__main__":
    play_match(rounds = 3, speed = 15, max_people = 6)
