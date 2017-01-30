from MoneyModel2 import *
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt

model = MoneyModel2(50, 10, 10)
for i in range(100):
    model.step()

gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
plt.show()

agent_wealth = model.datacollector.get_agent_vars_dataframe()
agent_wealth.head()
end_wealth = agent_wealth.xs(99, level="Step")["Wealth"]
end_wealth.hist(bins=range(agent_wealth.Wealth.max()+1))
plt.show()

one_agent_wealth = agent_wealth.xs(14, level="AgentID")
one_agent_wealth.Wealth.plot()
plt.show()
