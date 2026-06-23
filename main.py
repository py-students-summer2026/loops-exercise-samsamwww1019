import easy
import medium
import difficult

def do_easy():
    # "easy" problems
    # easy.one()
    # easy.two()
    # easy.three()
    # easy.four()
    # easy.five(10)
    # easy.six(8)
    # easy.seven('circumlocution')
    # easy.eight(24)
    # easy.nine()
    # easy.ten('circumlocution')

    easy.one()
    easy.two()
    easy.three()
    easy.four()
    easy.five(10)
    easy.six(8)
    easy.seven('circumlocution')
    easy.eight(24)
    easy.nine()
    easy.ten('circumlocution')
    pass # do nothing

def do_medium():
    # "medium" problems
    # medium.one()
    # medium.two()
    # medium.three()
    # medium.four()
    # medium.five(10)
    # medium.six(8)
    # medium.seven()
    # medium.eight(24)
    # medium.nine()
    # medium.ten()

    medium.one([4, 8, 2, 10, 6])
    medium.two([4, 8, 2, 10, 6])
    medium.three('racecar')
    medium.four(2, 2, 10)
    medium.five([4, 8, 2, 10, 6])
    medium.six(8)
    medium.seven(49)
    medium.eight()
    medium.nine('Hello, world! This is Python.')
    medium.ten([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
    pass # do nothing

def do_difficult():
    # "difficult" problems
    # difficult.one()
    # difficult.two()
    # difficult.three()
    # difficult.four()
    # difficult.five(10)
    # difficult.six(8)
    # difficult.seven()
    # difficult.eight(24)
    # difficult.nine()
    # difficult.ten()

    difficult.one(12)
    difficult.two(8)
    difficult.three('listen', 'silent')
    difficult.four(2, 2, 10)
    difficult.five([5, 2, 9, 1, 7])
    difficult.six(6)
    difficult.seven(12345)
    difficult.eight('The quick brown fox jumps over the lazy dog')
    difficult.nine('The quick brown fox jumps over the lazy dog')
    difficult.ten()
    pass # do nothing

def main():
    do_easy()
    do_medium()
    do_difficult()

main()