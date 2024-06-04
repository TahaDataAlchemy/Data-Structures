def sorted_squared_array(my_array):
  """
  Squares the values in a sorted array and returns a new array with the squares sorted in ascending order.

  Args:
    my_array: A list of integers sorted in ascending order.

  Returns:
    A new list of integers containing the squares of the values in the input array, sorted in ascending order.
  """
  if len(my_array) == 0:
    return []

  # Square the elements in-place
  for i in range(len(my_array)):
    my_array[i] = my_array[i] ** 2

  # Use built-in sorted function for efficient sorting
  return sorted(my_array)

# Example usage
if __name__ == "__main__":
  my_list = [-4, -1, 0, 3, 10]  # Use list instead of 'list' (reserved keyword)
  print(sorted_squared_array(my_list))

