def set_associative_mapping(blocks, cache_size, associativity):
    # Number of sets = total cache lines / associativity
    num_sets = cache_size // associativity

    # Initialize cache: list of sets, each with 'associativity' slots
    sets = [[None] * associativity for _ in range(num_sets)]

    print(f"\nSet-Associative Mapping ({associativity}-way)")
    print("Block\tSetIdx\tSetContents\t\tStatus")
    print("-" * 60)

    hits = 0
    misses = 0

    for block in blocks:
        set_idx = block % num_sets
        current_set = sets[set_idx]

        if block in current_set:
            status = "Hit"
            hits += 1
        else:
            misses += 1
            if None in current_set:
                empty = current_set.index(None)
                current_set[empty] = block
                status = "Miss (placed)"
            else:
                status = "Miss (set full, not placed)"

        print(f"{block}\t{set_idx}\t{current_set}\t{status}")

    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0

    print("\nSummary:")
    print(f"Total Accesses: {total}")
    print(f"Hits: {hits}")
    print(f"Misses: {misses}")
    print(f"Hit Ratio: {hit_ratio:.2%}")


# Input memory block sequence
blocks_input = input("Enter block sequence (comma-separated): ")
blocks = [int(x.strip()) for x in blocks_input.split(",")]

# Input cache size
cache_size = int(input("Enter cache size (number of lines): "))

# Input associativity value
associativity = int(input("Enter associativity (ways): "))

# Run the mapping function
set_associative_mapping(blocks, cache_size, associativity)
