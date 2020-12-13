def next_stop(min_time, bus):
    rem = min_time % bus
    wait_time = bus - rem
    return bus, wait_time


def compute(data):
    """
    >>> compute(["939", "7,13,x,x,59,x,31,19"])
    295
    """
    depart_time = int(data[0])
    buses = [int(b) for b in data[1].split(",") if b != "x"]

    bus, wait_time = min(
        (next_stop(depart_time, bus) for bus in buses),
        key=lambda b_wait_time: b_wait_time[1],
    )

    return bus * wait_time


def main():
    import pathlib

    input_path = pathlib.Path(__file__).with_name("input.txt")

    with input_path.open() as f:
        print(compute(f.read().strip().splitlines()))


if __name__ == "__main__":
    main()
