if __name__ == '__main__':


    n = int(input())
    arr = map(int, input().split())
   
    list1=[]


    for i in arr:


      list1.append(i)


    sublist = [x for x in list1 if x < max(list1)]
    print(max(sublist))
