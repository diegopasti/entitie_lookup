import random

from faker import Faker


def create_generic_entity():
    nationality = ["BRAZILIAN", "AMERICAN", "RUSSIAN", "JAPANESE"]

    faker = Faker()
    name = faker.name()
    birthdate = faker.date_of_birth(minimum_age=12, maximum_age=75)
    nationality = random.choice(nationality)
    children = random.randint(0, 3)
    father_name = faker.name_male()
    mother_name = faker.name_female()
    job = faker.job()

    person = {
        "name": name,
        "popular_name": name.split(" ")[0],
        "nationality": nationality,
        "birth_foundation": birthdate,
        "profession": job,
        "mother_name": mother_name,
        "father_name": father_name,
        "children": children,
    }

    return person
