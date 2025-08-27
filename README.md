# Retail Sales Dashboard

A **Retail Sales Analysis and Visualization Dashboard** built with **Python**, **Pandas**, **Seaborn**, **Matplotlib**, and **Streamlit**.  
This project performs data cleaning, preprocessing, analysis, and visualizations of retail transaction data to gain insights into sales trends, top cities, customer behavior, and payment methods.

---

## 📂 Project Files

- `Retail_Transactions_2000 (3).csv` → Raw dataset containing 2000 transactions.  
- `Retail_Cleaned.csv` → Preprocessed dataset with scaled numerical columns and dummy variables.  
- `app.py` → Streamlit dashboard application for interactive visualizations.  
- `Project.ipynb` → Jupyter notebook for data cleaning, EDA, and analysis.  

---

## 🛠 Features

- **Data Cleaning & Preprocessing**
  - Handle missing values in `Age` and `City`.
  - Remove duplicate transactions.
  - Standardize numerical columns (`Age`, `Price`, `TotalAmount`).
  - Encode categorical variables (`Gender`, `City`) for analysis.

- **Exploratory Data Analysis**
  - City-wise revenue and top customer cities.
  - Total sales by product category.
  - Monthly sales trend.
  - Payment mode usage analysis.
  - Customer spending by age group.
  - Heatmap of Product Category vs Payment Mode.

- **Interactive Dashboard (Streamlit)**
  - Visualize **top cities by customer count**.
  - Display **total sales by product category**.
  - View **monthly sales trends** interactively.

---

## 📈 Visualizations

1. **City-wise Revenue**: Bar chart of total sales per city.  
2. **Top Cities by Customer Count**: Bar chart showing the number of customers in the top 10 cities.  
3. **Product Category Sales**: Bar chart of total sales for each product category.  
4. **Monthly Sales Trend**: Line chart showing total sales per month.  
5. **Payment Mode Distribution**: Pie chart of payment method usage.  
6. **Age Group Spending**: Bar chart showing average spend by age group.  
7. **Product Category vs Payment Mode**: Heatmap displaying sales amounts per category and payment method.

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone <your-repo-link>
cd "TCS DATA in ML"
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Requirements include: pandas, numpy, matplotlib, seaborn, streamlit.

Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open the URL displayed in the terminal to access the dashboard, or use the live dashboard link:

```
Open Retail Sales Dashboard


## https://eda-in-retail-transaction-data-pj382g9ubwyhrcxpjhu8wm.streamlit.app/](https://eda-in-retail-transaction-data.streamlit.app/

```
💡 Insights
Bengaluru and Pune are the top cities in terms of revenue and customers.

Fashion and Electronics are among the highest-selling product categories.

Most popular payment methods are Card and Wallet.

Customers aged 26-40 contribute the most to sales.

📂 Folder Structure
nginx
Copy code
TCS DATA in ML/
│
├─ Retail_Transactions_2000 (3).csv
├─ Retail_Cleaned.csv
├─ Project.ipynb
├─ app.py
└─ README.md
