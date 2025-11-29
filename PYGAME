import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("X O Game")

# decide the background
WHITE = (0, 255, 255)
BLACK = (0, 0, 0)

# showing the game display size 
size = 200

# design the board
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

# decide the player who starts first
player = "X"

# decide the font of text
font = pygame.font.Font(None, 100)

# run continuously
run = True

while run:
    screen.fill(WHITE)
    
    # Draw grid lines
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 5) 
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 5)
    
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 5)

    # Draw X and O
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                # FIX 1: Coordinates must be inside one tuple (x, y)
                screen.blit(text, (col * size + 70, row * size + 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200

            if board[row][col] == "":
                # FIX 2: Use '=' for assignment, not '=='
                board[row][col] = player
                
                if player == "X":
                    player = "O"
                else:
                    player = "X"

    # FIX 3: Fixed typo 'pygaem' to 'pygame'
    pygame.display.update()

pygame.quit()