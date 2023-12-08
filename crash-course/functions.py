# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:31:31 2023

@author: Kuba
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.

8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.

8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""


def cityCountry(cityName,countryName): 
    return print(cityName + ', ' +countryName)
    
cityCountry('Santiago','Chile')


    
def makeAlbum(artistName, albumTitle, tracksNumber = ''):
    album = {'artist': artistName, 'album': albumTitle}
    if tracksNumber: 
        album['tracksNumber'] = tracksNumber
    return album 
    
        
makeAlbum('U2', 'costam')

makeAlbum('U2', 'costam', 17)
