year = input("Год: ")
year_int = int(year)

def is_year_leap(year_int):
    if ((year_int % 4) == 1):
        print(f"Год {year_int}: True")
    else:
        print(f"Год {year_int}: False")

result = is_year_leap(year_int)

