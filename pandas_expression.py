import pandas as pd
df = pd.read_csv("gene_expression.csv")
print(df)
max_expression = df["expression"].max()
print("Max expression:", max_expression)

print("Number of genes:", len(df))
print("Data shape:", df.shape)
print(df.head())
