s=0
while True:
    o=int(input("option:"))
    match o:
        case 1:
            s=int(input("enter the sal"))
            print("salary", s)
        case 2:
            if s==0:
                 print("Enter basic salary first")
            else:
                hra=s*0.2
                print(hra)
                da=s*0.1
                print(da)
        case 3:
            if s==0:
                 print("Enter basic salary first")
            else:
                ns=s+hra+da
                print("net",ns)
        case 4:
            if s==0:
                 print("Enter basic salary first")
            else:
               if ns>50000:
                   t=ns*0.1
               else:
                   t=ns*0.05
               print("tax",t)
        case 5:
            if s==0:
                 print("Enter basic salary first")
            else:
                print(s)
                print(hra)
                print(da)
                print(ns)
                print(t)
                print(ns-t)
        case 6:
            break
        case _:
              print("Invalid choice")


               
                                 
