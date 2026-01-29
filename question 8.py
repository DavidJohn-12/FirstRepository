data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}
import pandas as pd
# Create the DataFrame
df = pd.DataFrame(data)
# Add a new column derived from existing columns
df["A_plus_C"] = df["A"] + df["C"]

# Print the final DataFrame
print(df)