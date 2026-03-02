python
fruits = ['apple', 'banana', 'mango']

# Non-Pythonic way
for i in range(len(fruits)):
    print(i, fruits[i])

# Pythonic way using enumerate
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output for both:
# 0 apple
# 1 banana
# 2 mango

# You can also specify a custom start index
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# Output:
# 1 apple
# 2 banana
# 3 mango