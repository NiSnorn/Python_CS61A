

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs."""
    if b >= 0:
        h = a + b #add
    else:
        h = a + -1 * b #sub
    return h(a, b)

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.
    """
    return x**2 + y**2 + z**2 - max(x, y, z)**2

def largest_factor(x):
    """Return the largest factor of x that is smaller than x."""
    for i in range(x // 2, 1, -1):
        if x % i == 0:
            return i


# def if_function(condition, true_result, false_result):
#     """Return true_result if condition is a true value, and
#     false_result otherwise.
#
#     >>> if_function(True, 2, 3)
#     2
#     >>> if_function(False, 2, 3)
#     3
#     >>> if_function(3==2, 3+2, 3-2)
#     1
#     >>> if_function(3>2, 3+2, 3-2)
#     5
#     """
#     if condition:
#         return true_result
#     else:
#         return false_result

def if_function(condition, true_func, false_func):
    """Return the result of true_func if condition is a true value, and
    the result of false_func otherwise.
    """
    if condition():
        return true_func()
    else:
        return false_func()

def with_if_statement():
    if cond():
        return true_func()
    else:
        return false_func()
#
# def with_if_function():
#     return if_function(cond(), true_func(), false_func())

def with_if_function():
    return if_function(cond, true_func, false_func)

def cond():
    return False

def true_func():
    print(42)

def false_func():
    print(47)

# result1 = with_if_statement()
# # print(result1)
#
# result2 = with_if_function()
# # print(result2)

with_if_statement()
with_if_function()







def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while x != 1:
        if x%2==0:
            x = x//2
            print(x)
        else:
            x=x*3+1
            print(x)
        i+=1
    return i

a = hailstone(10)
print(a)