# LossLandsxVIT

## Setup:

1. Create a new conda environment: `conda create --name losslandvit python=3.6`
2. Install required packages: `pip install -r requirements.txt`
3. Clone original losslandscapes repository: `git clone https://github.com/tomgoldstein/loss-landscape.git`


4. Move model_loader.py to loss-landscape/cifar10/

5. Move `gelu.py` , `identity.py`, and `vit.py` to loss-landscape/cifar10/models/

## Train Vision Transformer:

`python loss-landscape/cifar10/main.py --model vit`

- It will be saved with a .t7 suffix

## Generate surface file:

`python plot_surface.py --x=-1:1:51 --y=-1:1:51 --model vit`

- *Please define other commandline parameters of the plot_surface.py to calculate directions and loss values correctly.

## Plotting: 

- Use `plot_1D.py` and `plot_2D.py` to generate plots.




