class LinearSearch:
    def __init__(self, ar, elem):
        print(self.run(ar, elem))

    def run(self, ar, elem):
        for i in ar:
            if elem == i:
                return True
        return False
