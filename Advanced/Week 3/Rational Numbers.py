SUPER_NUMS = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
SUB_NUMS = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
"""
version 1
2021, 10, 20
"""


def gcd(a, b):
    """
  Returns the Greatest Common Divisor between `a` and `b`.
  """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
  returns the lowest common multiple between `a` and `b`.
  """
    mult1 = 1
    mult2 = 1
    ao = a
    bo = b
    if ao != bo:
        while ao != bo:
            if ao < bo:
                mult1 += 1
                ao = a * mult1
            if bo < ao:
                mult2 += 1
                bo = b * mult2
    return ao, mult1, mult2


def rtonum(self, other):
    """
  returns the two rational fractions "self" and "other" as numbers
  """
    a = []
    b = []
    dod = ""
    switch = True
    i = [self.mixed, other.mixed]
    for l in i:
        if type(l) == type(str()):
            i[i.index(l)] = 0
    for nums in self.numerator + self.denominator:
        if nums in SUPER_NUMS:
            dod += str(SUPER_NUMS.index(nums))
        elif switch == True:
            a.append(dod)
            dod = ""
            switch = False
        if switch == False:
            dod += str(SUB_NUMS.index(nums))
    a.append(dod)
    if len(a) > 1:
        a[0] = int(a[0]) + (int(a[1]) * int(i[0]))
    else:
        a[0] = int(1) * int(i[0])
        a.append(int(1))
    dod = ""
    switch = True
    for nums in other.numerator + other.denominator:
        if nums in SUPER_NUMS:
            dod += str(SUPER_NUMS.index(nums))
        elif switch == True:
            b.append(dod)
            dod = ""
            switch = False
        if switch == False:
            dod += str(SUB_NUMS.index(nums))
    b.append(dod)
    if len(b) > 1:
        b[0] = int(b[0]) + (int(b[1]) * int(i[1]))
    else:
        b[0] = int(1) * int(i[1])
        b.append(int(1))
    return a, b



class Rational:
    """
  Represents any rational number in fraction form.
  """
    def __init__(self, numerator, denominator=1):
        """
    Initialises a rational number with the given numerator and denominator.
    """
        num = ""
        dem = ""
        mixed = ""
        neg = False
        if numerator == 0:
            mixed = 0
        if numerator < 0 and denominator > 0:
            numerator = abs(numerator)
            neg = True
        divis = gcd(numerator, denominator)
        numerator = int(numerator / divis)
        denominator = int(denominator / divis)
        if denominator <= numerator:
            mixed = 0
            while denominator <= numerator:
                numerator = numerator - denominator
                mixed += 1
        if numerator >= 10:
            for i in str(numerator):
                num = num + SUPER_NUMS[int(i)]
        else:
            num = SUPER_NUMS[numerator]
        if denominator >= 10:
            for s in str(denominator):
                dem = dem + SUB_NUMS[int(s)]
        else:
            dem = SUB_NUMS[denominator]
        self.numerator = num
        self.denominator = dem
        if neg == False:
            self.mixed = mixed
        else:
            if type(mixed) == type(int()):
                self.mixed = int(mixed * -1)
            else:
                self.mixed = "-"

    def __eq__(self, other):
        """
    Returns True if the two given Rational numbers are equal.
    """
        fra1, fra2 = rtonum(self, other)
        if fra1 == fra2:
            equals = True
        else:
            equals = False
        if equals == False:
            return False
        else:
            return True

    def __str__(self):
        """
    Returns a string representing this Rational number.
    """
        if self.numerator != SUPER_NUMS[0]:
            return str(self.mixed) + str(self.numerator) + "/" + str(
                self.denominator)
        else:
            return str(self.mixed)


    def __add__(self, other):
        """
    Returns the addition (+) of two Rational numbers.
    """
        firsfrac, secfrac = rtonum(self, other)
        low = lcm(int(firsfrac[1]), int(secfrac[1]))
        firsfrac[0] = firsfrac[0] * low[1]
        secfrac[0] = secfrac[0] * low[2]
        finalfrac = Rational(int(firsfrac[0]) + int(secfrac[0]), low[0])
        return finalfrac

    def __mul__(self, other):
        """
    Returns the multiplication (*) of two Rational numbers.
    """
        firsfrac, secfrac = rtonum(self, other)
        finalfrac = Rational(
            int(firsfrac[0]) * int(secfrac[0]),
            int(firsfrac[1]) * int(secfrac[1]))
        return finalfrac

    def __sub__(self, other):
        """
    Returns self minus (-) other of two Rational numbers.
    """
        firsfrac, secfrac = rtonum(self, other)
        low = lcm(int(firsfrac[1]), int(secfrac[1]))
        firsfrac[0] = firsfrac[0] * low[1]
        secfrac[0] = secfrac[0] * low[2]
        minus = ""
        if int(firsfrac[0]) - int(secfrac[0]) < 0:
            minus = "-"
        finalfrac = Rational(abs(int(firsfrac[0]) - int(secfrac[0])), low[0])
        finalfrac.mixed = minus + str(finalfrac.mixed)
        return finalfrac

    def __truediv__(self, other):
        """
    Returns self divided by (/) other.
    """
        firsfrac, secfrac = rtonum(self, other)
        finalfrac = Rational(
            int(firsfrac[0]) * int(secfrac[1]),
            int(firsfrac[1]) * int(secfrac[0]))
        return finalfrac


def test_rational():
    fract1 = Rational(0, 1421)
    fract2 = Rational(532, 13)
    print(fract1)
    print(fract2)
    print(fract1, "==", fract2, "is", fract1 == fract2)
    print(fract1, "+", fract2, "=", fract1 + fract2)
    print(fract1, "-", fract2, "=", fract1 - fract2)
    print(fract1, "*", fract2, "=", fract1 * fract2)
    print(fract1, "/", fract2, "=", fract1 / fract2)


import random

ADD = '+'
MINUS = '-'
TIMES = '×'
DIVIDE = '÷'


def random_rational():
    num = random.randint(0, 1000)
    den = random.randint(1, 1000)
    return Rational(num, den)


test = input('Run tests? ')
if test.lower().startswith('y'):
    test_rational()
else:
    user_answer = '0'
    while user_answer:
        num1 = random_rational()
        num2 = random_rational()
        operator = random.choice((ADD, MINUS, TIMES, DIVIDE))
        print()
        print('What is {} {} {}?'.format(num1, operator, num2))

        if operator == ADD:
            answer = num1 + num2
        elif operator == MINUS:
            answer = num1 - num2
        elif operator == TIMES:
            answer = num1 * num2
        else:
            answer = num1 / num2

        answers = [
            answer,
            random_rational(),
            random_rational(),
            random_rational()
        ]
        random.shuffle(answers)
        for i, choice in enumerate(answers):
            print('{}) {}'.format(i, choice))
        user_answer = input('> ')
        if user_answer and user_answer.isdigit() and int(user_answer) < 4:
            i = int(user_answer)
            user_answer_rational = answers[i]
            if user_answer_rational == answer:
                print('Correct!')
            else:
                print('Incorrect. The correct answer was: {}'.format(answer))
        else:
            print('Invalid input. The correct answer was: {}'.format(answer))
