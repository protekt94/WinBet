def bet():
    ratio_1 = float(input('Введите меньшую ставку: '))
    ratio_2 = float(input('Введите большую ставку: '))
    win = 100  # Минимальный выигрыш
    big_gen = [i_num * 1000 for i_num in range(101)]  # ставка на меньший коэффициент
    small_gen = [i_num * 100 for i_num in range(101)]  # ставка на больший коэффициент
    for i_big_ratio in big_gen:
        for i_small_ratio in small_gen:
            big_bet = i_big_ratio * ratio_1  # выигрыш от меньшей ставки
            small_bet = i_small_ratio * ratio_2  # выигрыш от большей ставки
            diff_big = big_bet - i_big_ratio
            diff_small = small_bet - i_small_ratio
            win_big = int(diff_big - i_small_ratio)  # чистый выигрыш от меньше ставки
            win_small = int(diff_small - i_big_ratio)  # чистый выигрыш от большей ставки
            if diff_big > i_small_ratio and \
                    diff_small > i_big_ratio and \
                    (win_big >= win or win_small >= win):
                print('\nДля победы нужно поставить {} : {}'
                      '\nВыигрыш составит {} : {}'
                      .format(i_big_ratio, i_small_ratio, win_big, win_small))


if __name__ == '__main__':
    bet()
