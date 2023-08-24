import pickle

def generate_pickle_data(filename):
    data = [
        {"Access Level": "1", "Identifier": "0000001234", "Name": "Anna", "hash": "abcd1234"},
        {"Access Level": "2", "Identifier": "0000001235", "Name": "Bob", "hash": "abcd1235"},
        {"Access Level": "3", "Identifier": "0000001236", "Name": "Charlie", "hash": "abcd1236"},
        {"Access Level": "1", "Identifier": "0000001237", "Name": "David", "hash": "abcd1237"}
    ]

    with open(filename, 'wb') as f:
        pickle.dump(data, f)

    print(f"Data saved to {filename}")

generate_pickle_data("sample_data.pkl")
