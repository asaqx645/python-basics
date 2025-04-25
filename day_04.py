# -----------------------------
# Conditional Statements
# -----------------------------

# age = int(input("Enter your age: "))
# print(age)
# if age < 13:
#     print(" You are a child.")
# elif age <= 20:
#     print(" You are a teenager.")
# else:
#     print(" You are an adult.")


# -----------------------------
# for Loop
# -----------------------------
# ages = [12, 15, 18, 20, 25] 
# print("what class is the object type: ", type(ages))
# for age_ in ages:
    # print("age of the person >>> {item}")
    # print(f"age of the person >>> {age_}")
    # print(age_)
    

# -----------------------------
# while Loop
# -----------------------------

# print("while loop - Countdown from 3:")
# count = 1
# print("count: ", count)
# while count < 3:# true - so the loop will print forever!!
#     print("infinite while loop!!")

# count_ = 5
# print("count: ", count_) # print out 5
# while count_ > 0:
#     print(f"Countdown: {count_}") # print out 5
#     count_ -= 1 # 5 - 1 = 4
#     print(count_) # print out 4
# print(f"End of the while loop, because incrementation has rached: {count_}")

# count = 3
# while count > 0: # true
#     print(f"Countdown: {count}")
#     count -= 1 # incrementation to infinite instead of decrementation to finite 
# print("Done!")

# -----------------------------
# Nesting Example
# -----------------------------

# print("Multiplication Table (1–3)")
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print("---")

# for x in range(2, 4): # total of 2 times
#     print("output of x:", x)
#     for y in range(1, 4): # 3 times
#         print("multiplication-output: ",x*y)

        # arithmetic operators
# a =10
# b = 20
# c = 350
# print(f"{a}")
# print(f"{a-b}")
# print(f"{a} // {b} = {a // b}") 
# print(f"{a} / {b} = {a / b:.2f}")
# print(f"{a} % {b} = {a % b}") 



# for number in range(1, 11):
#     if number % 2 == 0: # true
#         print(f"{number} is Even")
#     else:
#         print(f"{number} is Odd")