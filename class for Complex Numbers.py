# Define a class for Complex Numbers
class ComplexNumber:
    # Constructor to initialize real and imaginary parts
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Method to add two complex numbers
    def add(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return ComplexNumber(real_part, imag_part)

    # Method to display a complex number in a+bi format
    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
# Create two complex numbers
c1 = ComplexNumber(3, 2)  
c2 = ComplexNumber(1, 7)  

# Add the two complex numbers
result = c1.add(c2)

# Print the result
print(f"Result is: {result}")
