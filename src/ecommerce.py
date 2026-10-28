"""
ecommerce
Class EcommerceAnalyzer
takes filepath as arg and runs load_data on init, default filepath is "../data/ecommerce_sales.csv" 
wrapper class, import the functions for calculating metrics and visualizing diagrams from dataframe
"""
import sys
import os
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import src.io_utils as io
import src.metrics as metrics
# TODO implement src.viz
# import src.viz


DATAPATH = "../data/ecommerce_sales.csv"

class EcommerceAnalyzer:
    """
    Takes filepath as argument and runs the load_data on init
    default filepath is "../data/ecommerce_sales.csv" 
    """
    def __init__(self, path: str = DATAPATH):
        self.df = io.load_data(path)


    def compute_revenue(self) -> float:
        """Total revenue.
        Calls on src.metrics.compute_revenue in the background."""
        return metrics.compute_revenue(self.df)

    def compute_units(self) -> int:
        """Total number of units sold.
        Calls on src.metrics.compute_units in the background."""
        return metrics.compute_units(self.df)

    def compute_aov(self) -> float:
        """Average Order Value = total revenue / number of unique orders.
        Calls on src.metrics function in the background."""
        return metrics.compute_aov(self.df)

    def revenue_by_category(self) -> pd.DataFrame:
        """Revenue per category.
        Calls on src.metrics function in the background."""
        return metrics.revenue_by_category(self.df)

    def revenue_by_city(self) -> pd.DataFrame:
        """Revenue per city.
        Calls on src.metrics function in the background."""
        return metrics.revenue_by_city(self.df)

    def top_categories(self, n:int = 3) -> pd.DataFrame:
        """The n categories with the highest revenue (default: top 3)
        Calls on src.metrics function in the background."""
        return metrics.top_categories(self.df, n = n)

if __name__ == "__main__":
    ea = EcommerceAnalyzer()
    print(ea)
    print(f"testing compute_revenue\nTotal revenue: {ea.compute_revenue()}")
    print(f"testing compute_units\nTotal units sold: {ea.compute_units()}")
    print(f"testing compute_aov\nAverage order value: {ea.compute_aov()}")
    print(f"testing revenue_by_category\nRevenue by category: {ea.revenue_by_category()}")
    print(f"testing revenue_by_city\nRevenue by city: {ea.revenue_by_city()}")
    print(f"testing top_categories\nTop3 categories: {ea.top_categories()}")
    print(f"testing top_categories with argument\nTop5 categories: {ea.top_categories(5)}")
