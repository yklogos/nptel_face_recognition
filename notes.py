

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
            1. problems:
                1. length of names eg 3 or 4 word names, abreviated names
                2. honrifics get cut eg. Cloud Computing
                    
        3. image:
            1. image extraction in vedios:
                1. problems: 
                    1. completely wrong image eg. prof. meenakshi d’souza
                    2. face in miniplayer not detected eg. dr. yogish sabharwal
                    3. dark face detected not recognised
                    
                2. if not found in first vedio how to change search parameters:
                    1. options: increase time duration, frames searched per sec for vedio
                        
            2. check quality, suitable for face recognition, of extarcted image:
                1. currently only checking brightness
                2. problems specific to face recognition eg. frontal image, eyes closed
                
            3. TODO: get many images for 1 professor for different lighting conditions, moods and emotional states 
                
                
    2. face recognition:
    
https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python