# 1. Create dummy coupons.txt file
with open("coupons.txt", "w") as f:
    coupons_list = ["SAVE50", "WELCOME20", "SAVE50", "FESTIVE10", "SAVE50", "WELCOME20", "NEWUSER", "FESTIVE10", "SAVE50", "NEWUSER"]
    for coupon in coupons_list:
        f.write(coupon + "\n")

# 2. Track usage frequency
coupon_counts = {}
with open("coupons.txt", "r") as f:
    for line in f:
        coupon = line.strip()
        if coupon:
            coupon_counts[coupon] = coupon_counts.get(coupon, 0) + 1

unique_coupons = set(coupon_counts.keys())

# 3. Identify suspicious and max used coupons
suspicious_coupons = []
max_count = 0
most_frequent = ""

for coupon, count in coupon_counts.items():
    if count > 3:
        suspicious_coupons.append(coupon)
    if count > max_count:
        max_count = count
        most_frequent = coupon

# 4. Save to fraud_report.txt
with open("fraud_report.txt", "w") as f:
    for coupon in suspicious_coupons:
        f.write(coupon + "\n")

# Display Output
print("Coupon Usage Frequency:")
for coupon, count in coupon_counts.items():
    print(f"{coupon}: {count}")

print("\nSuspicious Coupons:")
for coupon in suspicious_coupons:
    print(coupon)

print(f"\nUnique Coupons:\n{unique_coupons}")
print(f"\nMost Frequently Used Coupon:\n{most_frequent}")
print("\nFraud Report Generated Successfully.")