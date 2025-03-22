
def validation(message):
    while True:
        enter_user = input(message).strip().replace(',', '.')
        if enter_user.isalpha():
            print(f'\033[31mError: "{enter_user}" is not a valid price\033[m')
        else:
            return float(enter_user)



