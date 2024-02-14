from pytest import approx, raises

def test_calc_area_square():
    from calc_area import calc_area_square

    input_numbers = [0, 1, 4, 100]
    output_numbers = [0, 1, 16, 10000]
    assert len(input_numbers) == len(output_numbers)

    # option 1
    for input, output in zip(input_numbers, output_numbers):
        assert calc_area_square(input) == output

    # option 2
    for i in range(len(input_numbers)):
        this_input = input_numbers[i]
        this_exp_out = output_numbers[i]
        assert calc_area_square(this_input) == this_exp_out


def test_calc_area_circle():
     from calc_area import calc_area_circle
#### Uncomment if you want to test a list of inputs outputs in a loop
#     # input_numbers = [0, 1, 4, 100]
#     # output_numbers = [0.0, 3.141592653589793, 50.26548245743669, 31415.926535897932]

#     # for i in range(len(input_numbers)):
#     #     this_input = input_numbers[i]
#     #     this_exp_out = output_numbers[i]
#     #     assert calc_area_circle(this_input) == this_exp_out
     
     assert calc_area_circle(2) == approx(12.5663, abs = 1e-3)  # we initially fail the test because we do not have percision

def test_calc_area_circle_errors():
    from calc_area import calc_area_circle

    with raises(ValueError):
        calc_area_circle(-1)

    with raises(TypeError):
        calc_area_circle('this is not a number')


def test_calc_area_rectangle():
    from  calc_area import calc_area_rectangle
    assert calc_area_rectangle(2,2) == 4
    #assert calc_area_rectangle(2,1) == 2  # coveage changes by changing assertions




# def test_calc_area_square():
#     assert calc_area_square(1) == 1
#     assert calc_area_square(0) == 0
#     assert calc_area_square(2) == 4
#     assert calc_area_square(3) == 9


# def calc_area_circle(radii):
#     if not isinstance(radii, float):
#         raise TypeError("The radius must be a number")
#     if radii < 0:
#         raise ValueError("The radius cannot be negative")
#     areas = math.pi * radii**2
#     return areas


# def test_calc_area_circle_raises():
#     with raises(TypeError):
#         calc_area_circle("a")
#     with raises(ValueError):
#         calc_area_circle(-1)


# def test_calc_area_circle():
#     inputs = [2, 4, 10]
#     exp_output = [12.5664, 50.2655, 314.159]

#     for i, e in zip(inputs, exp_output):
#         actual_output = calc_area_circle(i)
#         assert actual_output == approx(e, rel=1e-3, abs=1e-3)
