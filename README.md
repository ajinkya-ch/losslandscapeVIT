# LossLandsxVIT

*All files are stored in the CFS provided by NERSC.

## Setup:

1. Create a new conda environment: `conda create --name losslandvit python=3.6`
2. Install required packages: `pip install -r requirements.txt`
3. Clone original losslandscapes repository: `git clone https://github.com/ajinkya-ch/losslandscapeVIT.git`


## Train Vision Transformer (on Cori):

- Model trained for 950 epochs `python ./src/cifar10/main.py --model vit --lr 0.0001 --epochs 950 --ngpu 8`

- It will be saved with a .t7 suffix. 
model path: `/global/cfs/projectdirs/m636/AJ/VITlosslands/model_950.t7`


## Generate surface file:

`python plot_surface.py --x=-1:1:16 --y=-1:1:16 --model vit`

- This will generate a direction file (.h5) and a surface file (.h5)
direction file path: `global/cfs/projectdirs/m636/AJ/VITlosslands/model_950.t7_weights.h5`
surface file path: `global/cfs/projectdirs/m636/AJ/VITlosslands/model_950.t7_weights.h5_[-1.0,1.0,16]x[-1.0,1.0,16].h5`

## Plotting: 

- `plot_2D.py --surf_file global/cfs/projectdirs/m636/AJ/losslands/trained_nets/model_950.t7_weights.h5_[-1.0,1.0,16]x[-1.0,1.0,16].h5 --dir_file global/cfs/projectdirs/m636/AJ/losslands/trained_nets/model_950.t7_weights.h5` 

Path to plots: `/global/cfs/projectdirs/m636/AJ/VITlosslands`






