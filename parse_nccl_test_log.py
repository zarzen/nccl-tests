import sys


def convert_size(s):
    s = int(s)
    s /= 1024
    if s < 1024:
        return "{}KB".format(s)
    else:
        s /= 1024
        if s < 1024:
            return "{}MB".format(s)
        else:
            return None


def main():
    filename = sys.argv[1]


    with open(filename) as ifile:
        sizes = []
        bws = []
        for line in ifile:
            if not line.startswith("#"):
                entry = line.strip('\n').strip(' ').split(' ')
                entry = list(filter(lambda x: x != ' ' and x != '', entry))
                size = entry[0]
                bus_bw = float(entry[6]) * 8 # convert to Gbps
                sizes.append(convert_size(size))
                bws.append(bus_bw)
    
    print(sizes)
    print(bws)

if __name__ == "__main__":
    main()
