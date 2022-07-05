import random
class Bottle:
  def __init__(self, bottleType, bottleCapacity):
      self.bottleType = bottleType
      self.bottleCapacity = bottleCapacity
      self.bottleStatus = bottleCapacity
      self.bottleTemp = random.randint(40,60)

  def __repr__(self):
    rep = "Bottle Type: " + self.bottleType + "\nBottle Capacity: " + str(self.bottleCapacity) + " gallons\nBottle Status: "+ str(self.bottleStatus)  + " gallons\n"
    return rep

      
  def changeBottleStatus(self, change):
    self.bottleStatus = self.bottleStatus - change