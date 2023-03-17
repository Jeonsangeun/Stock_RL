# Stock_RL
난 부자가 되고싶어

주식을 하다가 문뜩 떠오른 생각이 있다. 지금까지 공부한 머신러닝, 딥러닝으로 주가를 예측하거나 매수, 매도 액션의 조언을 구해줄 수 있지 않을까?
참고를 얻기 위해서 구글링을 뒤적뒤적했다. (2020/12)

강화학습으로 주식을 하는 것은 의미가 없다.
데이터를 모으고 자동으로 연산하여 분석에 편리함을 줄 수 있는 코드를 짜보자. (2023/03)

## Allocation Planning 

국내 배당주를 분석할 수 있는 코드를 짜보자

import numpy as np
import openpyxl as excel
import FinanceDataReader as fdr
from tqdm import tqdm

## Reinforcement Learning

주식은 잘하는법이 없다고 했다. 하지만 옛날부터 주식을 해온사람과 이제 주식을 시작하는 주린이 사이에는 분명히 짬빠가 있을것이다.
옛날부터 주식을 하는 사람을 모델로 구현할 수 있다면 주린이라도 매수 매도에 도움을 주지 않을까?

