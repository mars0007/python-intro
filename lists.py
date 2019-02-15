# 1 without using sets funtion takes two lists an returns the items common to both lists, 
# 2 how that  diff or similar to/from creating a list of intersetsion of two sets
# 3 do not use zip, function thata takes 2 lists and prints val of each separtesd by comas
# 4 test how this is diff from using zip

def intersect (list_1, list_2):
    intersect_list = []
    for i in list_1:
        for j in list_2:
            if i == j:
                if i not in intersect_list:
                    intersect_list.append(i)
    return intersect_list

a_list = [1,2,3,4,5,6]
b_list = [1,5,3,6,2,6,4]

print('the itersect of two lists is {0}'.format(intersect(a_list,b_list)))

def my_zip(list_a, list_b):
    a = 0
    b = 0
    a_len = len(list_a)-1
    b_len = len(list_b)-1
    ziped_list = []
    while list_a[a] and list_b[b]:
        print('list a element is {0} and list b element is {1}'.format(list_a[a],list_b[b]))
        ziped_list.append(str(list_a[a])+str(list_b[b]))
        a+=1
        b+=1
        if a>a_len or b>b_len:
            break
    return ziped_list
    
for i in my_zip(a_list,b_list): 
    print(i)