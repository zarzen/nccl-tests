from collections import defaultdict


def main():
    """"""
    size_count = defaultdict(int)
    with open("./run.log") as ifile:
        for line in ifile:
            if "socketProgressOpt::" in line:
                splits = line.split(':')
                size = int(splits[-1])
                size_count[size] += 1
    keys = list(size_count.keys())
    total_times = sum(size_count.values())
    keys.sort()
    for k in keys:
        s = "{}, {}, {:.3f}%".format(k, size_count[k], (size_count[k]/total_times)*100)
        print(s)


if __name__ == "__main__":
    main()