import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._dispalying_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self._dispalying_surf.fill((255, 255, 255))
        self._running = True
        pygame.font.init()
        self._font = pygame.font.SysFont('Comic Sans MS', 30)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        pass

    def on_render(self):
        text = self._font.render('ULTIMATE SUDOKU', False, (0, 0, 0))
        textsurface = text.get_rect(center=(self.weight/2,self.height/2))
        self._dispalying_surf.blit(text, textsurface)
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.update()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
        
            