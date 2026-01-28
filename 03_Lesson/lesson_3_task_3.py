from adress import Address
from mailing import Mailing

mailing1 = Mailing(to_address=Address("103132", "Москва", "Ленина", "15", "36"),
                   from_address=Address("666600", "Барнаул", "Строителей", "60", "36"), cost=10000, track="A1")
print(mailing1)
