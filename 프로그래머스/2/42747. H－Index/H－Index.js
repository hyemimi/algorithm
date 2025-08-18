function solution(citations) {
    var answer = 0;
    const n = citations.length;
    citations.sort();

    /** Solution
        h-index는 h번 이상 인용된 논문이 h편 이상인 h 최댓값
    */
    
    citations.sort((a,b) => a - b); // O(NlogN)
    console.log(citations);
    
    for (let i=0; i<n; i++) {
        const thesis = citations[i]; // 논문 인용 횟수 = h번
        const cnt = (n - i) // h번 이상 인용된 논문의 갯수
        const h = Math.min(thesis, cnt);
        
        answer = Math.max(answer, h);
        

    }

    return answer;
}