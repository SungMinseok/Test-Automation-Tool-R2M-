# a1 = 'test_{0}_{1}_가나다.xlsx'
# a = a1
# arg0 = 'KR_R2M'
# arg1 = '패치'

# b = a.format(arg0, arg1)


# print(b)
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import test2

test2.test()