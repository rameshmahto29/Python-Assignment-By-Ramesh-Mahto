def mod_div(fun):
    def denol(a, b):
        if a < b:
            a, b = b, a
        return fun(a, b)
    return denol
@mod_div
def div(a, b):
    return a // b
a, b = map(int, input("Enter Numerator And Denominator Respectively : ").split())
print(div(a, b))