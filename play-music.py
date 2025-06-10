import vlc
import time
import sys
import tty
import termios

# listen to keyboardinput without Enter key
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

filePath = "easyLover.mp3"
player = vlc.MediaPlayer(filePath)

print("Tryck på '1' för att spela upp låten 'Easy Lover'")

while True:
    keyPressed = getch()
    if keyPressed == "1":
        player.play()
        time.sleep(1)
        songLength_ms = player.get_length()
        songLength_s = songLength_ms / 1000 if songLength_ms > 0 else 10
        print("Playing song...")
        print("Tryck 2 för att stanna låten ")

    elif keyPressed == "2":
        if player.is_playing():
            player.stop()
            print("Song stopped.")
            break
