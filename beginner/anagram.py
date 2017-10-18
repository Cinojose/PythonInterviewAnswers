import argparse


def checkAnagram(t1,t2):
    #print "anagram"
    angram = False
    lett_sum = 0
    for i in range (len(t1)):
        letter_bool = False
        for j in range(len(t2)):
            if t1[i] == t2[j]:
                letter_bool = True
        if letter_bool ==True:
            lett_sum +=1
    if lett_sum == len(t1):
        print "anagram"
    else:
        print "not anagram"


if __name__ =="__main__":
    parser = argparse.ArgumentParser("Function to check if anagram")
    parser.add_argument("text1",help="Text 1")
    parser.add_argument("text2",help="Text 2")

    args = parser.parse_args()

    print("text1 is {0}, text 2 is {1}".format(args.text1,args.text2))

    checkAnagram(args.text1,args.text2)
