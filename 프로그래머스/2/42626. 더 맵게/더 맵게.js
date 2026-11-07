class MinHeap {
    constructor() {
        this.heap = []
    }
    
    push (item) {
        
        this.heap.push(item)
        let i = this.heap.length - 1
        
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2)
            
            if (this.heap[parent] <= this.heap[i]) {
                // 부모가 더 작으면 최소힙 만족
                break
            }
            
            // 서로 교환
            [this.heap[parent], this.heap[i]] =  [this.heap[i], this.heap[parent]]
            
            i = parent
  
        }
 
    }
    
    pop () {
        if (this.heap.length === 0) return null
        
        const top = this.heap[0] // 루트 값 저장 
        const last = this.heap.pop() // 마지막 값 제거
        
        if (this.heap.length == 0) return top // 하나 밖에 없었으면 바로 반환
        
        this.heap[0] = last // 마지막 원소를 루트에 저장
        let i = 0
        
        while (true) {
            let smallest = i
            
            // 왼쪽 자식
            const l = i * 2 + 1
            const r = i * 2 + 2
            
            if ( l < this.heap.length && this.heap[l] < this.heap[smallest]) {
                smallest = l
            }
            
            if ( r < this.heap.length && this.heap[r] < this.heap[smallest]) {
                smallest = r
            }
            
            if (i == smallest) break
            
            // 더 작은 자식과 교환
          [this.heap[i], this.heap[smallest]] =
            [this.heap[smallest], this.heap[i]];

          // 교환한 자식 위치로 이동
          i = smallest;
            
        }
        
        return top;
    }
    get size () {
        return this.heap.length
    }
}


function solution(scoville, K) {
    
    heap = new MinHeap()
    
    let answer = 0
    
    // 힙에 스코빌레 지수 넣기
    for (const sco of scoville) {
        heap.push(sco)
    }
    
    while (heap.size >= 2) {
        first = heap.pop()
        
        if (first >= K) {
            // 가장 작은 게 k 이상이므로 종료
            return answer
        }
        
        second = heap.pop()
        
        new_mixed = first + (second*2)
        answer += 1
        
        heap.push(new_mixed)
    }
    
    if (heap.pop() >= K) {
        return answer
    }
    
    return -1

}