#!/usr/bin/env python3

weight = int(input())
height = int(input())
BMI = weight / (height * height) * 10000

if BMI < 18.5:
    print("underweight")
elif BMI >= 18.5 and BMI <= 24.99:
    print("normal")
elif BMI >= 25 and BMI <= 29.99:
    print("overweight")
else:
    print("obese")
