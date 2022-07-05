#import mlrose
from Customer import Customer
from Bottle import Bottle
from Dispatcher import Dispatcher
from AIPS import AIPS
from Shelf import Shelf

customerList = []
days = 10
#Customers (Code, xLoc, yLoc, Bottle Type, Bottle Size, Water Column, Consumption Rate)
c1 = Customer("A", 2, 3, "glass", 4, "regular", .5)

c2 = Customer("B", 6, 10, "glass", 6, "chilled", 2)

c3 = Customer("C", 70, 5, "plastic", 4, "chilled", .25)

c4 = Customer("D", 10, 15, "plastic", 6, "regular", 1)

c5 = Customer("E", 20, 1, "plastic", 4, "regular", .5)

#Make AIPS for each customer
a1 = AIPS("A", c1)
c1.setAIPS(a1)

a2 = AIPS("B", c2)
c2.setAIPS(a2)

a3 = AIPS("C", c3)
c3.setAIPS(a3)

a4 = AIPS("D", c4)
c4.setAIPS(a4)

a5 = AIPS("E", c5)
c5.setAIPS(a5)

customerList.append(c1)
customerList.append(c2)
customerList.append(c3)
customerList.append(c4)
customerList.append(c5)


#Dispatcher (Code, xLoc, yLoc, customerList)
#Enter Code as "DIS"
d1 = Dispatcher("DIS", 0, 0, customerList)

#Set DIS for each customer
c1.setDIS(d1)
c2.setDIS(d1)
c3.setDIS(d1)
c4.setDIS(d1)
c5.setDIS(d1)

d1.setBottlesInit()
#d1.printBottles()
d1.TSP()


#print(repr(a1))



#Make bottles for shelf
#bottle1 = Bottle("glass", 4, "full")

#Add bottle to shelf
#fullShelf1.addBottleToShelf(bottle1)



d1.deliverBottles()



#d1.printBottles()

# print("customer A bottles delivered:\n")
# c1.printBottlesDelivered()

# print("customer B bottles delivered:\n")
# c2.printBottlesDelivered()

# print("customer C bottles delivered:\n")
# c3.printBottlesDelivered()

# print("customer D bottles delivered:\n")
# c4.printBottlesDelivered()

# print("customer E bottles delivered:\n")
# c5.printBottlesDelivered()

#print("AIPS \n")

a1.checkCustomerBottlesDelivered()
a2.checkCustomerBottlesDelivered()
a3.checkCustomerBottlesDelivered()
a4.checkCustomerBottlesDelivered()
a5.checkCustomerBottlesDelivered()

# print("shit")
# print(c2.fullShelf.bottles[0])
# print(c2.fullShelf.bottles[1])
# print(c2.fullShelf.bottles[2])
# print(c4.fullShelf.bottles[0])
# print(c4.fullShelf.bottles[1])
# print(c4.fullShelf.bottles[2])

print("\n######################## Day: 0 Delivery Day ########################\n")

print(repr(c1))
print(repr(c2))
print(repr(c3))
print(repr(c4))
print(repr(c5))

for x in range(0, days):
  print("########################  Day: " + str(x + 1) + "  ########################\n")

  c1.simulateConsumption()
  c2.simulateConsumption()
  c3.simulateConsumption()
  c4.simulateConsumption()
  c5.simulateConsumption()
  
  c1.simulateWaterTemp()
  c2.simulateWaterTemp()
  c3.simulateWaterTemp()
  c4.simulateWaterTemp()
  c5.simulateWaterTemp()

  #print("Water temp :")
  #c1.waterColumn.printWaterTemp()

  a1.aips()
  a2.aips()
  a3.aips()
  a4.aips()
  a5.aips()
  
  print(repr(c1))
  print(repr(c2))
  print(repr(c3))
  print(repr(c4))
  print(repr(c5))
  
# make a loop here to call the aips() function each day to determine what to do.
# for x in days:
  

# c1.moveBottlesToAIPS()
# c2.moveBottlesToAIPS()
# c3.moveBottlesToAIPS()
# c4.moveBottlesToAIPS()
# c5.moveBottlesToAIPS()

