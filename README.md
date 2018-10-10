# IoTIntelli

Does your business know who is looking at your products in the store and how long? Are you showing the same set of products on digital displays for every customer?

This project will help businesses to better understand their customers behavior's in real world. It uses face detection to estimate gender and calculate time spent looking at the products in the store. It will be helpful for businesses to capture analytics from real world. It also exchanges the data in real time to take actions to helo your customers to make a purchase decision. Or show right ad on digital displays based on who is looking at the display.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. You can test this on your laptop or on your RaspberryPi or any microcontroller.

### Prerequisites

1. RaspberryPi or use your laptop
2. Install Python3. You can use Homebrew to install. 

```
brew install python
python -V
```

### Installing

1. Create virital environment to isolate dependencies for this project
    python3 -m venv /your-path
2. Launch virital environment created
    source /your-path/bin/activate
3. Clone this repository
   git clone https://github.com/epalakollu/IoTIntelli.git
4. Install dependencies
   cd IoTIntelli
   pip install -r requirements.txt
   pip install picamera
5. If no errors, extract pre-trained model. use gzip or gunzip. validate that face_recognizer_gender.yml present in ./src/product_analytics/data folder.
   gunzip ./src/product_analytics/data/face_recognizer_gender.yml.gz
6. Optionally install these dependencies if problem occurs in processing data
    sudo apt-get update
    sudo apt-get install libhdf5-dev
    sudo apt-get update
    sudo apt-get install libhdf5-serial-dev
    sudo apt install libqtgui4
    sudo apt install libqt4-test


## Running it on local

Open two windows and activate virtual environemnts
1. Run streaming detected faces data to consumers
    python src/product_analytics/stream-socket-events.py
2. Run detect faces and gender and push it to socket stream
    python src/product_analytics/detect-faces-gender.py


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [OpenCV](https://opencv.org/) - Open Source Computer Vision Library
* [Python](https://www.python.org/) - Written in Python


## Authors

* **Eswara Kumar** - (https://github.com/epalakollu)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
