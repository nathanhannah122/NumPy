import time
import random
import numpy as np

#adds title
print("--Python Vs NumPy--")
#creates list
nums = []

#creates 'while' loop to get the user to enter a valid integer
while True:
    try:
        limit = int(input("Please enter an amount of random numbers to add to a list "))
        break
    except ValueError:
        print("please enter a valid integer")
        continue

#creates loading output for user
print("Loading", end = '')
time.sleep(.5)
print(".", end = '')
time.sleep(.5)
print(".", end = '')
time.sleep(.5)
print(".")
time.sleep(.5)

#starts counter
start = time.perf_counter()

#adds random numbers to the list depending on the users input
for x in range(limit):
   nums.append(random.randint(0, limit))

min = limit + 1
for num in nums:
       if num < min:
           min = num

#ends counter
end = time.perf_counter()
#calculates time taken
elapsed_list = end - start
print(f"elapsed time for {limit} numbers in python is {elapsed_list}")

#now  using NumPy
start = time.perf_counter() #sets counter

#uses NumPy to get random numbers depending on users input
nums = np.random.randint(0, limit, limit)
min = nums.min()

end = time.perf_counter() #ends counter
elapsed_numpy = end - start
#calculates time taken
print(f"elapsed time for {limit} numbers in NumPy is  {elapsed_numpy}")
#displays difference in speed
print(f"Speed up obtained by NumPy over a Python list is {elapsed_list/elapsed_numpy}")



