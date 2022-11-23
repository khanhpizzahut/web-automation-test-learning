Welcome to QA team
-----------------

S1. install Python and setup path env (cmd: open .zprofile)

https://www.python.org/downloads/

S2. Install Pycharm Community:

https://www.jetbrains.com/pycharm/download/#section=mac

S3: Open project with Pycharm

S4: Add more Python interpreter:
* selenium
* pytest
* ConfigArgParse
* Openpyxl
* logger
* pip

<img width="978" alt="Screen Shot 2022-11-15 at 10 19 22 PM" src="https://user-images.githubusercontent.com/79838962/201956604-3179bf7d-646f-4c1d-acc4-5e6029519bef.png">

S5: Setup project run with pytest
<img width="975" alt="Screen Shot 2022-11-15 at 10 21 26 PM" src="https://user-images.githubusercontent.com/79838962/201958375-e521b43f-4204-425b-b34b-7b9d8e5cd25b.png">

S6: Make sure version chrome is `Version 107.0.5304.110 (Official Build) (x86_64)`
If not, please update new driver base on chrome version

<img width="402" alt="Screen Shot 2022-11-15 at 10 52 45 PM" src="https://user-images.githubusercontent.com/79838962/201964853-0957d71f-2a06-494d-9ce0-58e2a30d55e7.png">

S7: Open ``Terminal`` and do command line
* CD to folder testcases: path base on your pc

cd ...TestCases/Website/JP
-
* Run all testcases on this folder

python -m pytest 
-
OR

python3 -m pytest
-
If you have any question, please contact to `khanh.pham@yum.com`
