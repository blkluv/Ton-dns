# TON Fragment

## UnOfficial Fragment (Telegram - Ton Coin) Python library

[![PyPI version](https://img.shields.io/pypi/v/ton-fragment.svg)](https://pypi.org/project/ton-fragment)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/ton-fragment.svg)](#Installation)
[![Downloads](https://pepy.tech/badge/ton-fragment)](https://pepy.tech/project/ton-fragment)
[![Ton-Fragment](https://github.com/iw4p/ton-fragment/raw/master/images/main_page_fragment.jpeg
)](https://pypi.org/project/ton-fragment/)

### Note: ⚠️ This package is still under develop and need your contribution. Sometimes maybe you get an error, It's normal and fine; You can open an issue to keep me informed.

### Installation

```sh
$ pip install ton-fragment
```
Also can be found on [pypi](https://pypi.org/project/ton-fragment/)

## Usage
### Available options
```python
Usernames("auction", "priceH2L")
Usernames("auction", "listed")
Usernames("auction", "ending")

Usernames("sold", "priceH2L")
Usernames("sold", "listed")
Usernames("sold", "ending")

Usernames("sale", "priceH2L")
Usernames("sale", "listed")
Usernames("sale", "ending")

Numbers("auction", "priceH2L")
Numbers("auction", "listed")
Numbers("auction", "ending")

Numbers("sold", "priceH2L")
Numbers("sold", "listed")
Numbers("sold", "ending")

Numbers("sale", "priceH2L")
Numbers("sale", "listed")
Numbers("sale", "ending")
```
### Usernames
Get All Usernames - Top Auctions:
```python
from ton_fragment.usernames.usernames import Usernames
data = (Usernames("auction", "priceH2L"))
print(date)
```
Get All Usernames - Top Auctions - sort by recently listed:
```python
from ton_fragment.usernames.usernames import Usernames
data = (Usernames("auction", "listed"))
print(data)
```
Get All Usernames - Top Auctions - sort by ending soon:
```python
from ton_fragment.usernames.usernames import Usernames
data = (Usernames("auction", "ending"))
print(data)
```
### Numbers
Get All Numbers - Top Auctions:
```python
from ton_fragment.numbers.numbers import Numbers
data = (Numbers("sale", "priceH2L"))
print(data)
```
Get All Numbers - Top Auctions - sort by recently listed:
```python
from ton_fragment.numbers.numbers import Numbers
data = (Numbers("sale", "listed"))
print(data)
```
Get All Numbers - Top Auctions - sort by ending soon:
```python
from ton_fragment.numbers.numbers import Numbers
data = (Numbers("sale", "ending"))
print(data)
```
Get Information about a number
```python
from ton_fragment.numbers.number import Number
data = Number('8888888')
print(data.information())
print(data.number)
print(data.status)
print(data.ends_in)
```
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=iw4p/ton-fragment&type=Date)](https://star-history.com/#iw4p/ton-fragment&Date)

### Issues
Feel free to submit issues and enhancement requests or contact me via [vida.page/nima](https://vida.page/nima).

### Contributing
Please refer to each project's style and contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Update the Version** inside __init__.py
 4. **Commit** changes to your own branch
 5. **Push** your work back up to your fork
 6. Submit a **Pull request** so that we can review your changes
