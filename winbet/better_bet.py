from numpy import arange

bet = [round(i_bet, 2) for i_bet in arange(1.0, 10.01, 0.01)]
big_gen = [i_num * 1000 for i_num in range(11)]  # ставка на меньший коэффициент
small_gen = [i_num * 100 for i_num in range(11)]  # ставка на больший коэффициент
win = 100
for i_left_bet in bet:
    for i_right_bet in bet:
        for i_big_ratio in big_gen:
            for i_small_ratio in small_gen:
                big_bet = i_big_ratio * i_left_bet  # выигрыш от меньшей ставки
                small_bet = i_small_ratio * i_right_bet  # выигрыш от большей ставки
                diff_big = big_bet - i_big_ratio
                diff_small = small_bet - i_small_ratio
                win_big = int(diff_big - i_small_ratio)  # чистый выигрыш от меньше ставки
                win_small = int(diff_small - i_big_ratio)  # чистый выигрыш от большей ставки
                if diff_big > i_small_ratio and \
                        diff_small > i_big_ratio and \
                        (win_big >= win or win_small >= win):
                    with open('temp.txt', 'a+') as temp:
                        temp.write('\n{}'.format(str(round(i_right_bet/i_left_bet))))

