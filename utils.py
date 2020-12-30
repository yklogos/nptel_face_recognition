import pickle

def save_as_pickle(file_path, file):
    with open(file_path, 'wb') as f:
        pickle.dump(file, f)

def load_from_pickle(file_path):
    with open(file_path, 'rb') as f:
        file = pickle.load(f)
    return file