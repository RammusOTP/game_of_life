from test_funcs import *
from colours import RED, GREEN, RESET

def run_tests():
    """
    Iterates through the tests made in test_funcs.py and prints a nicer error message if failed.

    :return: PASSED or FAILED with error message
    """
    test_functions = [test_update_without_progress, test_update_with_progress]

    passed_tests = 0
    total_tests = len(test_functions)

    for test_func in test_functions:
        try:
            test_func()
            print(f"{GREEN}[PASSED]{test_func.__name__}{RESET}")
            passed_tests += 1
        except AssertionError as e:
            print(f"{RED}[FAILED]{test_func.__name__}: {e}{RESET}")

    print(f"\n{passed_tests}/{total_tests} tests passed.")


if __name__ == "__main__":
    run_tests()
