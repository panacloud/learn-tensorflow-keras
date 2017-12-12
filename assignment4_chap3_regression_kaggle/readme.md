# Assignment 3: Generate a scatter plot data and line with negative slope and containerize it.

The current code is not running correctly your job is to find and remove the bug

Do this Assignment after reading beginning of chapter 3 of "Machine Learning with TensorFlow" by Nishant Shukla:

https://www.manning.com/books/machine-learning-with-tensorflow

To run the app install Docker and give the following commands:

docker pull ziaukhan/learn-tensorflow-keras:assignment3

docker container run -it --name assignment2 -p 8888:8888 ziaukhan/learn-tensorflow-keras:assignment3

Docker repo:

https://hub.docker.com/r/ziaukhan/learn-tensorflow-keras/tags/


If you are working with the git repo only:

To edit the notebook just pull this code and come to this directory and run this command:
docker run -it -p 8888:8888 -v $(pwd)/notebooks:/notebooks  tensorflow/tensorflow:latest-py3

To build a image from git repo:

docker image build -t ziaukhan/learn-tensorflow-keras:assignment3 .

