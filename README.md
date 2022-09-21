# Panorama

Creates a simple panorama by performing image stitching using python and openCV. It is capable to handle multiples images to get a proper panoramic view. 


## Properties

This method utilises OpenCV's Stitcher_create() method, which is insensitive to :
- ordering of images
- orientation of images
- illumination changes
- noisy images that aren't part of panorama

It creates more aesthetically pleasing panorama output through the use of gain compensation and image blending, at the cost of processing time which takes around 10 seconds for complete pipeline.

Stitched images are further processed to eliminate most of the outer mismatched portions (black region) for enhanced view.


## Results

Inputs:
<div style="float:left">
<div style="float:left"><img width="25%" src="https://github.com/Sudarshana2000/Panorama/blob/master/input/IMG_1.jpg" />
<img width="25%" src="https://github.com/Sudarshana2000/Panorama/blob/master/input/IMG_2.jpg" />
<img width="25%" src="https://github.com/Sudarshana2000/Panorama/blob/master/input/IMG_3.jpg" />
<img width="25%" src="https://github.com/Sudarshana2000/Panorama/blob/master/input/IMG_4.jpg" />
</div>
<br /><br />

Panorama view:
<img src="https://github.com/Sudarshana2000/Panorama/blob/master/output/cropped1.jpg" />
<br />