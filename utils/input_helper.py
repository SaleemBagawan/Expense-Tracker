def get_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Please enter a valid number:')

def get_string_input(message):
    while True:
        value = input(message)
        if value: return value
        print('Input cannot be empty:')

        
        

