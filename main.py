# Importing necessary libraries
import pandas as pd  # For working with data in DataFrame format
import numpy as np   # For numerical operations (though not used directly in this code)
import matplotlib.pyplot as plt  # For creating plots
import seaborn as sea  # For statistical data visualization (based on matplotlib)

# Reading data from an Excel file
data = pd.read_excel(
    "input/PORDATA_Dias_sem_chuva.xlsx",
    sheet_name="Quadro",
    usecols="A:J",
    skiprows=7,
    nrows=61
)

# Setting display options for pandas to avoid truncating data when printing
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Renaming the first column to "Anos"
data.columns.values[0] = "Anos"

# Extracting the station names (all columns except the first one)
stations = data.columns[1:]

data = data.replace(0, np.nan)

print(data)

data_melted = data.dropna(subset=["Anos"]).melt(id_vars=['Anos'], value_vars=stations, var_name='Station', value_name='Days_without_Rain')

plt.figure(figsize=(12,8))

# The box plot will show the distribution (median, quartiles, outliers) of 'Days_without_Rain' for each 'Station'
sea.boxplot(x="Station", y="Days_without_Rain", data=data_melted)

# Adding a title to the plot
plt.title('Comparação dos Dias Sem Chuva nas Estações Meteorológicas')

# Adding labels to the x and y axes
plt.xlabel('Estação Meteorológica')
plt.xticks(rotation=45)  # Rotates the x-axis labels by 45 degrees to make them more readable
plt.ylabel('Número de Dias Sem Chuva')

# Adjusting the layout to ensure everything fits without overlap
plt.tight_layout()

try:
    plt.savefig('/app/output/dias_sem_chuva_plot_nan.png', dpi=300)
except Exception as e:
    print(f"Error saving plot: {e}")
