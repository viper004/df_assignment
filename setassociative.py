def set_associative_mapping(blocks, cache_size, associativity):
    # Number of sets = total cache lines / associativity (ways per set)
    num_sets = cache_size // associativity

    # Initialize cache: a list of sets, each set has 'associativity' slots initialized to None
    sets = [[None] * associativity for _ in range(num_sets)]

    print(f"Set-Associative Mapping ({associativity}-way) (no replacement)")
    print("Block\tSetIdx\tSetContents\t\tStatus")
    print("-" * 50)

    # Process each block in the reference string
    for block in blocks:
        # Find which set the block maps to
        set_idx = block % num_sets

        # Access the selected set
        current_set = sets[set_idx]

        # Check if block already exists in the set → HIT
        if block in current_set:
            status = "Hit"

        else:  # MISS case
            # If there is an empty slot (None), place the block there
            if None in current_set:
                empty = current_set.index(None)
                current_set[empty] = block
                status = "Miss (placed)"

            else:
                # Set is full and we are not doing replacement → block not inserted
                status = "Miss (set full, not placed)"

        # Print the result for this block access
        print(f"{block}\t{set_idx}\t{current_set}\t{status}")


# Example usage
blocks = [0, 1, 2, 3, 4, 0, 2]
set_associative_mapping(blocks, cache_size=4, associativity=2)
