from pygame import mixer
from datetime import datetime
from time import time

# Function to play the music and stop it when the correct word is input by the user
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        word = input()
        if word == stopper:
            mixer.music.stop()
            break


# Logging the performed task in txt file
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == "__main__":
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40 * 60
    eyessecs = 30 * 100
    exersecs = 45 * 150

    while True:

        # Initiate drinking water task
        if time() - init_water > watersecs:
            print("Water Drinking Time. Enter 'water' to stop the alarm.")
            musiconloop("paani.mp3", "water")
            init_water = time()
            log_now("Drank water at")

        # Initiate eyes exercise task
        if time() - init_eyes > eyessecs:
            print("Eyes Exercise Time. Enter 'eyes' to stop the alarm.")
            musiconloop("eyes.mp3", "eyes")
            init_eyes = time()
            log_now("Eyes relaxed at")

        #  Initiate physical exercise task
        if time() - init_exercise > exersecs:
            print("Physical Activity Time. Enter 'exer' to stop the alarm.")
            musiconloop("exercise.mp3", "exer")
            init_exercise = time()
            log_now("Pysical exercise at")
