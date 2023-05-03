import pygame
from pygame import mixer

class Music:
    def __init__(self, ai_game):
        """initialize music settings"""
        mixer.init()
        mixer.music.load('music/Space.wav')

    def play_bg(self):
        """play background music"""
        mixer.music.play(-1)

    def pause_bg(self):
        """pause background music"""
        mixer.music.pause()

    def play_bl(self):
        """play blaster sound"""
        blsater_fx = mixer.Sound("music/blaster.wav")
        mixer.Sound.set_volume(blsater_fx, .05)
        mixer.Sound.play(blsater_fx)

    def play_ex(self):
        """play explosion"""
        explosion_fx = mixer.Sound("music/explosion.wav")
        mixer.Sound.set_volume(explosion_fx, .05)
        mixer.Sound.play(explosion_fx)