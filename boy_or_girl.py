name = input()
 
dis_char = set(name)
count = len(dis_char)
 
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
