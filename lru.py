cache_size = int(input("Enter cache size: "))
cache = []
hits = 0
misses = 0

refs = input("Enter memory block references (space separated): ").split()

for block in refs:
    if block in cache:
        hits += 1
        cache.remove(block)
        cache.append(block)   # move to most recently used
        print(f"Hit  -> Cache: {cache}")
    else:
        misses += 1
        if len(cache) == cache_size:
            cache.pop(0)      # remove least recently used
        cache.append(block)
        print(f"Miss -> Cache: {cache}")

print("\nTotal Hits:", hits)
print("Total Misses:", misses)
print("Hit Ratio:", hits / (hits + misses))
