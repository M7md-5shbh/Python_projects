# created by M7md-5shbh
# it performs calculations like mean/median/mode/standard deviation/variance
#---------------------------------------------


def mean(data):
    """
    Calculates the mean of a given dataset.

      Args:
        data: A list/tuple of numbers.

      Returns:
        The mean value.
      """
    return round(sum(data) / len(data), 2)


def median(data):
    """
    Calculates the median of a given dataset.

      Args:
        data: A list/tuple of numbers.

      Returns:
        The median value.
      """
    if type(data) == tuple:
        data = list(data)

    data.sort()
    median_index = int(len(data)/2)
    if len(data) % 2 == 0:
        return (data[median_index] + data[median_index - 1]) / 2
    return data[median_index]



def mode(data):
    """
    Calculates the mode of a given dataset.

      Args:
        data: A list/tuple of numbers.

      Returns:
        The mode value.
      """
    if type(data) == tuple:
        data = list(data)
    highest_count = 0
    highest_value = None
    data.sort()
    for index,value in enumerate(data):
        if data.count(value) > highest_count:
            highest_count = data.count(value)
            highest_value = data[index]
    return highest_value


def std_dev(data, need_var=False):
    """
    Calculates the standard deviation of a given dataset.

      Args:
        data: A list/tuple of numbers.
        need_var: bool - if you only need the variance of the dataset.

      Returns:
        The standard deviation of the dataset or variance if need_var is True.
      """
    if type(data) == tuple:
        data = list(data)
    n = len(data)
    variance = sum((x - mean(data))**2 for x in data) / (n - 1)
    if need_var:
        return variance
    std_dev = variance ** 0.5
    return std_dev

def var(data):
    """
    Calculates the variance of a given dataset.

      Args:
        data: A list/tuple of numbers.

      Returns:
        The variance value.
      """
    if type(data) == tuple:
        data = list(data)
    n = len(data)
    variance = sum((x - mean(data)) ** 2 for x in data) / (n - 1)
    return variance


def percentile(data, percentile):
  """
  Calculates the percentile of a given dataset.

  Args:
    data: A list/tuple of numbers.
    percentile: The desired percentile (between 0 and 100).

  Returns:
    The percentile value.
  """
  if type(data) == tuple:
    data = list(data)
  data.sort()
  index = (percentile / 100) * (len(data) + 1)

  if index.is_integer():
      return data[int(index) - 1]
  else:
      lower_index = int(index)
      upper_index = lower_index + 1
      return (data[lower_index - 1] + data[upper_index - 1]) / 2

