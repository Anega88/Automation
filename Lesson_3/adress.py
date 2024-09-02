class Adress:

    def __init__(self, postCode, city, street, building, appart):
        self.postCode = postCode
        self.city = city
        self.street = street
        self.building = building
        self.appart = appart

      
    def printPostCode(self):
        return(self.postCode)
    
    def printCity(self):
        return(self.city)
    
    def printStreet(self):
        return(self.street)
    
    def printBuilding(self):
        return(self.building)
    
    def printAppart(self):
        return(self.appart)

