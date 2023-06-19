import numpy as np
import FinanceDataReader as fdr
import ML_RSB_env as RSB
import matplotlib.pyplot as plt

# Index(['Open', 'High', 'Low', 'Close', 'Volume', 'Change'], dtype='object')
stock = fdr.StockListing('KOSPI')
Find_id = stock['Name']
cmp_code = stock['Code']

stock_value = "삼성전자"
iid = int(Find_id.index[np.where(Find_id == stock_value)[0][0]])
cmp = cmp_code[iid]

start_day = '20220315'
end_day = '20230315'
risk = 0.9 # ~ 1.0
buy_flag = 1

input_size = 100 #(200 x 5)
output_size = 50 # maximum waitting (day)

Stock_data = fdr.DataReader(cmp, start_day, end_day)
record_price = np.array(Stock_data['Close'])
Stock_numpy = np.array(Stock_data)

max_length = int(record_price.shape[0])
init_price = 1000000

# print(record_price)
# print(Stock_numpy[:201, 3])

Buy_point = [[], []]
Sell_point = [[], []]

env = RSB.StockENV(Stock_numpy, record_price, init_price, input_size, output_size)

def main():
    interval = 10
    max_episode = 1
    cost = 0
    # start is inital price x 10
    for episode in range(max_episode):
        state, done = env.reset()
        # print(state.shape)
        # e = max((1. / ((episode // 500) + 1)), 0.1)
        e = 1
        while not done:
            # -----------------------------
            print("---------State---------")
            print("I have a money (KRW) : ", env.Price)
            print("I have a stock : ", env.Stock)
            now_stock = env.Reward_price[env.client_time]
            print("Now Stock close price : ", now_stock)

            if np.random.rand(1) < e:
                action = np.random.randint(1, output_size)
            else:
                action = np.random.randint(1, output_size)

            if env.Buy_flag == 1:
                print("Now I'm, trying Buy")
                Buy_point[0].append(env.client_time)
                Buy_point[1].append(now_stock)
            else:
                print("Now I'm, trying Sell")
                Sell_point[0].append(env.client_time)
                Sell_point[1].append(now_stock)

            print("-----------Action-------------")
            print(action, "day after ~ ")

            next_state, reward, done = env.step(action)
            print("-----------Reward-------------")
            print("Expect stock : ", env.Reward_price[env.client_time])
            print("Reward : {}".format(reward))
            print("Money : {}, Stock : {}, Expect_value : {}".format(env.Price, env.Stock, env.Price + env.Stock * env.Reward_price[env.client_time]))

            print("------------- Next state ---------------")

    plt.plot(range(max_length), record_price)
    plt.scatter(Buy_point[0], Buy_point[1], s=100, c='r')
    plt.scatter(Sell_point[0], Sell_point[1], s=100, c='b')
    plt.show()

if __name__ == '__main__':
    main()




