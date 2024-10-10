
```markdown
# [QUANT] Option Pricing Model

## Description

This project focuses on trading financial derivatives, specifically European call and put options, for a hypothetical company. The model estimates the option price based on historical data and various market factors. 

A derivative's value is derived from an underlying asset, such as a stock. The option pricing model determines the fair value of an option, which is crucial for investment banks and traders.

### Key Features of the Options:

- Call Option: Gives the buyer the right to purchase the underlying asset at a predetermined strike price before expiration.
- Put Option: Gives the buyer the right to sell the underlying asset at a predetermined strike price before expiration.

### Objective

The objective of this project is to estimate the option price using a mathematical model based on the following features:

- Type of the Option**: Call or Put
- Spot Value of the Underlier Stock
- Strike Price of the Option
- Risk-Free Rate**: The interest rate at which market participants can borrow or lend money
- Time to Expiry**: The time remaining until the option's expiration
- Market Fear Index**: A hypothetical metric indicating market volatility, ranging from 0 (calm) to 100 (volatile)
- Buy/Sell Ratio**: A hypothetical metric indicating market demand, ranging from 0.25 (high sell orders) to 4 (high buy orders)

## Training Dataset

The training dataset contains approximately 10,000 samples, each representing a unique option. The schema for the training dataset is as follows:

| Field               | Description                                                  |
|---------------------|--------------------------------------------------------------|
| Id                  | Unique identifier for each test case                        |
| OptionType          | Type of option (Call or Put)                                |
| Strike              | Option Strike Price ($)                                     |
| Spot                | Spot value of the underlier ($)                             |
| RiskFreeRate        | Interest rate (%)                                           |
| MarketFearIndex     | Market Fear Index (0-100)                                  |
| BuySellRatio        | Buy Order to Sell Order Ratio (0.25-4)                     |
| OptionPrice         | Observed Option Price ($)                                   |

### Evaluation Criteria

Each prediction will be assessed against the observed option prices in the dataset. Note that additional test cases will be run post-submission, and the final score may vary from the initial assessment.

## Input Format

The input will be a CSV file containing option information and relevant market data, structured similarly to the training dataset, but the `OptionPrice` column will be missing.

### How to Read Input

The input can be read as follows:

```python
#!/bin/python3
import pandas as pd
from io import StringIO

inputdata = input()
inputdata = inputdata.replace("\\n", "\n")
inputdata = StringIO(inputdata)
df = pd.read_csv(inputdata)
```

### Constraints

- Estimated option prices must be non-negative.

## Output Format

The output will be in CSV format, containing the predicted option prices for each unique option.

### Sample Input

```
Id,OptionType,Strike,Spot,TimeToExpiry,RiskfreeRate,MarketFearIndex,BuySellRatio
1,Put,120,148.5581572,0.944953829,0.027206587,71.28559419,0.487120444
```

### Sample Output

```
Id,OptionPrice
1,2.877918997
```

### Additional Sample Input

```
Id,OptionType,Strike,Spot,TimeToExpiry,RiskfreeRate,MarketFearIndex,BuySellRatio\nDummy,Call,60,148.1797401,1.243255425,3.1980597,6.436489684,1.068700429
```

### Additional Sample Output

```
Id,OptionPrice
Dummy,<Predicted Option Price>
```

## Conclusion

This model provides a method for estimating option prices based on key market indicators and option characteristics, facilitating informed trading decisions in financial markets.
```

Feel free to modify any sections to better fit your project or style!
