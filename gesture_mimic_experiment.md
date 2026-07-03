We have recently worked on a robitics project project; Where a huma will stand infornt of the camera and will wahe the hand in different positions up and down and left and reight, wrist open and close in all the posiotnion "so101 arm" which runs on lerobot is configures to mimic the same actions that a human is doing. 

To do this task first we have collected data with 2000 episioes with multiple people abd various backgrounds. The data for this task is collected in the following way: first a person will be instection to do an action lik elifitng the hand and openng the wrist , the arm comes as a pais a master arm and a slave arm, they will be connectd thosugh a cable and master arm is contoling arm and slave is scontrablable an they are configues in such a way that salve motors exactly imitates the master arm a hum operates the amaster arm looking at the person in front of camera and slave arm imitates the same action from the amster as it reives motor signals directly from contoling data set collectior. that may the reason this type of training is cll iitation learning. Now we have a vedio and corresponding action from the slave arm which is transferd from master, now we these wti will be synce and input output pairs of images and output action vectors will vcreated to generate the dataset. 


SFT:
  Now after collecting the data, we have finetuned smolVLA, ACT and pi0.5 models for this task. we have used MAE between the predicted trajectories and groundtruth trajectores is used as the metric to mesaure how good the modle Is. 

Speed is the new accuray:
 the main reason for picking up the task is to show case the compute speed and capacity of AMD x100~(GPK) boards and this task has special porperty where the faster the model can run the more input images it can precess and more reactive th e model can be and much better the response will be. 

While controling the loop we have used the async rtc loop in smolVLA lerobot huggigface setup. When we see an input image it can predict 50 action steps and when we consumed only one action we have very good fps ans when we consumer 10 actio fps dropped and when we consumed all 50 we have very bad accuracy, 


Some of the actoions done to imprpve the algorthmec latecy of the model are we have finetuned a smolVLA model woth 2000 person data, for the model we have found 2 diffusions steps are good enough to maintain accuracy insted of 10. The opensource algorithon has only torh compile for diffusion steps; but i have implemented the torch.compile compatable code for both encoder and llm pre-fill this has reduced the latency a lot. Now smol VLA architecture has 3 cameras no i have reduced the 3 camera input to single camera input because in this task we are using a single camera rest of the two channels , this has also further improved the accuracy as speed improved, Now insted of eager mode we ere able to use compiled graph and brought the latency to 

I have implemented a smoothing algorithm, which will average the action with a moving window and this has reduced the fricton effects in the robot. 


- explain about how lerobt accuracy work's why using longer chunk steps results in bad accuray why speed is important in this task , how we reduced alorithmic latency, make cleaner explanation of rtc and sync processing and write pseudo code of the algorithm. 

- Look at the lerobot setup in this code and understand rtc with asyc loop and haow th algoirthm works write the ouput in `/home/AMD/hvydana/presentations/confuence/smolvla_paper_and_rtc_understanding.md`

1. smoothing: 
  - code is here: /home/AMD/hvydana/presentations/GTAC2026-gesture_mimic/smooting.md

2. torch.complie Why this is needed and what does thos bring to table as opposed to existing default troch.compile patches: `/home/AMD/hvydana/Workspace/physical_ai_sdk/models/smolVLA`


read the results here: `/home/AMD/hvydana/presentations/confuence/`

I made a presentation some time ago use this to
 - `/home/AMD/hvydana/presentations/confuence/SmolVLA_improvements.md`
 - `/home/AMD/hvydana/presentations/confuence/SmolVLA_improvements.pdf`
 - `/home/AMD/hvydana/presentations/confuence/SmolVLA_improvements_2slides.pdf`

With all these write a paper with  imitation learning for an interanl conference in AMD highilighting AMD hardware and its capabilitues witht his task, I want to submit to internal conference in AMD.