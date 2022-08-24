# GAANA.COM

class Song:

    # Add attributes to the Object
    # With default values
    def __init__(self, track="", artist="", duration=""):
        self.track = track
        self.artist = artist
        self.duration = duration
        self.next_song= None
        self.previous_song = None

    # To update the Object Data
    def update(self, track="", artist="", duration=0.0):
        self.track = track
        self.artist = artist
        self.duration = duration

    # To show the object data
    def show(self):
        print("================")
        print(self.track, "[", self.duration, "mins]")
        print(self.artist)
        print("================")


song1 = Song(track="Kesariya", artist="Pritam, Arijit Singh", duration=4.3)
song2 = Song(track="Peaches", artist="Diljit", duration=3.5)
song3 = Song(track="Left and Right", artist="Charlie", duration=2.7)
song4 = Song(track="Fitoor", artist="Arijit Singh", duration=5.7)
song5 = Song(track="SYL", artist="Sidhu MW", duration=3.5)


print(song1, song1.__dict__)
print(song1, song1.__dict__)
print(song1, song1.__dict__)
print(song1, song1.__dict__)
print(song1, song1.__dict__)


song1.next_song = song2
song2.next_song = song3
song3.next_song = song4
song4.next_song = song5
song5.next_song = song1

song1.previous_song = song5
song2.previous_song = song1
song3.previous_song = song2
song4.previous_song = song3
song5.previous_song = song4

print("ITERATING FORWARD")

temp = song1
while True:
    temp.show()
    temp = temp.next_song

    if temp.next_song == song1:
        temp.show()
        break

print("iterating backward")

temp = song5
while True:

    temp.show()
    temp = temp.previous_song


    if temp.previous_song == song5:
        temp.show()
        break

