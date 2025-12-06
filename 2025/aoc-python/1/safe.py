import logging
# Password is locked in a safe
# Safe has a dial with an arrow, dial goes from 0-99 in order

# Attached document has sequence to open, rotations start with a letter indicating direction (L == left, R == right)
# Then there is a number of clicks in said direction
# Left from 0 -> 99, right from 99 -> 0, R8 from 11 -> 19

# Dial starts pointing at 50

# But the safe is a decoy and the real password is the number of times the dial is 
# pointing at 0 after any rotation in the sequence

def abort_gracefully(msg: str):
    logging.log(msg=msg, level=logging.ERROR)
    exit(1)

def parse_dir_and_dist(rot: str):
    direction = None
    dist = None
    if rot.startswith('R'):
        direction = 1
        try:
            dist = int(rot.split('R')[1])
        except Exception as e:
            abort_gracefully(e)
    elif rot.startswith('L'):
        direction = 0
        try:
            dist = int(rot.split('L')[1])
        except Exception as e:
            abort_gracefully(e)
    else:
        abort_gracefully("Invalid direction")

    return direction, dist

def calc_num(curr_num: int, direction: int, dist: int):
    if direction:
        updated_num = (curr_num + dist) % 99
    else:
        updated_num = (curr_num - dist) % 99

    return updated_num

def main():
    curr_num = 50
    zero_count = 0
    with open("./input.txt", 'r') as f:
        for rot in f:
            # 1 -> Right, 0 -> left
            direction, dist = parse_dir_and_dist(rot=rot.upper())
            curr_num = calc_num(curr_num=curr_num, direction=direction, dist=dist)
            print(curr_num)
            if curr_num == 0:
                zero_count = zero_count + 1
    
    logging.log(msg=f"Zero count {zero_count}", level=logging.INFO)

if __name__ == "__main__":
    logging.getLogger().setLevel(level=logging.INFO)
    main()