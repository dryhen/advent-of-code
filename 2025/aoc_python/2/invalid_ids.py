import os
import logging

# Given a single line that is a comma-separated list of product ID ranges
# Invalid IDs are IDs within those ranges where there is any sequence of digits repeated twice
# E.g. 50-60 has 55, 6400-6500 has 6464, etc.

# There are no leading 0s

# The goal is to find the sum of all of the invalid IDs

# This method is very dirty but it worksed to get the solution
# def check_ids(id_range):
#     invalid_ids = []
#     # Get the ends of the range and make them integers
#     ends = id_range.split('-')
#     ends[0] = int(ends[0])
#     ends[1] = int(ends[1])
#     for id in range(ends[0], ends[1] + 1):
#         # Make the id a string so we can use string comparison
#         idstr = str(id)
#         potential_rep = ""
#         # For each digit in the ID:
#         for dig in idstr:
#             # Add the current digit to the potential repetition string
#             potential_rep = "".join([potential_rep, dig])
#             rep_twice = "".join([potential_rep, potential_rep])
#             # See if the potential repetition twice is larger than the actual ID and stop running if so
#             if len(rep_twice) > len(idstr):
#                 break
#             # If the potential repetition twice is equal to the entire id, we append the ID to our invalid IDs list
#             if idstr == rep_twice:
#                 invalid_ids.append(id)
#                 break
#     return invalid_ids

# With assistance from ChatGPT, this was the superior solution
def check_ids(id_range):
    invalid_ids = []
    start, end = map(int, id_range.split('-'))

    for id in range(start, end + 1):
        idstr = str(id)
        # If we aren't dealing with an even length ID we can skip it
        if len(idstr) % 2 == 0:
            # '//' -> integer division, Python uses float division by default
            middle = len(idstr) // 2
            # Slice the string to the "middle" index, then from the "middle" index through the end
            # comparing to see if they are the same, then adding it to the list if so
            if idstr[:middle] == idstr[middle:]:
                invalid_ids.append(id)
    
    return invalid_ids

def main():
    invalid_ids = []
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/./input.txt', 'r') as f:
        ranges = f.readline().strip().split(',')
        # For every range, find the invalid IDs and add them to our running list
        for r in ranges:
            invalid_ids.extend(check_ids(r))
    # Add up all of the invalid IDs
    sum_invalids = sum(invalid_ids)
    logging.info(f'Sum of invalid IDs from provided ranges: {sum_invalids}')
    


if __name__ == "__main__":
    logging.getLogger().setLevel(level=logging.INFO)
    main()