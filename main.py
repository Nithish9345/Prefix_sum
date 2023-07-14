"""Prefix array
   Approach - 1. store prefix sum in an separate array
                 and use this for next sum"""

class Prefix:
    @staticmethod
    def prefix_array(array):
        prefix_array = []

        prefix_array.append(array[0])

        for i in range(1, len(array)):
            prefix_array.append(prefix_array[i - 1] + array[i])

        return prefix_array

array = list(map(int, input().split()))
result = Prefix()
print(result.prefix_array(array))





