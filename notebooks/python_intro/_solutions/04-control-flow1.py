# using the 'accumulator pattern' to check the number of counts
acc = 0
for letter in 'oxygen':
    acc += 1  # the in-place operator
print(acc)    