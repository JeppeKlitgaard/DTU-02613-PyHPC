import sys

if __name__ == "__main__":
    raw_grades = sys.argv[1:]
    grades = [float(x) for x in raw_grades]

    N = len(grades)
    s = sum(grades)
    mean = s/N

    status = "Pass" if mean >= 5 else "Fail"

    print(f"{mean:.2f} {status}")
