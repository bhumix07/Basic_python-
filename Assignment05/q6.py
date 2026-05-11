"""6. Weather Monitoring System
   A system checks weather conditions: 

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert"""



temp , humi = map(int,input("temprature and humidity ").split())


if temp >= 30:
    print("hot day")
    if humi >= 70:
        print("HIgh humidity alert")
else : 
    print("cold day")
        