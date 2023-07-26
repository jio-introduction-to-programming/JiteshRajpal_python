
def persist_data(data, filename):
    # Use Python built-in functions to write 'data' to 'filename'
    # open the file with write "w" mode

    file = open(filename,'w')

    #Write some data to the file

    file.write(data)

    # Close the file

    file.close()


def read_file(filename):
    pass  # Use Python built-in functions to read contents of 'filename' and print them to screen
    file = open(filename,'r')
    print(file.read())
    file.close()

def write_file(filename, data):
    pass  # Use Python built-in functions to write 'data' to 'filename'
    file = open(filename,'w')

    #Write some data to the file

    file.write(data)

    # Close the file

    file.close()


def delete_file(filename):
    pass  # Use Python built-in functions to delete 'filename'
    import os

    os.remove(filename)

def overwrite_file(filename, data):
    pass  # Use Python built-in functions to overwrite 'filename' with 'data'
    file = open(filename,'w')

    #Write some data to the file

    file.write(data)

    # Close the file

    file.close()

def append_file(filename, data):
    pass  # Use Python built-in functions to append 'data' to 'filename'
    file = open('example.txt','a')

    #Write some data to the file

    file.write('\nAppended more text by using python')

    # Close the file

    file.close()


def write_binary_file(filename, data):
    # Use Python built-in functions to write 'data' as binary to 'filename'
    file = open('filename.bin','wb')
    file.write(b'data')
    file.close()

def read_image_file(filename):
    # Use OpenCV to read 'filename' as an image
    import cv2
    img=cv2.imread('filename.jpg')
    cv2.imshow('image',img)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def read_csv_file(filename):
    # Use Pandas to read 'filename' as a csv
    import pandas as pd
    df=pd.read_csv('filename.csv')
    print(df)

def write_csv_file(filename, df):
    # Use Pandas to write dataframe 'df' to 'filename'
    import pandas as pd
    df = pd.Dataframe({'A': [1,2,3], 'B': [4,5,6]})
    df.to_csv('filename.csv', index=False)

def read_json_file(filename):
    # Use json to read 'filename' as a json
    import json
    with open(filename,'r')as filename:
        data=json.load(filename)
        print(data)


def read_json_file(filename):
    # Use json to read 'filename' as a json
    import json
    with open(filename, 'rb') as filename:
        print(json.load(filename))

def write_json_file(filename, data):
    # Use json to write 'data' to 'filename'
    import json
    d = {data}
    with open(filename, 'wb') as file:
        json.dump(data, filename)

def write_pickle_file(filename, data):
      # Use pickle to write 'data' to 'filename'
    import pickle
    with open(filename, 'wb') as file:
        pickle.dump(data, filename)

def read_pickle_file(filename):
     # Use pickle to read 'filename'
     import pickle
     with open(filename, 'rb') as filename:
        print(pickle.load(filename))
