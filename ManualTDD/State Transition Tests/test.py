# Initial State: Cache is empty
def test_initial_state_empty_cache():
    lru = LRUCache(2)
    assert lru.get(1) == -1  # Cache is empty, expect -1

# State 1 -> State 2: Add element to an empty cache
def test_add_element_to_empty_cache():
    lru = LRUCache(2)
    lru.put(1, 1)
    assert lru.get(1) == 1  # Cache now contains 1

# State 2 -> State 2: Add another element, cache not full
def test_add_element_to_non_full_cache():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1  # Cache contains both 1 and 2
    assert lru.get(2) == 2

# State 3 -> State 3: Cache is full, adding element should evict LRU
def test_add_element_to_full_cache():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)  # Cache is full, should evict 1 (the least recently used)
    assert lru.get(1) == -1  # 1 should be evicted
    assert lru.get(2) == 2  # 2 should still be present
    assert lru.get(3) == 3  # 3 should be added

# Access element in State 3: Make an element most recently used
def test_access_element_in_full_cache():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.get(1)  # Access 1, making it most recently used
    lru.put(3, 3)  # Should evict 2, not 1
    assert lru.get(2) == -1  # 2 should be evicted
    assert lru.get(1) == 1  # 1 should still be present
    assert lru.get(3) == 3  # 3 should be added