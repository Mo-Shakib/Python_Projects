from faker import Faker # importaing
fake = Faker()

print('Email:', fake.email())
print('Country:', fake.country())
print('Name:', fake.name())
print('URL:', fake.url())
