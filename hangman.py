#hang man

import random

words = ('cu','ti','bim','bao','meo','cho')

hang_art = {0:("   ",
               "   ",
               "   "),

            1:(" O ",
               "   ",
               "   "),

            2:(" O ",
               " | ",
               "   "),

            3:(" O ",
               "/| ",
               "   "),

            4:(" O ",
               "/|\\ ",
               "   "),

            5:(" O ",
               "/|\\ ",
               "/  "),

            6:(" O ",
               "/|\\ ",
               "/ \\")}


def dis_ma(wrong_guesses):
   for line in hang_art[wrong_guesses]:
      print(line)



def dis_hint(hint):
   print(' '.join(hint))




def dis_ans(answer):
   print(' '.join(answer))

def main():
   answer = random.choice(words)
   hint = ['_'] * len(answer)
   wrong_guesses = 0
   gues_letter = set()
   isrunning = True

   while isrunning:
      dis_ma(wrong_guesses)
      dis_hint(hint)
      guesss = input('Enter a letter: ').lower()

      if len(guesss) != 1 or not guesss.isalpha():
         print('Invalid input, one letter only')
         continue

      if guesss in gues_letter:
         print(f'{guesss} is already guessed')
         continue

      gues_letter.add(guesss)

      if guesss in answer:
         for i in range(len(answer)):
            if answer[i] == guesss:
               hint[i] = guesss
      
      else:
         wrong_guesses += 1

      if '_' not in hint:
         dis_ma(wrong_guesses)
         dis_ans(answer)
         print('You win!')
         isrunning = False
      elif wrong_guesses >= len(hang_art) - 1:
         dis_ma(wrong_guesses)
         dis_ans(answer)
         print('NGU CHUA')
         isrunning = False




if __name__ == '__main__':
    main()




