from random import choice
import os
import sys

library = {
    'after': 'so\'ng',
    'limon': 'limon',
    'word': 'so\'z',
    'paper': 'varoq',
    'mouse': 'sichqoncha'
}

users = {
    'Anvar': {
        'password': '1234',
        'point': 10
    },
    'Otabek': {
        'password': '1234',
        'point': 0
    }
}

# passwords = {}


def menu(login2):
  os.system('cls')
  global asking_login, get_login
  print('''Bittasini tanlang:
            1. O'yinni boshlash
            2. Natijalarni ko'rish
            3. Chiqish''')
  try:
    get = int(input())

    if get == 1:
      # os.system('cls')
      enter(login2)

    elif get == 2:
      # os.system('cls')
      oy_nat()
      menu(get_login)

    elif get == 3:
      text()
  except ValueError:

    # os.system('cls')
    print('1-3 tanlang')
    menu(get_login)


def text():

  print('''______ Learn English words ______
                1. O'yin natijalari
                2. Ro'yxatdan o'tish
                3. Kirish
                4. Chiqish''')

  try:
    main(int(input()))
  except ValueError:
    os.system('cls')
    main(text())


def kirish():
  global asking_login
  asking_login = input('Kirish uchun loginni kiriting: ')
  asking_password = input('Parolingiz: ')

  if asking_login in users.keys():
    if asking_password == users[asking_login]['password']:
      os.system('cls')
      enter(asking_login)
  elif asking_login not in users.keys() or asking_password not in users[asking_login]['password']:
    print('Login yoki parol xato kiritildi')
    main(text())


def choosen():

  return choice(list(library.keys()))


def oy_nat():
  sorted_users = dict(sorted(users.items(), key=lambda x: x[1]['point'], reverse=True))
  for i, (name, ball) in enumerate(sorted_users.items(), 1):

    print(f"{i}. {name}" + str(ball['point']).rjust(10) + " ball")


def log_in():
  global get_login
  get_login = input('Login: ')
  get_password = input('Parol: ')

  if get_login in users.keys():
    os.system('cls')
    print('Siz royxatda borsiz')
    main(text())

  while len(get_password) <= 3:
    print('Parol uzunligi 3 dan katta bo\'lishi kerak')
    get_password = input('Parolni kiriting: ')

  users[get_login] = {}
  users[get_login]['password'] = get_password

  users[get_login]['point'] = 0
  os.system('cls')
  print(f'{get_login.title()}, xush kelibsiz')
  return get_login


# returned_from_login =
# enter(get_login)


def enter(logg):
  global get_login
  count = 0
  xato = 0
  score = 0
  for i in range(1, 6):
    word = choosen()
    asking_translate = input(f'{word} so\'zini tarjimasini yozing: ').lower()

    if asking_translate == library[word]:
      count += 1
      score += 10
    elif asking_translate != library[word]:
      xato += 1
      print(f'\nXato. To\'g\'ri javob {library[word]}\n')

    # choosen()

  users[logg]['point'] += score

  os.system('cls')

  print(f'''Xatolar soni: {xato}
    To'g'ri javoblar soni: {count}\n \n O'yin tugadi. 5 tadan {count} ta to'g'ri topdingiz\n'''
        )

  menu(get_login)


def Chiqish():
  sys.exit()


def main(num):

  if num == 1:
    os.system('cls')

    oy_nat()
    main(text())

  elif num == 2:
    os.system('cls')

    menu(log_in())

  elif num == 3:
    os.system('cls')
    kirish()

  elif num == 4:
    Chiqish()

  elif ValueError:
    main(text())


# txt = text()
if __name__ == '__main__':
  main(text())
