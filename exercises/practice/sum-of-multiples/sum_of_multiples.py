def sum_of_multiples(limit:int , multiples:list):
    list_multiples=[]
    for i in multiples:
        for x in range(limit):
            if x % i ==0 and x not in list_multiples:
                list_multiples.append(x)
    return sum(list_multiples)

if __name__ == '__main__':
    nums = input().split()
    limit =int(nums[0])
    multiples = [int(i) for i in nums[1:]]
    result = sum_of_multiples(limit, multiples)
    print(result)
    
