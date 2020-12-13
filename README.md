# nptel_face_recognition
Face recognition task on nptel videos identifying professors
<br>Drive link for data: https://drive.google.com/drive/folders/19sTbgtfns6HDgiHDS6ArRTtqh7nLM_8-?usp=sharing

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

1. known_faces - dir for labelled faces 
(ver variable is added at the end to save with different methods of faces eg. known_faces3 - full frame, known_faces_with_diversity - faces with thresholding)
2. pkl_files - dir for pickle files containing youtube ids, aux dictionaries, lists (eg. list of professors whose name is found)
3. full_vedio - dir for downloaded vedios
4. experimental_scripts - dir for notebooks of indivisual functions
5. tracebacks - dir for usefull results in the form of cell outputs of notebooks in experimental_scripts
6. results - dir for evaluation results


## important files

1. download_vedios_from_channels.ipynb - downloads vedios from nptel channels
2. get_prof_name_face_from_vedio.ipynb - saves names and faces of professors
3. face_recognition_eval.ipynb - evaluation of all vedios using face recognition library
4. make_serengil_deepface_known_faces - makes labelled faces directory for deepface library(run before evaluation scripts and after saving faces) 
5. serengil_deepface_recognition_eval - face recognition evaluation of different models usign deepface library
6. serengil_deepface_verification_eval - face verification evaluation of different models usign deepface library





