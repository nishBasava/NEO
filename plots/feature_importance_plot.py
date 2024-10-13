import matplotlib.pyplot as plt

def plot_feature_importance(feature_importance, feature_names):
    plt.figure(figsize=(6, 6))
    plt.bar(range(len(feature_importance)), feature_importance, color='indigo')
    plt.xticks(range(len(feature_names)), feature_names, rotation=90)
    plt.xlabel('Input Feature')
    plt.ylabel('Feature Importance')
    plt.title('Feature Importance based on First Layer Weights')
    plt.show()

