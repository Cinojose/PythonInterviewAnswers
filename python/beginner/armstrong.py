import argparse

def armstrong(no):
    armstrong = False
    if(no <=1):
        armstrong = True
    else:
        s_no = str(no)
        len_no = len(s_no)
        sum_no = 0
        bal_no = no
        for i in range (len_no):
            temp_no = bal_no%10
            bal_no = bal_no/10
            sum_no = sum_no + (temp_no**len_no)
        if(sum_no == no):
            armstrong = True
        else:
            armstrong = False
    return armstrong

def armstrong2(no,no2):
    print ("number are {0},{1}".format(no,no2))
    for i in range(no,no2):
        if (armstrong(i) is True):
            print i


if __name__=="__main__":
    parser = argparse.ArgumentParser("Function to check if armstrong")
    parser.add_argument("extension",help="Y for interval N for normal")
    parser.add_argument("number",help="Number to check if armstrong",type=int)
    parser.add_argument("number2",help="Number 2",type=int,nargs='?', const=2)

    args = parser.parse_args()
    if args.extension is 'N':
        armstrong(args.number)

    else:
        print "2nd"
        armstrong2(args.number,args.number2)
