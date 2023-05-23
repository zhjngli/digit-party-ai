from game.digit_party import DigitParty

x = input("hi this is digit party. what game size? (default 5): ").strip()
if x == "":
    n = 5
else:
    n = int(x)

ds = input("do you want to input a series of digits? (for testing, default random): ")
if ds == "":
    game = DigitParty(n=n, digits=None)
else:
    game = DigitParty(n=n, digits=list(map(lambda s: int(s.strip()), ds.split(","))))

while not game.finished():
    print(game.show_board())
    print(f"current score: {game.score}")
    curr_digit, next_digit = game.next_digits()
    print(f"current digit: {curr_digit}")
    print(f"next digit: {next_digit}")
    print()
    coord = input(
        "give me 0-indexed row col coords from the top left to place the current digit (delimit with ','): "
    ).strip()
    print()

    try:
        rc = coord.split(",")[:2]
        r = int(rc[0])
        c = int(rc[1])
    except (ValueError, IndexError):
        print("can't read your coordinate input")
        continue

    try:
        game.place(r, c)
    except ValueError as e:
        print(str(e))

print(game.show_board())
print("game finished!")
print(f"your score: {game.score}")
print(f"theoretical max score: {game.theoretical_max_score()}")
print(f"% of total: {100 * game.score / game.theoretical_max_score()}")
