import pandas as pd

df = pd.read_csv("gene_expression.csv")

high_expression = df[df["expression"] > 5]

sorted_data = high_expression.sort_values("expression", ascending=False)

print(sorted_data)