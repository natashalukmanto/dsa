from typing import List

def candy(self, ratings: List[int]) -> int:
    candies = [1] * len(ratings)

    # Making sure the right neighbors with higher rating have more candies
    for i in range(len(ratings) - 1):
        if ratings[i] < ratings[i+1] and candies[i] >= candies[i+1]:
            candies[i+1] = candies[i] + 1
        #print("right nei", candies)
    
    # Making sure the left neighbors with higher rating have more candies
    for i in range(len(ratings) - 1, 0, -1):
        if ratings[i] < ratings[i-1] and candies[i] >= candies[i-1]:
            candies[i-1] = candies[i] + 1
        #print("left nei", candies)

    return sum(candies)


