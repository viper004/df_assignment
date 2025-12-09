# Direct Mapping Cache Simulation

def print_cache(cache):
    print("\nCurrent Cache State:")
    for i, line in enumerate(cache):
        print(f"Line {i}: Tag = {line['tag']}")
    print("-" * 40)


def main():
    print("=== Direct Mapping Cache Simulation ===")

    # Step 1: Input cache size
    cache_size = int(input("Enter number of cache lines: "))

    # Step 2: Initialize cache
    cache = [{"tag": None} for _ in range(cache_size)]

    while True:
        block = int(input("\nEnter block number (-1 to exit): "))

        if block == -1:
            print("Exiting simulation...")
            break

        # Step 3: Direct mapping
        line = block % cache_size

        print(f"\nBlock Number: {block}")
        print(f"Mapped Cache Line: {line}")

        # Step 4: Hit/Miss check
        if cache[line]["tag"] == block:
            print("Status: CACHE HIT ✔")
        else:
            print("Status: CACHE MISS ✘")
            print(f"Loading block {block} into line {line}...")
            cache[line]["tag"] = block

        # Step 5: Display updated cache
        print_cache(cache)


if __name__ == "__main__":
    main()
