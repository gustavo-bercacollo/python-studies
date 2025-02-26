# Exercise Python #018 - Sine, Cosine, and Tangent

from math import radians, cos, sin, tan

angle = radians(float(input('Enter the angle in degrees: ')))

sine = sin(angle)
cosine = cos(angle)
tangent = tan(angle)

print(f'Sine: {sine:.2f}\nCosine: {cosine:.2f}\nTangent: {tangent:.2f}')