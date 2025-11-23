# NOTY, Namer Of The Year

As you probably know, in Ferdowsi Univesity of Mashhad, all courses that are instructed by Professor Majid Mirzavaziri, follow a very strict set of rules. Especially for naming assignment files.

This repository contains a simple Python script that will help with chunking files, and naming them while considering the **current jalali date** and **the latest named file**.

## Installation

This Project is very lightweight and only uses two dependencies, therefore, the installation process is straight forward.

### 1. Clone the Repository
```bash
git clone https://github.com/erfanrajati/NOTY-namer-of-the-year.git
```
### 2. Install Dependencies
```bash
cd NOTY-namer-of-the-year
python -m pip install -r ./requiments.txt
```
### 3. Adjust the name format in `organizer.py`
The name of the files must include your name, lastname, course indicator and file type!

For example, for me, the constant will be as follows

```python
# organizer.py line 6
NAME_FORMAT = "Rajati.Erfan.cap.cn.%s.%s.%s.pdf"
```

The latest naming format (On Nov 2025) is
```
last_name.first_name.course_indicator.file_type.count.month.day.pdf
```
You must refer to your course description (gotten from Prof. Mirzaviziri himself) for the details.

### 4. Run the program and Enjoy ⭐

## Usage
The recommended usage flow of this program is rather simple and is explained below.

### 1. Scan your assignments
The best way of doing this is by using CamScanner which is very suitable for this action. [Download from official website](https://www.camscanner.com/). You can also use any other scanner you want, but make sure the scan is exported **in PDF format**.

### 2. Use the splitter (even if there is only one page)
Place your pdf scan in assets directory and run the splitter file.
```bash
python splitter.py
```
The script will prompt you into choosing the file name and chunk size. After the script is completed, you'll see your chunked PDFs in the repository root directory, named with positive integers. (1.pdf, 2.pdf, etc.)

**Note: If your file should not be splitted into equal sized chunks, you can skip this step and use online PDF organizers instead. But Make sure before running step 3, your files are all named by Possitive Integers in order and placed in repository root directory.**

### 3. Run the organizer
Before this step, make sure your have completed **Step 3 of Installation**. Then, simply run the script and watch your pain go away as the files are named peacefully one by one!
```bash
python organizer.py
```

## Contribution
Your contribution to this small project is highly appreciated. My suggestions for improvements are listed below. In case you have your own ideas for improvement, contact me on my LinkedIn profile, linked in my Github profile.

1. Code Refactor: Since the code is a mess, cleaning it is very much needed.
2. Dynamic Chunking Feature: It'd be very cool if the splitter could also chunk the pdf into dynamic (and not fixed) ranges.
3. The list will be updated based on feedbacks.

In case you were interested, you need to fork the repo on your own Github profile, create a branch for your feature and then push the changes to mine, I'll review and respond to your changes as soon as I could.

---

**Sincerely, Erfan Rajati**
