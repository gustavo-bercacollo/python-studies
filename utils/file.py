from utils.helpers import format_title

def exist_file(name):
    try:
        file = open(name, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True

def create_file(name):
    try:
        file = open(name, 'wt+')
        file.close()
    except:
        print('error! in create file')
    else:
        print(f'file {name} create successfully')


def read_file(name):
    try:
        file = open(name)

    except:
        print('Error in read file!')
    else:
        format_title('PEOPLE REGISTERED')

        lines = file.readlines()
        if not lines:
            print('No people.')
            return

        for i in lines:
            data = i.split(';')
            data[1] = data[1].replace('\n','')
            print(f'{data[0]:<20}{data[1]} years')
    finally:
        file.close()


def register_new_person(file_name, name, age):
    try:
        file = open(file_name, 'at')
    except:
        print('Error, in open file')
    else:
        try:
            file.write(f'{name:};{age}\n')
        except:
            print('Error, in write')
        else:
            print(f'New register {name} add')
            file.close()