import pygame, sys
import winning_movesBot as wmb
from collections import Counter
from random import choice
#add player vs player 
class Board:
    """Tictactoe board and related methods"""
    def __init__(self):
        self.board = board = {'tL': "", 'tM': "", 'tR': "",
                              'mL': "", 'mM': "", 'mR': "",
                              'bL': "", 'bM': "", 'bR': ""}
        self.keys = board_keys = ['tL', 'tM', 'tR',
                                  'mL','mM', 'mR',
                                  'bL', 'bM', 'bR']
        self.background = pygame.image.load('wafflebg.jpg')
    
    def win_check(self):
        """checks if there's a win"""
        x, y, z = 0, 1, 2
        for i in range(3):
            row = self.board[self.keys[x]] + self.board[self.keys[y]] + self.board[self.keys[z]]
            if row == "XXX" or row == "OOO": return True
            x, y, z = x + 3, y + 3, z + 3
        x, y, z = 0, 3, 6
        for i in range(3):
            row = self.board[self.keys[x]] + self.board[self.keys[y]] + self.board[self.keys[z]]
            if row == "XXX" or row == "OOO": return True
            x, y, z = x + 1, y + 1, z + 1
        x, y, z = 0, 4 , 8
        for i in range(2):
            row = self.board[self.keys[x]] + self.board[self.keys[y]] + self.board[self.keys[z]]
            if row == "XXX" or row == "OOO": return True
            x, z = x + 2, z - 2
    
    def draw_check(self):
        """checks if a draw has occurred"""
        has_content = 0
        for value in self.board.values():
            if value: has_content += 1
        if has_content == 9: return True
        
    def update_board(self, display, x_symbol, o_symbol):
        """displays an update board"""
        for index, content in enumerate(self.board.values()):
            if content == 'X':
                display.blit(x_symbol, rects[index])
            elif content == 'O':
                display.blit(o_symbol, rects[index])
        pygame.display.flip()

class Bot:
    """logic of bot and related methods"""
    def __init__(self, board, keys):
        self.winmoves = wmb.someDict
        self.board = board
        self.keys = keys
    
    def turn_text(self, display, font, board):
        """Delays bot move and displays txt that bot is moving"""
        dots = 0
        while dots <= 3:
            text_surf = font.render("Bot moves" + "."*int(dots), False, 'Purple', 'Pink')
            text_rect = text_surf.get_rect(center = (350, 250))
            display.blit(text_surf, text_rect)
            board.update_board(display, rezex, rezeo) #accidentaly causes cool lightup effect
            dots += 0.005
            
    def bot_winmove(self):
        """logic for making/blocking the winning move"""
        x, y, check = 0, 0, False 
        for i in range(9):
            if self.move_check(self.keys[i]):
                continue
            for o in range(i + 1, 9):
                if self.move_check(self.keys[o]) or self.board[self.keys[o]] != self.board[self.keys[i]]:
                    continue
                if self.keys[i] + self.keys[o] in self.winmoves.keys():
                    if self.move_check(self.winmoves[self.keys[i] + self.keys[o]]) != True:
                        continue
                    if self.board[self.keys[i]] + self.board[self.keys[o]] == "XX": #so OO's are prioritized
                        x, y, check = i, o, True
                        continue
                    self.board[self.winmoves[self.keys[i] + self.keys[o]]] = 'O'
                    return True
        if check:
            self.board[self.winmoves[self.keys[x] + self.keys[y]]] = 'O'
            return True
    
    def block_strat(self):
        """Blocks strategy that allows player to win"""
        if Counter(self.board.values())['X'] != 2:
            return False
        indices, values, x = [], list(self.board.values()), 0
        for i in values:
            if i == 'X':
                indices.append(x)
            x += 1
        sumz = indices[0] + indices[1]
        if sumz == 8 and indices[0] % 2 == 0:
            self.board[self.keys[choice([1, 7])]] = 'O'
            print("I worked")
            return True
        elif (indices[0] * indices[1]) % 2 != 0 and sumz != 8:
            sumz -= 4
            self.board[self.keys[sumz]] = 'O'
            print('I worked')
            return True
        return False
    
    def corners_out(self):
        """finalize draw when corners are filled"""
        for key in self.keys:
            if self.move_check(key):
                self.board[key] = 'O'
                return True

    def bot_move(self):
        """main bot loop"""
        for corner, i in enumerate(set(['0', '8', '6', '2'])):
            if self.bot_winmove(): break
            elif self.move_check('mM'):
                self.board['mM'] = 'O'
                break
            elif self.block_strat(): break
            elif self.move_check(self.keys[int(corner)]):
                self.board[self.keys[int(corner)]] = 'O'
                break
            elif i == 4:
                self.corners_out()
                break
            
    def move_check(self, move):
        """checks if tile corresponding to move is occupied"""
        for key in self.keys:
            if key == move:
                if self.board[key]:
                    return False #if not empty
                return True #if empty
                
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((750,750))
pygame.display.set_caption("Reze Tic-Tac-Toe")
#assets
pygame.mixer.music.load('Slow Summer Eve.mp3')
pygame.mixer.music.play(-1)
rezex = pygame.image.load('RezeX.png')
rezex = pygame.transform.scale(rezex, (140,140))
rezeo = pygame.image.load('RezeO.png')
rezeo = pygame.transform.scale(rezeo, (140,140))
font = pygame.font.Font(size=50)
win_text = font.render("Bot wins!", False, 'Purple', 'Pink')
draw_text = font.render("Draw!", False, 'Purple', 'Pink')
text_rect = win_text.get_rect(center = (350, 250))
#a list of 9 rects, pre-made using mouse inputs
rects = [pygame.Rect(71, 86, 131, 131), pygame.Rect(272, 91, 161, 125), pygame.Rect(510, 86, 122, 125),
         pygame.Rect(74, 295, 133, 143), pygame.Rect(275, 294, 150, 133), pygame.Rect(518, 296, 120, 123),
         pygame.Rect(75, 512, 139, 150), pygame.Rect(290, 512, 143, 146), pygame.Rect(527, 512, 119, 138)]

b = Board()
bot = Bot(b.board, b.keys)
turn_flag = True
game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #player input
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for rect in rects:
                if rect.collidepoint(event.pos):
                    if b.board[b.keys[rects.index(rect)]]: continue
                    if turn_flag:
                        b.board[b.keys[rects.index(rect)]] = 'X'
                        turn_flag = False
                        break
            if turn_flag != True:
                bot.turn_text(screen, font, b)
                bot.bot_move()
                turn_flag = True
                
    screen.blit(b.background)
    if b.win_check():
        screen.blit(win_text, text_rect)
        game_on = False
    if b.draw_check():
        screen.blit(draw_text, text_rect)
        game_on = False
    b.update_board(screen, rezex, rezeo)
    clock.tick(60)
    
while True: #so game doesnt crash when game ends
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()