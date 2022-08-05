from numpy import arange

left_bet = [round(i_bet, 2) for i_bet in arange(1.12, 2.31, 0.01)]
right_bet = [round(i_bet, 2) for i_bet in arange(1.96, 10.01, 0.01)]
big_gen = [i_num * 1000 for i_num in range(21)]  # ставка на меньший коэффициент
small_gen = [i_num * 100 for i_num in range(21)]  # ставка на больший коэффициент
win = 1000
with open('temp_1.csv', 'a+', encoding='UTF-8') as temp:
    temp.write('left_ratio;right_ratio;left_bet;right_bet;left_win;right_win;ratio')
    for i_left_bet in left_bet:
        for i_right_bet in right_bet:
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
                            (win_big >= win and win_small >= win):
                        temp.write('\n{left_bet};{right_bet};{big_ratio};{small_ratio};{win_big};{win_small};{ratio}'
                                   .format(left_bet=i_left_bet, right_bet=i_right_bet,
                                           big_ratio=i_big_ratio, small_ratio=i_small_ratio,
                                           win_big=win_big, win_small=win_small,
                                           ratio=str(round(i_right_bet / i_left_bet, 2))))
