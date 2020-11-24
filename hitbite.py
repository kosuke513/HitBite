import random

#正解となる4つの異なる数字をランダムにリストへいれる
numbers =[]
while len(numbers) < 4:
    n = str(random.randint(0,9))
    if not n in numbers:
        numbers.append(n)

hit = 0
bite = 0
hitbites = []

number_str = numbers[0] + numbers[1] + numbers[2] + numbers[3]

#プレイヤーの予測を蓄積するリスト
expectations = []
#プレイヤーの予測した4文字を格納するリスト
expected_numbers = []

#数値と位置が合っている数
bite = 0
#数値が合っている数
hit = 0

#gameの開始メソッド
def game():
    expect()
    judge()

def expect():
    if len(expectations) > 0:
        expect_log()
    print( '\n <<' + str(len(expectations) + 1) + '回目>> ' )
    expected_numbers.clear()
    expectation = input(' ４桁の数字を半角で入力し、予想しましょう！:')
    listed_expectation = list(expectation) #それぞれの数字をリスト化
    #ここに数字の重複を許さないコードや、数字以外の入力を許さないコード、桁数が増えすぎるなどをかく
    expectations.append(expectation) #数字を予想のリストに挿入
    for i in range(4):
        expected_numbers.append(listed_expectation[i])

def match_number():
    hit = 0
    bite = 0
    if bite == 4:
        win()
    else:
        for i in range(4):
            if numbers[i] == expected_numbers[i]:
                bite += 1
            elif numbers[i] == expected_numbers[0]:
                hit += 1
            elif numbers[i] == expected_numbers[1]:
                hit += 1
            elif numbers[i] == expected_numbers[2]:
                hit += 1
            elif numbers[i] == expected_numbers[3]:
                hit += 1

        hitbite =  '  Hit:' + str(hit) + ' Bite:' +str(bite)
        hitbites.append(hitbite)
        expect()

def judge():
    bite = match_number()
    if bite == 4:
        win()
    else:
        print_hitbite_score()
        expect()
        judge()

def print_hitbite_score():
    print(hitbites[len(expectations) - 1] + '\n')

def expect_log():
    i = 0
    while i < len(expectations) :
        print( '(' + str(i + 1) + ')入力した数字：' + expectations[i] + '  ' + hitbites[i])
        i += 1

def win():
    print('\nおめでとうございます！' + str(len(expectations)) + '回目で数字を当てました！')
    print('正解は『' + number_str + '』でした')
    print('------------予測のスコア--------------')
    expect_log()
    print('------------------------------------')

game()
