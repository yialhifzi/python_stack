# !! Uncomment #Number for solution !!

# #1
# def biggie_size(Lst):
#     for x in range(len(Lst)):
#         if Lst[x]>0:
#             Lst[x]='Big'
#     print(Lst)
# biggie_size([-2,-1,1,2,-2,-1])

# #2
# def count_positives(Lst):
#     count=0
#     for x in range(len(Lst)):
#         if Lst[x]>0:
#             count+=1
#     Lst[len(Lst)-1]=count
#     print(Lst)
# count_positives([1,1,1,-1,-1])

# #3
# def sum_total(Lst):
#     sum=0
#     for x in range(len(Lst)):
#         sum+=Lst[x]
#     print(sum)
# sum_total([1,2,3])

#4
# def avg(Lst):
#     sum=0
#     avg=0
#     for x in range(len(Lst)):
#         sum+=Lst[x]
#         avg=sum/len(Lst)
#     print(avg)
# avg([1,2,3])

# #5
# def length(Lst):
#     print(len(Lst))
# length([1,2,3])

#6
# def minimum(Lst):
#     mini=0
#     for x in range(len(Lst)):
#         if Lst[x]<mini:
#             mini=Lst[x]
#     print(mini)
# minimum([1,2,3,4,-1,-2])

#7
# def maximum(Lst):
#     maxi=0
#     for x in range(len(Lst)):
#         if Lst[x]>maxi:
#             maxi=Lst[x]
#     print(maxi)
# maximum([1,2,3,4,-1,-2,5])

# #8
# def ultimate_analysis(Lst):
#     diction={'sumTotal': 0 , 'average': 0, 'minimum': 0, 'maximum': 0, 'length': 0 }
    
#     sum=0
#     for x in range(len(Lst)):
#         sum+=Lst[x]
#     diction['sumTotal']=sum
    
#     avg=sum/len(Lst)
#     diction['average']=avg
    
#     mini=0
#     for x in range(len(Lst)):
#         if Lst[x]<mini:
#             mini=Lst[x]
#     diction['minimum']=mini

#     maxi=0
#     for x in range(len(Lst)):
#         if Lst[x]>maxi:
#             maxi=Lst[x]
#     diction['maximum']=maxi
    
#     diction['length']=(len(Lst))

#     print(diction)

# ultimate_analysis([1,2,3,0,20,-2])

#9
# def reverse_list(Lst):
#     L=len(Lst)
#     for x in range(int(L/2)):
#         temp=Lst[x]
#         Lst[x] = Lst[L-x-1]
#         Lst[L-x-1] = temp
#     print(Lst)
# reverse_list([1,2,3,4,5,6])
