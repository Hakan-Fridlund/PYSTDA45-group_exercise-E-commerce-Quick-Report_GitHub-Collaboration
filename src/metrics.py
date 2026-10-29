"""Key metrics and calculation functions for e-commerce data."""

from pathlib import Path

import pandas as pd


def _prepare_df(df: pd.DataFrame) -> pd.DataFrame:
    """Clean column names and text values, and calculate revenue = price * units."""
    data = df.copy()
    data.columns = data.columns.astype(str).str.strip()

    for column in data.select_dtypes(include=["object", "string"]).columns:
        data[column] = data[column].str.strip()

    required = {"order_id", "city", "category", "price", "units"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError("DataFrame is missing columns: " + ", ".join(sorted(missing)))

    # Stop if price or units has an invalid number.
    for column in ["price", "units"]:
        data[column] = pd.to_numeric(data[column], errors="raise")

    # Calculate revenue as price * units.
    data["revenue"] = data["price"] * data["units"]

    return data


def compute_revenue(df: pd.DataFrame) -> float:
    """Total revenue."""
    return float(_prepare_df(df)["revenue"].sum())


def compute_units(df: pd.DataFrame) -> int:
    """Total number of units sold."""
    return int(_prepare_df(df)["units"].sum())


def compute_aov(df: pd.DataFrame) -> float:
    """Average Order Value = total revenue / number of unique orders."""
    data = _prepare_df(df)
    number_of_orders = data["order_id"].nunique()

    if number_of_orders == 0:
        return 0.0

    return float(data["revenue"].sum() / number_of_orders)


def _revenue_by_group(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Revenue, orders, units, AOV and share of total per group, largest first."""
    data = _prepare_df(df)

    result = data.groupby(column, dropna=False).agg(
        revenue=("revenue", "sum"),
        orders=("order_id", "nunique"),
        units=("units", "sum"),
    )
    result["aov"] = result["revenue"] / result["orders"]
    total_revenue = result["revenue"].sum()

    if total_revenue != 0:
        result["share_%"] = result["revenue"] / total_revenue * 100
    else:
        result["share_%"] = 0.0

    return result.sort_values("revenue", ascending=False)


def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Revenue per category."""
    return _revenue_by_group(df, "category")


def revenue_by_city(df: pd.DataFrame) -> pd.DataFrame:
    """Revenue per city."""
    return _revenue_by_group(df, "city")


def top_categories(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """The n categories with the highest revenue (default: top 3)."""
    if n < 0:
        raise ValueError("n must be zero or greater.")

    return revenue_by_category(df).head(n)


if __name__ == "__main__":
    # Path to the CSV file in the data folder.
    project_folder = Path(__file__).resolve().parent.parent
    csv_path = project_folder / "data" / "ecommerce_sales.csv"

    df = pd.read_csv(csv_path)

    print(f"Total revenue: {compute_revenue(df):.2f}")
    print(f"Total units sold: {compute_units(df)}")
    print(f"Average Order Value (AOV): {compute_aov(df):.2f}")

    print("\nRevenue by category:")
    print(revenue_by_category(df))

    print("\nRevenue by city:")
    print(revenue_by_city(df))

    print("\nTop 3 categories by revenue:")
    print(top_categories(df))