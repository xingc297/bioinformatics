import pandas as pd
df = pd.read_csv("gene_expression.csv")
print(df[df["expression"] > 5])
