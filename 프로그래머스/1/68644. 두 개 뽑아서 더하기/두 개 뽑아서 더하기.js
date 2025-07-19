function solution(numbers) {
    var answer = [];
    
    /*
     1. 하나씩 뽑아서 다음 숫자와 더해서 저장
     2. 마지막 인덱스 전까지 실행
     3. 집합 처리 (중복 제거)
     4. 오름차순 정렬
    */
   
    // 1, 2
    for (let i=0; i<numbers.length-1; i++) {
        for (let j=i+1; j<numbers.length; j++) {
             answer.push(numbers[i] + numbers[j])
        }
       
    }
    
    // 3
    answer = [...new Set(answer)]
    
    // 4
    answer.sort((a,b) => a-b)
    
    
    return answer;
}