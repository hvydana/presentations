We had a meet and greet with a team lead by preteek prabhanjan; recetly the team has been working on https://github.com/AMD-AGI/Hyperloom; an agentic system that optimizes kernals on AMD HW.

These are the inutes of the meeting i have created:

Meet and greet with AIG-Models team,  
This was a nice meeting, and we have found out some interesting directions towards collaboration 


1.	Expanding hyper loom to Edge HW (GPK, krk2e, PNR), The suggestion from Prateek was to Take existing GEEK system and Work on GPK with some models to optimize some of the models that are already in PAI SDK. 
- Work will be started on GPU, NPU by (AMOL, Vaibhav, Karthik); in this process the Kernels will be optimized and and GEEK platform which right now works of MI300 will be expanded to embeded-HW;   
- By attemtping to optimize NPU model we will be contributing/playing a part in expanding GEEK type platform to NPU. 
-GEEK is a part of Hyperloom that optimizes kernals there are other part that creates traces, etc... 

2.	World Action Robotic models are being developed and optimized in the AIG models team and they are going to be trending in the next coming months, (srini,Hari) from our team will be leading this work to understand and integrate and benchmark on the Edge HW. 

3.	They have expertise and Synthetic Data Generation (kush ad ravi are working on this(genesis style Simulators) they can benefit from this)

4. They have proposed to have expertise in Kernel Generation; this could be further explirod by ourteam to produce something like MLIR(optimization library in migraphix) on NPU; 

5.	They are very interested in learning about Assets from PAVS,   AMD-ROS pipelines and AMD-cUROBO~(motion planner frameworks from NVIDIA ongoing work with our robotics team), I propose to setup a meeting with robotics team and give a walkthtrough of ongoing work. They can help how to use their work for model development for edege deplooyment. 

6. What they are looking at us is a gatway of making their work reach customer's. In this some time they want to share our deployment HW GPK board to benchmark their models they their model on our robotic arm and AMR. 

i want to mention the potential topics where there is overlap betwen teams; and how we can develp the collaboration 