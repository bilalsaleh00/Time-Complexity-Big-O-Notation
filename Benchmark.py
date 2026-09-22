import time


def has_duplicates_slow(data):
    """
    O(n^2)
    Check every pair using nested loops.
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return True

    return False


def has_duplicates_fast(data):
    """
    O(n)
    Use a set to track values already seen.
    """
    seen = set()

    for value in data:
        if value in seen:
            return True

        seen.add(value)

    return False


sizes = [1000, 5000, 10000]


for size in sizes:
    data = list(range(size))

    # Guaranteed duplicate at the end
    data.append(0)

    print(f"\n=== Size: {size} ===")

    # Slow version
    start = time.perf_counter()

    slow_result = has_duplicates_slow(data)

    end = time.perf_counter()

    print(
        f"Slow O(n^2): "
        f"{slow_result} - "
        f"{end - start:.6f} seconds"
    )


    # Fast version
    start = time.perf_counter()

    fast_result = has_duplicates_fast(data)

    end = time.perf_counter()

    print(
        f"Fast O(n): "
        f"{fast_result} - "
        f"{end - start:.6f} seconds"
    )