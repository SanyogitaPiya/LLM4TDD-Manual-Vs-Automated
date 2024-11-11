class LUPrefix:
    def __init__(self, n: int):
        # Initialize with total number of segments 'n'
        self.uploaded_segments = set()  # Set to keep track of uploaded segments
        self.longest_prefix = 0  # This will track the longest contiguous prefix

    def upload(self, segment: int) -> None:
        # Add the segment to uploaded set
        self.uploaded_segments.add(segment)
        
        # Update longest prefix if the next expected segment in sequence is uploaded
        while self.longest_prefix + 1 in self.uploaded_segments:
            self.longest_prefix += 1

    def longest(self) -> int:
        # Return the longest contiguous prefix length
        return self.longest_prefix
