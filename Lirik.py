import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Suki yo", 0.12),
        ("Ima Anata ni omoi nosete", 0.15),
        ("Hora sunao ni naru no Watashi", 0.15),
        ("Kono saki motto soba ni ite mo ii ka na?", 0.14),
        ("Koi to koi ga kasanatte", 0.13),
        ("Suki yo", 0.1),
    ]
    delays = [0.2, 1.1, 4.8, 9.5, 15.5, 19.0, 20.1]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()