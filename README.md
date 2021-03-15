<h4> Face Recognition </h4>
Face Recognition can be used to identify a person, given an anchor photo of him/her. You can give the path for your anchor image in the file. A window pops when the program is ran,
and the calculated distance between your image and the frame captured from your webcam is shown in the middle of the window. A distance smaller than 1.1 means that the people 
in the photos are the same.

<h5> Requirements: </h5>

<li> facenet-pytorch = 2.5.0 </li>
<li> torchvision = 0.5.0 </li>
<li> pytorch = 1.7.0 </li>
<li> opencv-python = 4.4.0.44 <li>


<h4> Object Recognition </h4>

I finetuned YOLOv4 to detect custom objects, but the weights are not in Github. 

Object classes are: Person, Headphone, Book, Telephone, Laptop

<h5> Requirements for Inference: </h5>

<li> opencv-python = 4.4.0.44 </li>
<li> numpy = 1.19.3 </li>
<li> YOLOv4 Weights </li>


<h4> OCR </h4>

Simple OCR program to read text from webcam frames. It is based on Tesseract.

<h5> Requirements: </h5>

<li> opencv-python = 4.4.0.44 </li>
<li> numpy = 1.19.3 </li>
<li> pytesseract = 0.3.7 <li>
<li> pillow = 8.0.1 </li>
 
