import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_visualization():
    # 1. Set Seaborn Best Practices / Professional Styling
    sns.set_theme(style="white")
    sns.set_context("talk")  # Scales elements for better readability

    # 2. Generate Realistic Synthetic Data
    # Scenario: Customer Engagement Score by Day of Week vs Time of Day
    np.random.seed(42)  # For reproducibility
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    time_slots = ['09:00', '11:00', '13:00', '15:00', '17:00', '19:00']
    
    # Generate data with a pattern (higher engagement on weekends and evenings)
    data = []
    for day in days:
        day_vals = []
        for i, time in enumerate(time_slots):
            # Base random value
            val = np.random.randint(20, 50)
            
            # Add realistic trends
            if day in ['Sat', 'Sun']: 
                val += 25  # Weekend spike
            if i >= 4: # Evening spike (17:00+)
                val += 15
                
            day_vals.append(val)
        data.append(day_vals)

    # Create DataFrame
    df = pd.DataFrame(data, index=days, columns=time_slots)

    # 3. Setup Figure Size (8 inches * 64 dpi = 512 pixels)
    plt.figure(figsize=(8, 8))

    # 4. Create Heatmap
    # Using 'YlGnBu' (Yellow-Green-Blue) for a professional business look
    heatmap = sns.heatmap(
        df, 
        annot=True,         # Show data values
        fmt="d",            # Integer format
        cmap="YlGnBu",      # Professional color palette
        linewidths=.5,      # Grid lines for separation
        cbar_kws={'label': 'Engagement Score'}
    )

    # 5. Add Titles and Labels
    plt.title('Customer Engagement Heatmap\n(Weekly Activity Analysis)', 
              pad=20, fontsize=16, fontweight='bold')
    plt.xlabel('Time of Day', labelpad=10)
    plt.ylabel('Day of Week', labelpad=10)

    # 6. Save Chart (Exactly as requested in instructions)
    # Note: bbox_inches='tight' removes whitespace, making it presentation-ready
    plt.savefig('chart.png', dpi=64, bbox_inches='tight')
    print("Chart saved successfully as chart.png")

if __name__ == "__main__":
    create_visualization()
