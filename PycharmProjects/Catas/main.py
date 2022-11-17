import pandas as pd
#import jaydebeapi


#if __name__== '__main__' :
#my_df = pd.read_excel(\home\demipt2\pandas.xlsx, sheet_name = 'sheet1', header = 0, index_col = None)
my_df = pd.read_excel('C:/Users/stasr/OneDrive?Data_Engineering/Final_Project/passport_blacklist_01032021.xlsx', sheet_name = 'blacklist', header = 0, index_col = None)

print(my_df)