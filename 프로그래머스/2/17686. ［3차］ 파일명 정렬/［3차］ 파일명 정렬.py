def solution(files):

    def getComponent(name):
        n = len(name)

        # HEAD 찾기
        i = 0
        while not name[i].isdigit():
            i += 1
        head = name[:i].lower()

        # NUMBER 찾기 (최대 5자리)
        j = i
        while j < n and name[j].isdigit() and j - i < 5:
            j += 1

        number = int(name[i:j])

        return head, number

    return sorted(files, key=getComponent)