##creates JSON file containing image path and class label for training data and validation data in 2 separate json files
#image_data_train.json: for training data
#image_data_val.json: for validation/testing data

import os
import json

def create_json(root_folder, filename):
    data = []
    for class_label in os.listdir(root_folder):
        class_path = os.path.join(root_folder, class_label)
        if os.path.isdir(class_path):
            for image_file in os.listdir(class_path):
                image_path = os.path.join(class_path, image_file)
                if os.path.isfile(image_path):
                    data.append({
                        "Image_path": image_path,
                        "Class_label": class_label
                    })

    with open(f'{filename}.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Provide the root folder containing the sub-folders of images for training & validation respectively
root_folder = '/Users/asmitasengupta/finproj/Birds_25/train'   
create_json(root_folder, 'image_data_train')
root_folder = '/Users/asmitasengupta/finproj/Birds_25/valid'
create_json(root_folder, 'image_data_val')

