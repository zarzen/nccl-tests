import json
import sys

def extract_raw_data(event_name, line):
    idx = line.index(event_name)
    data = line[idx+len(event_name):].strip('\n').strip(' ')
    fields = data.split(',')
    raw = {}
    for f in fields:
        name, val = f.strip(' ').split(' ')
        if name in ('op', 'fd', 'size', 'offset', 'block'):
            val = int(val)
        elif name in ('ts'):
            val = float(val)
        else:
            pass
        raw[name] = val
    return raw 


def main():
    filename = sys.argv[1]
    output_name = filename + ".trace.json"
    traces = []
    with open(filename) as ifile:
        socketEvent = "socketProgressOpt::"
        for line in ifile:
            if socketEvent in line:
                raw = extract_raw_data(socketEvent, line)
                op_event = 'SEND' if raw['op'] == 0 else "RECV"
                entry = {
                    'name': 'socketProgressOpt-'+op_event, 'ph': raw['ph'], 
                    'tid': raw['fd'], 'pid': 1, 'ts': raw['ts']*1e6, 
                    'args': {'size': raw['size'], 'offset': raw['offset'], 'block': raw['block']}}
                traces.append(entry)
            elif "ncclSocketTest::" in line:
                raw = extract_raw_data("ncclSocketTest::", line)
                op_event = 'SEND' if raw['op'] == 0 else "RECV"
                entry = {
                    'name': 'ncclSocketTest-'+op_event, 'ph': raw['ph'], 
                    'tid': raw['fd'], 'pid': 1, 'ts': raw['ts']*1e6, 
                    'args': {'size': raw['size'], 'offset': raw['offset'], 'block': raw['block']}}
                traces.append(entry)
    
    with open(output_name, 'w') as ofile:
        json.dump(traces, ofile )

if __name__ == "__main__":
    main()