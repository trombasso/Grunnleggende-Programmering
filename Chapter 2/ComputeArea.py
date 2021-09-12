circleRadius = float(input("Please enter circle radius (cm): "))
if circleRadius < 0:
    print("Incorrect input (number must be a positive integer)")
else:
    area = circleRadius * circleRadius * 3.14159
    print(f'The area of the circle is approx. {area:.0f} cm3')