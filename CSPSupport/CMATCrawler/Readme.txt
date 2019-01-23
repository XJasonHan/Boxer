Requirement: Python version >= 3.6

Create virtual environment
1. Copy the folder to local
2. In cmd line locate to local folder
3. Run command as "python -m venv venv"
4. Run command as "venv\scripts\activate.bat" and get cmd line as "(venv) D:\Tyler\CMATCrawler>"
5. Run command as "pip3 install -r req.txt"

Get the cookies
1. Access CMAT portal with Chrome 
2. On page 'https://cmat.cp.partner.microsoftonline.cn/Customer/CustomerSearch', press F12 to call out the developer tools
3. Click 'Network' tab and check 'Name' column if there is 'CustomerSearch'.
4. If there is 'CustomerSearch' in step 3, click on it.
5. In tab 'Headers', locate to 'Request Headers' and copy all value of 'cookies'.
6. Open file 'Raw_cookies' and replace the content with your copy in step 5. save and close the file.

In virtual environment run the command as below to crawl data from CMAT
Run command as "python Main.py"