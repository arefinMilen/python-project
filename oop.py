class Factory:
    def __init__(self,BT,tyers,ET):
      # print(BT,tyers,ET)
      self.BT = BT
      self.tyers= tyers
      self.ET = ET
    def showDetails(self):
        print(f"your details are: \n {self.BT},{self.tyers},{self.ET}")


ferari = Factory("covered",4,"8 cycle")
alto = Factory("covered",8,"4 cycle")
splender = Factory("open",2,"2 cycle")

# print(alto.ET)
splender.showDetails()

class Honda(Factory):
    def __init__(self,BT,tyers,ET,glass):
        super().__init__(BT,tyers,ET)
        self.glass = glass
obj1= Honda(1,2,3,4)

print(obj1.BT)
obj1.showDetails()