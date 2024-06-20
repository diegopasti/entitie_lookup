from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class PersonQueries:

    person_who_are_father = {"type": "PERSON", "children": {"$gte": 1}}
    person_who_are_adults = {
        "type": "PERSON",
        "birth_foundation": {"$lte": (date.today() - relativedelta(years=18)).strftime("%Y-%m-%d")}
    }
