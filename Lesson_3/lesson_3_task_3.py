from adress import Adress
from mail import Mailing

mail = Mailing(Adress("123456", "Belgrade", "Pushkina", 23, 128),
               Adress("987654", "Novi Sad", "Kukushkina", 13, 89),
               2500,
               "ANT05709865")


print(mail.sending())
