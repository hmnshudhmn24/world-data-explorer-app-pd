# 🌍 World Data Explorer App

This interactive **Streamlit** app lets you explore country-level data like GDP, life expectancy, and more. You can upload your own dataset and overlay it on top of the default world dataset.

## 🔍 Features

- World Bank-style stats: GDP, Life Expectancy, Internet Users
- Filter by country and indicator
- Upload your own country-level data
- Overlay and merge with default stats
- Interactive bar charts using Plotly

## 📁 Data Format

### Default Dataset

```csv
country,GDP,LifeExpectancy,InternetUsers
United States,21000000,78.5,89.7
China,14700000,76.9,70.4
...
```

### User Upload (must include `country` column)

```csv
country,CustomMetric
India,123
Germany,456
...
```

## 🚀 How to Run

1. Install requirements:

```bash
pip install pandas streamlit plotly
```

2. Run the app:

```bash
streamlit run app/main.py
```

3. Filter data and visualize insights!

## 📁 Project Structure

- `app/main.py` – Streamlit dashboard script
- `data/world_data.csv` – Default dataset
- `README.md` – Project documentation
