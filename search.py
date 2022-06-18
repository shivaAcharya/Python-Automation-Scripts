#! python3
# search.py - Program to search on Google from command line argument or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    if sys.argv[1] == 'youtube':
        webbrowser.open('https://www.youtube.com/results?search_query=' + ' '.join(sys.argv[2:]))
    else:
         webbrowser.open('www.google.com/search?q=' + ' '.join(sys.argv[1:]))
else:
    query = pyperclip.paste()
    webbrowser.open('www.google.com/search?q=' + query)
