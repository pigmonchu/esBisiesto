def esBisiesto(n):
    return n % 4 == 0 or (n % 400 == 0 and n % 100 != 0)

def esEntero(n):
    try:
        n = int(n)
        return True
    except ValueError:
        return False
        