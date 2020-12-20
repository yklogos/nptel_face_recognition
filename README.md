# nptel_face_recognition
indexing nptel vedios based on the profesor<br>drive link for data: https://drive.google.com/drive/folders/19sTbgtfns6HDgiHDS6ArRTtqh7nLM_8-?usp=sharing

## directory structure
```
├── data
| ├── known_faces
|     ├── <prof1 name>
|         ├── pic1.jpg
│         └── pic2.jpg
| ├── pkl_files
| ├── tracebacks
| ├── full_vedio
│   ├── <channel name 1>
|       ├── <playist name 1>
|           ├── <vedio id 1>.mp4
│           └── <vedio id 2>.mp4
├── experimental_scripts
├── results

```

## data directory descriptions

1. known_faces - labelled faces (ver variable is added at the end to save with different methods of faces eg. known_faces3 - full frame)
2. pkl_files - pickle files containing youtube ids, aux dictionaries, lists (eg. list of professors whose name is found)
3. full_vedio - downloaded vedios
4. experimental_scripts - jupyter notebooks 
5. tracebacks - usefull cell outputs of notebooks in experimental_scripts
6. results - dir for evaluation results

## important files
NOTE: seprate versions of noteboks to run on colab which use data from your drive 
1. download_vedios_from_channels.ipynb - downloads vedios from nptel channels
2. get_prof_name_face_from_vedio.ipynb - saves names and faces of professors
3. face_recognition_eval.ipynb - evaluation of all vedios using face recognition library
4. make_serengil_deepface_known_faces - makes labelled faces directory, from known_faces dir, for deepface library 
5. serengil_deepface_recognition_eval - face recognition evaluation of different models using deepface library
6. serengil_deepface_verification_eval - face verification evaluation of different models using deepface library
7. app.py - streamlit face recognition app on vedios in full_vedio




