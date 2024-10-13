# Age Calculator

from datetime import datetime

# Calculate Age
def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    return years, months, days

def main():
    birth_year = int(input("Enter Your Birth Year: "))
    birth_month = int(input("Enter Your Birth Month: "))
    birth_day = int(input("Enter Your Birth Date: "))

    birth_date = datetime(birth_year, birth_month, birth_day)
    years, months, days = calculate_age(birth_date)

    print(f"Your age is: {years} years, {months} months, and {days} days")

if __name__ == "__main__":
    main()