from smartphone import Smartphone

smartphone1 = Smartphone("Samsung", "S22", 89204587982)
smartphone2 = Smartphone("Samsung", "S24 Ultra", 89208792564)
smartphone3 = Smartphone("Xiaomi", "Redmi Note 13", 89202358746)
smartphone4 = Smartphone("IPhone", "15 Pro Max", 89204568291)
smartphone5 = Smartphone("Realme", "12 Pro", 89202468793)

catalog = [
        smartphone1,
        smartphone2,
        smartphone3,
        smartphone4,
        smartphone5
    ]

for phone in catalog:
    print(phone.list_of_phones())
