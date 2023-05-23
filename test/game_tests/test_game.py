from game.digit_party import Digit, DigitParty


def test_simple_game():
    g = DigitParty(n=2, digits=[2, 1, 1, 2])
    g.place(0, 0)
    g.place(1, 0)
    g.place(0, 1)
    g.place(1, 1)
    assert g.theoretical_max_score() == 3
    assert g.score == 3
    assert g.show_board() == "2\t \t1\n \tX\t \n1\t \t2"
    assert g.placements == [
        ((0, 0), Digit(2)),
        ((1, 0), Digit(1)),
        ((0, 1), Digit(1)),
        ((1, 1), Digit(2)),
    ]


def test_max_2x2_game():
    g = DigitParty(n=2, digits=[2, 2, 2, 2])
    g.place(0, 0)
    g.place(1, 0)
    g.place(0, 1)
    g.place(1, 1)
    assert g.theoretical_max_score() == 12
    assert g.score == 12


def test_random_game_no_errors():
    n = 5
    g = DigitParty(n=n, digits=None)
    for r in range(n):
        for c in range(n):
            g.place(r, c)


# def test_full_game():
#     g = DigitParty(n=5, digits=[])
