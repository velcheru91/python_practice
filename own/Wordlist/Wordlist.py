import sys, os
from string import ascii_lowercase

# each word {word, parts of speech, meaning}
class HashTable:
    def __init__(self):
        self.size = 26 # Number of alphabets
        self.table = {}
        for _ in range(26):
            self.table[ascii_lowercase[_]] = []
        print(self.table)

    def prompt(self):
        token = input("Enter 0 to insert word\
        1 to find word\
        2 to delete a word\
        -1 to quit. ")
        if ['-1','0','1','2'].__contains__(token):
            print("valid input")
            if token == '-1':
                print("Goodbye!.")
                return -1
            elif token == '0':
                self.insert()
        else:
            print("Invalid input, try again!")
        return 0

    def insert(self):
        user_word = input("Enter the word to insert, "
                          "no characters are allowed "
                          "other than lowercase alphabets.")
        if self.checkvalidinput(user_word) == -1:
            print("Invalid character found...cannot insert.\n")
        else:
            # insert
            self.table[user_word[0]].append(user_word)
            print(self.table)
        return 0

    def checkvalidinput(self, istring):
        for i in istring:
            if ascii_lowercase.__contains__(i):
                continue
            else:
                return -1
        return 0

def main():
    print("Hello this is word list dictonary")
    words = HashTable()
    while True:
        if -1 == words.prompt():
            return 0

main()
