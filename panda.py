import pandas as pd
import matplotlib.pyplot as plt
excel_file_path = 'Apartments.xlsx'
df = pd.read_excel(excel_file_path,sheet_name=2)
#print(df)
df_meterandprice = df.loc[:,['Price', 'Square meteres' , 'Walk distance from the University']]
df_meterandprice=df_meterandprice.set_index('Square meteres')
df_meterandprice['Price'] = df_meterandprice['Price']/1000
print(df_meterandprice)
ax = df_meterandprice.plot.bar()
plt.show()
