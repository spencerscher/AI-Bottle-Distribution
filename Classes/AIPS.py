import random

class AIPS:
    def __init__(self, AIPSCode, owner):
      self.AIPSCode = AIPSCode
      self.customer = owner
      

    def __repr__(self):
      rep = "AIPS Owner: " + self.customer.customerCode + "\n" 
      return rep

    # def bottleDelivered(self, bottle):
    #   self.bottlesDelivered.append(bottle)

    # def printBottlesDelivered(self):
    #   for x in self.bottlesDelivered:
    #     print(repr(x))

  #REVIEW THE FUNCTIONS BELOW...
    def controlWaterTemp(self):
      if self.robot.robotStandType == "chilled":
          if self.robot.robotWaterTemperature < 42:
              self.robot.robotCooler = "on"
          elif self.robot.robotWaterTemperature > 42:
              self.robot.robotCooler = "off"
          else:
              self.robot.robotCooler = "off"
      else:
          self.robot.robotCooler = "off"

    def replenishBottle(self):
      if self.fullShelf.shelf_type == "full" and self.robot.robotWaterLevel < 0.25:
        self.robot.robotReplenish = "on"
      else:
        self.robot.robotReplenish = "off"

# The AIPS issues the Replace Bottle command if the bottle on the water stand is empty. 
    def replaceBottle(self):
      #check if the bottle on the water stand is empty
      if self.robot.robotBottleType == "empty":
        self.robot.robotReplaceBottle = "on"
      else:
        self.robot.robotReplaceBottle = "off"

        #The AIPS issues the Alarm command to the dispatch center if it detects a leak.
    def alarm(self):
      if self.robot.robotLeak == "on":
        self.robot.robotAlarm = "on"
      else:
        self.robot.robotAlarm = "off"

        #creating a function here that will be called each day in SystemSoftware.py to run all of the AIPS checks.
    def aips(self):
      self.checkWaterStandStatus()
      self.checkReplenish()
      if(random.randint(1,30) < 2):
         self.replenishLeak()
      self.waterControl()

    #   self.checkCustomerBottlesDelivered()
    #   self.controlWaterTemp()
    #   self.replaceBottle()
    #   self.replenishBottle()
    #   self.alarm()

      #FINISH after doing change bottle function
    def checkWaterStandStatus(self):
      if(self.customer.waterColumn.bottleInStand != None):
        if(self.customer.waterColumn.bottleInStand.bottleStatus < self.customer.consumptionRate):
          self.customer.robotGrabBottleFromStand()
          self.customer.robotGrabBottleFullShelf()
          #self.customer.waterColumn.printBottleInStand()
  
    def checkCustomerBottlesDelivered(self):
      while (len(self.customer.bottlesDelivered)):
        self.customer.robotGrabBottle()

    def checkReplenish(self):
      #print ("bottles in shelf to check :", len(self.customer.fullShelf.bottles))
      #print ("bottle status to check :", self.customer.waterColumn.bottleInStand.bottleStatus)
      if((len(self.customer.fullShelf.bottles) <= 1) and self.customer.waterColumn.bottleInStand.bottleStatus <= .25) or (len(self.customer.fullShelf.bottles) == 0):
        #print ("replenishing#####################################")
        self.replenish()

    def replenish(self):
      print("Call DIS function to replenish customer: " + self.customer.customerCode + "\n")
      self.customer.DIS.replenishCustomer(self.customer)
      self.checkCustomerBottlesDelivered()
      print("Call DIS to remove bottles from empty shelf:", self.customer.customerCode, "\n")
      self.customer.DIS.takeEmptyBottles(self.customer)

    def replenishLeak(self):
      print ("ALARM Customer: ", self.customer.customerCode, " has a water leak!")
      print ("Call DIS to fix water leak\n")
      self.customer.robotGrabBottleFromStand()
      self.customer.robotGrabBottleFullShelf()

    def waterControl(self):
      if(self.customer.waterColumn.standType == "chilled"):
        if(self.customer.waterColumn.bottleInStand.bottleTemp >= 44):
          #turn on water cooler
          #self.waterCooler(true)
          print ("Water Temp Control: ON for customer", self.customer.customerCode, "\n")
          self.customer.waterColumn.bottleInStand.bottleTemp -= 4
          #print ("Water temp test control :", self.customer.waterColumn.bottleInStand.bottleTemp)

    #def waterCooler(self):
      
