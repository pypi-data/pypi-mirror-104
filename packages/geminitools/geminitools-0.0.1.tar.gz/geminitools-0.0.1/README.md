# geminitools

Geminitools is a Python package that can help you talk to the Gemini Exchange REST API. 

Geminitools is a simple API. You can't interface 1:1 with the Gemini Exchange API with geminitools. There are other packages for that. Instead, the main thing you can do is buy. As of yet there is no sell option (why would you want to anyway?).

## Installation

`pip install -i geminitools`

## Example Usage

```
import geminitools

gem = geminitools.Gem('https://api.gemini.com', 'key', 'secret')

gem.place_cost_buy_order('BTCUSD', 10, 70000)
```

## API

### class geminitools.Gem(base_url, key, secret)

#### get_supported_symbols()

Make a call to the `/v1/symbols` endpoint and return a list of accepted symbols.

#### get_ticker_price(symbol, price_type='ask')

Make a call to the `/v1/pubticker/` endpoint and return the value defined by `price_type` - defaults to 'ask', the asking price.

#### convert_cost_to_asset_amount(symbol, cost, rounded=8)

Divides `cost` by the current ticker price given by `symbol` rounding to `rounded` decimal places, and returns the resulting asset amount. 

E.g. if `symbol` is 'btcusd', `cost` is 50 (USD) and the current ticker price is 60000 (USD), the result would be 50 / 60000 = 0.00083333 (BTC)

#### place_amount_buy_order(symbol, amount, price)

Make a call to the `/v1/order/new` endpoint, placing a buy order for `amount` with a limit of `price`, and returns the API response. If you pass `symbol` 'BTCUSD', `amount` would be the quantity of BTC you want to buy, while `price` would be the max USD market price you're willing to pay.

E.g. `amount` = 0.1 and `price` = 10000 would cause 0.1 BTC to be bought if the price of BTC is less than or equal to 10000 USD.

#### place_cost_buy_order(symbol, cost, price)

Similar to `place_asset_buy_order` but calculates the amount of the asset to buy based on the `cost` passed. Returns the API response.

E.g. Passing `symbol` 'BTCUSD' and a `cost` value of 10 would cause the order of 10 USD worth of BTC to be bought.