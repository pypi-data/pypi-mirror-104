# mmcrypto

Python package get and save crypto data from wazirx.

Type these in our linux terminal to understand the usage
```py
pip3 install mmcrypto
python3
>>> from mmcrypto import Crypto, Price
>>> directory_to_save_data = '/home/user/data/'
>>> Crypto.update(directory_to_save_data)
>>> Crypto.all(directory_to_save_data)
>>> crypto = Crypto('btc', directory_to_save_data)
>>> list(crypto.get_prices())
>>> for p in crypto.get_prices():
...     for attr in Price.attrs:
...         print(attr, p[attr])
...     print()
...
>>>


```
