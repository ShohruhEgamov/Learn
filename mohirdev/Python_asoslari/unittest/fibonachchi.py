# 4. Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi funksiya
def is_fibonacci(son):
    def is_perfect_square(x):
        s = int(x ** 0.5)
        return s * s == x

    return is_perfect_square(5 * son * son + 4) or is_perfect_square(5 * son * son - 4)
