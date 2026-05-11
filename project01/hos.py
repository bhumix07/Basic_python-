print("READY with GROW..")
print("REGISTER")
name = input("Enter patient name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender male/female : ").lower()
Emergency  = input("Emergency.??? yes or no : ").lower()
# Registration 
if Emergency  == "yes":
    print("ICU immediately.")
else:
    if age <= 18:
        f = "ground floor"
        print("Go To Ground Floor.")
    elif gender == "female" or gender == "f":
        print("Go To Floor 1.")
        f = "floor 1"
    else:
        print("Go To Floor 2.")
        f = "floor 2"
print("THANK YOU FOR REGISTERING WITH US..")
dr1 = "Dr.sharma"
dr2 = "Dr. Mehta"
dr3 = "Dr. Singh"
urdr = ""
n = input("Enter the problem : ").lower()


# Doctor assignment and fee payment 
while True:
    if n == "fever" or n == "cough" or n == "cold" or n == "headache"or n == "body pain" or n == "stomachache" or n == "vomiting":
        print("You are assigned to ", dr1)
        print("take medicine and follow the diet plan. now you have pay 500 rs for 1st time ")
        fee = int(input("pay the fee amount : "))
        urdr = dr1 
        if fee == 500:
            print("Thank you for the payment.")
            break
        else:
            print("Please pay the correct amount.")           
    elif n == "diabetes" or n == "hypertension" or n == "heart disease" or n == "kidney disease" or n == "liver disease":
        print("You are assigned to ", dr2)
        print("take medicine and follow the diet plan. now you have pay 1000 rs for 1st time ")
        fee = int(input("pay the fee amount : "))
        urdr = dr2
        if fee == 1000:
            print("Thank you for the payment.")
            break
        else:
            print("Please pay the correct amount.")   
    else:
        print("ok consult with", dr3)
        fee = 0
        print("i can't help you with this problem..")
        break   
    
    
# Medicine purchase    
medical = input("Do you want to purchase medicine yes/no? ").lower()
if urdr == dr1 :
    if medical == "yes":
        print("You can purchase medicine from the pharmacy. The cost is 1200 rs.")
        med_fee = int(input("pay the medicine amount : "))
        if med_fee == 1200:
            print("Thank you for the payment.")
        else:
            print("Please pay the correct amount.")
elif urdr == dr2 :
    if medical == "yes":
        print("You can purchase medicine from the pharmacy. The cost is 2000 rs.")
        med_fee = int(input("pay the medicine  amount : "))
        if med_fee == 2000:
            print("Thank you for the payment.")
        else:
            
            print("Please pay the correct amount.")            
else:              
     print("Thank you") 
     med_fee = 0  
     
     
# Report     
print("------------Report-------------")
print("Patient Name :  ", name)
print("Age          :  ", age)
print("Gender       :  ",     gender)
print("Emergency    :  ",    Emergency)
print("Problem      :  ",       n)
print("floor        :  ",          f)
print("Doctor Assigned : ",urdr) 
print()
print("Medicines    :  ", medical)
print("doctor fee   :  ", fee)
print("GST          :     3%")
total = fee + (fee * 0.03)
t = total+ med_fee
print("Total Amount : ", t)
print()
print("Thank you for visiting our hospital. Take care of your health!") 