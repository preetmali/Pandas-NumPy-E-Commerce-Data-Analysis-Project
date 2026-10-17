E-Commerce Data Analysis Using Python, Pandas & NumPy
📌 Project Overview

This project analyzes e-commerce data to generate meaningful business insights using Python, Pandas, and NumPy. It examines product sales, revenue, city-wise sales, monthly performance, payment methods, and loss-making orders.

The goal is to transform raw CSV datasets into useful information that supports data-driven business decisions.

🎯 Objectives
Identify the best-selling products.
Find the categories generating the highest revenue.
Analyze sales across different cities.
Identify monthly sales performance.
Determine the most frequently used payment method.
Identify orders that result in a loss.
Explore the relationship between discounts and product sales.
🛠️ Technologies Used
Python — Programming language
Pandas — Data manipulation and analysis
NumPy — Numerical computations
CSV — Dataset storage
Git & GitHub — Version control and project hosting
📂 Project Structure
ecommerce-data-analysis/
│
├── Data/
│   ├── customers.csv
│   ├── orders.csv
│   └── products.csv
│
├── main/
│   ├── main.py
│   ├── data_cleaning.py
│   └── data_Analysis.py
│
├── reports/
│   ├── final_report.txt
│   └── final_report.csv
│
└── README.md
📊 Dataset Description

The project uses three CSV datasets:

1. Customers Dataset

Contains customer information, including customer IDs and city details.

2. Orders Dataset

Contains order information, including product IDs, quantities, order dates, payment methods, unit prices, and discounts.

3. Products Dataset

Contains product information, including product names, categories, and cost prices.

The exact columns depend on the provided CSV files.

🔍 Business Questions Answered
Which product sells the most?
Which category generates the highest revenue?
Which city generates the highest sales?
Which month generates the highest sales?
Which payment method is used the most?
Which orders result in a loss?
Which products show a positive relationship between discounts and sales quantity?
⚙️ Installation and Setup
Step 1: Install Python

Install Python on your system if it is not already installed.

Step 2: Clone the Repository
git clone https://github.com/YOUR-USERNAME/ecommerce-data-analysis.git

Replace YOUR-USERNAME with your GitHub username.

Step 3: Navigate to the Project Folder
cd ecommerce-data-analysis
Step 4: Install Required Libraries
python -m pip install pandas numpy
Step 5: Run the Project

If main.py is inside the main folder, run:

python main/main.py

Run this command from the project root directory.

📈 Output

After successful execution, the project generates:

final_report.txt — A readable text report containing the analysis results.
final_report.csv — A CSV report that can be opened in Excel or analyzed further.

Both reports are saved in the reports/ directory.

💡 Key Learning Outcomes
Reading and processing CSV files using Pandas.
Cleaning and preparing datasets.
Merging multiple datasets.
Performing group-by operations and aggregations.
Calculating revenue, costs, and profit.
Converting date columns and analyzing monthly sales.
Exploring correlations between numerical variables.
Exporting analysis results into report files.
🚀 Future Improvements
Create an interactive dashboard using Streamlit.
Add interactive visualizations using Plotly.
Improve data validation and missing-value handling.
Add customer segmentation and purchase behavior analysis.
Implement predictive sales analysis using Machine Learning.
Deploy the dashboard online.
👨‍💻 Author

Your Name

GitHub: https://github.com/preetmali
