from faker import Faker


class Generator:
    @staticmethod
    def generate_payload():
        fake = Faker()
        payload = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()

        }
        return payload
