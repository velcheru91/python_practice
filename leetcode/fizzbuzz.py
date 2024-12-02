class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for num in range(1,n+1):
            word = ""
            if num%3 == 0:
                word += "Fizz"
            if num%5 == 0:
                word += "Buzz"
            if word == "":
                word = str(num)
            answer.append(word)
        return answer

p =Solution()
print(p.fizzBuzz(3))
print(p.fizzBuzz(5))
print(p.fizzBuzz(15))
