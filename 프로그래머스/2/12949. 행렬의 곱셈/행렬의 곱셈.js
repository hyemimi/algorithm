function solution(arr1, arr2) {
    var answer = []
    let row1 = arr1.length;
    let col1 = arr1[0].length;
    let row2 = arr2.length;
    let col2 = arr2[0].length;
    
    // 정답 행렬의 크기는 row1 x col2
    
    // 정답 행렬 크기에 맞춰 초기화
    for (let i=0;i<row1; i++) {
        answer.push(Array(col2).fill(0))
    }
    
    for (let i=0; i<row1; i++) {
        for (let j=0; j<col2; j++) {
            for (let k=0;k<col1;k++) {
                answer[i][j] += arr1[i][k] * arr2[k][j]
            }
        }
    }
    

    
    
    return answer;
}