from faker import Faker

fake = Faker('ru_RU')

user_date = {
    "name": fake.name(),
    "address": fake.address(),
    "email": fake.email(domain="yandex.ru")
}
print(fake.name())
print(fake.address())
print(fake.email(domain="yandex.ru"))

print(user_date)