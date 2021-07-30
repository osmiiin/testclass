#%% 실수의 오류
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

print("%f" %0.3) # 6자리까지만 정확하므로 6자리가 기본값

#%% 실수의 오류 해결 1
import math

print(math.isclose(0.1 + 0.2, 0.3))

#%% 실수의 오류 해결 2
from decimal import Decimal

print(float(Decimal('0.1') + Decimal('0.2')))

# 두 값을 비교할 때는 is close 활용
# 연산을 통한 결과값은 decimal 활용
