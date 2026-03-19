# Week-04-Day-22-AM

**Dataset used:** Titanic (891 rows) — loaded directly via URL
(`https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`)

To use your own CSV replace the `url` line with:
```python
df = pd.read_csv('your_file.csv')
```

---

# Part A — Concept Application (40%)

### 1. Data Selection using Pandas
*   Use `loc` to select specific rows and columns (3 examples)
*   Use `iloc` for index-based selection (3 examples) <br>
[Solution](loc_iloc_selection.py)

### 2. Filtering Data
*   Filter rows based on multiple conditions
*   Extract high-value and category-specific subsets <br>
[Solution](filtering_data.py)

### 3. Descriptive Statistics
*   Use `describe()` to summarize the dataset
*   Manually interpret mean, std, min, max for Age and Fare <br>
[Solution](descriptive_statistics.py)

### 4. Histogram
*   Plot histogram for Age and Fare columns
*   Interpret distribution shape (skewness/spread) <br>
[Solution](histogram.py)

### 5. Bar Plot
*   Survival rate by Passenger Class
*   Average Fare by Passenger Class <br>
[Solution](bar_plot.py)

### 6. Line Chart
*   Rolling mean of Fare and Age across passenger index
*   Interpret trends and volatility <br>
[Solution](line_chart.py)

### 7. KDE Plot
*   KDE vs Histogram for Age
*   KDE comparison: Survived vs Not Survived <br>
[Solution](kde_plot.py)

---

## Part B — Stretch Problem (30%)

### 1. Grouped Analysis
*   Group by `Pclass` → compute mean Age, Fare, Survival Rate
*   Group by `Sex` → compute mean values <br>
[Solution](grouped_analysis.py)

### 2. Visualize grouped results using bar plot
*   Mean Age, Mean Fare, and Survival Rate side-by-side bar charts <br>
[Solution](grouped_analysis.py)

### 3. Compare two numerical features
*   Age distribution per class — KDE overlay
*   Mean Fare by Age group — Line chart <br>
[Solution](grouped_analysis.py)

### 4. Insights from Visualizations

*   **Class vs Age:** 1st class passengers were older on average (~38 years) compared to 3rd class (~25 years), suggesting wealthier, more established travellers booked higher classes.
*   **Class vs Fare:** 1st class avg fare (£84) was ~6× higher than 3rd class (£14), reflecting the sharp economic divide among passengers.
*   **Class vs Survival:** Survival rate drops steeply with class — 63% (1st) → 47% (2nd) → 24% (3rd). Proximity to lifeboats and evacuation priority likely drove this gap.
*   **Age KDE by class:** 3rd class KDE peaks earlier (~20–25), showing it was dominated by young migrants. 1st class KDE is broader and shifted right (~35–50).
*   **Fare by Age bin:** Passengers aged 40–60 paid the highest average fares, consistent with mid-to-late career wealth.

---

## Part C — Interview Ready (20%)

**Q1 — What is the difference between `loc` and `iloc` in Pandas?**

`loc` selects data using **labels** — row index names and column names. It is inclusive on both ends when slicing.

`iloc` selects data using **integer positions** — zero-based row/column positions. It is exclusive on the right end, like standard Python slicing.

| | `loc` | `iloc` |
| :--- | :--- | :--- |
| **Selection by** | Label / name | Integer position |
| **Row slice end** | Inclusive | Exclusive |
| **Example** | `df.loc[0:4, 'Age']` | `df.iloc[0:4, 3]` |
| **Supports conditions** | ✅ Yes | ❌ No |

```python
df.loc[df['Survived'] == 1, ['Name', 'Age']]  # condition + column names
df.iloc[0:5, 2:5]                              # rows 0–4, columns 2–4
```

**Q2 (Coding) — Filter rows where a column value is greater than average** <br>
[Solution](filter_above_average.py)

**Q3 — What is the purpose of `describe()`? What insights can we get from it?**

`describe()` generates summary statistics for all numerical columns in a DataFrame. It provides:

*   **count** — number of non-null values (reveals missing data)
*   **mean** — central tendency of the data
*   **std** — spread/variability; high std means data is widely spread
*   **min / max** — range boundaries; useful for spotting outliers
*   **25% / 50% / 75%** — quartiles; comparing 50% (median) to mean reveals skewness

### Key Insights from `describe()`:
*   If `mean >> median (50%)` → right-skewed distribution (e.g., Fare column)
*   If `std` is very large relative to `mean` → high variability or outliers present
*   If `min` is negative or `max` is unexpectedly large → check for data quality issues
*   `count < total rows` → missing values exist in that column

---

## Part D — AI-Augmented Task (10%)

### 1. Prompt AI:
*"Explain how to perform data analysis using Pandas and visualization using Matplotlib with examples."*

### 2. Document prompt and output

[AI Output](AI_output.md) for the above prompt

### 3. Evaluate

### Are Plots Correct?

*   **Histogram code:** Correct — uses `plt.hist()` with `bins`, `color`, and `edgecolor`. Appropriate for showing frequency distribution.
*   **Bar plot code:** Correct — uses `groupby().mean()` to aggregate then `.plot(kind='bar')`. Properly labels axes.
*   **Line chart code:** Correct — rolling mean smooths the noisy signal effectively.
*   **KDE code:** Correct — uses `gaussian_kde` from scipy, plots smooth density curve. Properly notes it avoids bin-width dependency.

### Is the Explanation Meaningful?

*   The `loc` vs `iloc` explanation correctly identifies label-based vs position-based selection — a commonly confused distinction.
*   The filter syntax using `&` with parentheses is correct and follows Pandas best practice.
*   The `describe()` explanation correctly lists all 8 output statistics and their interpretation.
*   The table comparing plot types (Histogram / Bar / Line / KDE) is a useful and accurate summary.

> **One improvement made:**
> The AI used `.plot(kind='bar')` (pandas shorthand) for bar plots. In our solutions we use `plt.bar()` directly for more explicit control over colors and annotations — matching the cleaner style of this repo.

### Runnability

All AI code snippets run without modification given `pandas`, `matplotlib`, and `scipy` are installed. The AI correctly used `df['Age'].dropna()` before plotting — an important detail to avoid NaN errors in histogram and KDE functions.
