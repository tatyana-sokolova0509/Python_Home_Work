class Smartphone:
    def __init__(self, brand, model, number: str):
        self.brand = brand
        self.model = model
        self.number = number

    def __str__(self) -> str:
        return f"{self.brand} - {self.model}. {self.number}"
