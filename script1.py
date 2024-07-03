# print(3+1)
# print(3*3)
# print(2**3)
# print("Hello, world!")
#
# print('py' + 'thon')
# print('py' * 3 + 'thon')
# print('py' - 'py')
# print('3' + 3)
# print(3 * '3')
# print(a)
# print(a = 3)
# print(a)
#
# print(1==1)
# print(1 == True)
# print(0==True)
# print(0==False)
# print(3==1*3)
# print((3==1)*3)
# print((3==3)*4+3==1)
# print(3**5>=4**4)
#
# print(5/3)
# print(5%3)
# print(5.0/3)
# print(5/3.0)
# print(5.2%3)
# print(2001**200)
#
# print(2000.3**200)
# print(1.0+1.0-1.0)
# print(1.0+1.0e20-1.0e20)


#1.7 Variable
#name = "Anusha"
#greeting = f"Hello, {name}!"
#print(greeting)

#2.1: Range
#range(5)
#range(0, 5)
#for i in range(5):
  #print(i)
 # list(range(5))

#2.2: For loops
#print("Numbers from 0 to 100:")
#for i in range(101):
#    print(i)
#print()

#b.Print the numbers 0 to 100 that are divisible by 7
#print("Numbers from 0 to 100 divisible by 7:")
#for i in range(101):
 #   if i % 7 == 0:
  #      print(i)
#print()

#(c) Print the numbers 1 to 100 that are divisible by 5 but not by 3
#print("Numbers from 1 to 100 divisible by 5 but not by 3:")
#for i in range(1, 101):
 #   if i % 5 == 0 and i % 3 != 0:
  #      print(i)
#print()

#(d) Print for each of the numbers x = 2; : : : 20, all numbers that divide x, excluding 1 and x. Hence,
#for 18, it should print 2 3 6 9.

#for x in range(2, 21):
 #   divisors = [i for i in range(2, x) if x % i == 0]
  #  if divisors:  # Only print if there are divisors
   #     print(f"Divisors of {x}: {divisors}")

# (a) Print numbers from 0 to 100 using a while loop
# print("Numbers from 0 to 100:")
# i = 0
# while i <= 100:
#     print(i)
#     i += 1
# print()
#
# (b) Print numbers from 0 to 100 that are divisible by 7 using a while loop
# print("Numbers from 0 to 100 divisible by 7:")
# i = 0
# while i <= 100:
#     if i % 7 == 0:
#         print(i)
#     i += 1

#  2.5: While loops
#  number_found = 0
# x = 11
# while number_found < 20:
#     if x % 5 == 0 and x % 7 == 0 and x % 11 == 0:
#      print(x)
#     number_found += 1
#x += 1

# 3.Functions
# def hello_world():
#     print('Hello, world!')
# hello_world()
#
# def hello_name(name):
#     print(f'Hello, {name}!')
# hello_name('anusha')

# def print_hello(name):
#     return(f'Hello, {name}!')
# print(print_hello('anusha'))

# def my_max(x, y):
#     if x >= y:
#         return x
#     else:
#         return y
# print(my_max(2,3))

# def my_max(x, y):
#     if x >= y:
#         return x
#     return y
# print(my_max(3,4))
#4.1
# def print_list_elements(l):
#     print(l)
# print_list_elements([1,2,3,4])
#
# def print_list_elements(l):
#     print(l[::-1])
# print_list_elements([1,2,3,4])

#4.2
# a=[1,2,3,4,5]
# b=a
# b[1]=6
# print(a,b)
# c=a[:]
# c[2]=9
# print(a,c)

#4.3
# a = [[1]] * 3
# print(a)

# b = [[2] for _ in range(3)]
# print(b)

# def func_list_index(l,i):
#     l[i] = 0
#     return l
# print(func_list_index([1,2,3,4,5],1))

# def func_sublists(l):
#      x = []
#      for i in l:
#          for j in i:
#              x.append(j)
#      return x
# print(func_sublists([[1,3],[3,6]]))

# import re
# def func_longest_word(text):
#      cleaned_text = re.sub(r'[^\w\s]', '', text)
#      x = cleaned_text.split(" ")
#      longest = ''
#      for i in x:
#         if len(i) > len(longest):
#             longest = i
#      return longest
# print(func_longest_word("“Hello, how was the football match earlier today???"))


# def func_pivots(x,l):
#      empty_list = []
#      for i in l:
#          if i < x:
#             empty_list.append(i)
#      for i in empty_list:
#          for j in l:
#              if i==j:
#                  l.remove(j)
#      return empty_list + [x] + l
# print(func_pivots(3, [6, 4, 1, 7]))


a = 10
b = 5
a,b = b,a
print(a,b)




