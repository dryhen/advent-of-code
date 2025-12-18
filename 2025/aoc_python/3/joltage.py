import os
import logging

def check_bank(bank):
    highest_index = 0
    for i in range(len(bank) - 1):
        if bank[i] > bank[highest_index]:
            highest_index = i
    
    bank_spl = bank[highest_index + 1:]
    second_index = 0
    for i in range(len(bank_spl)):
        if bank_spl[i] > bank_spl[second_index]:
            second_index = i

    return int(''.join([str(bank[highest_index]), str(bank_spl[second_index])]))

# With the help of reddit... https://www.reddit.com/r/adventofcode/comments/1pcxkif/2025_day_3_mega_tutorial/
def check_bank_2(bank):
    total_joltage = 0
    batteries_remaining = 12

    offset = 0
    while batteries_remaining > 0:
        highest = None
        # If we start at 0, we'd want to choose a digit such that AT LEAST 11 digits are remaining on the right hand side
        # Therefore we subtract by "batteries_remaining + 1"
        # Once we have the first digit, we need to offset by that index so we can choose a digit after it such that AT LEAST 10
        # digits are remaining on the right hand side
        # (repeat until batteries_remaining is exhausted)
        # curr_range = [offset, len(bank)-batteries_remaining+1+(12-batteries_remaining)]
        # curr_range_vals = [bank[offset], len(bank)-batteries_remaining]
        # upper_lim = len(bank)-batteries_remaining+1+(12-batteries_remaining) if len(bank)-batteries_remaining+1+(12-batteries_remaining) < len(bank) else len(bank)
        for i in range(offset, len(bank)-batteries_remaining+1):
            if highest == None:
                highest = bank[i]
            elif bank[i] > highest:
                highest = bank[i]
                offset = i + 1 # + 1 since we don't want to include that index
                break
        total_joltage = total_joltage + (highest * (10 ** (batteries_remaining - 1)))
        batteries_remaining = batteries_remaining - 1
    
    # logging.info(total_joltage)
    return total_joltage

# Try the above with recursion...

def main():
    bank_totals_1 = []
    bank_totals_2 = []
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/./input.txt', 'r') as f:
        for bank in f:
            jolt_list = [int(c) for c in bank.strip()]
            bank_totals_1.append(check_bank(jolt_list))
            bank_totals_2.append(check_bank_2(jolt_list))
    # Add up all of the joltage
    total_joltage = sum(bank_totals_1)
    logging.info(f'Pt1.) Total joltage: {total_joltage}')

    total_joltage_2 = sum(bank_totals_2)
    logging.info(f'Pt2.) Total joltage: {total_joltage_2}')
    


if __name__ == "__main__":
    logging.getLogger().setLevel(level=logging.DEBUG)
    main()