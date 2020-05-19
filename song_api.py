from pygame import mixer
import os


def play_this(string):
    mixer.init()
    mixer.music.load(string)
    mixer.music.play()
    print("song playing : ",string)
    while True:
        k = input()
        if k == "stop":
            mixer.music.stop()
            return
        if k == "pause":
            print("\t paused. Enter play to inpause")
            mixer.music.pause()

        if k == "play":
            print("\t unpaused")
            mixer.music.unpause()



print(os.getcwd())
os.chdir("//home//itachi//Music")



while True:
    list_songs = os.listdir("//home//itachi//Music")
    cnt_song = 0
    for item in list_songs:
        print(cnt_song,"-", item)
        cnt_song += 1

    to_pl=int(input("song number: "))
    while to_pl >= 0 and to_pl <= cnt_song:
        play_this(list_songs[to_pl])
        cnt_song=0
    else:
        print("out of range")






# play_this()