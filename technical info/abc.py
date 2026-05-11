a = int(input("Enter no.1"))
b = int(input("Enter no.2"))
c = int(input("Enter no.3"))
d = int(input("Enter no.4"))


if a>b :
    if a>c:
        if a>d:
            print("a is greater")
        else:
            print("d is greater")

    else:
	    if c>d:
 	        print("b is greater")
	    else:
	        print("d is greater")

else:
    if b>c:
        if b>d:
            print("b is greater")
        else:
            print("d is greater")   
    else:
	    if c>d:
	        print("c is greater")
	    else:
	        print("d is greater")
          