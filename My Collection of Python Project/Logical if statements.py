# Using logical if statements. Can look at Buying a House PY file for another example

has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Income and Credit are Good")
    # Using the 'and' method must have both bullion's True or False

if has_high_income or has_good_credit:
    print("Income or Credit meets requirements")
    # Using the 'or' method can have either bullion's True or False

if has_good_credit and has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan, Please review records for more details")

