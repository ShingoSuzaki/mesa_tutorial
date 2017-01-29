"""
作成されるagent数はは1000
グラフでは、横軸が各エージェントが持っているwealth、
縦軸がwealthの数に対応するエージェントの数
"""
import matplotlib.pyplot as plt
from MoneyModel import *

all_wealth = []
for j in range(100):
    # Run the model
    model = MoneyModel(10) # Number of agents is 10
    for i in range(10):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        all_wealth.append(agent.wealth)

plt.hist(all_wealth, bins=range(max(all_wealth)+1))
plt.xlabel("Number of agent's wealth")
plt.ylabel("Number of agents")
plt.show()
