from adress import Adress
from mail import Mailing
from union import message

to_address = Adress("987654", "Novi Sad", "Kukushkina", 13, 89)
from_address = Adress("123456", "Belgrade", "Pushkina", 23, 128)
mailing = Mailing(to_address, from_address, 2500, "ANT05709865")


result = message(to_address, from_address, mailing)
print(result)
