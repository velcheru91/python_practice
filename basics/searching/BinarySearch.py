from math import floor
class BinarySearch:
    def __init__(self, ar, ele):
        self.run(ar, ele, 0, len(ar))

    def run(self, arr, element, left, right):
        middle = floor((left + right)/2)
        if left > right:
            print("Not found.")
            return
        if arr[middle] == element:
            print("Found.")
            return
        elif element < arr[middle]:
            self.run(arr, element, left, middle-1)
        elif arr[middle] < element:
            self.run(arr, element, middle+1, right)
