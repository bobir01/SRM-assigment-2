import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter
import os

# 1. Load and Process Data
def load_data():
    try:
        factor_df = pd.read_csv('factor_data.csv')
        survival_df = pd.read_csv('survival_data.csv')
        return factor_df, survival_df
    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
        return None, None

# 2. Survival Analysis
def analyze_survival(survival_df):
    # Calculate mean survival by habitat
    survival_stats = survival_df.groupby('Habitat').agg({
        'Survival_Time': 'mean',
        'Censoring_Status': 'mean'
    }).round(2)
    
    return survival_stats

# 3. Environmental Risk Assessment
def assess_environmental_risk(factor_df):
    # Calculate risk score
    factor_df['risk_score'] = (-factor_df['AirQuality'] 
                              + factor_df['DeforestationRate']
                              - factor_df['SpeciesDiversity']
                              - factor_df['ReproductiveRates'])
    
    return factor_df['risk_score'].describe()

# 4. Calculate Key Metrics
def calculate_metrics(factor_df, survival_df):
    metrics = {
        'mean_survival_by_habitat': survival_df.groupby('Habitat')['Survival_Time'].mean(),
        'censoring_rates': survival_df['Censoring_Status'].mean(),
        'risk_score_summary': factor_df['risk_score'].describe(),
        'temperature_extremes': len(factor_df[factor_df['Temperature'].abs() > factor_df['Temperature'].std() * 2]) / len(factor_df)
    }
    return metrics

def create_visualizations(factor_df, survival_df):
    # Set the style for all plots
    plt.style.use('seaborn-v0_8')
    
    # 1. Survival Analysis Plot
    plt.figure(figsize=(12, 6))
    kmf = KaplanMeierFitter()
    
    colors = ['#2ecc71', '#e74c3c', '#3498db', '#f1c40f', '#9b59b6']
    for habitat, color in zip(survival_df['Habitat'].unique(), colors):
        mask = survival_df['Habitat'] == habitat
        kmf.fit(
            survival_df[mask]['Survival_Time'],
            survival_df[mask]['Censoring_Status'],
            label=habitat
        )
        kmf.plot(ci_show=True, color=color)
    
    plt.title('Survival Patterns Across Different Habitats', fontsize=14, pad=20)
    plt.xlabel('Time (days)', fontsize=12)
    plt.ylabel('Survival Probability', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(title='Habitat Type', title_fontsize=12)
    plt.tight_layout()
    plt.savefig('plots/survival_patterns.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Environmental Risk Distribution
    plt.figure(figsize=(12, 6))
    sns.histplot(data=factor_df, x='risk_score', bins=30, kde=True)
    plt.title('Distribution of Environmental Risk Scores', fontsize=14, pad=20)
    plt.xlabel('Risk Score', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('plots/risk_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Environmental Factors Correlation
    plt.figure(figsize=(10, 8))
    correlation_matrix = factor_df[['AirQuality', 'Temperature', 'DeforestationRate', 
                                  'SpeciesDiversity', 'ReproductiveRates']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.2f', cbar_kws={'label': 'Correlation Coefficient'})
    plt.title('Correlation Between Environmental Factors', fontsize=14, pad=20)
    plt.tight_layout()
    plt.savefig('plots/correlation_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Survival Time Distribution by Habitat
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=survival_df, x='Habitat', y='Survival_Time', hue='Habitat', 
                palette=colors, legend=False)
    plt.title('Distribution of Survival Times Across Habitats', fontsize=14, pad=20)
    plt.xlabel('Habitat Type', fontsize=12)
    plt.ylabel('Survival Time (days)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plots/survival_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Create plots directory if it doesn't exist
    if not os.path.exists('plots'):
        os.makedirs('plots')
        
    # Load data
    factor_df, survival_df = load_data()
    if factor_df is None or survival_df is None:
        return
    
    # Perform analyses
    survival_stats = analyze_survival(survival_df)
    risk_stats = assess_environmental_risk(factor_df)
    metrics = calculate_metrics(factor_df, survival_df)
    
    # Create visualizations
    create_visualizations(factor_df, survival_df)
    
    # Print summary
    print("\n=== Wildlife Population Analysis Results ===")
    print("\nSurvival Statistics by Habitat:")
    print(survival_stats)
    print("\nEnvironmental Risk Summary:")
    print(risk_stats)
    print("\nKey Metrics:")
    for key, value in metrics.items():
        print(f"\n{key}:")
        print(value)

if __name__ == "__main__":
    main()
