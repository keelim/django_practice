import pandas as pd


def make_code(x):
    x = str(x)
    return 'A' + '0' * (6 - len(x)) + x


path = r'C:\Users\h0033\Desktop\python_practice\data.xls'
code_data = pd.read_excel(path)
code_data = code_data[['종목코드', '기업명']]
code_data['종목코드'] = code_data['종목코드'].apply(make_code)
