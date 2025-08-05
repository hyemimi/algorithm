function solution(want, number, discount) {
    var answer = 0;
    
    const wantItem = {}
    
    // 정현이가 원하는 아이템과 갯수 저장
    for (const [idx, item] of want.entries()) {
        wantItem[item] = number[idx]
    }
    
    for (const[idx, item] of discount.entries()) {
        // (idx+1 + 10) 일간 유효
        const countItem = {}
        
        for (let i=idx; i < idx+10; i++) {
            
            if (i >= discount.length) break;
            
            if (!(discount[i] in wantItem)) continue;
  
            if (countItem[discount[i]]) {
                countItem[discount[i]] += 1;
            }
            else {
                countItem[discount[i]] = 1;
            }

        }
        
        if(isEqual(countItem, wantItem)) {
            answer += 1
        }
        
        
        
    }
    
    function isEqual(obj1, obj2) {
        const keys1 = Object.keys(obj1);
        const keys2 = Object.keys(obj2);
        if (keys1.length !== keys2.length) return false;

        for (const key of keys1) {
            if (obj1[key] !== obj2[key]) return false;
        }
        return true;
    }

    
    return answer;
}