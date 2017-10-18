
import argparse



def prime(no):
    divisor=1
    prime = True
    if( no <=1 ):
        prime = True
    else:
        for i in range (2,no):
            if ( no % i == 0 ):
                prime = False
                divisor = i
                break
    if prime:
        print ("{0} is a prime".format(no))
    else:
        print ("{0} is not a prime and it's divisible by {1}".format(no, int(divisor)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Prime number checker')
    parser.add_argument("number",help="Number to check if prime",type=int)
    args = parser.parse_args()
    prime(args.number)
