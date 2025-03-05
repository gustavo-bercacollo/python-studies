# Python Exercise #036 - Approving a Loan

print("-=" * 20)
print("🏦 Bank Loan Approval System 🏠")
print("-=" * 20)

house_price = float(input("House price: $"))
buyer_salary = float(input("Buyer salary: $"))
years_pay_off = int(input("Years to pay off: "))

monthly_installment = house_price / (years_pay_off * 12)

print(f"\n💰 To pay a house of \033[1;32m${house_price:.2f}\033[m in {years_pay_off} years, "
      f"the monthly installment will be \033[1;32m${monthly_installment:.2f}\033[m")

if monthly_installment > buyer_salary * 0.30:
    print("❌ Loan\033[1;31m denied!\033[m The installment exceeds 30% of the buyer's salary.")
else:
    print("✅ Loan\033[1;32m approved!\033[m The installment is within the allowed range.")
