Look at /home/amd/Work/presentations/PAVS_Physical_AI_SDK_SW_Arch_and_Strategy_2026.pdf,  


Model lifecycle:

1. Now i want make a new presentation where for the model the lifecycle is enablement, profiling,  benchmarking, finetuning , 

## later part may need more work than expected
2. We have individual models first we need to support individual models and later we have to expand to orchestartion of models to exand to systems, 

## Effective utilization
Our interaction with External teams should be progressive, before giving the work to sow we need to do an initial attempt atleaselike enablement  so that we can get wore work done from mcw at finetuning , 

## Speed matters
we need to start ths step as early as possible and but in parallel
    - Herei want a table with differnt models some with  tick at enablement and some at profiling some at finetuning 
    all 4 steps are at 4 coluns 

## Possible envinronemnt & need for CI-CD  
We need to have dockerfile and python virual environemnts(uv + pyproject.toml or pip+requirements.txt)  for each model or systems while deployiong we need to have  continous github  produce branch dev branch and ci/cd to not have regrssions ;

## enviromentmens
 - for each model/system its own vrtual env, which could be seperated for different dir could be ideal where users can go swith this on and explore the model; where we have a platform with al the models and yet not deal with versnion matching all the tools accrossthe models. 

### We need more scope adding some more latest models if there is some new scope at open source 
 - Expeting end-to-end Neural alternatives to todays pipelines may gradually start working and we need to be ready ti include them 

### benchmarking and doccumentation should be done in collaboration with github 
    - gitpages could be an usefull tool ; 
    - show an example how gitpages look like 


For all the slides i want a appropriate image or graphic to show what i intend 

  
