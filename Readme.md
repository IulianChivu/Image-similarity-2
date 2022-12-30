# Pentru a rula proiectul:
1) Creare v-env python==3.9.0 (conda create -n sccv-proiect python=3.9.0) + activare (conda activate sccv-proiect)
2) Instalarea bibliotecilor (python -m pip install -r requirements-pip.txt --extra-index-url https://download.pytorch.org/whl/cu116)
3) Se descarca baza de date 'Oxford5k' utilizand urmatorul link: https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/
4) Imaginile sunt descarcate de pe linkul de mai sus si salvate intr-un folder numit 'oxford_dataset'

# CNN Method:
5) Se ruleaza comanda in cli anaconda: python prepare_dataset.py pentru prelucrarea bazei de date
6) Se descarca model_test_2_resnet.pt, im_indices.json, faiss_index
7) Se ruleaza comanda in cli anaconda: python find_most_similar_image.py [path_catre_imagine_de_intrare] de exemplu: python find_most_similar_image.py oxford_dataset_splited\test\2\ashmolean_000203.jpg

# LBP + Euclidean Distance Method:
8) Se ruleaza comanda in cli anaconda: python prepare_dataset_lbp.py pentru crearea bazei de date formata din descriptori lbp (~15 sec - Intel I7)
9) Se ruleaza comanda in cli anaconda: python find_most_similar_image_lbp.py [path_catre_imagine_de_intrare] de exemplu: python find_most_similar_image_lbp.py oxford_dataset_splited\test\3\balliol_000116.jpg


# Train
Proiect_SCCV_Image_Retrieval_CNN.ipynb -> scriptul complet care contine si partea de antrenare a retelei CNN
