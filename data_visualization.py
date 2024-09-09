import matplotlib.pyplot as plt

def plot_scores(df):
    """Plotar a pontuação dos dados."""
    plt.figure(figsize=(10, 6))
    plt.bar(df['name'], df['score'], color='skyblue')
    plt.xlabel('Name')
    plt.ylabel('Score')
    plt.title('Scores of Participants')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('data/scores_plot.png')
    plt.show()


