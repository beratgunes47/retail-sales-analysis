import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/Superstore.csv")

#print("ilk 5 satır:")
#print(df.head())

#print("\nKolonlar:")
#print(df.columns)

#print("\nGenel bilgi:")
#print(df.info())

#print("Toplam Satış:", df["Sales"].sum())


#print("Toplam Kar:", df["Profit"].sum())

print("\n kategoriye göre toplam kar:")

print(df.groupby("Category")["Profit"].sum())


print("\n kategoriye göre toplam satış:")

print(df.groupby("Category")["Sales"].sum())

category_analysis = df.groupby("Category").agg({
    "Sales":"sum",
    "Profit":"sum"
})


category_analysis["Kar_marji_%"]=(
    category_analysis["Profit"] / category_analysis["Sales"]
) * 100

category_profit = df.groupby("Category")["Profit"].sum()
category_sales = df.groupby("Category")["Sales"].sum()

margin = pd.DataFrame()
margin["Sales"] = category_sales
margin["Profit"] = category_profit
margin["Profit_Margin"] = margin["Profit"] / margin["Sales"]

print("Kategori Analizi:")
print(margin)
#print("Kategori analizi:")
#print(category_analysis)

#print("Kategoriye göre ortalama indirim:")
#print(df.groupby("Category")["Discount"].mean())

#print("\nDiscount ile Profit korelasyonu:")
#print(df[["Discount", "Profit"]].corr())

#print("\nFurniture alt kategori kar analizi:")
furniture_df = df[df["Category"] == "Furniture"]
#print(furniture_df.groupby("Sub-Category")["Profit"].sum())


#print("\nTables Ortalama İndirim:")
tables_df = df[df["Sub-Category"] == "Tables"]
#print(tables_df["Discount"].mean())

#print("\nTables Toplam Satış:")
#print(tables_df["Sales"].sum())


furniture_df = df[df["Category"]=="Furniture"]
subcat_profit = furniture_df.groupby("Sub-Category")[["Profit","Discount"]].agg({"Profit":"sum","Discount":"mean"})
print("\nFurniture Alt Kategori Analizi:")
print(subcat_profit)

plt.figure(figsize=(8,5))
sns.barplot(x=category_profit.index, y=category_profit.values)
plt.title("Kategoriye Göre Toplam Kar")
plt.ylabel("Profit")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=subcat_profit.index, y=subcat_profit["Profit"].values)
plt.title("Furniture Alt Kategori Kar")
plt.ylabel("Profit")
plt.show()