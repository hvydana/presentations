Corrections in the paper: 
    1. all mathematical symbols and equantion should use proper latex match sysmbols. 
    2. "SciPy matrix inversions ", calling it scipy matrix inversion is giveing aless tech feel, just call in matrix inverions 
    3. "It is an artifact of a sequential, Python-loop-heavy implementation." we can just call it as due to sequenctial implemetations or something more research language.
    4.  Use this to represent: sequential operation (`/home/AMD/hvydana/presentations/gif_gen/gaussian_frames/frame_025.png`) and optimized verion is (`/home/AMD/hvydana/presentations/gif_gen/gaussian_frames/frame_093.png`) , can be understood as beofre and after. we have `.gif` if its possible to add in .pdf add `gaussian_scan.gif`
    5. we dont need references like `infer.py` PyTorch backend (infer.py), as we are writing a paper, also the same case with `onnx_infer.py` but explantion is corrrect.

    6. reference to fast api in this is not needed 
    - ```text
    FastAPI serving layer (app/): Wraps either backend in a REST API with /predict and /health routes, a per-class model registry loaded from a configurable directory, and covariance-mode selection via the use_diagonal_cov flag at startup.```