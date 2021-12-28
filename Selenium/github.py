# 1st file: install git
import os
result = os.system("git --version")
if result == 1:
##    import os
##    os.system("py -m pip install selenium")
##    os.system("py -m pip install webdriver-manager")
##    from selenium import webdriver
##    from webdriver_manager.chrome import ChromeDriverManager
##    driver = webdriver.Chrome(ChromeDriverManager().install())
##
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome('chromedriver')

    
    import platform
    if platform.system() == 'Windows':
        driver.get('https://git-scm.com/download/win')
        if platform.machine().endswith('64'):
            driver.implicitly_wait(3)
            # launch git bash
            driver.find_element(By.LINK_TEXT, '64-bit Git for Windows Setup').click()  

# 2nd file: set up user and commit
'git config --global user.email "hafiz071197@gmail.com"'
'git config --global user.name "gucky0'"

##repo = r"C:\Users\PeakV\Downloads\Python"
##
##commit_message = "add star array files to github"
##os.chdir(repo)
##
##line2 = "git init" # to undo: rmdir /s .git
##line3 = "git status"
##line4 = "git add -A"
##line5 = f'git commit -m "{commit_message}"'
##line6 = "git remote add origin https://github.com/gucky0/Star"
##line7 = "git remote -v"
##line8 = "git push -f origin main" # git show-ref then use master if needed
##
##def osu(line):
##    os.system(line + " & pause")
##
##lines = [var for var in dir() if not var.startswith("__") and var not in ("os", "osu", "repo", "commit_message")]
##
##for line in lines:
##    osu(locals()[line])
