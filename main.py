from action import *

f_inp = int(input("Enter a number:"))
s_inp = int(input("Enter a number:"))
o_inp = input("Choose Operator | + - * /")

if o_inp == "+":
    res = add(f_inp, s_inp)
    print(res)
if o_inp == "-":
    res = sub(f_inp, s_inp)
    print(res)
if o_inp == "*":
    res = mul(f_inp, s_inp)
    print(res)
if o_inp == "/":
    res = div(f_inp, s_inp)
    print(res)

