


# User se number le lo
# typecasting bhi kr rahe hai saath me 
num = int(input("Koi ek number daalo jiska multiplication table chahiye: "))

# for loop aur while loop dono se table print krna hai
print(f"\nMultiplication table of {num} using for loop:")
# for loop se
for i in range(1, 11):  # 1 se 10 tak and by deafault step 1 hota hai 
    print(f"{num} x {i} = {num * i}")

print(f"\nMultiplication table of {num} using while loop:")


# while loop se
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1  # i ko badhao





#  break, continue, pass with examples
# break is use for exiting the loop
# continue is use for skipping the current iteration
# pass is use when we want to do nothing (it is a placeholder)



# Generate sequences (range(start, stop, step)).
# start to the end and the step of the to movement 
