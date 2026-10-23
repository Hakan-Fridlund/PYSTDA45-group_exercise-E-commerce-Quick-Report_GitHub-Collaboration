
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
* **Filename:** ecommerce_sales.csv
* **Columns:** order_id, date, city, category, price, units, revenue

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
* Write at least **2 custom Python functions** for calculations (e.g., compute_revenue() or top_categories()).
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
   git clone https://github.com/Hakan-Fridlund/PYSTDA45-group_exercise-E-commerce-Quick-Report_GitHub-Collaboration.git
   ```
2. Install dependencies (e.g., pandas, matplotlib, jupyter et.c.):
   ```bash
   pip install -r requirements.txt
   ```
3. Open and run the notebook inside the `notebooks/` directory.

---

## Team Roles & Responsibilities
* **[Håkan Fridlund]**: Project architecture, documentation, and workflow management - as well as developing the EcommerceAnalyzer class to integrate data functions
* **[Sabine Magnusson]**: Responsible for implementing and cleaning the data pipeline in src/io_utils.py, which involved handling missing data, correcting types, and verifying revenue logic to provide a structured dataset
* **[Bijayalaxmi Dash]**: Responsible for developing business metrics in src/metrics.py, creating functions to analyze KPI´s like revenue, total units, Average Order Value (AOV) and regional/category sales
* **[Marwa Elsentawy]**: Responsible for creating data visualization functions in src/viz.py, generating labeled bar and line charts to track revenue by category and sales trends over time
* **[Zahra Ebrahimi]**: Responsible for compiling the final report in notebooks/report.ipynb, executing the analysis pipeline to display metrics and charts alongside narrative insights, outliers, and strategic recommendations
* **[Emelie Karlström]**: Quality Assurance & Integration Lead, responsible for code reviews, pull request approvals, and manual integration testing to ensure error-free execution and full compliance with all project requirements

---

## Tools & Technologies

During this project, the team utilized the following development tools and libraries:
* **Python 3.14.7** – The primary programming language used for all logic and analysis.
* **Pandas** – For data ingestion, comprehensive data cleaning, and statistical calculations.
* **Matplotlib** – For generating and styling the analytics visualizations (bar and line charts).
* **Jupyter Notebook** – As the interactive environment to compile and present the final executive report.
* **Git & GitHub** – For version control, issue tracking, and a Kanban-based project management workflow.

## Insights & Key Takeaways

Through this collaborative exercise, the team gained valuable insights into both technical pipelines and cooperative development workflows:
* **The Power of Modular Programming** – Splitting tasks into dedicated modules allowed us to work in parallel without blocking each other. Integrating everything into a central class proved the value of clean, reusable code architecture.
* **Hands-on EDA & Analytical Experience** – Conducting Exploratory Data Analysis (EDA) allowed us to bridge the gap between raw data and business value. We gained practical experience in uncovering seasonal trends, identifying outliers, and transforming analytical findings into concrete management recommendations.
* **Git Workflow Mastery** – Using an active Kanban board, naming feature branches properly, and enforcing a thorough Pull Request review process gave us practical experience in avoiding merge conflicts and maintaining main branch stability.
* **Data Integrity Matters** – We realized how crucial the initial data cleaning phase is; validating types and testing internal logic (like revenue consistency) early prevented errors from cascading into our metrics and visualizations.


