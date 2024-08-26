# def number_to_output(number):
#   output_dict = {3: '101', 5: '10101', 12: '101010101010', 26: '10101010101010101010101010', 28: '1010101010101010101010101010'}
#   return output_dict[number]

# while True:
#   input_number = int(input("Enter a number (1, 2, 3, or 4): "))

#   if input_number not in [1, 2, 3, 4]:
#     print("Invalid input. Please enter a number between 1 and 4.")
#     continue

#   output_string = number_to_output(input_number)

#   print(f"The output for {input_number} is: {output_string}")

# def stringy(size: int):
#   """
#   Generates a string of alternating 1s and 0s of the given size, starting with 1.

#   Args:
#       size: The size of the desired string (positive integer).

#   Returns:
#       A string of alternating 1s and 0s.
#   """
#   # Validate input size
#   if size <= 0:
#     raise ValueError("Size must be a positive integer.")

#   # Build the string using list comprehension
#   return ''.join(['1' if i % 2 == 0 else '0' for i in range(size)])

# # Example usage
# print(stringy(6))   # Output: 101010
# print(stringy(4))   # Output: 1010
# print(stringy(12))  # Output: 101010101010


# Recently you had a quarrel with your math teacher. Not only that nerd demands knowledge of all the theorems, but he turned to be an constructivist devotee! After you recited by heart Lagranges theorem of sum of four squares, he now demands a computer program to obtain such a decomposition, so that to see that you really understand a topic. What a downer!

# You remember well the theorem. Any positive integer can be decomposed into a sum of four squares of integers. Seems not too hard... But after a quarrel, your teacher wants blood. Apparently he will test your program on extremely huge numbers... And your program better finished working before the break - you don't want to get F, do you?

# Tip: random tests feature 20 numbers as high as 2^128 and 20 number as high as 2^1024.

# from typing import Tuple


# def four_squares(n: int) -> Tuple[int, int, int, int]:
#     return 0, 0, 0, 0


# from solution import four_squares

# @test.describe("Static tests")
# def static_tests():
#     for i in [0, 1, 17, 33, 215, 333, 2**12-3, 1234567890, 106369249365575352836589875696130383747]:
#         a, b, c, d = four_squares(i)
#         error_msg = None
#         if type(a) is not int: error_msg = "1st square is not of type int"
#         if type(b) is not int: error_msg = "2nd square is not of type int"
#         if type(c) is not int: error_msg = "3rd square is not of type int"
#         if type(d) is not int: error_msg = "4th square is not of type int"
#         s = a * a + b * b + c * c + d * d
#         if s != i: 
#             error_msg = f"Incorrect sum.\nSquares: [{a}, {b}, {c}, {d}]\nActual: {a * a + b * b + c * c + d * d}\nExpected: {i}"
#         if error_msg is not None:
#             test.fail(error_msg)
#         else:
#             test.pass_()
