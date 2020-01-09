def my_decorator(func):
    def wrapper():
        print("Algo está sucediendo antes de que se llame a la función")
        func()
        print("Algo está sucediendo después de que se llama a la función")
    return wrapper


@my_decorator 
def  say_whee (): 
    print ( "¡Whee!" )



say_whee() 