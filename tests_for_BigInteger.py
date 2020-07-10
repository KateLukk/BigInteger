from BigInteger import BigInteger


def test_summation():
    s = BigInteger('+', '687911')
    s1 = BigInteger('-', '538689')
    s2 = BigInteger('-', 'h')
    s3 = BigInteger('+', '17812')
    s4 = BigInteger('-', '3456876')
    result1 = s.summation(s3)
    result2 = s1.summation(s3)
    result3 = s2.summation(s)
    result4 = s4.summation(s1)
    assert result1 == '705723'
    assert result2 == '-520877'
    assert result3 == 'only digit'
    assert result4 == '-3995565'


def test_multiplication():
    s = BigInteger('+', '356887')
    s1 = BigInteger('-', '102567')
    s2 = BigInteger('+', '10256567')
    s3 = BigInteger('-', '876547')
    result = s.multiplication(s2)
    result1 = s.multiplication(s3)
    result2 = s1.multiplication(s2)
    result3 = s1.multiplication(s3)
    assert result == '3660435426929'
    assert result1 == '-312828229189'
    assert result2 == '-1051985307489'
    assert result3 == '89904796149'


def test_difference():
    s = BigInteger('+', '356887')
    s1 = BigInteger('-', '102567')
    s2 = BigInteger('-', '1025787867')
    s3 = BigInteger('+', '57565778')
    result = s.difference(s1)
    result1 = s.difference(s3)
    result2 = s1.difference(s2)
    assert result == '459454'
    assert result1 == '-57208891'
    assert result2 == '1025890434'



def test_division():
    s = BigInteger('+', '3564')
    s1 = BigInteger('-', '63')
    s2 = BigInteger('+', '36')
    s3 = BigInteger('-', '36')
    s4 = BigInteger('-', '5355')
    result = s.division(s2)
    result1 = s.division(s3)
    result2 = s4.division(s1)
    assert result == '99'
    assert result1 == '-99'
    assert result2 == '85'


test_summation()
test_difference()
test_division()
test_multiplication()

