import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'Last week']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Miriam', 'Daniel', 'David', 'Godfrey']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'University', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']

print (random.choice(when) + ', ' + random.choice(who) + " called " + random.choice(name) + " who lived in " + random.choice(residence) + ", went to the " + random.choice(went) + ' and ' + random.choice(happened))