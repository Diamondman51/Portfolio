from random import randint

def get_num():
    try:
        global coun
        num_user = int(input('Sonni kiriting: '))
        coun += 1
        # calcul()
        return num_user
    except ValueError:
        print('Faqat son kiritish kerak!!!')
        return get_num()
    
def choosen_num():
    comp_num = randint(1, 100)
    print('Kompyuter sonni tanladi...')
    
    return comp_num

def calcul(n, m):
    if  n == m:
        return print(f'\nYutdingiz, urinishlar soni {coun}\n')
    elif n > m:
        
        print('\nSiz kiritgan son katta\n')
        n = get_num()

    elif n < m:
        print('\nSiz kiritgan son kichkina\n')

        n = get_num()

    calcul(n, m)

coun = 0

# m = choosen_num()
# from_user = get_num()
if __name__== '__main__':
    calcul(get_num(), choosen_num())
