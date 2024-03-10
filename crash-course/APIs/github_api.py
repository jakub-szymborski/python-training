# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:22:28 2024

@author: Kuba
"""

import requests
import pygal 


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code) # 200 - succesfull 

# store API response in a variable 
response_dict = r.json()
if response_dict['incomplete_results']:
    print('Results incomplete')

print(response_dict.keys())

print('Total repositories:', response_dict['total_count'])

repo_dicts = response_dict['items']

print('Repos returned: ',len(repo_dicts))

# first repo: 
first_repo = repo_dicts[0]
print('\nKeys:', len(first_repo))
for key in sorted(first_repo.keys()):
    print(key)
    
def print_repo_details(repo_dict):
    print('\nName: ', repo_dict['name'])
    print('\nOwner: ', repo_dict['owner']['login'])
    print('\nStars: ', repo_dict['stargazers_count'])
    print('\nRepo url: ', repo_dict['html_url'])
    print('\nCreated: ', repo_dict['created_at'])
    print('\nUpdated: ', repo_dict['updated_at'])
    print('\nDescription: ', repo_dict['description'])
    
print_repo_details(first_repo)

github_limit = 'https://api.github.com/rate_limit'

def check_api_limit(adress):
    limit_req = requests.get(adress)
    limit_dict = limit_req.json()
    print('\nPrimary API limit remaining: ', limit_dict['rate']['remaining'])
    print('\nSearch API limit remaining: ',
          limit_dict['resources']['search']['remaining'])

check_api_limit(github_limit)

# extracting names and star counts: 
names, plot_dicts = [], []
for repo in repo_dicts: 
    plot_dict = {
    'value': repo['stargazers_count'],
    'label': repo['name'],
    'xlink': repo['html_url']
    }
    plot_dicts.append(plot_dict)
    
# pygal config: 

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False 
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False 
my_config.width = 1000



#pygal chart
chart = pygal.Bar(my_config)
chart.title = 'Most Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')

"""
# extracting names and star counts: 
names, stars = [], []
for repo in repo_dicts: 
    names.append(repo['name'])
    stars.append(repo['stargazers_count'])


"""