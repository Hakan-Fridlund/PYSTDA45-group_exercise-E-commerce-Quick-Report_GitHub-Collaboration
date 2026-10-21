"""
ecommerce
Class EcommerceAnalyzer
will take filepath  and runs the load_data on init, all functions should be imported from files
"""
import src.io_utils as io
import src.metrics
import src.viz

# TODO write the class docstring
class EcommerceAnalyzer:
    """
    Docstring for class
    """
    def __init__(self, path: str = "../data/ecommerce_sales.csv"):
        # TODO here we have the load_data (placeholder), dataframe will load on init
        self.df = io.load_data(path)

    def get_aov(self):
        # TODO also placeholders for function examples
        return metrics.compute_aov(self.df)

    def get_revenue(self):
        ...





if __name__ == "__main__":
    ea = EcommerceAnalyzer()
    print(ea.get_revenue())
