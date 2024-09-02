from adress import Adress
from mail import Mailing
         
def message(to_adress, from_adress, mailing):
    return (f"Отправление {mailing.printTrack()} из "
            f"{from_adress.printPostCode()}, {from_adress.printCity()}, "
            f"{from_adress.printStreet()}, {from_adress.printBuilding()}-{from_adress.printAppart()} "
            f"в {to_adress.printPostCode()}, {to_adress.printCity()}, "
            f"{to_adress.printStreet()}, {to_adress.printBuilding()}-{to_adress.printAppart()}. "
            f"Стоимость {mailing.printCost()} рублей.")
