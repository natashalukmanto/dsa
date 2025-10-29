def countGoodTriplets(arr, a: int, b: int, c: int) -> int:
        num_triplets = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if (abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c):
                        num_triplets += 1
        return num_triplets
    
# Brute force is enough, optimization is an overkill.