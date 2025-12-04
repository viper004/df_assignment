cache = ["A", "B", "C"]     # initial cache
print(cache)

new = "D"
print(f"{new} is the new cache element")

# LRU = last element, so remove it
lru = cache.pop()           
cache.append(new)

print(f"{cache} is the new cache since {lru} is least recently used")
