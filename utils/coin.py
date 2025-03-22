
def half_price(value):
    half = value / 2
    return format_coin(half)

def double_price(value):
    double  = value * 2
    return format_coin(double)

def increase_percent(value, num):
    percent = (value * (num / 100)) + value
    return  format_coin(percent)

def decreases_percent(value, num):
    percent =  value - (value * (num / 100))
    return format_coin(percent)

def format_coin(value):
    return f'${value:.2f}'

def resume(value, decrease_num, increase_num):
    print(f'The half of {format_coin(value)} is {half_price(value)}')
    print(f'The double of {format_coin(value)} is {double_price(value)}')
    print(f'Increasing 10% of {format_coin(value)} we have {increase_percent(value, increase_num)}')
    print(f'Decreasing 13% of {format_coin(value)} we have {decreases_percent(value, decrease_num)}')