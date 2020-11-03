pickle files are stored with profs whose names, faces are or arent deetcted
traceback are stored for text, image extraction code with stats

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
    
https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python