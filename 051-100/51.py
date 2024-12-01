# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

# for i in range(10):
#     for j in range(1, 10 + 1):
#         x = i * 10 + j
#         print(f"{x}".zfill(2) + " ", end="")
#     print()


def get_numbers_containing_zeroes():
    i = 10
    yield i

    while True:
        istr = str(i)
        # If we have only 1 0, increment the first non-zero digit starting from the right (smallest place value)
        if istr.count("0") == 1:
            # If we have just 1 0, then it will either be the last value, in which case we increment the second to last value
            if istr[-1] == "0":
                i += 10
            # Or it will be somewhere else, and we just increment the last value
            else:
                i += 1
        # Otherwise we increment the first digit after we find a zero starting from the right (smallest place value)
        else:
            for k in range(len(istr) - 1, -1, -1):
                if istr[k] == "0":
                    break
            # Convert string index of first zero digit, to the place value of the column
            # e.g. 100,    k = 2, num_to_add = 1
            #      400334, k = 2, num_to_add = 1000
            num_to_add = 10 ** (len(istr) - k - 1)
            i += num_to_add
        yield i


gen = get_numbers_containing_zeroes()

zz = 0
num_zero_nums = 0
while num_zero_nums < 183:
    zz += 1
    if "0" in str(zz):
        print(zz, next(gen))
        num_zero_nums += 1
