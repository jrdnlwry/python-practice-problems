"""
DESCRIPTION:

You probably know the "like" system from Facebook and other pages.

People can "like" blog posts, pictures or other items.

We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.

It must return the display text as shown in the examples:

Accept a list element of name(s)

If the list is empty:
	- "no one likes this"

If the list has one entity:
	- {name} "likes this"

If the list has two entities:
	- {name} "and" {name} "like this"

If the list has three entities:
	- {name} "," {name} "and" {name} "like this"

If the list has N entities:
	N represents the number of entities in the array
	- {name}, {name} "and" {N} "others like this"

"""
def likes(names):

      if len(names) == 0:
        return "no one likes this"
      elif len(names) == 1:
        return f"{names[0]} likes this"
      elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
      elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
      elif len(names) >=4:
        return f"{names[0]}, {names[1]} and" + " " + str(len(names) - 2) + " others like this"
      

entity6 = ["Alex", "Jacob", "Mark", "Max", "Frank"]

print(likes(entity6))