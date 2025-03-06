# Two Tests
      There are two tests here one uses Visual Studio and Selenium with NUnit Testing, The second one uses Python and Selenium.
      Both need the Chrome Driver which is found on this website https://googlechromelabs.github.io/chrome-for-testing/
      Download using Curl -O https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.35/win64/chromedriver-win64.zip
      Then unzip to desired location.  You will need to know this path when editing the chrome driver path.
## C# and Visual Studio 
### Packages needed for Visual Studio
      - selenium.webdriver\4.29.0\
      - dotnetseleniumextras.waithelpers\3.11.0\
### Project needed for Visual Studio
      - NUnit Test Project
      - Login WebPage ( https://practicetestautomation.com/practice-test-login/ )
### Project Setup
      - Install Visual Studio
      - Download and unzip chrome driver
      - Make sure chrome is installed on system
      - Use one of two options
            Clone this repository and open the project in visual studio then change the driver path to where you stored it.
            Create a new Nunt project and copy over the code from the unit tests file.
            Make sure Nuget packages are installed and then run the tests.
            This uses a test login server https://practicetestautomation.com/practice-test-login/ to test.

## Python Selenium
### Packages need for Visual Studio
      - Selenium (pip install selenium)
      - The rest are built into python.
### Project Setup
      - Install Python
      - Make sure selenium is instaleld
      - Copy or clone pyton file
      - Run in python 3.13
