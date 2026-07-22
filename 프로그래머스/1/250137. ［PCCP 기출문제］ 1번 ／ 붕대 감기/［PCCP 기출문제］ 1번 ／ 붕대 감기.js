function solution(bandage, health, attacks) {
    var answer = 0;
    
    // 공격당하거나 끝나면 다시 붕대 감기 시작, 연속 성공 시간 0 초기화
    // 0 이하면 죽음
    
    const n = attacks.length
    const endTime = attacks[n-1][0]
    
    let time = 1
    let attackIdx = 0
    let successTime = 0
    let curHealth = health
    
    const skillTime = bandage[0]
    const secondRecovery = bandage[1]
    const plusRecovery = bandage[2]
    
    while (attackIdx <= n-1) {
        
        // 캐릭터의 체력이 0 이하일 경우 죽음
        if (curHealth <= 0) {
            return -1
        }
        
        // if 몬스터의 공격시간일 경우: successTime을 0으로 초기화하고, 현재 체력을 깎음
        if (attacks[attackIdx][0] === time) {
            successTime = 0
            curHealth -= attacks[attackIdx][1]
            
            attackIdx += 1
            time += 1
            continue
        }
        
        else {
          
            successTime += 1
            curHealth += secondRecovery
            
            // if t초 동안 붕대 감기 성공 시 -> 체력 회복 (최대 체력 회복 유의), 0으로 초기화
            if (successTime >= skillTime) {
                curHealth = Math.min(health, curHealth + plusRecovery)
                successTime = 0
                
                time += 1 
                continue
            }
            
            else {
                // else 1초 체력 회복 (최대 체력 회복 유의)
                curHealth = Math.min(health, curHealth)      
                time += 1 
            }          
            
        }

    }
    
    if (curHealth <= 0) {
        return -1
    }

    
    return curHealth;
}