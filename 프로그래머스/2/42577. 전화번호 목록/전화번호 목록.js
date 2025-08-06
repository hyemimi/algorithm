function solution(phone_book) {
    var answer = true;
    const n = phone_book.length;
    
    phone_book.sort();
    
    for (let i=0; i<n-1; i++) {
        if (phone_book[i+1].startsWith(phone_book[i])) {
            return false
        }
    }
    return answer;
}