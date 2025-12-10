def set_associative_mapping(blocks, cache_size, associativity):
    num_sets = cache_size // associativity
    sets = [[None] * associativity for _ in range(num_sets)]

    print(f"Set-Associative Mapping ({associativity}-way) (no replacement)")
    print("Block\tSetIdx\tSetContents\t\tStatus")
    print("-" * 50)

    for block in blocks:
        set_idx = block % num_sets
        current_set = sets[set_idx]

        if block in current_set:
            status = "Hit"
        else:
            if None in current_set:
                empty = current_set.index(None)
                current_set[empty] = block
                status = "Miss (placed)"
            else:
                status = "Miss (set full, not placed)"

        print(f"{block}\t{set_idx}\t{current_set}\t{status}")


# Example
blocks = [0, 1, 2, 3, 4, 0, 2]
set_associative_mapping(blocks, cache_size=4, associativity=2)
