# Importing libraries

import requests

URL = "https://www.githubstatus.com/"
page = requests.get(URL)

words_to_search = 'All Systems Operational'

if(words_to_search in page.text):
    print('Text found!! Yay')
else:
    #print('Text NOT found!')
    raise Exception('Text NOT found!')