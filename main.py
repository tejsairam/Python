import turtle

# we created an object called turtle
turtle = turtle.Turtle()

# defining a function for square

def square(length):
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)
  turtle.forward(length)
  turtle.left(90)

square(120*2)
square(120 / 2)
turtle.forward(60)
square(120/2)

print(125.4 // 4)

print(True)
print(False)

is_john_killer = True
is_bob_killer = False

if is_bob_killer == True:
  print("Bob is the Killer")
else:
  print("John is the killer")


print(5 == 5)