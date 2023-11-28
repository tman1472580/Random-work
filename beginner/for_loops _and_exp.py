friends = ["Jim","Karen","Kevin"]
for index in range(len(friends)):
    print(friends[index])

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num

print(raise_to_power(3, 2))
