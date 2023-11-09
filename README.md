# CardToExcel

A web application that lets you automate guest lecture information extraction from invitation cards

## Installation

In order to run CardToExcel you will need the following dependencies
* Python3
* flask using pip3
* openpyxl using pip3
* Pillow using pip3
* Tesseract-OCR
* pytesseract using pip3

Instructions

* Create an empty directory and cd into it
```bash
mkdir CardToExcel 
cd CardToExcel
```
* Clone the repository
```bash
git clone --depth=1 https://github.com/ArnabBanik-repo/flyer-information-extractor/ .
```
* Install Tesseract-OCR on your system
  For windows: Save it in C:\Program Files (x86) 
  
* Install dependencies
```bash
  ./bin/pip3 install flask openpyxl pytesseract
```
* Run the server
```bash
  ./bin/python3 server.py
```
* Get sample Invitation Flyer images from Dataset_generator/dataset/images folder

In order to generate more Flyer samples, cd into the Dataset_generator directory and run the dataset_generator
```bash
  ./bin/python3 dataset_generator.py
```


## Authors
- [Arnab Banik](https://www.github.com/ArnabBanik-repo)
- [Aleena](https://www.github.com/a-leena)
- [Sneha Michelle V](https://www.github.com/Namslay26)
