# Digital Image Processing 
Assignment #5

Due: Tue 12/03/21 11:59 PM

1. Grayscale to color conversion:
Write code to convert a grayscale image into a color image using the two techniques covered in class: Color slicing and Intensity to color tranformation using rectified sine wave functions. 
The input to your program is a 2D matrix.

  - Starter code available in directory Coloring/
  - Coloring/Coloring.py: Edit the functions 'intensity_slicing', and 'color_transformation' you are welcome to add more function.
  - For this part of the assignment, please implement your own code for all computations, do not use built-in functions  from PIL, opencv or other libraries - that directly accomplish the objective of the question. You can use math and random related functions.
 
    
color_slicing(image, n_slices):
    - Write code to tranform greyscale image to color image using intensity slicing. 
    - The function returns the colored image.

color_transformation(image, n_slices, theta): 
    - Write code to tranform greyscale image to color image using intensity to color transformation using rectified sin waves.
    - The function returns the colored image.

  - This part of the assignment can be run using dip_hw5_color.py (there is no need to edit this file)
  - Usage: 
  
        ./dip_hw5_color -i cat.jpg -n 5
        python dip_hw5_color.py -i cat.jpg -n 5
        
  - Please make sure your code runs when you run the above command from prompt/terminal
  - Any output images or files must be saved to "output/" folder (dip_hw5_color.py automatically does this)
  
-------------

Four images are provided for testing: cat, Medical, luggage, and pluto  
PS. Files not to be changed: requirements.txt and Jenkins file 
  
1. Any output file or image should be written to output/ folder

The TA will only be able to see your results if these condition is met

1. Grayscale to color conversion       - 75 Pts.

    Total                              - 75 Pts.

---------------------