# num=[50,40,23,70,56,12,5,10,7]
# print(len(num))



# num=[50,40,23,70,56,12,5,10,7]
# i=0
# c=0
# while i<len(num):
#     if 20<=num[i]<=40:
#         c+=1
#     i+=1
# print("the numbers between 20 and 40 are",c)



# num=[-50,-40,-23,-70,-56,-12,-5,-10,-7]
# i=0
# max=num[0]
# while i<len(num):
#     if max<num[i]:
#         max=num[i]
#     i=i+1
# print(max)



# num=[50,40,23,70,56,12,5,10,7]
# min=num[0]
# for i in num:
#     if min>i:
#         min=i
# print(min)



# names=["anu","shiva","deepa"]
# names+=["kavi"]
# print(names)


# names=["anu","shiv","deepu"]
# names+=["abhi"]
# names[2:]
# print(names)


# names=["abhi","rishi","deepa"]
# i=0
# j=2
# name=[]
# while i<len(names):
#     if i==j:
#         name.append("vasu")
#     name.append(names[i])
#     i+=1
# print(name)



# names=["abhi","rishi","deepa"]
# names[2]="shiva"
# print(names)



# n=["n","i","t","i","n"]
# a=n
# l=len(n)
# sum=""
# i=l-1
# while i>-1:
#     sum+=n[i]
#     i-=1
# print(list(sum))
# if (list(sum))==a:
#     print("polindrom")
# else:
#     print("not")



# n=input("enter")
# a=n
# while len(n)>0:
#     if a==n[::-1]:
#         print("polindrome")
#         break
#     else:
#         print("not")



# binary=[1,0,0,1,1,0,1,1]
# l=len(binary)
# i=l-1
# a=0
# sum=0
# while i>-1:
#     sum+=binary[i]*(2**a)
#     i=i-1
#     a=a+1
# print(sum)

# a=["apple","banana","mango"]
# b=["berry","orange"]
# a.extend(b)
# print(a)

# a=["rithu","madhu","mouni"]
# a.clear()
# print(a)

# a=["rithu","madhu","mouni"]
# del a[:]
# print(a)


# a=["priya"
# ,"rithu","madhu"]
# a.pop(1)
# print(a)


# list1=[10,20,30,40,50,60]
# list2=[30,10,60,70,80]
# list3=[]
# i=0
# while i<len(list1):
#     if list1[i]not in list2:
#         list3.append(list1[i])
#     i+=1
# print(list3)



# num=30
# n=[10,11,12,13,14,17,18,19]
# i=0
# a=[]
# while i<len(n):
#     j=0
#     while j<len(n):
#         b=n[i]+n[j]
#         s=[n[i],n[j]]
#         if num==b:
#             a.append(s)
#         j+=1
#     i+=1
# print(a)



# marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,53,49]]
# i=0
# avg=0
# while i<len(marks):
#     j=0
#     while j<len(marks):
#         avg1=sum(marks[0])/len(marks[0])
#         avg2=sum(marks[1])/len(marks[1])
#         avg3=sum(marks[2])/len(marks[2])
#         j+=1
#     i+=1
# print(avg1)
# print(avg2)
# print(avg3)



# n=[10,11,12,13,14,17,18,19]
# i=0
# list=[]
# while i<len(n):
#     list1=[]
#     j=i
#     while j<len(n):
#         if n[i]+n[j]==30:
#             list1.append(n[j])
#             list1.append(n[i])
#             list.append(list1)
#         j+=1
#     i+=1
# print(list)



# num=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# a=[]
# b=[]
# while i<len(num):
#     if num[i]%2==0:
#         a.append(num[i])
#     else:
#         b.append(num[i])
#     i+=1
#     print("even=",a)
#     print("odd=",b)