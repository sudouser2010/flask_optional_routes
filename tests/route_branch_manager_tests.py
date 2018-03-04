from .. optional_routes import OptionalRoutes
from . test_cases import TEST_CASES


if __name__ == '__main__':
    route_branch_manager = OptionalRoutes(None)

    for test_case in TEST_CASES:
        _input = test_case[0]
        _expected_output = test_case[1]

        actual_output = route_branch_manager.generate_optional_routes(_input)
        actual_output = set(actual_output)
        print(_input, _expected_output, actual_output)
        assert actual_output == _expected_output, "Expected Output Doesn't Match Actual"

    print('All Tests Done')
