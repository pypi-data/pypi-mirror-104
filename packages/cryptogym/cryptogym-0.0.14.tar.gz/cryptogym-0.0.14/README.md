# Crypto
- A crypto currency trading environment.
- Based on [OpenAI Gym](https://gym.openai.com/)


# Install
```sh
 pip install cryptogym
  ```
# Parameters
- `dataset`: str.  
  - Location of the CSV dataset
- `available_cash`: int.  
  - Starting amount of money that can be used to be traded for a cryptocurrency
-- `purchase_size`: float. default=*1* 
  - Percentage of how much of that cryptocurrency can be purchsaed  
- `n_action`: int. default=*10* 
  - Number of available action. 
  - I.E. 10 action means 10 selling and 10 buying options.
- `loss_limit`: float. default=*0.7* 
  - Stops when portfolio losses X amount of the available_cash. 
- `min_max`: bool. default=*True* 
  - If true use a **min max scaler** else **standard scaler** for normalization. 
- `SEED`: int. default=*1337*  
  - Sets random seed.


# Requirements
- CSV with only open, high , low and close prices.

# Implementation
```python
from cryptogym.env import cryptoEnv
env = cryptoEnv("BTC_dataset.csv",100)
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

<sub><sup>MIT LICENSE</sup></sub>
  

  


