
def selection_sort(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        m = min(b)
        b.remove(m)

        return [m] + selection_sort(b)




a = [1, 4, 0, 2, 6, 7]
print(selection_sort(a))

def reverse_string(s):
    if s == '':
        return ''
    else:
        return reverse_string(s[1:]) + s[0]

me = 'VAIBHAV'
print(reverse_string(me))


def power_problem(b, n):
    if n == 0:
        return 1
    elif n < 0:
        return power_problem(b, n+1)/b
    else:
        return b*power_problem(b, n-1)


print(power_problem(5, -3))