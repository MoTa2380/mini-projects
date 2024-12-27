import pandas as pd
import matplotlib.pyplot as plt 

class DataAnalyzer:
    """Class for analyzing CSV data and plotting pie charts for specified columns."""

    def __init__(self, file_path: str):
        self.data = pd.read_csv(file_path)

    def preprocess_column(self, column_name: str, top_n: int) -> pd.Series:
        """Prepares data for pie chart by grouping less frequent values into 'Other'."""
        value_counts = self.data[column_name].value_counts()
        top_values = value_counts.nlargest(top_n)
        other_count = value_counts.iloc[top_n:].sum()
        prepared_data = top_values

        if other_count > 0:
            prepared_data['Other'] = other_count

        return prepared_data

    def plot_pie_chart(self, column_name: str, top_n: int):
        """Plots a pie chart for the given column with a specified number of pies."""
        data = self.preprocess_column(column_name, top_n)
        plt.figure(figsize=(8, 8))
        
        data.plot.pie(
            autopct="%1.1f%%",
            startangle=80,
            textprops={'fontsize': 8},
            labeldistance=1.01,
        )
        plt.title(f"Distribution of {column_name}")
        plt.ylabel("")
        plt.show()


file_path = "unicorn_data_www.cbinsights.com_research-unicorn-companies_table_0.csv"  # Replace with your file path
analyzer = DataAnalyzer(file_path)

analyzer.plot_pie_chart("Country", top_n=9)
analyzer.plot_pie_chart("Industry", top_n=6)
