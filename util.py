"""Module util"""

def factors(num):
    """Function factors return all primer factors of num with their times."""
    count = {}
    seen = set()
    can = 2
    while can <= num:
        if can not in seen:
            while num % can == 0:
                if can not in count:
                    count[can] = 1
                else:
                    count[can] += 1
                num //= can
                seen.add(can * count[can])
        can += 1
    return count

def is_prime(num):
    '''Function is_prime tell num is prime or not'''
    return factors(num) == {num:1}

def is_perfect_square(num):
    '''Function is_perfect_square tell num is perfect square or not'''
    return all(c % 2 == 0 for c in factors(num).values())

def is_perfect_cubic(num):
    '''Function is_perfect_cubic tell num is perfect cubic or not'''
    return all(c % 3 == 0 for c in factors(num).values())
