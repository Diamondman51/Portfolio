from random import choice

import os

sp = ['Qog\'oz', 'Qaychi', 'Quduq']

def choose():
    return choice(sp)

def user():
    try:

        get_from_user = int(input('''Bittasini tanlang:
        
        1. Quduq
        2. Qaychi
        3. Qog\'oz
        4. Chiqish
        
        '''))
        if get_from_user == 4:
            return 4
        
        elif 0 < get_from_user < 4:    

        
            
            if get_from_user == 1:
                return sp[2]
            elif get_from_user == 2:
                return sp[1]
            elif get_from_user == 3:
                return sp[0]
            # elif get_from_user == 4:
            #     return 4
            else:
                return sp[3]                
            
        else:
            print('Faqat 1 - 4 gacha son kiriting')
            return user()
    except ValueError:
        print('Faqat son kiriting!!!')



def main(comp, user1):
    os.system('cls')
    if comp == 'Qog\'oz' and user1 == 'Qaychi' or comp == 'Qaychi' and user1 == 'Quduq' or comp == 'Quduq' and user1 == 'Qog\'oz':
        print(f'''Siz yutdingiz :D
            
            Kompyuter tanlagani '{comp}': '{user1}' bu esa siz tanlaganingiz\n''')
        
    elif user1 == 4:
        return print('Siz o\'yindan muvaffaqiyatli chiqdingiz\n')
        
    elif user1 == 'Qog\'oz' and comp == 'Qaychi' or user1 == 'Qaychi' and comp == 'Quduq' or user1 == 'Quduq' and comp == 'Qog\'oz':
        print(f'''Kompyuter yutdi :(
            
            Kompyuter tanlagani '{comp}' : '{user1}' bu esa siz tanlaganingiz\n''')
    elif user1 == comp:
        print('Durrang\n')
    
        
    main(choose(), user())
        

if __name__ == '__main__':
    main(choose(), user())
