#Create a function for easier calculation inside of while loop
def ground_shipping(ground_weight):
  ground_cost = 0
  flat_charge = 20
  #Ground Shipping
  if ground_weight <= 2:
    ground_cost = 1.50 
  elif ground_weight >= 2 and ground_weight <=6:
    ground_cost = 3.00
  elif ground_weight >= 6 and ground_weight <=10:
    ground_cost = 4.00
  else:
    ground_cost = 4.75
  #Declare new costs
  initial_ground_cost = ground_cost*ground_weight + flat_charge
  premium_ground_cost = initial_ground_cost + 125
  #Print everything

  sentence = f"Weight: {ground_weight}lbs \nPrice: ${(ground_weight * ground_cost) + 20}"
  return sentence

while True:
  ground_weight = input("Enter number of pounds for Ground Shipping!\n\nTo stop calculating enter 'Stop'.")
  if ground_weight == "Stop" or ground_weight == "stop":
    break
  ground_weight = int(ground_weight)
  print("Ground Shipping costs:")
  print(ground_shipping(ground_weight))


