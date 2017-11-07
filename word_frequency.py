'''
word_frequency.py
Written by Sagar Bhat

Python program for counting
frequency of words in an input
sentence by arranging them 
alphabetically

'''

if __name__ == '__main__':

    words = raw_input("Enter a sentence: ").split()
    dict = {key:words.count(key) for key in words}
    for key in sorted(dict.keys()):
        print "{0}:{1}".format(key,dict[key])
