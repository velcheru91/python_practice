class SelectionSort:
    def __init__(self):
        self.idx = None
        self.val = None

    def run(self, ar):
        temp_idx = -1
        count = 0
        for i in range(0, len(ar)):
            les_val = ar[i]
            for j in range(i+1,len(ar)):
                count += 1
                if ar[j]<les_val:
                    temp_idx = j
                    les_val = ar[j]
            if temp_idx != -1:
                temp = ar[temp_idx]
                ar[temp_idx] = ar[i]
                ar[i] = temp
                temp_idx = -1
        # print(count)
        return ar
