from typing import Iterator, List
import heapq, math

class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)
    
def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    max_heap = []
    
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)
        
    return [star[1] for star in max_heap]

def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    stars_list = []
    
    for star in stars:
        heapq.heappush(stars_list, star)
    
    res = []
    for _ in range(k):
        res.append(heapq.heappop(stars_list))
        
    return res