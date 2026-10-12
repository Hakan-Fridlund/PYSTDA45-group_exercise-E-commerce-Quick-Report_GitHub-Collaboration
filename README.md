
# E-commerce: Quick Report & GitHub Collaboration

## Project Case Overview
You are a team of data analysts working for a fictional e-commerce platform. Management has requested a rapid, data-driven decision support document ahead of the upcoming campaign period. 

The objective is to deliver an executable, reproducible analytics project hosted on GitHub. This project consists of a clean, end-to-end Jupyter Notebook showing key performance indicators (KPIs) and visualizations, accompanied by a brief executive summary.

### Management Objectives
The report must answer the following questions from management:
* **What sells?** – Which product categories drive the most revenue?
* **Where do we sell?** – Which cities generate the highest revenue?
* **When do we sell?** – Are there any visible seasonal or time-based patterns during the observed period?
* **What does a typical order look like?** – Average Order Value (AOV) and distribution.
* **Top Lists** – Top 3 product categories by revenue.
* **Anomalies** – Any unexpected patterns or data points that stand out?

The report must conclude with **2–3 actionable recommendations** (bullet points) based on the findings (e.g., *"Focus marketing efforts on Category X in City Y during Month Z"*).

---

## Dataset (CSV)
* **Filename:** `ecommerce_sales.csv`
* **Columns:** `order_id`, `date`, `city`, `category`, `price`, `units`, `revenue`

---

## Project Requirements (Passing Grade / G)

### 1. Repository & Collaboration
* Set up a shared GitHub repository for the group.
* Collaborate using **branches** and **Pull Requests (PRs)**.
* Deliver an executable analysis in a single Jupyter Notebook that runs flawlessly from top to bottom.

### 2. Key Performance Indicators (KPIs)
The notebook must calculate at least 5 core metrics:
* Total revenue and total units sold.
* Average Order Value (AOV).
* Total revenue per category.
* Total revenue per city.
* Top 3 categories by revenue.

### 3. Visualizations
Include at least **2 visualizations** (e.g., a bar chart for revenue per category and a line chart for sales over time by week/month).
* Each plot must feature clear headers, labeled axes, and 1–2 sentences of Markdown explaining the insights.

### 4. Code Quality
* Write at least **2 custom Python functions** for calculations (e.g., `compute_revenue()` or `top_categories()`).
* Ensure the notebook runs without any errors from start to finish.

---

## Repository Structure
```text
├── data/
│   └── ecommerce_sales.csv
├── notebooks/
│   └── report.ipynb
├── src/                      # Optional: For modular Python scripts
└── README.md
```

---

## How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com
   ```
2. Install dependencies (e.g., pandas, matplotlib, seaborn):
   ```bash
   pip install -r requirements.txt
   ```
3. Open and run the notebook inside the `notebooks/` directory.

---

## Team Roles & Responsibilities
* **[Member 1 Name]**: *e.g., Repository Setup, Data Cleaning, and KPI functions*
* **[Member 2 Name]**: *e.g., Visualizations, Plot Styling, and Markdown explanations*
* **[Member 3 Name]**: *e.g., Code Quality Review, Documentation, and Recommendations*
