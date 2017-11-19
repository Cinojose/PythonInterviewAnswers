import argparse

dict_one ={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",
           7:"seven",8:"eight",9:"nine",10:"Ten",11:"Eleven",12:"Twelve",
           13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",
           18:"eighteen",19:"ninteen"}
dict_two = {1:"Ten",2:"Twenty",3:"Thirty",4:"Fourty",5:"Fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}

dict_three = {100:"Hundred",1000:"Thousand"}

def translate(number):
    word_string = ""
    temp_num = number
    while temp_num >0:
        if temp_num >0 and temp_num <20:
            word_string = word_string +dict_one[temp_num]+" ,"
            temp_num =0
        elif temp_num >=20 and temp_num <100:
            num_a = temp_num/10
            temp_num = temp_num%10
            word_string = word_string + dict_two[num_a] +" ,"
        elif temp_num >=100 and temp_num <1000:
            num_a = temp_num/100
            temp_num = temp_num/10
            word_string = word_string + dict_one[num_a] + dict_three[100]+" ,"
    print word_string

if __name__=="__main__":
    parser = argparse.ArgumentParser("Function to translate intiger to string")
    parser.add_argument("number",type=int,help="Number to translate")
    args = parser.parse_args()
    print args.number
    translate(args.number)
