# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"

while choice.lower() == "y":
    # get and validate monthly investment
    monthly_investment = float(input("Enter monthly investment:       "))

    while monthly_investment <= 0:
        print("Entry must be greater than 0. Please try again.")
        monthly_investment = float(input("Enter monthly investment:       "))

    # get and validate yearly interest rate
    yearly_interest_rate = float(input("Enter yearly interest rate:     "))

    while yearly_interest_rate <= 0 or yearly_interest_rate > 15:
        print("Entry must be greater than 0 and less than or equal to 15.")
        print("Please try again.")
        yearly_interest_rate = float(input("Enter yearly interest rate:     "))

    # get and validate number of years
    years = int(input("Enter number of years:          "))

    while years <= 0 or years > 50:
        print("Entry must be greater than 0 and less than or equal to 50.")
        print("Please try again.")
        years = int(input("Enter number of years:          "))

    # convert yearly interest rate to monthly interest rate
    monthly_interest_rate = yearly_interest_rate / 12 / 100

    # calculate and display future value for each year
    future_value = 0

    for year in range(1, years + 1):
        for month in range(12):
            future_value += monthly_investment
            monthly_interest_amount = future_value * monthly_interest_rate
            future_value += monthly_interest_amount

        print("Year = ", year, "\tFuture Value = ", round(future_value, 2))

    print()

    choice = input("Continue (y/n)? ")
    print()

print("Bye!")