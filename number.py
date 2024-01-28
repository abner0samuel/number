from random import randint
score = 0
while True:
    num1 = randint (1,50)
    num2 = randint (1,100)
    answer = num1 * num2
    print('all the following questions')
    print(f'{num1}  x {num2}  =')
    num = int(input ())
    if answer  == num:
        print('you are correct')
        score +=1
        print(f'your score is : {score}')
    else:
        print(f'you are wrong the answer is {answer}')