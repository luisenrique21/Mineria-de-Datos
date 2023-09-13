import kaggle

# Configura tu API key de Kaggle (obtenla desde tu cuenta de Kaggle), y ponla en la carpeta que se creó al importar kaggle
#link del archivo: https://www.kaggle.com/datasets/bergurtamimi/premier-league-odds-history

api = kaggle.api
kaggle.api.dataset_download_files('bergurtamimi/premier-league-odds-history', path='./', unzip=True)


