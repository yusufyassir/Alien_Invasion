import pygame
from pygame import mixer

class Music:
    def __init__(self, ai_game):
        """initialize music settings"""
        mixer.init()
        mixer.music.load('music/Space.wav')

    def play(self):
        """play music"""
        mixer.music.play()

    def pause(self):
        """pause music"""
        mixer.music.pause()