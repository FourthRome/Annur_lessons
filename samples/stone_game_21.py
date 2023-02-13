def is_game_over(pile_a, pile_b):
    return pile_a + pile_b >= 77


def player_1(pile_a, pile_b, turn_num, turn_to_win=None):
    if turn_to_win and turn_num > turn_to_win:
        return False
    options = (
        (pile_a, pile_b * 2),
        (pile_a * 2, pile_b),
        (pile_a + 1, pile_b),
        (pile_a, pile_b + 1),
    )
    result = True
    for move in options:
        if is_game_over(*move):
            return False
        result = result and player_2(*move, turn_num, turn_to_win)
    return result


def player_2(pile_a, pile_b, turn_num, turn_to_win=None):
    if turn_to_win and turn_num > turn_to_win:
        return False
    options = (
        (pile_a, pile_b * 2),
        (pile_a * 2, pile_b),
        (pile_a + 1, pile_b),
        (pile_a, pile_b + 1),
    )
    result = False
    for move in options:
        if is_game_over(*move):
            if turn_to_win:
                if turn_to_win == turn_num:
                    return True
                else:
                    return False
            else:
                return True
        result = result or player_1(*move, turn_num + 1, turn_to_win)
    return result


if __name__ == '__main__':
    for s in range(68, 1, -1):
        if player_1(8, s, 1):
            print(s)
