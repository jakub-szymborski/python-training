# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:26:14 2023

@author: Kuba
Write a findAndReplace() function that has three parameters: text is the string with text to
be replaced, oldText is the text to be replaced, and newText is the replacement text. Keep in mind
that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in
'MY DOG JONESY' won’t be replaced.
"""

def findAndReplace(text, oldText, newText):
    replacedText = ''

    i = 0
    while i < len(text):
        
        if text[i : i + len(oldText)] == oldText:
            replacedText += newText
            i += len(oldText) 
        else:
            replacedText += text[i]
            i += 1
            
    return replacedText



assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'