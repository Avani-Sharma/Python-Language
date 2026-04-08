# variable length keyword arguments: in which we can key and value pairs as much we want variable,
# it returns the data in the form of dictionary

def details(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} -> {value}')
    return kwargs
details(name = 'avani', batch = 'a23', location = 'bhiwadi')