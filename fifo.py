import time
for i, line in enumerate(lines):
if line.block is None:
return i
# all full, apply policy
if self.policy == 'FIFO':
# FIFO queue holds indices in insertion order
q = self.fifo_queues[set_idx]
# rotate until front index is valid
while q and lines[q[0]].block is None:
q.popleft()
if not q:
# fallback: evict index 0
return 0
victim = q.popleft()
return victim
elif self.policy == 'LRU':
# least recent last_used
oldest_i = min(range(len(lines)), key=lambda i: lines[i].last_used)
return oldest_i
else: # LFU
minfreq = min(line.freq for line in lines)
candidates = [i for i,line in enumerate(lines) if line.freq==minfreq]
# tie-breaker: oldest insert_time
victim = min(candidates, key=lambda i: lines[i].insert_time)
return victim


def access(self, block):
self.time_counter += 1
set_idx = self._which_set(block)
found_idx = self._find_block(set_idx, block)
if found_idx != -1:
# HIT
self.hits += 1
line = self.sets[set_idx][found_idx]
line.last_used = self.time_counter
line.freq += 1
event = 'HIT'
else:
# MISS -> replace
self.misses += 1
victim = self._choose_victim(set_idx)
line = self.sets[set_idx][victim]
# if FIFO, we will push the index into queue after insert
line.block = block
line.insert_time = self.time_counter
line.last_used = self.time_counter
line.freq = 1
if self.policy == 'FIFO':
self.fifo_queues[set_idx].append(victim)
event = 'MISS'
return event


def cache_state(self):
# textual representation of each set
state = []
for s_idx, lines in enumerate(self.sets):
items = [str(line.block) if line.block is not None else '-' for line in lines]
state.append(f"Set {s_idx}: [" + ", ".join(items) + "]")
return " | ".join(state)


def summary(self):
total = self.hits + self.misses
hit_ratio = (self.hits/total) if total>0 else 0
return {'hits':self.hits, 'misses':self.misses, 'hit_ratio':hit_ratio}


if __name__ == '__main__':
# sample run: modify as needed
seq = [1,2,3,2,4,1,5,2,3,2]
sim = CacheSimulator(num_lines=4, mapping='set', assoc=2, policy='LRU')
print('Starting simulation — mapping=set-assoc(2-way), policy=LRU, lines=4')
for ref in seq:
ev = sim.access(ref)
print(f'Ref {ref}: {ev} | State: {sim.cache_state()}')
print('Summary:', sim.summary())