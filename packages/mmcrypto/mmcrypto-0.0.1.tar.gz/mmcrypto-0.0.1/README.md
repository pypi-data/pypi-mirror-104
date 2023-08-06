# mmcrypto

Python package get and save crypto data from wazirx.

Type these in our linux terminal to understand the usage
```py
pip3 install mmcrypto
python3
>>> from mmcrypto import Crypto
>>> directory_to_save_data = '/home/user/data/'
>>> Crypto.update(directory_to_save_data)
>>> Crypto.all(directory_to_save_data)
>>> crypto = Crypto('btc', directory_to_save_data)
>>> crypto.get_prices()
>>> 


```
