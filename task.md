This presenation is an answer to the question how many steps should i run to get to the numbers then i have designed this sdk /home/AMD/hvydana/Workspace/physical_ai_sdk where you have 3 options to get to numbers 

(slide-1)
1. 0 steps --> in eavy examples we have `/home/AMD/hvydana/Workspace/physical_ai_sdk/examples/mobilesam/METRICS_TABLE.md` users can see the numbers here directly we have plan to make this a webpage
2. Docker solution WE will haave a docker which will com with pre-instaled rocm and raizenAI and when i run `make benchmark-all-devices metric` it wll create -> `/home/AMD/hvydana/Workspace/physical_ai_sdk/examples/mobilesam/METRICS_TABLE.md` and user can see it 

3. Manually 1. install-rocm -> `./install_rocm_stack.sh` +
            2. install raizen-ai `./install_ryzen_ai_source_stack.sh`
            3. cd examples/mobilesam
            4. `make benchmark-all-devices metric` ->  `/home/AMD/hvydana/Workspace/physical_ai_sdk/examples/mobilesam/METRICS_TABLE.md` 

I want all the above details in slide-1

# Easy-to-use(slide-2)
    
    1. Make based Uniformity: I want to communicate this message (In every example there will same commands and when user runs a commands the same commands will be present in all the example and expect results ) 
    
    2. Every model will have cpu, gpu, Npu flow to benchmark the device wrt compute 
    and throughput and latency. 
    3. In every example there will be an eval pipeline with will take sample inputs and produce sample outputs to see 

    4. In every example will have its own guiding doccumentaton with helps as a tutrorial to get to a result 


# Contributions (slide-3)
    - I want to mention that pavs starts from a code from researcher's Desk to finished product. 
    - I want to show an example yolo setup in the code and i want to use thse snapshost to show this is aresearch code `/home/AMD/hvydana/AIG_Model_delovery_cropped.png`,
    `/home/AMD/hvydana/yolo_aig.png` these are what i get as input and what i give to the user is in ../Workspace/physical_ai_sdk/examples/yolov12/. I want to convicing 3 images in single slide that shows How well thr tooklit is designed. 
    - I want to highlight the point that I am taking a resercher code and making vertical softfare. Team name is Physcial AI and vertical software so I want to higlight
    - Vertical Software(reserch Deck --> Vertical software) I want to drive this point 




# Contributions (slide-4)
    2. Devloper friendly inference tools cloud and edge 
        like Profilers(lamonade, npu-aianalyzer, rocprofiles), 
        - tutorials to use them -- ease of usage
    
    3. VLLm, Lama CPP, Inference infra/platforms for runing LLMS we make it easy to use them in AMD ecosystes.(Bridging bap between opensource ecosustem AMD HW Ecosystem)
    
    4. Build a platform that is willing to solve and fix and evlove with client In developing vartical application in taegtted domains(Healthcare, Automtive, Indistrial) facing applications, prhycal AI vertcials. Building Real ROI WRT AI.
    



# Painpoints(slide-5)
    1. Installtion of rocm still not stable on edge devices
    2. Rocm installtion has a reboot in the installtion phase that makes users uncomfortable
    4. There is a sudo required for system both rocm and raizen ai installtion





