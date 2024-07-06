from datetime import date, datetime

def transform_string_to_date(date_str: str) -> date:
    """Transforms date string to date object
    
    Throws:
        ValueError - when date format is not %Y-%m-%d
    """
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def calculate_age(birthday_date: str) -> int:
    birthday_date = transform_string_to_date(birthday_date)
    today = datetime.today().date()
    
    # if birthday_date.month < today.month:
    #     if birthday_date.day > today.day:

    # if (birthday_date.month < today.month) and (birthday_date.day > today.day)

    if ((birthday_date.month, birthday_date.day) > (today.month, today.day)):
        return today.year - birthday_date.year - 1
    return today.year - birthday_date.year

print(calculate_age("2000-07-07"))