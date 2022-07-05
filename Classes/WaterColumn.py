class WaterColumn:
  def __init__(self, standType, owner):
      self.customer = owner
      self.standType = standType
      self.bottleInStand = None

  def __repr__(self):
    rep = "Water Column: " 
    if(self.bottleInStand == None):
      rep += "None" + "\nBottle Status: No Bottle in stand" 
    else: 
      rep += "1" + "\nBottle Status: " + str(self.bottleInStand.bottleStatus) + " gallons left"
    rep += "\nWater Column Type: " + self.standType
    return rep

  def addBottleToStand(self, bottle):
    self.bottleInStand = bottle

  def printBottleInStand(self):
    print(repr(self.bottleInStand))

  def simulateConsumption(self):
    if(self.bottleInStand != None):
      if(self.bottleInStand.bottleStatus >= self.customer.consumptionRate):
        self.bottleInStand.changeBottleStatus(self.customer.consumptionRate)
        #self.bottleInStand.bottleStatus = self.bottleInStand.bottleStatus - self.customer.consumptionRate
      else:
        print("No More Water - Customer: " + self.customer.customerCode + "\n")

  def simulateWaterTemp(self):
    if(self.bottleInStand != None):
      #print ("Bottle temp before mess with me :", self.bottleInStand.bottleTemp)
      if (self.bottleInStand.bottleTemp < 75):
        self.bottleInStand.bottleTemp += 1
      #print ("Bottle Temp dont mess with me :", self.bottleInStand.bottleTemp)

  def printWaterTemp(self):
    print(self.bottleInStand.bottleTemp)
      
        
      