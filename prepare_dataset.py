import os
import shutil
import splitfolders

# get a list of all files in the 'oxford_dataset' directory
file_list = os.listdir('oxford_dataset')

# create a dictionary to store the images by class
classes = {}

# iterate through the list of files
for file in file_list:
    # extract the class name from the file name
    split_class_name = file.split('_')
    if len(split_class_name) == 3:
        class_name = split_class_name[0] + "_" + split_class_name[1]

    if len(split_class_name) == 2:
        class_name = split_class_name[0]

    # add the image to the list of images for the corresponding class
    file = os.path.join(class_name, file)
    file = os.path.join("data", file)
    if class_name in classes:
        classes[class_name].append(file)
    else:
        classes[class_name] = [file]

# the classes dictionary now contains the images grouped by class
for class_name in classes:
    os.makedirs(os.path.join("data", class_name))

# Save each value to its corresponding folder
for class_name, values in classes.items():
    for value in values:
        file_name = value.split("\\")[2]
        src = os.path.join("oxford_dataset", file_name)
        dst = value
        try:
            shutil.move(src, dst)
        except:
            pass

classes_array = list(classes.keys())
classes_dict = {value: position + 1 for position, value in enumerate(classes_array)}

# Set directory to rename folders in
data_dir = 'data'

# Loop over old and new folder names
for old_name, new_name in classes_dict.items():
    # Construct old and new folder paths
    new_name = str(new_name)
    old_folder_path = os.path.join(data_dir, old_name)
    new_folder_path = os.path.join(data_dir, new_name)

    # Rename folder
    os.rename(old_folder_path, new_folder_path)

splitfolders.ratio("data", output="oxford_dataset_splited",
    seed=1337, ratio=(.8, .1, .1), group_prefix=None, move=False)

print("Baza de date a fost creata cu succes")