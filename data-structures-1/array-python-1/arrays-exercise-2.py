"""
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""


heros=['spider man','thor','hulk','iron man','captain america']
print(heros)

print("Array length: ", len(heros))  #1

heros.append("black panther")
print("Updated array 1: ", heros)  #2

heros.remove("black panther")
heros.insert(3, "black panther")
print("Updated array 2: ", heros)  #3

heros[1:3] = ["doctor strange"]
print("Updated array 3: ", heros)  #4

heros.sort()
print("Updated array 4: ", heros) 
print("Sorting without using .sort(): ", sorted(heros))  #5