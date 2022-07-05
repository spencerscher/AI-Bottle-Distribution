class Robot:
  def __init__(self, robotID, owner):
    self.customer = owner
    self.robotID = robotID
    self.DeliveredBottlesToStack = []
    self.bottleInHand = None
    # self.robotReplenish = "off"
    # self.robotReplaceBottle = "off"
    # self.robotBottleType = "empty"
    # self.robotLeak = "off"
    # self.robotAlarm

  def __repr__(self):
    rep = "Robot bottles to stack in full shelf: " + str(len(self.DeliveredBottlesToStack))
    return rep

  def grabBottle(self, bottle):
    self.bottleInHand = bottle

  def placeBottleOnFullShelf(self):
    if(self.bottleInHand != None):
      self.customer.fullShelf.addBottleToShelf(self.bottleInHand)
      self.bottleInHand = None
    
  def placeBottleOnEmptyShelf(self):
    if(self.bottleInHand != None):
      self.customer.emptyShelf.addBottleToShelf(self.bottleInHand)
      self.bottleInHand = None

  def placeBottleOnStand(self):
    if(self.bottleInHand != None):
      self.customer.waterColumn.addBottleToStand(self.bottleInHand)
      self.bottleInHand = None

  def printBottleInHand(self):
    print(repr(self.bottleInHand))

  def printOwner(self):
    print(repr(self.customer))
