from union import Addressable


class Adress(Addressable):

    def __init__(self, postCode, city, street, building, appart):
        self.postCode = postCode
        self.city = city
        self.street = street
        self.building = building
        self.appart = appart

    def whichAdress(self):
        return (f"{self.postCode}, {self.city}, {self.street},"
                f"{self.building}-{self.appart}")
