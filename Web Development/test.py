def canMakeArithmeticProgression(arr):
    arr.sort()  # sort in place
    diff = arr[1] - arr[0]
    
    for i in range(1, len(arr) - 1):
        if arr[i+1] - arr[i] != diff:
            return False
    return True
arrvar = [2, 1, 3]
canMakeArithmeticProgression(arrvar)