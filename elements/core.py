import pygame
from elements.Character import *
from elements.tools import *

def checkVoid(target):
    if (len(target) == 0):
        return (False)
    else:
        return (True)

def doNothing(target):
    return (True)

class Core:
    def __init__(self):
        pygame.init()
        self.tools = Compare()
        self.gameDisplay = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("SCRAME")
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.gray = (100, 100, 100)
        self.warrior = 0
        self.input_name = ""
        self.unitList = []
        self.isScreenSaver = False

    def text_objects(self, text, font, color=(255, 255, 255)):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def click_button(self, msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, ac,(x,y,w,h))

            if click[0] == 1 and action != None:
                self.isScreenSaver = True
                action()
        else:
            pygame.draw.rect(self.gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("comicsansms", int((w + h) / 4))
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.gameDisplay.blit(textSurf, textRect)

    def getScreen(self):
        if (self.isScreenSaver):
            pygame.image.save(self.gameDisplay, "images/save.png")
            self.screenSaver = pygame.image.load("images/save.png")
            self.isScreenSaver = False
            exit(0)

    def drawBoxes(self):
        zeroX = 1025
        zeroY = 110
        size = 90

        X = [size * i + zeroX for i in range(11)]
        Y = [size * i + zeroY for i in range(0, 10)]

        for x in range(0, 10):
            self.drawText(str(x), zeroX + 50 + x * size, zeroY - 50, 50)
            self.drawText(str(x), zeroX - 50, zeroY + 50 + x * size, 50)

        for x in X:
            for y in Y:
                pygame.draw.rect(self.gameDisplay, self.black, (x, y, 80, 80))
                self.drawText(str(int((x - 1025)/90)) + "/" + str(int((y - 110) / 90)), x + 45, y + 45, 20)

    def askMe(self, msg, x, y, w, h, col1, col2, condition=checkVoid, errorMsg="Error"):
        loop = True
        active = True
        text = ""
        idx = 0
        error = False

        while loop:
            self.gameDisplay.fill(self.black)
            pygame.draw.rect(self.gameDisplay, self.gray, (0, 0, 900, 1080))
            pygame.draw.rect(self.gameDisplay, self.gray, (1020, 0, 900, 1080))
            self.drawBoxes()
            self.drawUnits()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            idx = len(text) * int(x / 10)

            if active:
                pygame.draw.rect(self.gameDisplay, col2,(x ,y,w + idx,h))
            else:
                pygame.draw.rect(self.gameDisplay, col1,(x ,y,w + idx,h))
            if error:
                self.drawText(errorMsg, 500, 350, 50)
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                if click[0] == 1 and active:
                    active = False
                elif click[0] == 1 and not active:
                    active = True
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    loop = False
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE and active):
                        text = text[:-1]
                    elif (event.key == pygame.K_RETURN):
                        if (condition(text)):
                            return text
                        else:
                            error = True
                    else:
                        if active:
                            text += event.unicode
            smallText = pygame.font.SysFont("comicsansms", int((w + h) / 4))
            textSurf, textRect = self.text_objects(msg + text, smallText)
            textRect.center = ( (x+(((w + idx)/2)), (y+(h/2))))
            self.gameDisplay.blit(textSurf, textRect)
            pygame.display.update()
            self.clock.tick(15)

    def createMage(self):
        name = self.askMe("name: ", 500, 500, 600, 100, self.green, self.red)
        x = self.askMe("x (0 ~ 9): ", 500, 500, 600, 100, self.green, self.red, self.tools.checkPos, "X in 0-9")
        y = self.askMe("y (0 ~ 9): ", 500, 500, 600, 100, self.green, self.red, self.tools.checkPos, "Y in 0-9")
        hp = self.askMe("hp: ", 500, 500, 600, 100, self.green, self.red, self.tools.checkNum, "Hp is a number")
        mp = self.askMe("mp: ", 500, 500, 600, 100, self.green, self.red, self.tools.checkNum, "Mp is a number")
        unit = Mage(name, int(x), int(y), int(hp), int(mp))
        self.unitList.append([False, unit])
        self.input_name = ""

    def createWarrior(self):
        name = self.askMe("name: ", 500, 500, 600, 100, self.green, self.red)
        x = self.askMe("x (0 ~ 9): ", 500, 500, 600, 100, self.green, self.red, self.tools.checkPos, "X in 0-9")
        y = self.askMe("y (0 ~ 9): ", 500, 500, 600, 100, self.green, self.red, self.tools.checkPos, "Y in 0-9")
        hp = self.askMe("hp: ", 500, 500, 600, 100, self.green, self.red, self.tools.checkNum, "Hp is a number")
        mp = self.askMe("mp: ", 500, 500, 600, 100, self.green, self.red, self.tools.checkNum, "Mp is a number")
        unit = Warrior(name, int(x), int(y), int(hp), int(mp))
        self.unitList.append([False, unit])
        self.input_name = ""

    def drawText(self, msg, x, y, size):
        font = pygame.font.Font("font/font.ttf", size)
        textSurf, textRect = self.text_objects(msg, font)
        textRect.center = ((x, y))
        self.gameDisplay.blit(textSurf, textRect)

    def drawUnits(self):
        for unit in self.unitList:
            if unit[0] == False:
                self.gameDisplay.blit(unit[1].img, (unit[1].x, unit[1].y))

    def mouseToUnit(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for unit in self.unitList:
            if unit[1].x + 50 > mouse[0] > unit[1].x and unit[1].y + 50 > mouse[1] > unit[1].y:
                self.drawText("name: " + unit[1].name, unit[1].x + 50, unit[1].y + 60, 20)
                self.drawText("hp: " + str(unit[1].hp), unit[1].x + 50, unit[1].y + 80, 20)
                self.drawText("mp: " + str(unit[1].mp), unit[1].x + 50, unit[1].y + 100, 20)
                if (click[0] == 1):
                    x = self.askMe("x: ", 50, 800, 100, 50, self.black, self.green, doNothing)
                    y = self.askMe("y: ", 50, 800, 100, 50, self.black, self.green, doNothing)
                    hp = self.askMe("hp: ", 50, 800, 100, 50, self.black, self.green, doNothing)
                    mp = self.askMe("mp: ", 50, 800, 100, 50, self.black, self.green, doNothing)
                    unit[1].changeX(x)
                    unit[1].changeY(y)
                    unit[1].changeMp(mp)
                    unit[1].changeHp(hp)
    def start_game(self):
        loop = True

        while loop:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    loop = False
            self.gameDisplay.fill(self.black)
            pygame.draw.rect(self.gameDisplay, self.gray, (0, 0, 900, 1080))
            pygame.draw.rect(self.gameDisplay, self.gray, (1020, 0, 900, 1080))
            self.click_button("Warrior", 350, 100, 100, 50, self.red, self.blue, self.createWarrior)
            self.click_button("Mage", 350, 200, 100, 50, self.red, self.blue, self.createMage)
            self.drawBoxes()
            self.drawUnits()
            self.mouseToUnit()
            pygame.display.update()
            self.clock.tick(15)

    def main_menu(self):
        loop = True

        while loop:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    loop = False
            self.gameDisplay.fill(self.black)
            self.click_button("Start", 920, 500, 200, 100, self.red, self.green, self.start_game)
            pygame.display.update()
            self.clock.tick(20)
