"""
ecommerce
Class EcommerceAnalyzer
will take filepath  and runs the load_data on init, all functions should be imported from files
"""
# .(dot) lets you import from the same folder without installing packages
from . import io_utils as io
from . import metrics
from . import viz


class EcommerceAnalyzer:
    """
    Todo: Docstring for class
    """
    def __init__(self, path: str = "../data/ecommerce_sales.csv"):
        # TODO here we have the load_data (placeholder)
        self.df = io.load_data(path)

    def get_aov(self):
        # TODO also placeholder for function example
        return metrics.compute_aov(self.df)
