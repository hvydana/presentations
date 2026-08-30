The presentation i have here : `/home/AMD/hvydana/presentations/Physical_AI_SDK_v2.md` read and understand the contextxt; now  theere wy a discussion why a model zoo is needed i want to add some important slides why a model zoo is needed; 

I want to convery this points:

1. If you needs a off-the shelf user exprience; i.e, A user can download the model and start building application's then then he needs a prepackaged model best suited for his applicatiion.

2. Take nvidia as example how nvidia model-zoo(`https://catalog.ngc.nvidia.com/?topTech=model`) servers ISAC-ROS:`https://github.com/NVIDIA-ISAAC-ROS`, image:`/home/AMD/hvydana/presentations/model_zoo/Nvidia-model-zoo.png`;  see how th interaction between ngc and isac-ros same setup is needed for AMD. 

3. Right now we are packaging all the models in release tarball and this can get heavy when we start adding optimized variants of CNN's and LLMS, this can be typically 100+GB and they have to sit on every users disk even if he only want to use a couple of CNN's. 

4. Drawa better representation of image(`/home/AMD/hvydana/presentations/model_zoo/usage_flow.png`), in this flow i want to metion if AIG gives pytorch model we pick it up and export to onnx to ru it on migraphix, vitis-ai, and then quantize witrh awq and export; or int4 quantization where calibration data ; or do the simialr flow for NPU, if we dont save these stage end customer have to run the pytorch to fianll int-4 on his disk at the time of usage, and this will give poor user erprience thats why all the compnies like nvidia, qualcomn(`https://aihub.qualcomm.com/models/mobilenet_v3_large?tags=backbone`) , i am creatng a model zoo closer to qualcommn model zoo but the graphcs are not yet there we will be havig thisn in this way(`/home/AMD/hvydana/presentations/model_zoo/AMD_PAVS_MODEL_ZOO.png`)

5. How the zoo helps in bringung the great user exprience(`/home/AMD/
hvydana/presentations/model_zoo/user_exprience.png`)

6. What are we(PAVS) expecting from a model-ZOO(A storage space like huggingface and we dont care who maintains it could be AMD central wide infra), but what we need is operational flexibility freedome to create a directoies, store the weights and make it public for customer consumption.

7. What we should not Do: if AIG hosts model zoo, we have to place it in the zoo; now to be in their dashboard we have to write the reserch code that fits in AIG git repo; which means we write simialr setup which is not vertical software(if this has to be done it has to be done like book-keeping but not turn our sdk to match the repo and dashboard); this direction nullifies the value-add physical AI and Vertical software team brings, while making the slide use the slide to from (`/home/AMD/hvydana/presentations/Physical_AI_SDK_v2.md`), this was the intial promise to convert research code to vertical software. if this has to be done it has to be done like a bookeeping stuff, not a customer facing stuff.

8. A looking at AIG git and model zoo it server the reserch engineer who knows nitty grites of AI model and rewire them on his own; our setup brings a different kind of user when will take ai models (does not need to know nity gritties, but just uses them a blackboxes) and build application's using models. He does not need to know which layer is breaking which workflow is more gpu haevy and and laighter varint can be used insted of current model etc. the application ingineer knows the input and outpout of the model and builds his application around this. 

- use the existing presentation pick the slides needed and modify what ever is needed and make a 8-9 slides why model zoo is needed and what we are expecting from models zoo