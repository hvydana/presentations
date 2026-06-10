Look at the presentation and keep the same theme, but modify the content `SmolVLA_Gesture_Chunk_Study.md`, i have worked on optimizing smolVLA and I have done changes in this sequence, i want this in one or 2 or 3 sldes.

- First  the model was running at 2 infernces/fps  we found its unncessry to run this many diffusiin steps reduced this from 30 to 2 this has mad the inderences to 4.5~5 inf/sec 
- Now we have implemented the torch compile where the compiled graph , to dot this we had to rewrite some modues in lerobot smolVLA to that the while flow becomes a graph that could run with optimicxed kernels on cpu this has brought fps to 8.5inf/sec
- We got the next big improvement moving from fp32 to fp16 and this has given 13-15 inf/sec , to do this in our current we found that if we dont cast the weoghts to fp16 from start torch.compile is adding puscale and downscale optionations around every layer in graph where overhead eats the impovement form lowe precssion. 
- since we have enough speed we have switcehd to rtc(realtime chunking mode on: camera pipeline and model will be operatiing parallel threds shareing the same gpu), this will improve the reactive ness of the overall pipelines. 

we have reduced `chunk_size_threshold` where after consuming 5 images the model will intiate next processing of next image, so this will initate further reactiveness of the whole pipelline. 


- As we improve the throughput of the model, we improve acruacy as it can consume mor einformation from camera stream if not model has to guess a lot and thats where the sync between persion actions romot mimic gets lost dues to slowness the model has tp drop the images without processg. 
- As speed of thr model increases the accriacy in the benahiour, because robot does not consume long-sequece prediciton which will be unreliable because robot is looking at curet stae and predicting long future becausing the processing is slow, of the proceesin is fast the new image and precition will overwirte with recent tdata this will increase the accuracy of the model. 
- smothness: We ahve observed that there is shake, jitter in the operation of robot  as its ti training on less data and outpus space si loarge(continus actions), we have implemented somtheing post processign that would remov this jitter and have smoth actions

- We have increased the size of data and fintuned the model which has given better accuracy. this has give better improvenets in MAE from 6 to 2.7 which is much more usable

Thiis is slide bout the steps taken to imprve the gesture mimic model with smolVLA +lerobot 
I want to show sequence ostsps and some significace why its needs to be done , i want sequce of action in slide 1 and some reaosn in slide 2 and 3 , i ahve troughput and accruacy as two tracks, this needs ot go to upper level managemens   

