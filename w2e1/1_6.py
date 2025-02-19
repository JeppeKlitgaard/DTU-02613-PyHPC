import sys

if __name__ == "__main__":
    raw_ins = sys.argv[1:]
    ins = [int(x) for x in raw_ins]

    filter_even = lambda x: x % 2 == 0
    outs = list(filter(filter_even, ins))

    print(outs)
