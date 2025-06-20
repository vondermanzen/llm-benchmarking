#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd


def create_feature_plot():
    """Create a plot based on feature scores from features.txt."""
    try:
        # Read the features.txt file
        df = pd.read_csv('features.txt', sep='\t')
        
        # Define feature weights (positive = good, negative = bad)
        feature_weights = {
            'Open Source': 8,
            'Self-hostable': 7,
            'LLM Agnostic': 6,
            'Tab Completion': 5,
            'Chat': 4,
            'Modify Files': 4,
            'Run Commands': 3,
            'Select Context': 3,
            'Multi-IDE': 2,
            'Data Retained': -5,
            'Data Re-used': -8
        }
        
        # Calculate scores for each tool
        tool_scores = {}
        
        for _, row in df.iterrows():
            tool_name = row['Tool']
            score = 0
            
            for feature, weight in feature_weights.items():
                if feature in row and row[feature] == 'Yes':
                    score += weight
            # Minimum score is zero
            score = max(score, 0)
            tool_scores[tool_name] = score
        
        # Sort by score (descending)
        sorted_scores = dict(sorted(tool_scores.items(), key=lambda x: x[1], reverse=True))
        
        # Create the plot
        plt.figure(figsize=(14, 10))
        tools = list(sorted_scores.keys())
        scores = list(sorted_scores.values())
        
        # All bars the same color
        color = '#2E8B57'
        bars = plt.bar(tools, scores, color=color, alpha=0.8)
        
        # Customize the plot
        plt.title('Coding Assistants Feature-Based Scoring', fontsize=16, fontweight='bold')
        plt.xlabel('Coding Assistant', fontsize=12, fontweight='bold')
        plt.ylabel('Feature Score', fontsize=12, fontweight='bold')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels on top of bars
        for bar, score in zip(bars, scores):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    f"{score}", ha='center', va='bottom', 
                    fontweight='bold', fontsize=10)
        
        # Adjust layout and save
        plt.tight_layout()
        plt.savefig('feature_scores.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Feature-based plot saved as 'feature_scores.png'")
        
        # Print the scores
        print("\nFeature-based scores:")
        for tool, score in sorted_scores.items():
            print(f"{tool}: {score}")
            
        # Print feature weights for reference
        print("\nFeature weights used:")
        for feature, weight in feature_weights.items():
            print(f"{feature}: {weight:+d}")
            
    except Exception as e:
        print(f"Error creating feature plot: {e}")

def main():
    print("Generating feature-based scoring plot...")
    print("="*60)
    create_feature_plot()

if __name__ == "__main__":
    main() 