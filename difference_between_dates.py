"""
Написати функцію, яка буде шукати різницю між двома датами (у днях)

"""

"Hello зв'язок", 'Hello'

from datetime import date, datetime

# Написати функцію, яка буде шукати різницю між двома датами (у днях)
#
#
# Hello!


# Рахувати відстань між датами

# Перетворювати дату на date
def transform_string_to_date(date_str: str) -> date:
    """Transforms date string to date object
    
    Throws:
        ValueError - when date format is not %Y-%m-%d
    """
    return datetime.strptime(date_str, "%Y-%m-%d").date()

# Рахувати відстань між датами
def calculate_distance_between_dates_in_days(date_one: date, date_two: date) -> int:
    # difference = date_two - date_one
    # return difference.days
    return (date_two - date_one).days

def difference_between_dates(date_one: str, date_two: str) -> int:
    # return calculate_distance_between_dates_in_days(transform_string_to_date("2000-01-01"), transform_string_to_date("2000-02-02"))
    date_one = transform_string_to_date(date_one)
    date_two = transform_string_to_date(date_two)
    return calculate_distance_between_dates_in_days(date_one, date_two)


# print(transform_string_to_date("2000-01-01"))

# date_one = transform_string_to_date("2000-01-01")
# date_two = transform_string_to_date("2000-02-02")
# print(calculate_distance_between_dates_in_days(date_one, date_two))

print(difference_between_dates("2000-01-01", "2000-02-02"))