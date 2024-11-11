def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
    
        # Initialize a dictionary to store how many targets each seed destroys
        destroyed_count = {}
        
        for seed in nums:
            # Count how many targets are destroyed by this seed
            destroyed_count[seed] = sum(1 for target in nums if (target - seed) % (space) == 0)
        
        # Return the seed that destroys the most targets
        # In case of a tie, return the smallest seed
        return min(destroyed_count, key=lambda x: (-destroyed_count[x], x))