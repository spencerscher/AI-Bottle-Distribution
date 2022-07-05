from Bottle import Bottle

import math


class Dispatcher:
    def __init__(self, dispatcherCode, dispatcherXLoc, dispatcherYLoc, customerList):
        self.dispatcherCode = dispatcherCode
        self.dispatcherXLoc = dispatcherXLoc
        self.dispatcherYLoc = dispatcherYLoc
        self.customerList = customerList
        self.bottlesToDistribute = []
        self.deliveryRoute = []

    def __repr__(self):
        rep = "Dispatcher Code: " + self.dispatcherCode + "\nX Location: " + str(self.dispatcherXLoc) + "\nY Location: " + str(
            self.dispatcherYLoc) + "\n"
        return rep

    def setBottlesInit(self):
        for x in self.customerList:
            bottleType = x.customerBottleType
            bottleCapacity = x.customerBottleCapacity
            for i in range(4):
                tempBottle = Bottle(bottleType, bottleCapacity)
                self.bottlesToDistribute.append(tempBottle)

    def printBottles(self):
        for x in self.bottlesToDistribute:
            print(repr(x))

    def TSP(self):
        temp_dispatcher = (0, self.dispatcherXLoc, self.dispatcherYLoc)
        coords_list = []
        coords_list.append(temp_dispatcher)

        #print ("This is the initial Coords_list :", coords_list)
        for x in self.customerList:
            temp_customer = (x.customerCode, x.customerXLoc, x.customerYLoc)
            if (x.customerCode == "A"):
                temp_customer = (1, x.customerXLoc, x.customerYLoc)
            if (x.customerCode == "B"):
                temp_customer = (2, x.customerXLoc, x.customerYLoc)
            if (x.customerCode == "C"):
                temp_customer = (3, x.customerXLoc, x.customerYLoc)
            if (x.customerCode == "D"):
                temp_customer = (4, x.customerXLoc, x.customerYLoc)
            if (x.customerCode == "E"):
                temp_customer = (5, x.customerXLoc, x.customerYLoc)
            if (x.customerCode == "F"):
                temp_customer = (6, x.customerXLoc, x.customerYLoc)
            if (x.customerCode == "G"):
                temp_customer = (7, x.customerXLoc, x.customerYLoc)

            coords_list.append(temp_customer)
        print("This is the coords_list : ", coords_list)

      # Function to calculate the distances between cities for all cities
        def getDistanceMatrix(houses):
            distanceMatrix = []
            for currentNode in houses:
                subArray = []
                for comparisonNode in houses:
                    subArray.append(getDistanceBetweenCities(
                        currentNode, comparisonNode))
                distanceMatrix.append(subArray)
            return distanceMatrix

      # Function to calculate the distance between 2 input cities
        def getDistanceBetweenCities(city1, city2):
            x1 = city1[1]
            y1 = city1[2]
            x2 = city2[1]
            y2 = city2[2]
            numToGetSquareRootOf = ((pow((x1 - x2), 2)) + (pow((y1 - y2), 2)))
            if numToGetSquareRootOf < 0:
                numToGetSquareRootOf *= -1
            return int(math.sqrt(numToGetSquareRootOf))

      # Function to calculate which house is the closest
          # This is the GREEDY APPROACH Apsect
        def getNearestHouse(distanceMatrix, cityId):
            i = 0
            for distanceList in distanceMatrix:
                if i == cityId:
                    smallestDistance = min(
                        idx for idx in distanceList if idx > 0)
                    if smallestDistance > 9999 * 3:
                        return -1, -1
                    else:
                        return smallestDistance, distanceList.index(smallestDistance)
                i += 1

      # Function to calculate the distance a hous
        def getDistanceForHome(thePath, houses):
            for house in houses:
                if house[0] == thePath[0]:
                    firstCity = house
                if house[0] == thePath[len(thePath) - 1]:
                    lastCity = house
            return getDistanceBetweenCities(firstCity, lastCity)

      # Function to add house to path and remove from houses to visit
        def addHouse(pathArray, housesToVisit, distanceMatrix, house_id):
            pathArray.append(house_id)
            prev_house_id = pathArray[len(pathArray) - 2]
            for house in housesToVisit:
                if house[0] == prev_house_id:
                    housesToVisit.remove(house)
            for distanceList in distanceMatrix:
                distanceList[prev_house_id] = 99999

      # Fuction to returns the id and distance in the path
        def chooseHouse(pathArray, citiesToVistit, distanceMatrix):
            if len(pathArray) == 0:
                return 0, 0, 0
            bestDistance, idOfBestHouse = getNearestHouse(
                distanceMatrix, pathArray[(len(pathArray) - 1)])
            if idOfBestHouse == -1:
                return -1, -1, -1
            #print ("The idOfBestHouse :", idOfBestHouse)
            #print ("The bestDistance :", bestDistance)
            return 0, idOfBestHouse, bestDistance

      # Function that returns the best path
        def findBestPath(distanceMatrix, houses_to_add):
            pathArray = []
            flag = 0
            totalDistance = 0
            while flag is not -1:
                flag, city_id, distance = chooseHouse(
                    pathArray, houses_copy, distanceMatrix)
                if flag == 0:
                    addHouse(pathArray, houses_to_add, distanceMatrix, city_id)
                    totalDistance += distance
            return totalDistance, pathArray

      # initializes the house and distance matrix
        houses = coords_list
        houses_copy = list(houses)
        distance_matrix = getDistanceMatrix(houses)

      # functions to find th best path and total distance
        totalDistance, thePath = findBestPath(distance_matrix, houses_copy)
        #print ("This be the houses :", houses)
        #print ("This be the Path :", thePath)
        totalDistance += getDistanceForHome(thePath, houses)

      # print the total distance and best path
        print("\nThe total distance traveled :", totalDistance)
        bestPath = []
      # conver thePath id to best Path
        for node in thePath:
            if (node == 0):
                bestPath.append("Dis")
            if (node == 1):
                bestPath.append("A")
            if (node == 2):
                bestPath.append("B")
            if (node == 3):
                bestPath.append("C")
            if (node == 4):
                bestPath.append("D")
            if (node == 5):
                bestPath.append("E")
            if (node == 6):
                bestPath.append("F")
            if (node == 7):
                bestPath.append("G")
        #print("The best path : ", bestPath)
        self.deliveryRoute = bestPath.copy()
        print("\nDelivery Route: ", self.deliveryRoute)
