# escape 코드
# \n \t \\ \' \000(널문자)

#separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep=",")
print('010', '1111', '2222', sep="-")
print('python','gmail.com', sep='@')

print()

#end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)

print()

# format 사용(d, s, f) digit string float
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two')) # 암묵적으로 앞이 0 뒤가 1
print('{1} {0}'.format('one', 'two'))
print()
# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice')) # 중앙정렬

print('%.5s' % ('pythonStudy')) #공간이 5개
print('{:10.5}'.format('pythonStudy')) #공간은 10개, 5개만 출력
print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()

print('%06.2f' % (3.1415926538))
print('{:06.2f}'.format(3.1415926538))