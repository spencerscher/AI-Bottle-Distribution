#create a new class shelf
class Shelf:
    #create a full-bottle shelf which can store up to 3 bottles and an empty-bottle shelf that can store up to 2 bottles
    def __init__(self, shelf_type):
        self.shelf_type = shelf_type
        self.bottles = []

    def __repr__(self):
      rep = "Bottles on " + self.shelf_type + " shelf: " + str(len(self.bottles))
      return rep


    
    def addBottleToShelf(self, bottle):
      self.bottles.append(bottle)