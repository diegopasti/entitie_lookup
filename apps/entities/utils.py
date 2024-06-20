import random

from faker import Faker


def create_generic_entity():
    """
    Genereate random entity data

    :return:  new Entity data
    """

    nationality = ["BRAZILIAN", "AMERICAN", "RUSSIAN", "JAPANESE"]

    faker = Faker(locale='pt-BR')
    name = faker.name().upper().replace("DRA. ","").replace("DR. ","")
    birthdate = str(faker.date_of_birth(minimum_age=12, maximum_age=75))
    nationality = random.choice(nationality).upper()
    children = random.randint(0, 3)
    father_name = faker.name_male().upper()
    mother_name = faker.name_female().upper()
    job = faker.job().upper()

    documents = [create_generic_document() for item in range(random.randint(1, 2))]
    address = [generate_address() for item in range(random.randint(1, 3))]

    person = {
        "identifier": faker.cpf(),
        "name": name,
        "popular_name": name.split(" ")[0],
        "nationality": nationality,
        "birth_foundation": birthdate,
        "profession": job,
        "mother_name": mother_name,
        "father_name": father_name,
        "children": children,

        "documents": documents,
        "address": address,
        "contacts": []
    }

    return person


def create_generic_document():
    """
    Genereate random document data

    :return:  new document data
    """

    document_types = ["REGISTRY", "CERTIFICATE", "LICENSE"]
    sender_options = ["SSP", "PC"]

    faker = Faker()
    number = faker.ean()
    emission_date = str(faker.date_this_decade(before_today=True))
    expiration_date = str(faker.date_this_decade(after_today=True))
    sender = f"{random.choice(sender_options)}-{faker.state_abbr()}"

    document = {
        "type": random.choice(document_types),
        "number": number,
        "sender": sender,
        "emission_date": emission_date,
        "expiration_date": expiration_date
    }

    return document

def generate_address():
    """
    Genereate random address data

    :return:  new address data
    """

    faker = Faker(locale='pt-BR')
    street = faker.street_name().upper()
    number = random.randint(1, 2000)
    district = faker.neighborhood().upper()
    city = faker.city().upper()
    state = faker.state().upper()
    country = "BRASIL"
    postal_code = faker.postcode()

    return {
        "street": street,
        "number": number,
        "district": district,
        "city": city,
        "state": state,
        "country": country,
        "postal_code": postal_code,
        "full_address": f"{street}, {number}, {district}, {city}, {state}, {country} - {postal_code}"
    }




