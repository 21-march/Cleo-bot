import assistantFunctions as af

"""
Cleo bot virtual assistant

----------------------------
Notes:
-Remove pressure from the weather function
and replace with wind
--Make sure to convert the deg of wind into cardinal directions
https://windy.app//storage/posts/June2022/how-to-read-wind-direction.jpg
----------------------------

@author: Ibrahim Salman
@version: 0.1
"""

print("Hello, I'm Cleo your virtual assistant\n")
print("(Type 'quit' to exit the program)")

def bot_message():
    request = input('\nHow may I assist you today?\n> ')
    if request == 'quit':
        print('Goodbye!')
        return False
    else:
        print(af.request_parse(request))
        return True

# this is so ghetto man 
start = True
while start != False:
    if not bot_message():
        break
