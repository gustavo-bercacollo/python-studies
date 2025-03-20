# Python Exercise #101 - Voting Functions

def check_voting_eligibility(birth_year):
    from datetime import date
    current_year = date.today().year
    age = current_year - birth_year

    print(f'With {age} years: ', end='')
    if 18 <= age < 65 :
        return 'MANDATORY VOTE'
    elif 16 <= age < 18 or age > 65:
        return 'OPTIONAL VOTING'
    else:
        return 'DO NOT VOTE'



print(check_voting_eligibility(int(input('What year were you born? '))))