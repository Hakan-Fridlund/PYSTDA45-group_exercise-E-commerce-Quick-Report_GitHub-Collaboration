"""
ecommerce
Class EcommerceAnalyzer
takes filepath as arg and runs load_data on init, default filepath is "../data/ecommerce_sales.csv" 
wrapper class, import the functions for calculating metrics and visualizing diagrams from dataframe
"""
from pathlib import Path
import sys
SRC_DIR = Path(__file__).resolve().parent
ROOT_DIR = SRC_DIR.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import src.io_utils as io
import src.metrics as metrics
import src.viz as viz

DATAPATH = SRC_DIR.parent / "data" / "ecommerce_sales.csv"

class EcommerceAnalyzer:
    """
    Takes filepath as argument and runs the load_data on init
    default filepath is "../data/ecommerce_sales.csv" 
    """
    def __init__(self, path = DATAPATH):
        self.df = io.load_data(path)


    def compute_revenue(self) -> float:
        """Total revenue.
        Calls on src.metrics.compute_revenue in the background."""
        return round(metrics.compute_revenue(self.df),2)

    def compute_units(self) -> int:
        """Total number of units sold.
        Calls on src.metrics.compute_units in the background."""
        return metrics.compute_units(self.df)

    def compute_aov(self) -> float:
        """Average Order Value = total revenue / number of unique orders.
        Calls on src.metrics function in the background."""
        return round(metrics.compute_aov(self.df),2)

    def revenue_by_category(self) -> pd.DataFrame:
        """Revenue per category.
        Calls on src.metrics function in the background."""
        return metrics.revenue_by_category(self.df).round(2)

    def revenue_by_city(self) -> pd.DataFrame:
        """Revenue per city.
        Calls on src.metrics function in the background."""
        return metrics.revenue_by_city(self.df).round(2)

    def top_categories(self, n:int = 3) -> pd.DataFrame:
        """The n categories with the highest revenue (default: top 3)
        Calls on src.metrics function in the background."""
        return metrics.top_categories(self.df, n = n).round(2)




    def plot_revenue_by_category(self) -> plt.Axes:
        """Plots bar diag with revenue by category.
        Displays chart automatically (no need for plt.show() in notebook)
        return viz.plot_revenue_by_category(self.df)"""

    def plot_revenue_by_city(self) -> plt.Axes:
        """Plots line diag with revenue by city. 
        Displays chart automatically (no need for plt.show() in notebook)
        Calls on src.viz function in the background."""
        return viz.plot_revenue_by_city(self.df)

    def plot_revenue_over_time(self) -> plt.Axes:
        """Plots line diag with revenue over time, with regression line.
        Displays chart automatically (no need for plt.show() in notebook)
        Calls on src.viz function in the background."""
        return viz.plot_revenue_over_time(self.df)

    def plot_total_revenue_and_units(self) -> numpy.ndarray:
        """Plots bar diag with total revenue and units, returns an array with 2plt.Axes
        Displays chart automatically (no need for plt.show() in notebook),
        Calls on src.viz function in the background."""
        return viz.plot_total_revenue_and_units(self.df)

    def plot_aov(self) -> plt.Axes:
        """Boxplot diag with distribution of revenue.
        Displays chart automatically (no need for plt.show() in notebook)
        Calls on src.viz function in the background."""
        return viz.plot_aov(self.df)

    def plot_top_3categories(self) -> plt.Axes:
        """Plots bar diag for revenue of top 3 categories.
        Displays chart automatically (no need for plt.show() in notebook)
        Calls on src.viz function in the background."""
        return viz.plot_top_3categories(self.df)

    def plot_swarm(self) -> plt.Axes:
        sns.set_style('darkgrid')
        ax = sns.swarmplot(x='category', y='price', data=self.df, size=1.5, hue='category', palette='colorblind')
        plt.title('Prisfördelning per kategori', fontsize=14, fontweight='bold', pad=15)
        plt.xlabel('Kategori', fontsize=11, labelpad=10)
        plt.ylabel('Pris per enhet (kr)', fontsize=11, labelpad=10)
        plt.xticks(rotation=60)
        plt.show()
        return ax

    def get_outliers(self, k=3.0):
        q1, q3 = self.df['revenue'].quantile([0.25, 0.75])
        iqr = q3 - q1
        return self.df[(self.df['revenue'] < (q1 - k * iqr)) | (self.df['revenue'] > (q3 + k * iqr))].sort_values(by='revenue', ascending=False).head(5)

if __name__ == "__main__":
    ea = EcommerceAnalyzer()
    print(f"testing compute_revenue\nTotal revenue:\n {ea.compute_revenue()}")
    print(f"testing compute_units\nTotal units sold:\n {ea.compute_units()}")
    print(f"testing compute_aov\nAverage order value:\n {ea.compute_aov()}")
    print(f"testing revenue_by_category\nRevenue by category:\n {ea.revenue_by_category()}")
    print(f"testing revenue_by_city\nRevenue by city:\n {ea.revenue_by_city()}")
    print(f"testing top_categories\nTop3 categories:\n {ea.top_categories()}")
    print(f"testing top_categories with argument\nTop5 categories:\n {ea.top_categories(5)}")
