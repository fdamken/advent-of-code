import math


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        earliest_timestamp = int(lines[0])
        bus_ids = [int(bus_id) for bus_id in lines[1].split(',') if bus_id != 'x']

    bus_id_wait_minutes = []
    for bus_id in bus_ids:
        wait_minutes = int(math.ceil(earliest_timestamp / bus_id)) * bus_id - earliest_timestamp
        bus_id_wait_minutes.append((bus_id, wait_minutes))

    min_bus_id, min_wait_minutes = min(bus_id_wait_minutes, key=lambda x: x[1])
    print('Result: %d' % (min_bus_id * min_wait_minutes))


if __name__ == '__main__':
    main()
