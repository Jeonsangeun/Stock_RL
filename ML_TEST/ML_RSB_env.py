import numpy as np
import FinanceDataReader as fdr

class StockENV:
    def __init__(self, stock, Closed_stock, init_price, input_size, output_size):
        self.Stock_data = stock
        self.Reward_price = Closed_stock
        self.input = input_size
        self.output = output_size
        self.client_time = self.input
        self.end_time = len(self.Reward_price) - 1
        self.Stock = 0
        self.Money = init_price
        self.Price = 0
        self.Buy_flag = 1


    def reset(self):
        self.client_time = self.input
        self.Stock = 0
        self.Price = self.Money
        self.Buy_flag = 1

        state = self.Buy_flag * self.Stock_data[:self.input, :]
        done = False

        return state, done

    def step(self, action):
        reward_price = self.Reward_price[self.client_time]
        self.client_time += action
        done = False

        signal_ratio = 0.0  # action signal : sr < 1 : Negative, sr > 1 : Positive
        # sr = 0 heavy penalty | sr = 1 not bad | sr >> 1 fucking good
        # reward = w * (1 - tanh(sr))

        if self.client_time >= self.end_time:
            done = True
            if self.Buy_flag == 1:
                self.Stock += self.Price // reward_price
                print("End Total usage : ", self.Stock * reward_price)
                self.Price = self.Price % reward_price

            elif self.Buy_flag == -1:
                self.Price += self.Stock * reward_price
                print("End Total take : ", self.Stock * reward_price)
                self.Stock = 0

            signal_ratio = (self.Stock * self.Reward_price[-1] + self.Price) / self.Money
            self.client_time = self.end_time

        else:
            if self.Buy_flag == 1:
                self.Stock += self.Price // reward_price
                print("Total usage : ", self.Stock * reward_price)
                self.Price = self.Price % reward_price
                signal_ratio = self.Reward_price[self.client_time] / reward_price

            elif self.Buy_flag == -1:
                self.Price += self.Stock * reward_price
                print("Total take : ", self.Stock * reward_price)
                self.Stock = 0
                signal_ratio = reward_price / self.Reward_price[self.client_time]

            self.Buy_flag = -1 * self.Buy_flag

        next_state = self.Buy_flag * self.Stock_data[(self.client_time - self.input):self.client_time, :]
        reward = np.tanh(signal_ratio - 1) - 1
        return next_state, reward, done



