# Task 3 – Dashboard Development

**CODTECH IT Solutions | Data Analytics Internship**

---

## Internship Details
| Field | Details |
|-------|---------|
| **Name** | Ankit Kumar Pradhan |
| **Intern ID** | CITS442 |
| **Company** | Codtech IT Solutions Private Limited |
| **Domain** | Data Analytics |
| **Mentor** | Neela Santhosh Kumar |
| **Duration** | 4 Weeks |
| **Task** | Dashboard Development |

---

## 📌 Objective

Create an interactive dashboard to visualize a sales dataset and derive actionable business insights.

---

## 🛠️ Tool Used

**Plotly Dash** — an open-source Python framework for building analytical web applications without requiring JavaScript.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `app.py` | Main Dash application — all charts and callbacks |
| `sales_data.csv` | Sample retail sales dataset (60 records, 2024) |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 📊 Dataset Description

The dataset (`sales_data.csv`) contains **60 retail sales transactions** from January–December 2024.

| Column | Description |
|--------|-------------|
| Order ID | Unique order identifier |
| Date | Order date (YYYY-MM-DD) |
| Category | Product category (Technology, Furniture, Office Supplies) |
| Sub-Category | Product sub-category |
| Product | Product name |
| Region | Sales region (North, South, East, West) |
| State | US state |
| Sales | Revenue in USD |
| Quantity | Units sold |
| Discount | Discount applied (0.0 – 0.15) |
| Profit | Profit in USD |

---

## 📈 Dashboard Features

The dashboard contains the following interactive visualisations:

1. **KPI Cards** — Total Sales, Total Orders, Total Profit, Average Order Value  
2. **Monthly Sales & Profit Trend** — Bar + Line combo chart  
3. **Sales by Category** — Donut / Pie chart  
4. **Sales & Profit by Region** — Grouped bar chart  
5. **Sales vs Profit Scatter** — Bubble chart (bubble size = Quantity)  
6. **Sales by Sub-Category** — Horizontal bar chart  

### 🎛️ Filters
- **Category** filter (Technology / Furniture / Office Supplies / All)  
- **Region** filter (North / South / East / West / All)  

All charts update dynamically when filters change.

---

## 🚀 How to Run

### 1. Clone / Download the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:8050/
```

---

## 💡 Key Insights from the Dashboard

- **Technology** is the highest-revenue category, driven by Phones and Laptops.  
- **West region** (California) leads in overall sales volume.  
- **Q4 (Oct–Dec)** shows a seasonal sales spike across all categories.  
- Products with **0% discount** consistently deliver higher profit margins.  
- **Office Supplies** have the highest order frequency but the lowest average order value.

---

## 🧰 Technologies

- Python 3.10+
- [Plotly Dash](https://dash.plotly.com/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)