#        for node in thePath:
#          print (node)


#        dist_list = [] #(start city, neighbor city, distance)
#        for x in self.customerList:
#            distance = math.sqrt((self.dispatcherXLoc-x.customerXLoc)**2 + (self.dispatcherYLoc - x.customerYLoc)**2)
#            temp_dist = (self.dispatcherCode, x.customerCode, distance)
#            dist_list.append(temp_dist)
#
#        #print ("This is the initial dist_list :", dist_list)

# This part prints out a full list of distances to all nodes
#        for y in self.customerList:
#          for x in self.customerList:
#            distance = math.sqrt((x.customerXLoc-y.customerXLoc)**2 + (x.customerYLoc - y.customerYLoc)**2)
#            temp_dist = (x.customerCode, y.customerCode, distance)
#            if (x.customerCode == y.customerCode):
#              break
#            for item in dist_list:
#              if (distance == item):
#                break
#            #for x in dist_list:
#                #if (temp_dist != x):
#            dist_list.append(temp_dist)


#        print ("Full distance list: ", dist_list)

#        for x in self.customerList:
#            tempDistance = self.distanceCustomerDispatcher(x)
#            x.setDistanceFromDIS(tempDistance)
#            print(str(x.distanceFromDIS) + "\n")
        # Sort list to be in order of customers distance from Dispatcher
#        self.customerList.sort(key=lambda x: x.distanceFromDIS)
#        print("##########################")
        # print customer list
#        for x in self.customerList:
#            print(str(x.distanceFromDIS) + "\n")
#        self.deliveryRoute.append(self.customerList[0])
#        print(self.deliveryRoute[0])

    # Print Delivery route
        # FIXME
   # def printDeliveryRoute(self):
    # print(x)

    def distanceBetweenCustomers(customer1, customer2):
        return math.sqrt((customer1.customerXLoc - customer2.customerXLoc)**2 + (customer1.customerYLoc - customer2.customerYLoc)**2)

    def distanceCustomerDispatcher(self, customer):
        return math.sqrt((self.dispatcherXLoc - customer.customerXLoc)**2 + (self.dispatcherYLoc - customer.customerYLoc)**2)


    def deliverBottles(self):
        # deliver bottles to each customer in order of the deliveryRoute
        for i in self.deliveryRoute:
            if i == "Dis":
                continue
            else:
                for x in self.customerList:
                    if i == x.customerCode:
                      for y in reversed(self.bottlesToDistribute):
                        if(len(x.bottlesDelivered) < 4):
                          if (x.customerBottleType == y.bottleType) and (x.customerBottleCapacity == y.bottleCapacity):
                            x.bottleDelivered(y)
                            self.bottlesToDistribute.remove(y)

    def replenishCustomer(self, customer):
      tempBottle1 = Bottle(customer.customerBottleType, customer.customerBottleCapacity)
      tempBottle2 = Bottle(customer.customerBottleType, customer.customerBottleCapacity)
      self.bottlesToDistribute.append(tempBottle1)
      self.bottlesToDistribute.append(tempBottle2)
      for y in reversed(self.bottlesToDistribute):
        if(len(customer.bottlesDelivered) < 2):
          if (customer.customerBottleType == y.bottleType) and (customer.customerBottleCapacity == y.bottleCapacity):
            customer.bottleDelivered(y)
            self.bottlesToDistribute.remove(y)


    def takeEmptyBottles(self, customer):
      customer.emptyShelf.bottles.clear()