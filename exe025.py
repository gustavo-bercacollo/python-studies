# Exercise Python #025 - Searching for a String within Another

full_name = str(input("Enter your full name: ")).strip().lower()

check_word = "silva" in full_name

print(f"Does your name have 'Silva'? {check_word}")
