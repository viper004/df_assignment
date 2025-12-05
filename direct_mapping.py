# Basic Direct Mapping Example

cache_size = int(input("Enter number of cache lines: "))
block = int(input("Enter memory block number: "))

cache_line = block % cache_size

print(f"Block {block} will go to Cache Line {cache_line}")
