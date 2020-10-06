

def solution(phone_book):
    answer = True
    pb = list(map(int,phone_book))
    fire = str(min(pb))
    if fire in phone_book:
        phone_book.remove(fire)
    for i in phone_book:
        if fire in i and i.find(fire) == 0:
            answer = False

        return answer


print(solution(phone_book=["119", "97674223", "1195524421"]))


### 한줄쏘쓰
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True