from union import Addressable


class Mailing:

    def __init__(self, to_adress: Addressable,
                 from_adress: Addressable,
                 cost: int, track: str):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из"
                f"{self.from_adress.whichAdress()}"
                f"в {self.to_adress.whichAdress()}."
                f" Стоимость {self.cost} рублей.")
