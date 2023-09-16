from datetime import date


def get_user_birthday():
    birth_year = int(input('Please enter your birth year: '))
    birth_month = int(input('Please enter your birth month: '))
    birth_day = int(input('Please enter your birth day: '))

    user_birthday = date(birth_year,birth_month,birth_day)

    return user_birthday

def calculate_age(user_birthday):

    date = date.today()
    year_diff = today.year - user_birthday.year
    precedes_flag = ((today.month, today.day) < (user_birthday.month, user_birthday.day))

    age = year_diff - precedes_flag

    return age

if __name__ == "__main__":
    current_age = calculate_age(user_birthday)
    print(f"your age is: {current_age}")
