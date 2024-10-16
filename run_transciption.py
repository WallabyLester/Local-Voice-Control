import sounddevice as sd
from rt_audio_to_text import RTAudioToText
import pygame
from pygame.locals import *


class GameWindow:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.scr = pygame.display.set_mode((w, h))

        pygame.font.init()
        self.my_font = pygame.font.SysFont('roboto', 50)
        self.small_font = pygame.font.SysFont('roboto', 45)
        self.text_surface_space = self.my_font.render('Press <Space> to start recording', False, (200, 200, 200))
        self.text_surface_recording = self.my_font.render('RECORDING', False, (200, 200, 200))
        self.text_surface_label = self.small_font.render('Output: ', False, (200, 200, 200))
        self.text_surface_output = self.small_font.render('No output yet', False, (200, 200, 200))
        self.clock = pygame.time.Clock()
        self.recording_flag = False

    def update_display(self):
        if self.recording_flag:
            self.scr.fill((0,0,0))
            self.scr.blit(self.text_surface_recording, ((w/2)-100, h/2))
        else: 
            self.scr.fill((0,0,0))
            self.scr.blit(self.text_surface_space, ((w/2-250), h/2))
            self.scr.blit(self.text_surface_label, ((0), 25))
            self.scr.blit(self.text_surface_output, ((120), 25))

        pygame.display.flip()


if __name__=="__main__":
    fps = 35
    exitFlag = False
    w, h = 1000, 200
    game_window = GameWindow(w, h)
    rt_model = RTAudioToText()
    fs = 16000
    duration = 2    # chunk of audio in sec

    while not exitFlag:
        events = pygame.event.get()
        for event in events:                    
            if event.type == pygame.KEYDOWN:
                mods = pygame.key.get_mods()
                if event.key == pygame.K_SPACE:
                    game_window.recording_flag = True
                
                elif event.key == pygame.K_ESCAPE:
                    exitFlag = True
        
        game_window.update_display()

        if game_window.recording_flag:
            with sd.InputStream(callback=rt_model.recording_callback, dtype='int16', channels=1, samplerate=fs, blocksize=fs*duration):
                print("Recording...")
                sd.sleep(duration * 1000) # in ms
        
            game_window.text_surface_output = game_window.small_font.render(rt_model.output, False, (200, 200, 200))
            game_window.recording_flag = False

        game_window.clock.tick(fps)

    pygame.display.quit()
    pygame.quit()
