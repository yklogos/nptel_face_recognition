points for the next meeting:
    0. models 
    1. mention nptel papers found, why so less? any other platform to find papers  
    2. ask for list of nptel, other platform research papers, projects for better understanding of usefull features, easier to implement as data is already there
    4. request for full paper
    5. a way to block a import from printing mesages, warnings, tqdms 
    6. free conferences to attend in winters
    7. how to follow current research, like ML newspaper, in genral and in a specific field 
    8. long stretch but a web application
    . ASR dbts:
        1. acousic faeture generator
        2. acoustic modes?

# vedio indexing company
https://www.google.com/url?hl=en&q=https://lake.videoken.com/exchange&sa=D&ust=1606540394377000&usg=AFQjCNEgB9tyNOXHpvyLO9BuvCbOmZwkjw
# vedio doi
https://av.tib.eu/
    
Tasks:
    0. genral:
        1. 
        2. testing method:
            1. both accuracy(optimizing metric) and fn, fp rate(satisfizing metric)
        3. other relaetd projects nptel (explaination + slides, summarization, combining vedios from differnt iits)
        
    1. get labeled data:
        1. data:
            1. source: 
                1. nptel vedio
                2. nptel site(not very helpfull)
                3. onlinecourses.nptel.ac.in(standard xml format for prof name for course name)
                4. prof. site(not standard xm format for photo)
                5. google images
                
            2. problem with only slides with no face or name:
                1. eg. Computer Architecture Prof. Smruti Ranjan Sarangi
                2. can mayne output only slides or something
                
            3. features data should have:
                1. unique names
                2. good photos for face recog
            
            
        2. text:
            1. name extraction:
                1. in vedios:
                    0. problems: 
                        1. for profs names not detected:
                            1. IIT K (channel)Aerospace Engineering, Advance Analytical Course
                            2. IIT M Particle Characterization (PG)
                            3. IIT KGP Cloud Computing
                            
                        2. garbage words detected with profs name(eg. dr. a. kushari ds eer eet..):
                            1. IIT K (channel)Aerospace Engineering
                            2. IIT B Introduction to Mechanobiology, Introduction To Proteomics
                        
                    1. current method: 
                        1. check in title at the end of paylist name
                        2. check for honorific (eg. prof, dr etc):
                            1. if found check for end word (eg. department), slice sent from honrific to end word
                            2. if end word not found but honorific found, check for expeceted lastname:
                                1. if len(lastname)<4 include lastnaem else exclude
                        5. if honorific not found ret None
                    
                2. on swayam site: <div, class="col-lg-12 col-md-12 col-sm-12 col-xs-12"> tag 
                    
                    
        3. image:
            1. image extraction in vedios:
                1. problems: 
                    1. completely wrong image eg. prof. meenakshi d’souza
                    2. face in miniplayer not detected eg. dr. yogish sabharwal
                    3. dark face detected not recognised
                    4. how to know if face is different??
                    5. if face is detected, no encoding are returned
                    
                2. if not found in first vedio how to change search parameters:
                    1. options: increase time duration, frames searched per sec for vedio
                        
            2. check quality, suitable for face recognition, of extarcted image:
                1. currently only checking brightness
                2. problems specific to face recognition eg. frontal image, eyes closed
                
            3. TODO: get many images for 1 professor for different lighting conditions, moods and emotional states 
                
                
    2. face recognition:

accurate slide detection, so what isnt a slide is a prof face
request paper https://www.sciencedirect.com/science/article/abs/pii/S0957417420301664 
check if 
face_recognition low recogntion rate
face_recognition performs better at identification if not changed to rgb, discovery by acident


details on deepface models:
    1. VGG Face:
        3. model: parameters: 145,002,878
                
    2. FaceNet:
        1. input: 160×160 RGB images
        2. output: 128 dimensional 
        3. model: inception_resnet_v1, parameters: 22,808,144
                
    3. OpenFace:
        1. input: 96×96 RGB images 
        2. output: 128 dimensional output
        3. model: inception_resnet_v1, parameters: 3,743,280
                
    4. DeepFace:
        3. model: 8 layered CNN, parameters: 137,774,071
        
    5. DeepID:
        1. The 1st generation expect 39×31 sized 1 channel input whereas 2nd generation(DeepID2) expects 55×47 sized 3 channel (RGB) input 
        2. output: 160 dimensional last layer
        3. model: 4 convolution layers and one fully connected layer
            
    6. Dlib:
        1. input: 150x150x3    
        2. output: 128 dimensional vectors
        3. model: 29 convolution layers


tunable parameters

get labeled naems, faces:
1. name heuristic
2. image:
    1. heuristic to save a image(disimilarity)
    2. number of images to save
    3. does validation of image based on the image itself improve accuracy
    4. num for vedios from which to take images

face_recognition:
1. face_locations:
	1. number_of_times_to_upsample - Higher numbers find smaller faces.
	2. model - Which face detection model to use. "hog" is less accurate but faster on CPUs. "cnn" is a more accurate
                  deep-learning model which is GPU/CUDA accelerated (if available). The default is "hog".

2. face_encodings:
    :param num_jitters: How many times to re-sample the face when calculating encoding. Higher is more accurate, but slower (i.e. 100 is 100x slower)
    :param model: Optional - which model to use. "large" or "small" (default) which only returns 5 points but is faster.
            
    tolerance - for verification

deepface:
1. find, verify:
	1. model_name among  ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib"]
	2. detector_backend among ['opencv', 'ssd', 'dlib', 'mtcnn']
2. number of preditions 


metrics:
get metrics for chanels, playlist, vedio seperately
1. num vedios downloaded
2. num names, faces extraced
3. num of faces recognized
4. accuracy of faces verified

doubts and concerns:
    1. face_recognition low recogntion rate
    2. face_recognition performs better at identification if not changed to rgb, which shouldnt be the case
    3. using deep face 1/2hr 1 vedio 6 models, 5 predictions
    4. code optimization in genral