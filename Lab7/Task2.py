def travel_cost():
    """
    Returns the yearly costs of travel, 22£ per week.
    :return: The cost of travel.
    """
    # There are 52 weeks in a year minus two for Christmas and Summer holidays.
    return 22 * 50


def living_expenses(after_tax_income):
    """
    Returns the yearly living expenses, which is 5% of the after tax income.
    :param after_tax_income: The yearly income after income tax.
    :return: The living expenses.
    """

    return after_tax_income * 0.05


def council_tax_contribution():
    """
    Returns the amount of council tax owed which is just a 1500£ flat fee per year.
    :return: The council tax contribution.
    """

    return 1500


def national_insurance_contribution(pre_tax_income):
    """
    Returns the total amount of national insurance contributions for the year.
    You pay National Insurance contributions if you earn more than £200 a week.
    You pay 12% of your earnings above this limit and up to £800 a week.
    The rate drops to 2% of your earnings over £801 a week.
    :param pre_tax_income: The yearly income before tax.
    :return: The national insurance contribution.
    """
    weekly_income = pre_tax_income / 52

    if weekly_income <= 200:
        return 0

    if weekly_income <= 800:
        return ((weekly_income - 200) * 0.12) * 52

    return (600 * 0.12 + (weekly_income - 800) * 0.02) * 52


def income_tax(pre_tax_income):
    """
    Returns the total amount of tax at a rate of 35% in any amount over the free tax allowance of 11000£
    :param pre_tax_income: The yearly income before tax.
    :return: The amount of tax to be paid.
    """
    tax_allowance = 11000
    tax_rate = 0.35

    # Calculate the tax to be paid on the taxable income that is greater than the free tax allowance.
    if pre_tax_income <= tax_allowance:
        return 0
    else:
        return (pre_tax_income - tax_allowance) * tax_rate


def pension_contribution(pre_tax_income):
    """
    Returns the pension contribution based on the pre-tax income.
    :param pre_tax_income: The pre-tax income.
    :return: The pension contribution
    """
    return pre_tax_income * 0.09


while True:  # Added to make the program repeat as per additional task 2.
    # Ask the user for their yearly income.
    pre_tax_income = float(input("Please enter your yearly income into the expenditure calculator in £: "))

    # Calculate all outgoings.
    tax = income_tax(pre_tax_income)
    pension = pension_contribution(pre_tax_income)
    national_insurance = national_insurance_contribution(pre_tax_income)
    council_tax = council_tax_contribution()
    living = living_expenses(pre_tax_income - tax)
    travel = travel_cost()

    # Calculate total cost.
    total_cost = tax + pension + national_insurance + council_tax + living + travel

    # Print the results back to the user.
    print("\nThese are your outgoings\n-------------")
    print("Pre-tax Income :", pre_tax_income)
    print("Tax :", tax)
    print("Pension contribution :", pension)
    print("National Insurance contribution :", national_insurance)
    print("Council tax contribution :", council_tax)
    print("Living expenses :", living)
    print("Travel costs :", travel)
    print("Your total outgoings are :", total_cost)

    # Ask the user if they want to start again.
    if input("Continue? (y/n) : ") == "n":
        break
