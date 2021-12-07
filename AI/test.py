data = ['A', 'B','C', 'B', 'B'] #list

int('3')  # '3' -> 3
list('3') # '3' -> ['3']

# [] => list
# {k:v} => dict
# {} => set (집합) => 집합 안에는 중복된 갑이 올 수 없음!
# () => tuple

print(data)       # list
print(set(data))  # set
print(list(set(data)))  #list


data2 = (5, 3)
print(data2)

num1, num2 = (5, 3)
print(num1)
print(num2)      # tuple unpacking