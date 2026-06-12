# A file named login_logs.txt contains user login attempts in the following format: 
# username,status 
# anuj,Success 
# rahul,Failed 
# anuj,Failed 
# priya,Failed 
# rahul,Failed 
# neha,Success 
# anuj,Failed 
# karan,Failed 
# rahul,Success 
# priya,Failed 
# Tasks 
# 1. Count successful and failed login attempts.  
# 2. Identify users with more than 2 failed attempts.  
# 3. Create a dictionary storing the number of failures per user.  
# 4. Create a set of users who logged in successfully.  
# 5. Display users whose accounts should be reviewed.  


# Task: Handle file operations and compute login stats
# 1. Create the dummy login_logs.txt file as specified in the problem
with open("login_logs.txt", "w") as f:
    f.write(
        "username, status\n"
        "anuj, Success\n"
        "rahul, Failed\n"
        "anuj, Failed\n"
        "priya, Failed\n"
        "rahul, Failed\n"
        "neha, Success\n"
        "anuj, Failed\n"
        "karan, Failed\n"
        "rahul, Success\n"
        "priya, Failed\n"
    )

# 2. Initialize tracking variables
success_count = 0
failed_count = 0
failure_dict = {}
successful_users = set()

# 3. Read and process the log file
with open("login_logs.txt", "r") as f:
    # Skip the header line
    next(f)
    for line in f:
        if line.strip():
            username, status = line.strip().split(", ")
            if status == "Success":
                success_count += 1
                successful_users.add(username)
            elif status == "Failed":
                failed_count += 1
                failure_dict[username] = failure_dict.get(username, 0) + 1

# 4. Identify accounts requiring review (> 2 failed attempts)
review_accounts = [user for user, count in failure_dict.items() if count > 2]

# 5. Display Output
print("Successful Login Attempts:", success_count)
print("Failed Login Attempts:", failed_count)
print("\nFailure Count per User:")
for user, count in failure_dict.items():
    print(f"{user}: {count}")

print("\nUsers with Successful Logins:")
print(successful_users)

print("\nAccounts Requiring Review:")
if review_accounts:
    for user in review_accounts:
        print(user)
else:
    print("None")