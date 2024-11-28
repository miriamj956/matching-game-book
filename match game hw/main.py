import pygame   
pygame.init()

screen = pygame.display.set_mode([600,600])

screen.fill("violet")

cover1 = pygame.image.load("kyoshi.jpg")
cover1 = pygame.transform.scale(cover1, (130,100))
screen.blit(cover1, (80,70))

cover2 = pygame.image.load("seven.jpg")
cover2 = pygame.transform.scale(cover2, (100,120))
screen.blit(cover2, (80, 230))

cover3 = pygame.image.load("sugar.jpg")
cover3 = pygame.transform.scale(cover3, (90, 130))
screen.blit(cover3, (80, 400))

font = pygame.font.SysFont("Comic Sans", 18)

text1 = font.render("Tomiyaki Kagisora", True, "red")
screen.blit(text1, (400, 100))

text2 = font.render("F. C. Yee", True, "blue")
screen.blit(text2, (400, 260))

text3 = font.render("Taylor Jenkins Reid", True, "green")
screen.blit(text3, (400, 460))

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, "purple", pos, 10, 0)
        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.circle(screen, "purple", pos2, 10, 0)
            pygame.draw.line(screen, "purple", pos, pos2, 5)


