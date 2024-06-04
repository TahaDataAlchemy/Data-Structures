def monotonic_array(array):
    """
    An array is monotonic if it is either monotone increasing or monotone decreasing. 
    An array is monotone increasing if all its elements from left to right are non-decreasing. 
    An array is monotone decreasing if all its elements from left to right are non-increasing. 
    Given an integer array return true if the given array is monotonic, or false otherwise.

    Args:
        Array
    output:
        monotonic Array
    """

    if len(set(array))<=1:
        return True
    
    increasing = True
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            increasing = False
            break
        
    if not increasing:
        decreasing = True
        for i in range(len(array)-1):
            if array[i]<array[i+1]:
                decreasing = False
    return increasing or decreasing
    
if __name__ == "__main__":
    test_cases = [

                  [1, 2, 3, 4, 5],  # Increasing
                  [5, 4, 3, 2, 1],  # Decreasing
                  [1, 1, 1, 2,1],  # Monotonic (constant)
                  [1, 2, 3, 2, 1],  # Not monotonic
    ]
    for i in test_cases:
        print(monotonic_array(i))
