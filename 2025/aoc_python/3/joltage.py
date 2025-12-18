import os
import logging

# Each line is a "bank" of batteries
# Need to turn on two batteries in each bank such that the "joltage" of each battery selected (a number from 1-9)
# Places the two greatest values together (side by side) to create a 2 digit number

# Then we add these sums up

# Is there an opporunity for recursion somewhere to speed this up?

# Python has a built in "max" function, but I wanted to know I could still write out this logic....
# ...that being said there has to have been a cleaner way
# def check_bank(bank: str):
#     highest = [0, bank[0]]
#     second_highest = [None, None]
#     for i in range(1, len(bank)):
#         curr_jolt = bank[i]
#         if curr_jolt > highest[1]:
#             second_highest[1] = highest[1]
#             second_highest[0] = highest[0]
#             highest[1] = curr_jolt
#             highest[0] = i
#         elif second_highest[1] == None or curr_jolt > second_highest[1]:
#             second_highest[1] = curr_jolt
#             second_highest[0] = i

#     return int(''.join([str(highest[1]), str(second_highest[1])]) if highest[0] < second_highest[0] else ''.join([str(second_highest[1]), str(highest[1])]))

# Even using max() it's still flawed...
def check_bank(bank: str):
    highest = max(bank)
    highest_i = bank.index(highest)
    
    bank_modified = bank
    bank_modified[highest_i] = 0

    second_highest = max(bank)
    second_highest_i = bank.index(second_highest)

    return int(''.join([str(highest), str(second_highest)]) if highest_i < second_highest_i else ''.join([str(second_highest), str(highest)]))



def main():
    bank_totals = []
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/./input.txt', 'r') as f:
        for bank in f:
            jolt_list = [int(c) for c in bank.strip()]
            bank_totals.append(check_bank(jolt_list))
    # Add up all of the joltage
    total_joltage = sum(bank_totals)
    logging.info(f'Total joltage: {total_joltage}')
    


if __name__ == "__main__":
    logging.getLogger().setLevel(level=logging.INFO)
    main()