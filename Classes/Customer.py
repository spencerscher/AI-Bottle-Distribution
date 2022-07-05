from Shelf import Shelf
from Robot import Robot
import random
from WaterColumn import WaterColumn
class Customer:
    def __init__(self, customerCode, customerXLoc, customerYLoc, customerBottleType, customerBottleCapacity, customerWaterColumnType, consumptionRate):
        self.customerCode = customerCode
        self.customerXLoc = customerXLoc
        self.customerYLoc = customerYLoc
        self.customerBottleType = customerBottleType
        self.customerBottleCapacity = customerBottleCapacity
        self.waterColumn = WaterColumn(customerWaterColumnType, self)
        self.bottlesDelivered = []
        self.fullShelf = Shelf("full")
        self.emptyShelf = Shelf("empty")
        self.robot = Robot(customerCode, self)
        self.consumptionRate = consumptionRate
        #self.waterTemp = random.randint(35,50)
      #add a rate at which the customer drinks the water. This rate will be used to determine how much water to subtract as each day goes by (in simulated time).

    def __repr__(self):
        rep = "Customer Code: " + self.customerCode + "\nX Location: " + str(self.customerXLoc) + "\nY Location: " + str(
            self.customerYLoc) + "\nBottle Type: " + self.customerBottleType + "\nBottle Capacity: " + str(self.customerBottleCapacity) + " gallons\n" + repr(self.fullShelf) + "\n" + repr(self.emptyShelf) + "\n" + repr(self.waterColumn) + "\n"
        return rep

    def setDistanceFromDIS(self, distanceFromDIS):
        self.distanceFromDIS = distanceFromDIS

  #Used in Dispatcher to add bottle to customer
    def bottleDelivered(self, bottle):
      self.bottlesDelivered.append(bottle)

    def printBottlesDelivered(self):
      for x in self.bottlesDelivered:
        print(repr(x))
        
    # def setDistanceFromCustomer
    # def distancesFromCustomers(self, customer)
    @classmethod
    def setAIPS(self, AIPS):
        self.AIPS = AIPS

    @classmethod
    def setDIS(self, DIS):
        self.DIS = DIS

 #   def moveBottlesToAIPS(self):
 #     for x in reversed(self.bottlesDelivered):
 #       self.AIPS.bottleDelivered(x)
 #       print(self.AIPS)
 #       self.bottlesDelivered.remove(x)
      # self.AIPS.bottlesDelivered = self.bottlesDelivered.copy()

#This is for full bottles
    def robotGrabBottle(self):
      tbottle = self.bottlesDelivered.pop()
      #print("robot hand\n" + repr(tbottle))
      self.robot.grabBottle(tbottle)
      #print("Robot Bottle in hand: \n")
      
      if(self.waterColumn.bottleInStand == None):
        self.robot.placeBottleOnStand()
        #print("Bottle added to waterColumn\n")
      if(len(self.fullShelf.bottles) < 3): 
        self.robot.placeBottleOnFullShelf()
        #print("Bottle added to Shelf")
        
      #self.robot.printOwner()
    
    def robotGrabBottleFromStand(self):
      self.robot.grabBottle(self.waterColumn.bottleInStand)
      self.waterColumn.bottleInStand = None
      self.robot.placeBottleOnEmptyShelf()
      

    def robotGrabBottleFullShelf(self):
      #print("bottle full shelf: \n" + repr(self.fullShelf.bottles[0]))
      #print(self.fullShelf.bottles[0])
      tempb = self.fullShelf.bottles.pop()
      #print("full shelf b" + repr(tempb))
      self.robot.grabBottle(tempb)
      #self.robot.printBottleInHand()
      self.robot.placeBottleOnStand()
      #self.waterColumn.printBottleInStand()

    def simulateConsumption(self):
      self.waterColumn.simulateConsumption()

    def simulateWaterTemp(self):
      self.waterColumn.simulateWaterTemp()


