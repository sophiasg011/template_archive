import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### DEFINE
def main():
    df = pd.read_csv('output/data_merged.csv')
    plot_data(df)
    df = clean_data(df)
    df.to_csv('output/data_cleaned.csv', index = False)

# updated plot_data to show percentage
def plot_data(df):
    values = df['chips_sold']   
    plt.hist(values, weights = [1/len(values)] * len(values))
    plt.gca().yaxis.set_major_formatter(lambda x, _: f'{x*100:.0f}%')
    plt.savefig('output/chips_sold.pdf')

# updated from NaN to nan for version compatibility issue
def clean_data(df):
    df['chips_sold'][df['chips_sold'] == -999999] = np.nan
    return(df)
    
### EXECUTE
main()
