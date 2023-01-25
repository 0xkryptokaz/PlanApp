from datetime import datetime, timedelta

def credit():
    while True:
        try:
            plan_cost = float(input("enter plan cost: "))
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
            end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
            break
        except ValueError:
            print("please enter a valid number")
    credit = plan_cost / 30.00
    date_diff = end_datetime - start_datetime
    sum = credit * date_diff.days
    return sum

sum = credit()
print("{:.2f}".format(sum))
input("Press enter to exit.")
