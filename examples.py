from ton_fragment.numbers.numbers import Numbers

auction_numbers = Numbers('auction')
print(auction_numbers.result)

listed_auction_numbers = Numbers('auction', 'listed')
print(listed_auction_numbers.result)

ending_auction_numbers = Numbers('auction', 'ending')
print(ending_auction_numbers.result)

sold_numbers = Numbers('sold')
print(sold_numbers.result)

listed_sold_numbers = Numbers('sold', 'listed')
print(listed_sold_numbers.result)

ending_sold_numbers = Numbers('sold', 'ending')
print(ending_sold_numbers.result)

sale_numbers = Numbers('sale')
print(sale_numbers.result)

listed_sale_numbers = Numbers('sale', 'listed')
print(listed_sale_numbers.result)

ending_sale_numbers = Numbers('sale', 'ending')
print(ending_sale_numbers.result)

from ton_fragment.usernames.usernames import Usernames

auction_usernames = Usernames('auction')
print(auction_usernames.result)

listed_auction_usernames = Usernames('auction', 'listed')
print(listed_auction_usernames.result)

ending_auction_usernames = Usernames('auction', 'ending')
print(ending_auction_usernames.result)

sold_usernames = Usernames('sold')
print(sold_usernames.result)

listed_sold_usernames = Usernames('sold', 'listed')
print(listed_sold_usernames.result)

ending_sold_usernames = Usernames('sold', 'ending')
print(ending_sold_usernames.result)

sale_usernames = Usernames('sale')
print(sale_usernames.result)

listed_sale_usernames = Usernames('sale', 'listed')
print(listed_sale_usernames.result)

ending_sale_usernames = Usernames('sale', 'ending')
print(ending_sale_usernames.result)

from ton_fragment.numbers.number import Number

example_number = '8888888'
phone_number = Number(example_number)
print(phone_number.data)
print(phone_number.number)
print(phone_number.status)
print(phone_number.ends_in)