# Exercise Python #022 - Text Analyzer

name = str(input('Enter your full name: ')).strip()
name_upper = name.upper()
name_lower = name.lower()
letters = len(name.replace(' ', ''))
firth_name = name.split()[0]
firth_name_count = len(firth_name)


print(
    f"""
    Analysing your name...
    Your upper name is {name_upper}
    Your lower name is {name_lower}
    Your name has a total of {letters} letters
    Your firth name is {firth_name} and its have {firth_name_count} letters
    """
)