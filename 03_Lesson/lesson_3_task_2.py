from smartphone import Smartphone

catalog = []

smartphone1 = Smartphone("Samsung", "S1", "+79239211111")
catalog.append(smartphone1)

smartphone1 = Smartphone("Samsung", "S2", "+79239222222")
catalog.append(smartphone1)

smartphone1 = Smartphone("Apple", "5", "+79239233333")
catalog.append(smartphone1)

smartphone1 = Smartphone("Apple", "12", "+79239244444")
catalog.append(smartphone1)

smartphone1 = Smartphone("Honor", "50", "+79239255555")
catalog.append(smartphone1)

for tel in catalog:
    print(tel)
