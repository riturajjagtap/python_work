import re
import argparse

def Main():
    par=argparse.ArgumentParser()
    par.add_argument("word",help="Specify word to search for")
    par.add_argument("fname", help="Specify file to search in")
    args=par.parse_args()

    filename=open(args.fname,'r')
    lineNum=0
    flag=0

    for line in filename.readlines():
        line=line.strip('\n\r')
        lineNum+=1
        res=re.search(args.word,line,re.M|re.I)
        #res = re.search(args.word, line)
        if res:
            print(str(lineNum)+" : Line : "+line)
            res2 = re.sub(args.word, "SINGHAM", line)
            print(str(lineNum) + " : Repalced : " + res2)
            flag=1

    if(flag==0):
        print("NOT FOUND")

if __name__=='__main__':
    Main()

