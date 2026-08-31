def count_pairs_slow(numbers, target):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i]  +  numbers[j]  ==  target:
                count  += 1
    return count
def count_pairs_fast(numbers, target):
    count = 0
    seen = set()
    for num in numbers:
        needed = target - num
        if needed in seen:
            count += 1
        seen.add(num)
    return count    
        


sizes = [1000, 5000, 10000]

import time
for size in sizes:
    numbers = list(range(size))
    target = size

    start = time.perf_counter()
    count_pairs_slow(numbers, target)
    end = time.perf_counter()

    print(f"Slow - Size {size}: {end - start:.6f} seconds")

    start = time.perf_counter()
    count_pairs_fast(numbers, target)
    end = time.perf_counter()

    print(f"Fast - Size {size}: {end - start:.6f} seconds")
    print()
