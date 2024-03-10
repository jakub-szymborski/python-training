# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:16:47 2024

@author: Kuba
"""

import requests 

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)
sub_ids = r.json()

top_sub_id = sub_ids[0] 

top_sub_url = 'https://hacker-news.firebaseio.com/v0/item/' +\
    str(top_sub_id) + '.json'

top_sub_r = requests.get(top_sub_url)
print('Status code:', top_sub_r.status_code)
top_sub_dict = top_sub_r.json()

def get_one_story(story_id):
    story_url = 'https://hacker-news.firebaseio.com/v0/item/' +\
        str(story_id) + '.json'
    story_r = requests.get(story_url)
    print('Status code for id {0}: {1}'.format(story_id, story_r.status_code))
    response_dict = story_r.json()
    story_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(story_id),
        'comments': response_dict.get('descendants', 0) #dict.get to handle case of no comments, then 0 will be returned
        }
    return story_dict

def print_story(a_dict):
    print('\nTitle:',a_dict['title'])
    print('\nLink:',a_dict['link'])
    print('\nComments:',a_dict['comments'])
    

get_one_story(sub_ids[1])
print_story(get_one_story(sub_ids[1]))

# print top 30

for story in sub_ids[:30]:
    print_story(get_one_story(story))