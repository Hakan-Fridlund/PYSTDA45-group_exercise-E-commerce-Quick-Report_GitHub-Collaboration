"""
Class EcommerceAnalyzer for analyzing data.
mostly a wrapper class, imports the functions for loading and cleaning data, 
calculating metrics and visualizing diagrams on dataframe.
"""
from pathlib import Path
import sys
SRC_DIR = Path(__file__).resolve().parent
ROOT_DIR = SRC_DIR.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
import pandas as pd
import numpy as np
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
    Also creates an instance of Ecommerce_viz for plot functions.
    """
    def __init__(self, path = DATAPATH):
        self.df = io.load_data(path)
        self.viz_engine = viz.Ecommerce_viz(self.df)


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
        Calls on src.viz class enginge in the background."""
        return self.viz_engine.plot_revenue_by_category()

    def plot_revenue_by_city(self) -> plt.Axes:
        """Plots line diag with revenue by city. 
        Displays chart automatically (no need for plt.show() in notebook)
        Calls on src.viz class enginge in the background."""
        return self.viz_engine.plot_revenue_by_city()

    def plot_revenue_over_time(self) -> None:
        """Plots line diag with revenue over time, with regression line.
        Displays chart automatically (no need for plt.show() in notebook)
        Calls on src.viz class enginge in the background."""
        return self.viz_engine.plot_revenue_over_time()

    def plot_total_revenue_and_units(self) -> np.ndarray:
        """Plots bar diag with total revenue and units, returns an array with 2plt.Axes
        Displays chart automatically (no need for plt.show() in notebook),
        Calls on src.viz class enginge in the background."""
        return self.viz_engine.plot_total_revenue_and_unit()

    def plot_aov(self) -> plt.Axes:
        """Boxplot diag with distribution of revenue.
        Displays chart automatically (no need for plt.show() in notebook)
        Calls on src.viz class enginge in the background."""
        return self.viz_engine.plot_aov()

    def plot_top_3categories(self) -> None:
        """Plots piechart for revenue of top 3 categories.
        OBS! the function name in viz.py is misspelled catotegories.
        Displays chart automatically (no need for plt.show() in notebook)
        Calls on src.viz class enginge in the background."""
        return self.viz_engine.plot_top_3catotegories()

    def plot_swarm(self) -> plt.Axes:
        """Plots swarm diag for distribution of price per category"""
        sns.set_style('darkgrid')
        ax = sns.swarmplot(x='category',
                           y='price',
                           data=self.df,
                           size=1.5,
                           hue='category',
                           palette='colorblind')

        plt.title('Price Distribution by Category', fontsize=14, fontweight='bold', pad=15)
        plt.xlabel('Category', fontsize=11, labelpad=10)
        plt.ylabel('Price per Unit', fontsize=11, labelpad=10)
        plt.xticks(rotation=60)
        plt.show()
        return ax

    def get_outliers(self, k:float=1.5 , n:int=5) -> pd.DataFrame:
        """ The n top outliers, k value is default to 1.5 standard IQR factor,
        can be raised to find extreme outliers"""
        q1, q3 = self.df['revenue'].quantile([0.25, 0.75])
        iqr = q3 - q1
        return (self.df[(self.df['revenue'] < (q1 - k * iqr)) |
                         (self.df['revenue'] > (q3 + k * iqr))]
                .sort_values(by='revenue', ascending=False)
                .head(n).set_index('order_id'))


if __name__ == "__main__":
    ea = EcommerceAnalyzer()
    print(f"testing compute_revenue\nTotal revenue:\n {ea.compute_revenue()}")
    print(f"testing compute_units\nTotal units sold:\n {ea.compute_units()}")
    print(f"testing compute_aov\nAverage order value:\n {ea.compute_aov()}")
    print(f"testing revenue_by_category\nRevenue by category:\n {ea.revenue_by_category()}")
    print(f"testing revenue_by_city\nRevenue by city:\n {ea.revenue_by_city()}")
    print(f"testing top_categories\nTop3 categories:\n {ea.top_categories()}")
    print(f"testing top_categories with argument\nTop5 categories:\n {ea.top_categories(5)}")
