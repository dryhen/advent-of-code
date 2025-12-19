import pytest
from joltage import check_bank, check_bank_2

testing_data = [
    {"input": [7,2,2,5,8,1], "expected_result": 81},
    {"input": [0,1,7,0,0,0], "expected_result": 70},
    {"input": [0,0,0,0,0,0], "expected_result": 0},
    {"input": [9,9,9,9,9,9], "expected_result": 99},
    {"input": [9,1,5,6,4,8,7,8], "expected_result": 98},
    {"input": [8,1,5,6,4,5,7,8], "expected_result": 88},
    {"input": [1,1,5,8,8,5,7,1], "expected_result": 88}
]

testing_data_2 = [
    {"input": [7,2,2,5,8,1,2,3,6,7,4,9,0,1,2,3], "expected_result": 812367490123},
    {"input": [7,2,8,2,5,4,1,2,3,6,7,4,9,0,1,9,2,3,3,3,4,9,2,2,2,2,1,3], "expected_result": 993349222213},
]

def test_check_bank():
    for data in testing_data:
        assert check_bank(data["input"]) == data["expected_result"]

def test_check_bank_2():
    for data in testing_data_2:
        assert check_bank_2(data["input"], 12) == data["expected_result"]