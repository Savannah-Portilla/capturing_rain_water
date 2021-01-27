from time import time

small = [1,0,1]
medium = [4,2,1,3,0,1,2]
edge_case = [0,1,0]

#----- OPTIMIZED SOLUTION O(N) -----------------------
def optimized_rain_water(histogram):
  total = 0
  max_value = histogram[0]
  left_maxes = []
  for i in range(len(histogram)):
    if histogram[i] > max_value:
      max_value = histogram[i]
    left_maxes.append(max_value)
  print("left_maxes = ", left_maxes)
  max_value = histogram[-1]
  right_maxes = []
  histogramrev = histogram[::-1]
  for i in range(len(histogramrev)):
    if histogramrev[i] > max_value:
      max_value = histogramrev[i]
    right_maxes.append(max_value)
  right_maxes.reverse()
  print("right_maxes = ", right_maxes)
  for i in range(len(histogram)):
    minimum = min(left_maxes[i], right_maxes[i])
    total = total + (minimum - histogram[i])
#--------------------------------------------------

#------ NAIVE SOLUTION O(N^2)----------------------
def rain_water(histogram):
  total_water = 0
  for i in range(1, len(histogram) - 1):
    # from indicy 1 to -1
    print("(histogram[i]), index = ", histogram[i])
    print("(i), index = ", i)
    print("([:i]), index = ", histogram[:i])
    print("([i:]), index = ", histogram[i:])
    left_values = histogram[:i]
    print("left_values = ", left_values)
    left_max = max(left_values)
    print("left_max = ", left_max)
    right_values = histogram[i:]
    print("right_values = ", right_values)
    right_max = max(right_values)
    print("right_max = ", right_max)
    fill_mark = min(left_max, right_max)
    print("fill_mark = ", fill_mark)
    print(total_water, "+", fill_mark, "-", histogram[i])
    if total_water + (fill_mark - histogram[i]) >= 0:
      total_water = total_water + (fill_mark - histogram[i])
    print("total water = ", total_water)
    print("-----------------------------------")
  print("----------------------------------")
  print("Left max is: {0}".format(left_max))
  print("Right max is: {0}".format(right_max))
  print(total_water)
#-------------------------------------------------------

start = time()
rain_water(medium)
finish = time()

start2 = time()
optimized_rain_water(medium)
finish2 = time()

first = finish - start
sec = finish2 - start2
print("first = ", first)
print("second = ", sec)
print("difference = ", first - sec)
