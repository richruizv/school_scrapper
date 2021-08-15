import pandas as pd 
import numpy as np
from scrapper import parse_link,parse_page,parse_page_from_url_list


def run():
    df = pd.read_csv('csv/universidades_2.csv',encoding='UTF-8')

    df = df.replace(np.nan, '', regex=True)
    df_list = df.values.tolist()
    
    parse_page(df_list[7],test = 1)

    parse_page_from_url_list(df_list[7], test = 0 )





if __name__ == "__main__":
    run()