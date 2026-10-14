#assignment 4

def create_account(first_name,
                   last_name,
                   username,
                   password,
                   opening_balance = 0):
    account = { "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "password": password,
                "opening_balance": opening_balance}
    return account


def calculate_interest(account, rate=5, time=1):
# parameters =rate, principal and  time
    """Calculates simple interest over a period of a year based on the opening balance."""
    principal = account['opening_balance']

    #Interest Formula: (Principal * Rate * Time) / 100
    result = (principal * rate * time) / 100

    print(f"Opening Balance: ${principal}")
    print(f"Interest Rate: {rate}%")
    print(f"Time Period: {time} year(s)")
    print(f"Calculated Simple Interest: ${result}")

    return result