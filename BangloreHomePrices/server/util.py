import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price (location,sqft,bath,bhk):
    try:
        loc_index = __data_columns.index(location.lower())  #loc_index = np.where(X.columns==location)[0][0] #used in jupyter notebook
    except:
        loc_index= -1

    x_array = np.zeros(len(__data_columns)) #x_array = np.zeros(len(X.columns)) #used in jupyter notebook here x.columns=__data_columns
    x_array[0] = sqft
    x_array[1] = bath
    x_array[2] = bhk # It assign sqft,bath,bhk values to corresponding positions in X_array
    if loc_index >= 0: #one hot encoding
        x_array[loc_index] = 1
    return round(__model.predict([x_array])[0],2)    # round is to convert float to 2 decimel places

def get_location_names():
    return __locations
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __locations
    global  __data_columns
    #when we want to modify the value of a global variable within the function ,we need to add global keyword
    #if we dont add global keyword ,it will be considered as a local variable

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns'] #data columns is the key of columns.json file
        __locations = __data_columns[3:] #first 3 columns are sqft, bath, bhk and the locations are avaible after 3rd index in columns.json file

    global __model
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)   # Import the model
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('kalhalli',1000, 2, 2))
    print(get_estimated_price('ejipura', 1000, 2, 2))

