import pytest
from joltage import check_bank

testing_data = [
    {"input": [7,2,2,5,8,1], "expected_result": 78},
    {"input": [0,1,7,0,0,0], "expected_result": 17},
    {"input": [0,0,0,0,0,0], "expected_result": 0},
    {"input": [9,9,9,9,9,9], "expected_result": 99},
    {"input": [9,1,5,6,4,8,7,8], "expected_result": 98},
    {"input": [8,1,5,6,4,5,7,8], "expected_result": 88},
    {"input": [1,1,5,8,8,5,7,1], "expected_result": 88}
]

def test_check_bank():
    for data in testing_data:
        assert check_bank(data["input"]) == data["expected_result"]

# def test_check_bank_0():
#     assert check_bank(testing_data[0]["input"]) == testing_data[0]["expected_result"]

# def test_check_bank_1():
#     assert check_bank(testing_data[1]["input"]) == testing_data[1]["expected_result"]

# def test_check_bank_2():
#     assert check_bank(testing_data[2]["input"]) == testing_data[2]["expected_result"]

# def test_check_bank_3():
#     assert check_bank(testing_data[3]["input"]) == testing_data[3]["expected_result"]

# def test_check_bank_4():
#     assert check_bank(testing_data[4]["input"]) == testing_data[4]["expected_result"]

# def test_check_bank_5():
#     assert check_bank(testing_data[5]["input"]) == testing_data[5]["expected_result"]

# def test_check_bank_6():
#     assert check_bank(testing_data[6]["input"]) == testing_data[6]["expected_result"]