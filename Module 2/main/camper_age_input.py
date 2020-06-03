def main():
    print("Please enter a number to represent the age of the child.")
    age_in_years = int(input())
    age_in_months = convert_to_months(age_in_years)
    print("The age of the camper in months is:",age_in_months)


def convert_to_months(years):
    age = years * 12

    return (age)


if __name__ == '__main__':
    main()


#bugs: In the initial draft of the program,
#I had the print statement called like is:+age_in_months)
#This had the odd side effect of printing out none of the correct values.( the year repeated 6-8 times)
#This is apparently because the + operation in the print statement is only for strings.

