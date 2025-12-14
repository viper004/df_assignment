from collections import deque
class CacheLine:
    def __init__(self):
        self.block = None
        self.insert_time = 0
        self.last_used = 0
        self.freq = 0
class CacheSimulator:
    def __init__(self, num_lines, mapping='set', assoc=2, policy='FIFO'):
        self.num_lines = num_lines
        self.assoc = assoc
        self.num_sets = num_lines // assoc
        self.policy = policy

        self.sets = [
            [CacheLine() for _ in range(assoc)]
            for _ in range(self.num_sets)
        ]

        self.fifo_queues = [deque() for _ in range(self.num_sets)]
        self.time_counter = 0
        self.hits = 0
        self.misses = 0

    def _which_set(self, block):
        return block % self.num_sets

    def _find_block(self, set_idx, block):
        for i, line in enumerate(self.sets[set_idx]):
            if line.block == block:
                return i
        return -1

    def _choose_victim(self, set_idx):
        lines = self.sets[set_idx]

        for i, line in enumerate(lines):
            if line.block is None:
                return i

        if self.policy == 'FIFO':
            q = self.fifo_queues[set_idx]
            while q and lines[q[0]].block is None:
                q.popleft()
            return q.popleft() if q else 0

        if self.policy == 'LRU':
            return min(range(len(lines)), key=lambda i: lines[i].last_used)

        minfreq = min(line.freq for line in lines)
        candidates = [i for i, line in enumerate(lines) if line.freq == minfreq]
        return min(candidates, key=lambda i: lines[i].insert_time)

    def access(self, block):
        self.time_counter += 1
        set_idx = self._which_set(block)
        found_idx = self._find_block(set_idx, block)

        if found_idx != -1:
            self.hits += 1
            line = self.sets[set_idx][found_idx]
            line.last_used = self.time_counter
            line.freq += 1
            return 'HIT'

        self.misses += 1
        victim = self._choose_victim(set_idx)
        line = self.sets[set_idx][victim]

        line.block = block
        line.insert_time = self.time_counter
        line.last_used = self.time_counter
        line.freq = 1

        if self.policy == 'FIFO':
            self.fifo_queues[set_idx].append(victim)
        return 'MISS'
    def cache_state(self):
        state = []
        for s_idx, lines in enumerate(self.sets):
            items = [str(line.block) if line.block is not None else '-' for line in lines]
            state.append(f"Set {s_idx}: [{', '.join(items)}]")
        return " | ".join(state)

    def summary(self):
        total = self.hits + self.misses
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_ratio': self.hits / total if total else 0
        }
if __name__ == '__main__':
    seq = [1, 2, 3, 2, 4, 1, 5, 2, 3, 2]
    sim = CacheSimulator(num_lines=4, assoc=2, policy='LRU')

    print("Starting simulation — Set Associative (2-way), Policy = LRU\n")
    for ref in seq:
        ev = sim.access(ref)
        print(f"Ref {ref:2} → {ev:4} | {sim.cache_state()}")
    print("\nSummary:", sim.summary())
