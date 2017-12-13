#Exercise 3:
#Encapsulate this code in a function named count, and generalize it so that it accepts the string 
#and the letter as arguments.

word = input("Enter a word.")
let = input("Enter a letter.")

def counter():
  count = 0
  for letter in word:
    if letter == let: 
      count = count + 1
  return count
  
print counter()
