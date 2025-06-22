from faker import Faker

fake = Faker()

def generate_email():
    return fake.email()
