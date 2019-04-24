#! python3

import re, pyperclip, pprint

# Creates a regex for phone numbers
phoneNumbers = re.compile('''#This program will search for these formats: 713-222-2222, 000-0000 ext 123, (281) 055-0555
(
((\d\d\d)|(\(\d\d\d\)))?              #area code (optional)
(\s|-)                            #first separator
\d\d\d                              #first 3 digits
-                          #separator
\d\d\d\d                            #last 4 digits
((ext(\.)?\s|x)
(\d{2,5}))?         #extension (optional)
)
''', re.VERBOSE)

# Creates a regex for emails
emailAddresses = re.compile('''

[a-zA-Z0-9_.+]+                     #name
@                                   #@ symbol
[a-zA-Z0-9_.+]+                     #domain

''', re.VERBOSE)

# Gets sample text off the clipboard
plainText = pyperclip.paste()

# Looks for phone numbers in the sample text
extractedPhone = phoneNumbers.findall(plainText)

# Looks for e-mails in the sample text
extractedEmail = emailAddresses.findall(plainText)

# Filters out non-phone numbers
allPhones = []
for phone in extractedPhone:
    allPhones.append(phone[0])

# Copies the extracted email/phone numbers to the clipboard
results = '\n'.join(allPhones) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)
