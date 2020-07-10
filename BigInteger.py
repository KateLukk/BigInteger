class BigInteger:
    def __init__(self, sign, string):
        self.sign = sign
        self.string = string

    def __addition(self, obj, znak):
        d = 0
        ans = ''
        a = self.string
        b = obj.string
        if int(b) > int(a):
            a, b = b, a
        a, b = a[::-1], b[::-1]
        for i in range(len(a)):
            if i < len(b):
                sum = int(a[i]) + int(b[i]) + d
            else:
                sum = int(a[i]) + d
            if sum >= 10:
                ans += str(sum % 10)
                d = sum // 10
            else:
                ans += str(sum)
                d = 0

        return znak + ans[::-1]

    def __minus(self, obj, zn):
        a = self.string
        b = obj.string
        if int(b) > int(a):
            a, b = b, a
            if obj.sign == '-':
                zn = ''
            else:
                zn = '-'
        else:
            if self.sign == '-':
                zn = '-'
        a, b = a[::-1], b[::-1]
        z = 0
        ans = ''
        for i in range(len(a)):
            if i < len(b):
                raz = int(a[i]) - z - int(b[i])
            else:
                raz = int(a[i]) - z
            if raz < 0:
                ans += str(10 + raz)
                z = 1
            else:
                ans += str(raz)
                z = 0
        ans = ans[::-1]
        if ans[0] == '0':
            ans = ans[1:]
        return zn + ans

    def summation(self, obj):
        if not obj.string.isdigit():
            return 'only digit'
        zn = ''
        if not self.string.isdigit():
            return 'only digit'

        if obj.sign == self.sign == '-':
            zn += '-'

        elif obj.sign == '+' == self.sign:
            zn = ''

        else:
            return self.__minus(obj, zn)
        return self.__addition(obj, zn)

    def multiplication(self, obj):
        if not self.string.isdigit():
            return 'only digit'
        znak = ''
        if self.sign == obj.sign == '-' or (self.sign == '+' and obj.sign != '-'):
            znak = '+'
        else:
            znak = '-'
        if not obj.string.isdigit():
            return 'only digit'
        a = self.string
        b = obj.string
        if int(b) > int(a):
            a, b = b, a
        a, b = a[::-1], b[::-1]
        d = 0
        ans, b1, ans1 = '', '', ''
        d1 = 0
        for i in range(len(a)):
            for j in range(len(b)):
                first = int(a[i])
                second = int(b[j])
                pr = first * second + d
                if j == (len(b) - 1):
                    ans += str(pr)[::-1]
                    d = 0
                    break
                else:
                    ans += str(pr % 10)
                    d = pr // 10
            w = '0' * i + ans
            for k in range(len(w)):
                if i == 0:
                    b1 += ans
                    break
                else:
                    ans = w
                    if k < len(b1):
                        sum = int(ans[k]) + int(b1[k]) + d1
                    else:
                        sum = int(ans[k]) + d1

                    if sum >= 10:
                        ans1 += str(sum % 10)
                        d1 = sum // 10
                    else:
                        ans1 += str(sum)
                        d1 = 0
            if i != 0:
                b1 = ans1
                ans1 = ''
            d1 = 0
            ans = ''
        if b1[len(b1) - 1] == '0':
            return 0
        elif znak == '-':
            return '-' + b1[::-1]
        else:
            return b1[::-1]

    def difference(self, obj):
        if not self.string.isdigit():
            return 'only digit'
        if not obj.string.isdigit():
            return 'only digit'
        zn = ''
        if obj.sign == '+' == self.sign:
            zn = '-'
            return self.__minus(obj, zn)
        elif obj.sign == '-' == self.sign:
            zn = ''
            return self.__addition(obj, zn)
        elif obj.sign == '-' and self.sign == '+':
            zn = ''
            return self.__addition(obj, zn)
        elif obj.sign == '+' and self.sign == '-':
            zn = ''
            return self.__minus(obj, zn)


    def division(self, obj):
        if not self.string.isdigit():
            return 'only digit'
        znak = ''
        if self.sign == obj.sign == '-' or (self.sign == '+' and obj.sign != '-'):
            znak = '+'
        else:
            znak = '-'
        if not obj.string.isdigit():
            return 'only digit'
        a = self.string
        b = obj.string
        if int(b) > int(a):
            a, b = b, a
        d = a[0]
        i = 0
        ost = 0
        ans = ''
        while i <= len(a) + 1:
            if int(d) >= int(b):
                ans += str(int(d) // int(b))
                ost = str(int(b) * (int(d) // int(b)))
                d1 = d[::-1]
                ost1 = ost[::-1]
                z = 0
                ans1 = ''
                for j in range(len(d1)):
                    if j < len(ost1):
                        raz = int(d1[j]) - z - int(ost1[j])
                    else:
                        raz = int(d1[j]) - z
                    if raz < 0:
                        ans1 += str(10 + raz)
                        z = 1
                    elif raz > 0:
                        ans1 += str(raz)
                        z = 0

                d = ans1[::-1]
                ans1 = ''
            else:
                if i != 0 and i < len(a):
                    d += a[i]
                if i == len(a):
                    d += a[i - 1]
            i += 1
        if znak == "-":
            return znak + ans
        return ans


# s = BigInteger('-', '5355')
#
# s2 = BigInteger('-', '63')
# print(s.division(s2))
