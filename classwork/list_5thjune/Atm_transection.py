#taking treansection
transactions = [5000,-2000,3000,-1000,-500,7000]
deposits = []
withdrawals = []
#total deposit
current_balance = sum(transactions)
for amt in transactions:   
    if amt > 0:
        deposits.append(amt)  # Filter into deposits list
    elif amt < 0:
        withdrawals.append(amt)
          #  Filter into withdrawals list
total_deposits_count = sum(deposits)
total_withdrawals_count = sum(withdrawals)

#  Find the largest deposit and largest withdrawal
# (Using absolute value for withdrawal to show magnitude, or leave as negative depending on preference)
largest_deposit = max(deposits) if deposits else 0
largest_withdrawal = min(withdrawals) if withdrawals else 0 

# --- Display Results ---
print("## ATM Transaction Summary ##")
print(f"1. Current Balance: ${current_balance}")
print(f"2. Total Deposits Count: {total_deposits_count}")
print(f"   Total Withdrawals Count: {total_withdrawals_count}")
print(f"3. Largest Deposit: ${largest_deposit}")
print(f"   Largest Withdrawal: ${largest_withdrawal} (Magnitude: ${abs(largest_withdrawal)})")
print(f"4. Separate Lists:")
print(f"   - Deposits: {deposits}")
print(f"   - Withdrawals: {withdrawals}")
