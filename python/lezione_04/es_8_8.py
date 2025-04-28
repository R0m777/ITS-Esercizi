'''Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, 
call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.'''

def make_album(artist:str,title:str, num_song=None) -> dict:
   album:dict = {"artist":artist, "album":title}
   if num_song is None:
        num_song = "Unknown"
        album["Num_songs"] = num_song
        return album
   else:
        album["Num_songs"] = num_song
   return album
 
while True:
        artist = str(input("inserisci un nome: "))
        title = str(input("inserisci un titolo: "))
        break

album1 = make_album("Harry","The best")
album2 = make_album("The beatls","Roks")
album3 = make_album("Shakira","World cup",12)
album4 = make_album(artist,title)

print(album1)
print(album2)
print(album3)
print(album4)