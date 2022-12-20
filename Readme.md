# Pentru a rula proiectul
1) Se descarca baza de date utilizand urmatorul link: https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/
2) Imaginile sunt descarcate de pe linkul de mai sus si salvate intr-un folder numit oxford_dataset
3) Se creeaza un folder nou cu numele data
4) Se ruleaza comanda in cli anaconda: python prepare_dataset.py pentru prelucrarea bazei de date
5) Se descarca model_test_2_resnet.pt, im_indices.json, faiss_index
6) Se ruleaza comanda in cli anaconda: python find_most_similar_image.py [path_catre_imagine_de_intrare] de exemplu: python find_most_similar_image.py oxford_dataset_splited\test\2\ashmolean_000203.jpg