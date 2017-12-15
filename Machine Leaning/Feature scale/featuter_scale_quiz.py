""" quiz materials for feature scaling clustering """


# FYI, the most straightforward implementation might
# throw a divide-by-zero error, if the min and max
# values are the same
# but think about this for a second--that means that every
# data point has the same value for that feature!
# why would you rescale it?  Or even use it at all?

def featureScaling(arr):
    max_arr = max(arr)
    min_arr = min(arr)
    scaled = []
    for n in arr:
        try:
            scaled.append(round((n - min_arr) / (max_arr - min_arr), 3))
        except:
            scaled.append(1)
    return scaled


data = [115, 140, 175]
print(featureScaling(data))
