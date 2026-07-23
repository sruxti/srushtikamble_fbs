# CONVERT THE TIME ENTERED IN HH,MIN AND SEC INTO SECONDS.

minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds= (minutes * 60) + seconds

print("Total seconds =", total_seconds)