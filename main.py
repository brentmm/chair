class chair():
  #constructor
  def __init__(self, legs, material, colour, price):
    self.legs = legs
    self.material = material
    self.colour = colour
    self.price = price
  
  #string outline
  def __str__(self):
    return("This a " + self.colour + "" + self.material + " chair that has " + self.legs + " legs and cost $" + self.price + ".")

#user input making chair
colour = input("Pick a Colour: ")
material = input("Pick a material: ")
legs = str(input("Select how many legs: "))
price = str(input("What is the price: "))

#printing users chair
print()
print(chair(legs, material, colour, price))