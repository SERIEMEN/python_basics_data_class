from pythonProject.interest import create_account, calculate_interest

#Create an account using the create_account function(user account is the new dictionary created)
user_account = create_account(
    first_name="Sarah",
    last_name="Connor",
    username="sconnor",
    password="skynet_password123",
    opening_balance=5000.00
)

print("--- Account Created Successfully ---")
print(user_account)
print("\n--- Interest Calculation ---")

# Step 2: Pass the dictionary into the calculate_interest function
calculate_interest(user_account)