# GAANA.COM
# DUBLEE LINKED LIST

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
    """def update(self, track="", artist="", duration=0.0):
        self.track = track
        self.artist = artist
        self.duration = duration"""

    # To show the object data
    def show(self):
        print("================")
        print(self.track, "[", self.duration, "mins]")
        print(self.artist)
        print("================")


class PlayList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("playlist created...")

    def append(self, song):
        self.size +=1
        if self.head is None:
            self.head = song
            self.tail = song
        else:
            self.tail.next_song = song
            song.previous_song = self.tail
            self.tail = song


play_list = PlayList()
print("play_list:", play_list, "Data:", vars(play_list))

song1 = Song(track="Kesariya", artist="Pritam, Arijit Singh", duration= 4.3 )
print("song1:", song1, "Data:", vars(song1))

song2 = Song(track="Peaches", artist="Diljit", duration=3.5)
print("song2:", song2, "Data:", vars(song2))

song3 = Song(track="Left and Right", artist="Charlie", duration=2.7)
print("song3:", song3, "Data:", vars(song3))

song4 = Song(track="Fitoor", artist="Arijit Singh", duration=5.7)
print("song4:", song4, "Data:", vars(song4))

song5 = Song(track="SYL", artist="Sidhu MW", duration=3.5)
print("song5:", song5, "Data:", vars(song5))

print("after adding songs")

play_list.append(song=song1)
play_list.append(song=song2)
play_list.append(song=song3)
play_list.append(song=song4)
play_list.append(song=song5)

print("song1:", song1, "Data:", vars(song1))
print("song2:", song2, "Data:", vars(song2))
print("song3:", song3, "Data:", vars(song3))
print("song4:", song4, "Data:", vars(song4))
print("song5:", song5, "Data:", vars(song5))


"""
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
        """






