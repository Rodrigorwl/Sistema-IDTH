from scripts.data_processing import load_data, process_data
from scripts.data_visualization import plot_scores

def main():
    # Caminho para o arquivo de dados
    data_file = 'data/data.csv'
    
    # Carregar e processar dados
    data = load_data(data_file)
    processed_data = process_data(data)
    
    # Plotar os dados processados
    plot_scores(processed_data)

if __name__ == "__main__":
    main()



