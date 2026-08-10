# Import Required Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Dataset
df = pd.read_csv('Gurgaon_Real_Estate_Data.csv')
# print(df.head())

# Basic Dataset Overview
# print(df.shape)
# print(df.info())

# Standardize Column Names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
# print(df.columns)
# print(df.info())


# Convert Numeric Columns
df["price"] = df["price"].astype(str).str.replace(",", "", regex=False).astype(float).astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)
# print(df.info())

# Clean Categorical Columns
df["status"] = df["status"].str.strip().str.lower()
df["flat_type"] = df["flat_type"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower().map({"approved by rera": True, "not approved by rera": False})
# print(df.info())

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Answering Business Questions with Analysis

# 1. Which is the costliest flat in the dataset?
costliest_flat = df.loc[df["price"].idxmax()]
print(f"The costliest flat in the dataset is a {costliest_flat['flat_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']/10000000} crores. It has an area of {costliest_flat['area']} sqft and a rate per sqft of {costliest_flat['rate_per_sqft']}. The flat is built by {costliest_flat['builder_name']} and is {'approved by RERA' if costliest_flat['rera_approval'] else 'not approved by RERA'}.")

# 2. Which locality has the highest average price?
locality_avg_price = df.groupby("locality")["price"].mean().sort_values(ascending=False)
print(f"The locality with the highest average price is {locality_avg_price.idxmax()} with an average price of {locality_avg_price.max()/10000000} crores.")

# 3. Which locality has the highest rate per square foot?
locality_avg_rate = df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False)
print(f"The locality with the highest rate per square foot is {locality_avg_rate.idxmax()} with an average rate of {locality_avg_rate.max()}.")

# 4.  Ready-to-move vs Under-construction pricing?
status_pricing = df.groupby("status")["price"].median()
print(f"The median price for ready-to-move flats is {status_pricing['ready to move']/10000000} crores.")
print(f"The median price for under-construction flats is {status_pricing['under construction']/10000000} crores.")

# 5. Does RERA approval affect pricing?
rera_pricing = df.groupby("rera_approval")["price"].median()
print(f"The median price for RERA approved flats is {rera_pricing[True]/10000000} crores.")

# 6. How does area impact price?
sns.scatterplot(x="area", y="price", data=df)
plt.show()

# 7. Which BHK configuration is most expensive?
bhk_avg_price = df.groupby("flat_type")["price"].mean().sort_values(ascending=False)
print(f"The most expensive BHK configuration is {bhk_avg_price.idxmax()} with an average price of {bhk_avg_price.max()/10000000} crores.")

# 8. Which property type is the costliest?
property_type_avg_price = df.groupby("property_type")["price"].mean().sort_values(ascending=False)
print(f"The costliest property type is {property_type_avg_price.idxmax()} with an average price of {property_type_avg_price.max()/10000000} crores.")

# 9. Do certain builders price higher?
builder_avg_price = df.groupby("builder_name")["price"].mean().sort_values(ascending=False)
print(f"The builder with the highest average price is {builder_avg_price.idxmax()} with an average price of {builder_avg_price.max()/10000000} crores.")

# 10. Are larger homes more expensive per sqft?
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.show()

print("\nAnalysis completed successfully.\n")
print("Summary of Key Findings:")
print(f"1. The costliest flat is a {costliest_flat['flat_type']} located in {costliest_flat['locality']} priced at {costliest_flat['price']/10000000} crores.")
print(f"2. The locality with the highest average price is {locality_avg_price.idxmax()} with an average price of {locality_avg_price.max()/10000000} crores.")
print(f"3. The locality with the highest rate per square foot is {locality_avg_rate.idxmax()} with an average rate of {locality_avg_rate.max()}.")
print(f"4. The median price for ready-to-move flats is {status_pricing['ready to move']/10000000} crores, while for under-construction flats it is {status_pricing['under construction']/10000000} crores.")
print(f"5. The median price for RERA approved flats is {rera_pricing[True]/10000000} crores, indicating that RERA approval may positively influence pricing.")





