"""Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4"""



total_sec = int(input("enter the sec "))

hrs = total_sec//3600
min = (total_sec-hrs*3600)//60
sec = (total_sec-hrs*3600-min*60)
print(hrs)
print(min)
print(sec)