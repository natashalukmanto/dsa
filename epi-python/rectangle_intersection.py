import collections

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))
"""
Named tuples are basically easy-to-create, lightweight object types. 
Named tuple instances can be referenced using object-like variable dereferencing or the standard tuple syntax. 
They can be used similarly to struct or other common record types, except that they are immutable and more readable.

Source/Credit: https://stackoverflow.com/a/2970722
Docs: https://docs.python.org/3/library/collections.html#collections.namedtuple 
"""

"""
The question basically can be simplified to:
    - Given two `Rect`, you either
        - Return Rect(0, 0, -1, -1) if you find no intersection between the two `Rect`
        - Return the intersection area if there is an intersection
    - What counts as an intersection?
        - Intersection is when there's an overlap between the two `Rect` this also includes the boundary,
            i.e. if you find a side of r1 that is overlapping with the side of r2, this counts as an intersection.
            
So, how can we approach this problem?
    - First, let't talk about how to figure out if the r1 and r2 has an intersection.
        - We can make a helper function that does exactly this
    - Then based on what the helper function returns (either True or False), we can specify the return type
"""

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # First, let's make the helper function talked about above
    
    # not_intersect will return True if r1 and r2 doesn't intersect. Why did I implement the negation instead? 
    # While this could be counter-intuitive, it's actually easier (in my opinion)
    # Intersection can happen with a lot of stuff r1 could be inside r2, r2 could be inside r1, r1's width can be inside r2's width but the height not, and vice versa.
    # But, there's only 4 ways it can happen if r1 and r2 don't intersect:
        # 1. r1 is completely to the left of r2
        # 2. r1 is completely to the right of r2
        # 3. r1 is completely above of r2
        # 4. r1 is completely below of r2
        
    def not_intersect(r1: Rect, r2: Rect) -> bool:
        # pass. Let's implement this later and start with the easier part: when it doesn't intersect, we return Rect(0, 0, -1, -1)
        # Then according to the above explanation, let's implement not_intersect
        return (r1.x + r1.width < r2.x) or (r2.x + r2.width < r1.x) or (r1.y + r1.height < r2.y) or (r2.y + r2.height < r1.y)
    
    if not_intersect: 
        return Rect(0, 0, -1, -1)
    
    # If not return the intersection, you have to draw the rectangles to understand this!
    return Rect(
        max(r1.x, r2.x),
        max(r1.y, r2.y), 
        min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
        min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y)
    )
    
    
    