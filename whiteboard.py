# it's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, 
# the original string. You don't have to worry with strings with less than two characters.
# EXAMPLES:
# remove_char('eloquent') --> 'loquen'
# remove_char('country') --> 'ountr'
# remove_char('person') --> 'erso'
# remove_char('place') --> 'lac'
# remove_char('ok') --> ''
# remove_char('ooopsss') --> 'oopss'

def removeFirstAndLast(word):
  newWord = ""  
  for letter in range(len(word)):
    if letter == 0 or letter == len(word)-1:
      continue
    else:
      newWord += word[letter]
  return newWord

print(removeFirstAndLast('ooopsss'))
  