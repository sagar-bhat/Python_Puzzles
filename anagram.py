def is_anagram(s1,s2):

    arr1 = [c for c in s1 if c != ' ']
    arr2 = [c for c in s2 if c != ' ']

    if len(arr1) == len(arr2):
        try:
            for i in range(len(arr1)):
                arr2.remove(arr1[i])
        except:
            return "No"

        return "Yes"
        
    else:
        return "No"


if __name__ == '__main__':

    s1 = "TOM MARVOLO RIDDLE"
    s2 = "I AM LORD VOLDEMORT"
    print is_anagram(s1,s2)

    s1 = "xoriantsolutions"
    s2 = "xorandornot"
    print is_anagram(s1,s2)

