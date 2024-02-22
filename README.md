# pi_print
A simple python program to print digits of pi to an image.

Below is a 200 x 200 pixel image as an example of the program output which represents the first 200^2 digits of pi. Each pixel is an 8 bit (0 - 255) transformation of the digit at the given position, starting from the left uppermost corner and going to the right lowermost corner.

![pies](https://github.com/rentazillla/pi_print/assets/14893909/6e6d00c5-ffec-459a-8514-ae7583195834)

In future iterations of this project I plan to introduce a timer to determine how the time to complete the computation depends on how many digits you wish to calculate. Each digit should take time = O(n log n) to compute where n is the index of the digit in question.
