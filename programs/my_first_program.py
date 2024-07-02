from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Complex arithmetic operations
    addition = my_int1 + my_int2
    subtraction = my_int1 - my_int2
    multiplication = my_int1 * my_int2
    division = my_int1 / my_int2  # Note: Ensure my_int2 is not zero to avoid division by zero error
    modulus = my_int1 % my_int2

    return [
        Output(addition, "addition_output", party1),
        Output(subtraction, "subtraction_output", party1),
        Output(multiplication, "multiplication_output", party1),
        Output(division, "division_output", party1),
        Output(modulus, "modulus_output", party1)
    ]
