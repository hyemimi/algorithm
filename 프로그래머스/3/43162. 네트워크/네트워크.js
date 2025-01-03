function solution(n, computers) {
    var answer = 0;
    let ch = Array.from({length:n}, ()=>0) // 방문 체크 배열
    
   function BFS (i) {
       ch[i] = 1
       queue = []
       queue.push(i)
       
       while (queue.length) {
           node = queue.shift()
           
            for (let j=0; j < n; j++) {
               if (computers[node][j] === 1 && ch[j] === 0) {
                   queue.push(j)
                   ch[j] = 1
               }
            }
       }
      
   }
  
    for (let i=0; i<n; i++) {
         if (ch[i] === 0) {
            BFS(i);
            answer += 1;
         }
    }
    
    return answer;
}