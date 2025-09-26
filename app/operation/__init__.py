# operations.py

class Operation:
    """
    The Operation class encapsulates basic arithmetic operations as static methods.
    This design groups related functions (addition, subtraction, multiplication, division, and power) 
    in a single class, making the code more modular and organized.

    **Object-Oriented Programming (OOP) Principles Illustrated:**
    - **Encapsulation:** This class groups all arithmetic operations together, making it easier 
      to maintain, test, and reuse these methods in other parts of the code.
    - **Abstraction:** Users of this class only need to know the function names and purpose, 
      not how they work internally.
    - **Reusability:** Static methods can be called directly on the class without creating an instance, 
      making it straightforward to reuse these methods anywhere.
    - **Organization:** By placing all basic operations in a single class, the code becomes 
      more structured and readable.
    
    **Why Static Methods?**
    - **Statelessness**: These methods do not rely on any instance-specific data; they only 
      depend on input parameters. Static methods are ideal for utility functions that 
      perform independent operations.
    - **Ease of Access**: Because we don’t need to create an instance of Operation to call 
      these methods, it’s easy to use them across different parts of the program.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        Adds two floating-point numbers and returns the result.

        **Parameters:**
        - `a (float)`: The first number to add.
        - `b (float)`: The second number to add.
        
        **Returns:**
        - `float`: The sum of `a` and `b`.

        **Example:**
        >>> Operation.addition(5.0, 3.0)
        8.0
        """
        return a + b  # Performs addition of two numbers and returns the result.
    
    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        Subtracts the second floating-point number from the first and returns the result.

        **Parameters:**
        - `a (float)`: The number from which to subtract.
        - `b (float)`: The number to subtract.
        
        **Returns:**
        - `float`: The difference between `a` and `b`.

        **Example:**
        >>> Operation.subtraction(10.0, 4.0)
        6.0
        """
        return a - b  # Subtracts the second number from the first and returns the difference.
    
    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        Multiplies two floating-point numbers and returns the product.

        **Parameters:**
        - `a (float)`: The first number to multiply.
        - `b (float)`: The second number to multiply.
        
        **Returns:**
        - `float`: The product of `a` and `b`.

        **Example:**
        >>> Operation.multiplication(2.0, 3.0)
        6.0
        """
        return a * b  # Multiplies the two numbers and returns the product.
    
    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Divides the first floating-point number by the second and returns the quotient.

        **Parameters:**
        - `a (float)`: The dividend.
        - `b (float)`: The divisor.
        
        **Returns:**
        - `float`: The quotient of `a` divided by `b`.

        **Raises:**
        - `ValueError`: If the divisor `b` is zero, as division by zero is undefined.

        **Example:**
        >>> Operation.division(10.0, 2.0)
        5.0
        >>> Operation.division(10.0, 0.0)
        Traceback (most recent call last):
            ...
        ValueError: Division by zero is not allowed.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")  # Raises an error if division by zero is attempted.
        return a / b  # Divides `a` by `b` and returns the quotient.

    @staticmethod
    def power(a: float, b: float) -> float:
        """
        Raises the first floating-point number to the power of the second and returns the result.

        **Parameters:**
        - `a (float)`: The base number.
        - `b (float)`: The exponent.
        
        **Returns:**
        - `float`: The result of `a` raised to the power of `b`.

        **Example:**
        >>> Operation.power(2.0, 3.0)
        8.0

        **Design Insight: Why Include Power in Basic Operations?**
        - Exponentiation is a fundamental arithmetic operation, especially in scientific and financial calculations.
        - Including it in the `Operation` class keeps all core math utilities centralized and consistent.
        """
        return a ** b  # Raises `a` to the power of `b` and returns the result.
    
    @staticmethod
    def root(a: float, b: float) -> float:
       """
    Computes the b-th root of the first floating-point number and returns the result.

    **Parameters:**
    - `a (float)`: The radicand (number under the root).
    - `b (float)`: The degree of the root.

    **Returns:**
    - `float`: The b-th root of `a`, equivalent to `a ** (1 / b)`.

    **Example:**
    >>> Operation.root(27.0, 3.0)
    3.0

    **Design Insight: Why Include Root in Basic Operations?**
    - Root extraction is the inverse of exponentiation and essential in algebraic, geometric, and statistical computations.
    - Including it in the `Operation` class ensures symmetry with `power`, supporting both forward and inverse exponential logic.
    """
       if b == 0:
         raise ValueError("Cannot compute zeroth root.")
         return a ** (1 / b)  # Computes the b-th root of `a`.

