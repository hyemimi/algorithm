def solution(s):
    answer = []
    

    s= s.replace("{{","")
    s= s.replace("}}","")
    s= s.split("},{")
    
    arr = []
    
    for x in s:
        arr.append(x.split(','))
   
    
    sortedArr = sorted(arr, key=len)
    
    for item in sortedArr:
        
        for ele in item:
            if int(ele) in answer:
                continue
            
            answer.append(int(ele))
 
    
    return answer