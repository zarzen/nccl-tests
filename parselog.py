from collections import defaultdict
import sys

def main():
    """"""
    size_count = defaultdict(int)
    filename = sys.argv[1]
    send_4 = 0
    recv_4 = 0
    persistentSocketThread_sizes = defaultdict(int)
    with open(filename) as ifile:
        for line in ifile:
            if "socketProgressOpt:: op" in line:
                splits = line.split(':')
                size = int(splits[-1])
                size_count[size] += 1
            elif "bootstrapNetSend:" in line:
                send_4 += 1
            elif "bootstrapNetRecv" in line:
                recv_4 += 1
            elif "persistentSocketThread" in line:
                splits = line.split('size')
                size = int(splits[-1])
                persistentSocketThread_sizes[size] += 1

    keys = list(size_count.keys())
    total_times = sum(size_count.values())
    keys.sort()
    total_size = 0
    for k in keys:
        s = "{}, {}, {:.3f}%".format(k, size_count[k], (size_count[k]/total_times)*100)
        print(s)
        total_size += (k * size_count[k])
    print('transfer send/recv', total_size / 1e6, "MB")
    print('send 4', send_4, 'recv_4', recv_4)
    print(persistentSocketThread_sizes)

if __name__ == "__main__":
    main()