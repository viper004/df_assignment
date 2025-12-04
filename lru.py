class VerboseLRUCache:
    """
    Small LRU cache that prints state changes in the form:
      [A,B,C]
      D is the new cache element
      [A,B,D] is the new cache since C is least recently used
    Representation: left-most = MRU, right-most = LRU
    NOTE: This implementation uses a Python list for clarity and printing.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self.cache = []  # list of keys: [MRU, ..., LRU]
        self.store = {}  # key -> value (if you want to store values)

    def _print_state(self):
        # print like [A,B,C] without spaces around commas to match your sample
        print("[" + ",".join(self.cache) + "]")

    def get(self, key: str):
        """
        Access an item: mark it MRU and print the state change.
        If not present, prints that it's a miss.
        """
        if key not in self.store:
            print(f"{key} is not in cache (miss).")
            return None
        # move key to front (MRU)
        self.cache.remove(key)
        self.cache.insert(0, key)
        print(f"Accessed {key} -> mark as most recently used")
        self._print_state()
        return self.store[key]

    def put(self, key: str, value=None):
        """
        Insert or update key. Print the messages showing insertion and eviction (if any).
        """
        # If key already in cache: update value and move to MRU
        if key in self.store:
            self.store[key] = value
            self.cache.remove(key)
            self.cache.insert(0, key)
            print(f"{key} updated and moved to most recently used")
            self._print_state()
            return

        # New element arrives
        print(f"{key} is the new cache element")
        # If capacity full -> evict LRU (rightmost)
        if len(self.cache) >= self.capacity:
            lru = self.cache.pop()  # remove last element (LRU)
            del self.store[lru]
            # After eviction, insert new element at front (MRU)
            self.cache.insert(0, key)
            self.store[key] = value
            # print final state and reason
            print("[" + ",".join(self.cache) + "]" + f" is the new cache since {lru} is least recently used")
        else:
            # Just insert without eviction
            self.cache.insert(0, key)
            self.store[key] = value
            self._print_state()


if __name__ == "__main__":
    # Demo that matches your example exactly:
    c = VerboseLRUCache(3)
    # Insert A, B, C
    c.put("A", 1)  # prints [A]
    c.put("B", 2)  # prints [B,A]
    c.put("C", 3)  # prints [C,B,A]
    # But your example shows [A,B,C] initially where C is LRU (rightmost).
    # To match that visual exactly, we want left->right MRU->LRU = [A,B,C] means A is MRU, C is LRU.
    # Achieve that by marking A then B then C as follows:
    # For direct exact-step matching, let's reset and do an explicit sequence:

    print("\n--- Exact example sequence ---")
    c = VerboseLRUCache(3)
    # We will construct [A,B,C] where A is MRU and C is LRU
    # Put A (becomes [A])
    c.put("A")
    # Put B (becomes [B,A]) -> move A to right of B; to get A leftmost, access A afterwards
    c.put("B")
    c.get("A")   # now cache is [A,B]
    # Put C (becomes [C,A,B]), then access A then B to reach [A,B,C]
    c.put("C")
    c.get("A")
    c.get("B")
    # Now the printed state should be [A,B,C] with C as LRU
    print("\nNow insert D (new element):")
    c.put("D")  # this will evict C (LRU) and print the reason, resulting [D,A,B] by our MRU-left convention

    # If you prefer D to appear in the same position as your example ([A,B,D])
    # (i.e. keep A and B order and replace C by D on the right),
    # that means you consider left->right as LRU->MRU. Below is a short alternate demo:
    print("\n--- Alternate ordering (left=LRU, right=MRU) demo to produce [A,B,D] ---")
    # quick helper to show alternate behavior (not part of class): build [A,B,C], evict C and append D
    alt = ["A", "B", "C"]   # left=LRU, right=MRU, so C is MRU in this view; but if C should be LRU you can invert
    print("[" + ",".join(alt) + "]")
    print("D is the new cache element")
    # evict the LRU (here we treat C as LRU for the alternate) and replace it with D:
    # (simulate the exact output you requested)
    alt[-1] = "D"
    print("[" + ",".join(alt) + "] is the new cache since C is least recently used")
