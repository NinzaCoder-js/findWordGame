import random

def sozni_top():
    words = [ 'code', 'coder', 'develop', 'developer']
    wordRand = random.choice(words)
    array = ['_'] * len(wordRand)
    count = 0


    def qayta_oynash():
        a = input("Yan o'ynashni xoxlaysizmi ? (ha/yoq): ")
        if a == 'ha':
           return sozni_top()
        elif a == 'yoq':
            print("O'yin uchun rahmat")

    def natija():
        natija_text = ' '.join(array)
        print(natija_text)
        print('')


    natija()

    while True:
        if '_' in array:
            harf = input('Harf kiriting >> ')
            if harf in wordRand:
                for i in range(len(wordRand)):
                    if wordRand[i] == harf:
                        array[i] = harf
                natija()
            else:
                print("So'zda bunday harf mavjud emas !")
                count += 1
                if count >= 4:
                    print('Siz yutqazdingiz')
                    qayta_oynash()
                    break

                else:
                    print(f"Sizda {4 - count}-ta urunish mavjud ")
                natija()
        else:
            print('TABRIKLAYMAN !!! \nSiz yuttingiz ')
            qayta_oynash()
            break

sozni_top()

