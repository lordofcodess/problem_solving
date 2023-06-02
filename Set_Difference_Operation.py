n1 = int(input())
list1 = set(input().split())
n2 = int(input())
list2 = set(input().split())


    
f_list = list1.difference(list2)

count = 0
for eachPerson in f_list:
    count += 1
    
print (count)
