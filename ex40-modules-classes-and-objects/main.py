import stuff

# to get key apple from dictionary
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# module style
stuff.apple()
print(stuff.tangerine)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print("I AM CLASSY APPLES!")


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    
    def repeat(self, num):
        for i in range (0,num):
            print(self.lyrics)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)

happy_bday = Song(["Happy birthday to you", 
                   "I don't want to get sued", 
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", "With pockets full of shells"])

lyrics = ["Humpty dumpty sat on the wall", 
 "Humpty dumpty had a great fall", 
 "..."]
# passing a list of strings as the lyrics
humpty_dumpty = Song(lyrics)



happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

humpty_dumpty.sing_me_a_song()

bulls_on_parade.repeat(4)