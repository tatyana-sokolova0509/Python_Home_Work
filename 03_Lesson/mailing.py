from adress import Address


class Mailing:
    def __init__(self, to_address: Address, from_address: Address, cost: int, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self) -> str:
        return f"Отправление {self.track} из {self.to_address} в {self.from_address}. Стоимость {self.cost} рублей"
