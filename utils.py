def get_int_input(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print('Please enter a valid number.')

def get_string_input(text):
    while True:
        value = input(text)
        if not value:
            print('Please enter something:')
        else:
            return value