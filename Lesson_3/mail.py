from adress import Adress


class Mailing:

    def __init__(self, to_adress: Adress,
                 from_adress: Adress,
                 cost: int, track: str):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track

    def sending(self):
        return (f"Отправление {self.track} из"
                f"{self.from_adress.whichAdress()}"
                f"в {self.to_adress.whichAdress()}."
                f" Стоимость {self.cost} рублей.")
