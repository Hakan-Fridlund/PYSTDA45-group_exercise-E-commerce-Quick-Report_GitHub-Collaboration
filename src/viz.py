# """
# viz.py = plot-funktioner
# """

"""
 from src.viz import (
     plot_revenue_by_category(df)
     plot_revenue_over_time(df) 
     plot_revenue_by_city(df)
     plot_total_revenue_and_units(df)
     plot_aov(df)
     plot_top_3categories(df)) 
"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

def plot_revenue_by_category(df):
     print("Saknade värden: ")
     print(df[["category", "revenue"]].isnull().sum())

     # Skapa en kopia av data
     data = df.copy()

     # Kontrollera att revenue är numerisk
     data["revenue"] = pd.to_numeric(data["revenue"], errors="coerce")
     
     #Ta bort rader som saknar kategori eller intäkt
     data = data.dropna(subset=["category", "revenue"])
     
     #Sammanfatta intäkten per kategori
     category_revenue =(
          data.groupby("category")["revenue"].sum().sort_values(ascending=False)
          )
     
     #Skappa stapeldiagram
     ax = category_revenue.plot(
          kind="bar",
          figsize=(10,6),
          color=["steelblue", "orange", "seagreen", "coral", "mediumpurple"],
          capsize=10,
          yerr=4
     )
     #Lägga till rubrik och axelrubrik och diagramets layout
     
     ax.text(1, 1.05, "Diagrammet visar total intäkt per kategori.\n""Blir det lätt att jämföra kategorinas intäkter.",
             transform=ax.transAxes,
             ha="center",
             va="bottom",
             fontsize=9)
     ax.set_title("Total intäkt per kategori", fontweight="bold")
     ax.set_ylabel("Total intäkt")
     ax.set_xlabel("Kategori")
     ax.grid(True, axis="y", alpha=0.3)  
     plt.xticks(rotation=45, ha="right")
     plt.tight_layout()

     #visa diagramet
     plt.show()

     return ax 

def plot_revenue_by_city(df):

     # En kopia av data
     data = df.copy()

     #Kontrollera saknade värden
     print("Saknade värdden: ")
     print(df[["city", "revenue"]].isnull().sum())

     #Kontrollera datatype
     data["revenue"] = pd.to_numeric(data["revenue"], errors="coerce")

     #Ta bort saknade rader
     data = data.dropna(subset=["city", "revenue"])

     # Sammanfatta intäkter per stad
     city_revenue=(data.groupby("city")["revenue"]).sum().sort_values(ascending=False)

     #Skapa stapeldiagramm
     ax = city_revenue.plot(
          kind="bar",
          figsize=(10, 5),
          color=["seagreen", "mediumpurple", "coral", "steelblue", "orange"],
          capsize=10,
          yerr=4
     )

     #Lägga till rubriker
     ax.set_title("Total intäkt per stad", fontweight="bold")
     ax.set_xlabel("Stad")
     ax.set_ylabel("Total intäkt")
     ax.grid(True, axis="y")
     plt.xticks(rotation=45, ha="right")
     plt.tight_layout()

     #Visa diagrammet
     plt.show()

     return ax      

def plot_revenue_over_time(df):
    
     # få en kopia av data
     data = df.copy()

     # Kontrollera saknade värden
     print("Saknade värden: ")
     print(df[["date", "revenue"]].isnull().sum())

     #Kontrollera datatyper
     data["date"] = pd.to_datetime(data["date"], errors="coerce")
     data["revenue"] = pd.to_numeric(data["revenue"], errors="coerce")

     #Radera rader som saknar datum eller intäkt
     data = data.dropna(subset=["date", "revenue"])

     #Sortera data efter datum
     data = data.sort_values("date")

     #Använd datum som index
     data = data.set_index("date")

     #Sammanfatta intäkter per månad
     monthly_revenue = data["revenue"].resample("MS").sum()

     #Skappa linjediagrammet
     ax = monthly_revenue.plot(
          kind="line",
          figsize=(10, 5),
          marker="o",
          color="darkorange",
          linestyle=":",
          linewidth=2,
          label="Månadsintäkt"
     )

     # räkna trenlinjen
     x = np.arange(len(monthly_revenue))
     y = monthly_revenue.values

     if len(x) > 1:
          slope, intercept = np.polyfit(x, y, 1)
          trendline = slope * x + intercept

          # lägga till trendlinjen
          ax.plot(
               monthly_revenue.index,
               trendline,
               color="blue",
               linestyle="--", 
               linewidth=2,
               label="Trendlinje"
          )

     #Lägga till rubrik, axelrubriker och diagrammets layout
     ax.text(0.5, 1.16, "Diagrammet visar hur intäkterna förändras varje månad.",
             transform=ax.transAxes, ha="center", fontsize=10)
     ax.set_title("Försäljning över tid", fontweight="bold")
     ax.set_xlabel("Månad")
     ax.set_ylabel("Total intäkt (kr)")
     ax.grid(True, alpha=0.3)  
     ax.legend()    
     plt.xticks(rotation=45, ha="right")
     plt.tight_layout()

     #Visa diagrammet
     plt.show()

     return ax

def plot_total_revenue_and_units(df):
     #Räkna nyckeltal
     total_revenue = pd.to_numeric(df["revenue"], errors="coerce").sum()
     total_units = pd.to_numeric(df["units"], errors="coerce").sum()

     #Skapa en nykeltal figur
     fig, axes = plt.subplots(1, 2, figsize=(12, 6))
     fig.suptitle("Total revenue and units sold", fontsize=16, fontweight="bold", y=0.98)
     fig.text(0.5, 0.91,
              "Diagrammet visat den totala intäkten och den totalt sålda enheter.",
              ha="center", fontsize=10)

     #diagrammet rubriker
     axes[0].text(0.5, 0.5,
                  f"{total_revenue:,.0f} kr",
                  ha="center", va="center",
                  fontsize=20)

     #total intäkt
     axes[0].bar(["Total intäkt"], [total_revenue], color="steelblue", width=0.5)
     axes[0].set_title("Total intäkt")
     axes[0].set_ylabel("Intäkt (kr)")
     axes[0].bar_label(axes[0].containers[0],
                       labels=[f"{total_revenue:,.0f} kr"],
                       padding=5)
     axes[0].grid(True, axis="y", alpha=0.3)
     
     #total enheter
     axes[1].bar(["Sålda enheter"], [total_units], color="seagreen", width=0.5)
     axes[1].set_title("Total antal sålda enheter")
     axes[1].bar_label(axes[1].containers[0],
                       labels=[f"{total_units:,.0f}"],
                       padding=5)
     axes[1].grid(True, axis="y", alpha=0.3)

     fig.subplots_adjust(top=0.78, wspace=0.35)

     #Visa
     plt.tight_layout()
     plt.show()

     return axes

def plot_aov(df):
     
     #kopia av datan
     data = df.copy()

     #kontrollera datatype
     data["revenue"] = pd.to_numeric(data["revenue"], errors="coerce")

     #ta bort rader som saknar värden
     data = data.dropna(subset=("order_id", "revenue"))

     #räkna intäkt per order
     order_revenue = data.groupby("order_id")["revenue"].sum()

     #Beräkna genomsnittligt ordervärde
     aov = order_revenue.mean()
     median_värde = order_revenue.median()

     print(f"AOV: {aov:.2f} kr")
     print(f"Median order value: {median_värde:.2f} kr")

     #boxplot
     fig, ax = plt.subplots(figsize=(10, 7))
     ax.boxplot(order_revenue, vert=False,
                patch_artist=True,
                boxprops=dict(facecolor="lightblue"),
                medianprops=dict(color="darkblue", linewidth=2))

     ax.axvline(aov, color="red", linestyle="--", label=f"AOV = {aov:.2f}")
     ax.axvline(median_värde, color="green", linestyle=":", label=f"Median= {median_värde:.2f}")

     ax.text(0.5, 0.93, "Diagrammet visar hur ordervärderna är fördelade.",
             transform=ax.transAxes, ha="center", fontsize=10)
     
     ax.set_title("Average Order Value(AOV)",fontweight="bold", pad=65)
     ax.set_xlabel("Ordervärde (kr)")
     ax.set_yticks([1])
     ax.set_yticklabels(["Orders"])
     #ax.set_xlim(min(0, order_revenue.min()), order_revenue.max() *1.05)
     ax.legend()
     ax.grid(True, axis="x", alpha=0.3)

     plt.tight_layout()
     fig.subplots_adjust(top=0.80)
     plt.show()

     return ax

def plot_top_3categories(df):

     # kopia av datan
     data = df.copy()

     #kontrollera datatyp
     data["revenue"] = pd.to_numeric(data["revenue"], errors="coerce")

     #ta bort rader som saknar värde
     data = data.dropna(subset=["category", "revenue"])

     #räkna intäkt per kategory och dem 3 högsta
     top_tre = (data.groupby("category")["revenue"].sum().nlargest(3))

     #stapeldiagram
     ax = top_tre.plot(kind = "bar", figsize=(8, 5), color=["purple", "seagreen", "coral"])
     ax.set_title("Top 3 kategorier efter intäkt", fontweight="bold")
     ax.set_xlabel("Kategori")
     ax.set_ylabel("Total intäkt (kr)")
     plt.xticks(rotation=45, ha="right")
     plt.tight_layout()
     plt.show()

     return ax 


if __name__ == "__main__":
     df = pd.read_csv("data/ecommerce_sales.csv")
     plot_revenue_by_category(df)
     plot_revenue_over_time(df) 
     plot_revenue_by_city(df)
     plot_total_revenue_and_units(df)
     plot_aov(df)
     plot_top_3categories(df)
