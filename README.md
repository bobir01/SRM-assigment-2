# Wildlife Population Environmental Impact Analysis

This project analyzes the environmental impacts on wildlife populations across different habitats using survival analysis and environmental risk assessment techniques.

## Overview

The analysis focuses on understanding how various environmental factors affect wildlife survival rates across different habitat types. It processes two main datasets:

1. `factor_data.csv`: Environmental variables
   - Air Quality
   - Temperature
   - Deforestation Rate
   - Species Diversity
   - Reproductive Rates

2. `survival_data.csv`: Population survival data
   - Survival Time (days)
   - Censoring Status
   - Habitat Types

## Key Features

- Survival analysis across different habitats
- Environmental risk assessment
- Correlation analysis of environmental factors
- Statistical summaries and visualizations

## Installation

1. Create a virtual environment:
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate  # On Unix/macOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the analysis script:
```bash
python wildlife_analysis.py
```

This will generate:
- Analysis results in the terminal
- Visualization plots in the `plots/` directory

## Analysis Results and Visualizations

### 1. Survival Patterns Across Habitats
![Survival Patterns](plots/survival_patterns.png)

This Kaplan-Meier survival analysis reveals:
- Grassland habitats show the highest survival probability over time
- Wetland areas demonstrate consistently lower survival rates
- Forest and Savanna habitats maintain intermediate survival patterns
- Confidence intervals (shaded areas) indicate the reliability of survival estimates
- Significant divergence in survival patterns becomes apparent after approximately 50 days

### 2. Environmental Risk Distribution
![Risk Distribution](plots/risk_distribution.png)

The environmental risk score distribution shows:
- Normal distribution centered near zero (mean = 0.087)
- Standard deviation of 1.81 indicates moderate variability
- Most populations experience risk scores between -2 and +2
- Extreme risk scores (>|3|) are relatively rare
- Slight positive skew suggests a tendency toward higher risk conditions

### 3. Environmental Factor Correlations
![Correlation Matrix](plots/correlation_matrix.png)

Key correlations between environmental factors:
- Strong positive correlation between Species Diversity and Reproductive Rates
- Negative correlation between Deforestation Rate and Air Quality
- Temperature shows moderate correlations with multiple factors
- Air Quality positively correlates with Species Diversity
- Complex interactions suggest interconnected ecosystem dynamics

### 4. Survival Time Distribution by Habitat
![Survival Distribution](plots/survival_distribution.png)

The box plot analysis reveals:
- Median survival times vary significantly across habitats
- Grassland habitats show the highest median survival time (~111 days)
- Wetland areas have the lowest median survival time (~80 days)
- Mountain habitats show the highest variability in survival times
- Outliers present in all habitats suggest individual resilience

## Conservation Implications

Based on the analysis results:

1. **Priority Areas**:
   - Wetland habitats require immediate conservation attention
   - Mountain regions need stabilization measures to reduce survival variability

2. **Success Models**:
   - Grassland conservation practices should be studied and replicated
   - Forest management strategies show moderate success

3. **Risk Management**:
   - Environmental risk scores can predict population vulnerabilities
   - Temperature extremes affect 4.8% of observations
   - Air quality improvements could benefit multiple environmental factors

4. **Monitoring Recommendations**:
   - Regular tracking of species diversity as a key indicator
   - Focus on reproductive rates in high-risk areas
   - Continuous assessment of habitat-specific survival patterns

## Dependencies

- pandas>=1.5.0
- matplotlib>=3.5.0
- seaborn>=0.12.0
- lifelines>=0.27.0

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
