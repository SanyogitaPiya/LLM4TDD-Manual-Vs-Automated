def test_lfu_cache():
    operations = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    expected_output = [None, None, None, 1, None, -1, 3, None, -1, 3, 4]

    results = []
    lfu = None

    for op, arg in zip(operations, arguments):
        if op == "LFUCache":
            lfu = LFUCache(*arg)
            results.append(None)
        elif op == "put":
            lfu.put(*arg)
            results.append(None)
        elif op == "get":
            result = lfu.get(*arg)
            results.append(result)
    
    assert results == expected_output

def test_lfu_cache_additional():
    operations = ["LFUCache", "put", "get", "put", "get", "put", "get", "get", "put", "get", "get"]
    arguments = [[3], [10, 10], [10], [20, 20], [20], [30, 30], [10], [20], [40, 40], [10], [30]]
    expected_output = [None, None, 10, None, 20, None, 30, 20, None, 10, 40]

    results = []
    lfu = None

    for op, arg in zip(operations, arguments):
        if op == "LFUCache":
            lfu = LFUCache(*arg)
            results.append(None)
        elif op == "put":
            lfu.put(*arg)
            results.append(None)
        elif op == "get":
            result = lfu.get(*arg)
            results.append(result)
    
    assert results == expected_output