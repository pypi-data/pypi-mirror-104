# Crypto
- A crypto currency trading environment.
- Very similar to [OpenAI](https://gym.openai.com/)

# Install

# Parameters
- `dataset`: str.  
  - Location of the CSV dataset
- `available_cash`: int.  
  - Starting amount of money that can be used to be traded for a cryptocurrency
- `n_action`: int. default=*10* 
  - Number of available action. 
  - I.E. 10 action means 10 selling and 10 buying options.
- `loss_limit`: float. default=*0.7* 
  - Stops when portfolio losses X amount of the available_cash. 
- `SEED`: int. default=*1337*  
  - Sets random seed.


# Requirements
- CSV with only open, high , low and close prices.

# Implementation
```python
env = cryptoEnv("xxx_dataset.csv",100)
for i in range(10):
  s = env.reset()
  done = False
  while not done:
    action = env.action_space.sample()
    s_, r, done, info = env.step(action)
    s = s_
```
## Optional
- Call the save_records functions to plot the data after each episode
  ```python
  env.save_records()
  ```


