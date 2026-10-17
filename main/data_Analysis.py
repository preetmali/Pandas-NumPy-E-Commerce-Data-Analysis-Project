import pandas as pd
import numpy as np

def Analysis_data(cu,ore,prod):
   summary={}
   

   # Which product sells the most?
   merged_df=ore.merge(prod,how='outer',on='Product_ID') 
   product_name= merged_df.groupby('Product_Name')
   summary["Which product sells the most?"]=product_name['Quantity'].sum().sort_values(ascending=False).index[0]

   # Which category generates the highest revenue?
   merged1_df=ore.merge(prod,how='outer',on='Product_ID')
   merged1_df['Revenue']=(merged1_df['Unit_Price']*merged1_df['Quantity'])*(1-(merged1_df['Discount_Percent']/100))
   Category1=merged1_df.groupby('Category')['Revenue'].sum().sort_values(ascending=False).index[0]
   summary["Which category generates the highest revenue?"]=Category1
   ore['Revenue']=merged1_df['Revenue']


   # Which city generates the highest sales?
   mergedC_df=cu.merge(ore,how='outer',on='Customer_ID')
   summary['Which city generates the highest sales?']=mergedC_df.groupby('City')['Revenue'].sum().sort_values(ascending=False).index[0]

   # How much sales revenue is generated each month?
   # print(ore.head())
   ore['Order_Date']=pd.to_datetime(ore['Order_Date'], errors='coerce')
   ore['Month_name']=ore['Order_Date'].dt.strftime('%b')
   summary['Which month generates the highest sales?']=ore.groupby('Month_name')['Revenue'].sum().sort_values(ascending=False).index[0]


   # Which payment method is used the most?
   summary["Which payment method is used the most?"]= ore['Payment_Method'].value_counts().idxmax()


   # Which orders result in a loss?
   merged_loss_df = ore.merge(prod, how='inner', on='Product_ID')
   merged_loss_df['Total_Cost'] = merged_loss_df['Cost_Price'] * merged_loss_df['Quantity']
   merged_loss_df['Profit'] = merged_loss_df['Revenue'] - merged_loss_df['Total_Cost']
   loss_orders = merged_loss_df[merged_loss_df['Profit'] < 0]
   if not loss_orders.empty:
    summary['Which orders result in a loss?']=(loss_orders[['Order_ID', 'Product_Name', 'Quantity', 'Revenue', 'Total_Cost', 'Profit']])
   else:
    summary['Which orders result in a loss?']=("No orders resulted in a loss! All orders are profitable.")


   # Which products experience increased sales due to discounts?
   merged_discount_df = ore.merge(prod, how='inner', on='Product_ID')
   product_corr = merged_discount_df.groupby('Product_Name').apply(
   lambda x: x['Discount_Percent'].corr(x['Quantity']) if len(x) > 1 else np.nan)
   product_corr = product_corr.dropna()
   products_boosting_sales = product_corr[product_corr > 0].sort_values(ascending=False)   
   if not products_boosting_sales.empty:
    for p_name, score in products_boosting_sales.items():
        summary['Which products experience increased sales due to discounts?']=(f"Product: {p_name} | Correlation Score: {score:.2f}")
   else:
    summary['Which products experience increased sales due to discounts?']=("The data is insufficient, or no positive impact of discounts on sales was observed.")


   return summary
