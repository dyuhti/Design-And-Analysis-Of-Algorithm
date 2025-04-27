import pandas as pd

# Sample data
data = {
    'symbol': ['He', 'Na', 'Ca', 'La', 'Cl', 'O', 'N'],
    'type': ['Noble', 'Metal', 'Metal', 'Metal', 'Nonmetal', 'Nonmetal', 'Nonmetal'],
    'electrons': [0, 1, 2, 3, 1, 2, 3]
}

# Create DataFrame
elements = pd.DataFrame(data)

# Perform a self-join on the DataFrame to match Metals with Nonmetals
metals = elements[elements['type'] == 'Metal']
nonmetals = elements[elements['type'] == 'Nonmetal']

# Create all pairs of metals and nonmetals
result = pd.merge(metals, nonmetals, how='cross')

# Select and rename the columns
result = result[['symbol_x', 'symbol_y']]
result.columns = ['metal', 'nonmetal']

# Print the result
print(result)
