'''Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the  dictionaries are storing the album information correctly. 
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.'''

def make_album(artist,title, num_song=None) -> dict:
    
    album:dict = {"artist":artist, "album":title}
    if num_song is None:
        num_song = "Unknown"
        album["Num_songs"] = num_song
        return album
    else:
        album["Num_songs"] = num_song
    return album
album1 = make_album("Harry","The best")
album2 = make_album("The beatls","Roks")
album3 = make_album("Shakira","World cup",12)

print(album1)
print(album2)
print(album3)

    