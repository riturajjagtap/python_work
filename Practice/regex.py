import re

def Main():
    line="I think I understand regular expressions"
    res=re.match("think",line,re.M|re.I)
    if res:
        print("Match found : "+res.group())
    else:
        print("No match found")

    sres=re.search('think',line,re.M|re.I)
    if sres:
        print("Search found : "+sres.group())
    else:
        print("Nothing found in search")


if __name__=="__main__":
    Main()


