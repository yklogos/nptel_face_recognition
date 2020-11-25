# nptel_face_recognition
Face recognition task on nptel videos identifying professors 

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
2. pkl_files - dir for pickle files containing youtube ids, aux dictionaries, lists (eg. list of professors whose name is found)
3. full_vedio - dir for downloaded vedios
4. experimental_scripts - dir for notebooks of indivisual functions
5. tracebacks - dir for usefull tracebacks of notebooks in experimental_scripts
6. results - dir for evaluation results


## important files

1. download_vedios_from_channels.ipynb - downloads vedios from nptel channels
2. get_prof_name_face_from_vedio.ipynb - saves names and faces of professors
3. face_recognition_eval.ipynb - evaluation of all vedios using face recognition library





