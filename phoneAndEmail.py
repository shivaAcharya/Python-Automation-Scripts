#! Python3
# phoneAndEmail.py - Finds phone numbers and email addresses from the clipboard

import pyperclip, re, sys

# Copy text from clipboard.

text = str(pyperclip.paste())

matches = []

# Look for patterns for phone numbers.

phoneNumRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?              # area code
            (\-|\s|\.)?                     # separator
            (\d{3})                         # first 3 digits
            (\-|\s|\.)                      # separator
            (\d{4})                         # last 4 digits
            (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
            )''', re.VERBOSE)

# Look for patterns for email address.

emailRegex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+       # username
            @                       # @ symbol
            [a-zA-Z0-9.-]+          # domain name
            (\.[a-zA-Z]{2,4})       # dot-something
            )''', re.VERBOSE)


# Find all matches in the clipboard text

for groups in phoneNumRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
    sys.exit()
else:
    print('No phone numbers or email addresses found.')
    sys.exit()
