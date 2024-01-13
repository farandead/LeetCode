def canFormArray(arr, pieces):
    arr = sorted(arr)
    new_array = []
    for piece in pieces:
        new_array+=piece
    return sorted(new_array) == arr

print(canFormArray([15,88],[[88],[15]]))