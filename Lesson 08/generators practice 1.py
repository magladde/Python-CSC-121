# Generate the items, instead of returning a list
def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_of_first_n = sum(first_n(1000000))
print(sum_of_first_n)

# list comprehension
n = 1000000
sum_of_first_n = sum([num for num in range(n)])
print(sum_of_first_n)

# generator expression
n = 1000000
sum_of_first_n = sum(num for num in range(n))
print(sum_of_first_n)