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

# Built with the help of reddit... https://www.reddit.com/r/adventofcode/comments/1pcxkif/2025_day_3_mega_tutorial/
def check_bank_2(bank, battery_count):
    total_joltage = 0
    bank_length = len(bank)
    batteries_remaining = battery_count
    offset = 0
    while batteries_remaining > 0:
        highest = None
        # If we start at 0, we'd want to choose a digit such that AT LEAST 11 digits are remaining on the right hand side
        # Therefore we subtract by "batteries_remaining + 1"
        # Once we have the first digit, we need to offset by that index so we can choose a digit after it such that AT LEAST 10
        # digits are remaining on the right hand side
        # (repeat until batteries_remaining is exhausted)
        upper_lim = bank_length-batteries_remaining+1
        for i in range(offset, upper_lim):
            if highest == None or int(bank[i]) > highest:
                highest = int(bank[i])
                offset = i + 1 # + 1 since we don't want to include that index
        # If batteries_remaining is n, 10^(n-1) gives us the necessary amount of right hand zeroes to place our digit correctly
        total_joltage = total_joltage + (highest * (10 ** (batteries_remaining - 1)))
        batteries_remaining = batteries_remaining - 1
    return total_joltage

# Try the above with recursion?
# def check_bank_2(bank, batteries_remaining):
#     if batteries_remaining == 0:
#         return 0
#     if batteries_remaining == len(bank):
#         return

#     return max()
#... only day 3 and my brain hurts

def main():
    bank_totals_1 = []
    bank_totals_2 = []
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/./input.txt', 'r') as f:
        for bank in f:
            jolt_list = [int(c) for c in bank.strip()]
            bank_totals_1.append(check_bank(jolt_list))
            # bank_totals_2.append(check_bank_2(jolt_list))
            # bank_totals_1.append(check_bank(bank))
            bank_totals_2.append(check_bank_2(bank.strip(), 12))
    # Add up all of the joltage
    total_joltage = sum(bank_totals_1)
    logging.info(f'Pt1.) Total joltage: {total_joltage}')

    total_joltage_2 = sum(bank_totals_2)
    logging.info(f'Pt2.) Total joltage: {total_joltage_2}')
    


if __name__ == "__main__":
    logging.getLogger().setLevel(level=logging.DEBUG)
    main()