def most_popular_creator(creators, ids, views):
    from collections import defaultdict
    
    # Step 1: Calculate total views for each creator and track each creator's ids and views
    total_views = defaultdict(int)
    creator_videos = defaultdict(list)
    
    for creator, id_, view in zip(creators, ids, views):
        total_views[creator] += view
        creator_videos[creator].append((view, id_))
    
    # Step 2: Find the maximum total views among creators
    max_total_views = max(total_views.values())
    popular_creators = [creator for creator, view in total_views.items() if view == max_total_views]
    
    # Step 3: For each popular creator, get the lexicographically smallest id among videos with max views
    result = []
    for creator in popular_creators:
        # Sort the creator's videos first by view count (descending) then by id lexicographically (ascending)
        top_video = min(creator_videos[creator], key=lambda x: (-x[0], x[1]))  # `min` ensures lexicographically smallest ID
        result.append([creator, top_video[1]])
    
    return result
