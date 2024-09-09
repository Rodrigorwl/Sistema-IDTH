import pandas as pd

def load_data(file_path):
    """Carregar dados do CSV."""
    return pd.read_csv(file_path)

def process_data(df):
    """Processar dados e adicionar uma coluna de 'Passou' baseada no score."""
    df['Passou'] = df['score'] >= 80
    return df

data_visualization.py
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

main.py
from scripts.data_processing import load_data, process_data from scripts.data_visualization import plot_scores def main(): # Caminho para o arquivo de dados data_file = 'data/data.csv' # Carregar e processar dados data = load_data(data_file) processed_data = process_data(data) # Plotar os dados processados plot_scores(processed_data) if __name__ == "__main__": main()

