math_equation=input()
math_equation=math_equation.replace("+", "")
math_equation=sorted(math_equation)
print("+".join(math_equation))