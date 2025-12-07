#Hoemwork 1 + 2 Review
# 1. Git vs GitHub: Git is the tool on my computer that tracks changes in my files. GitHub is the website where I store or share those repos online.

# 2. Terminal vs Command Line: The terminal is the actual app I open, and the command line is the place inside it where I type stuff.

# 3. Local vs Remote Repository:  Local repo is the version saved on my own laptop. Remote repo is the one saved on GitHub or another server.

# 4. Version Control: Version control is just a system that lets me keep track of changes and go back to older versions if I mess something up.

# 5. Staging Area: The staging area is where Git holds the changes I picked before I commit them.

# 6. git add: git add tells Git which files I want to move into the staging area.

# 7. git commit: git commit saves a snapshot of whatever I staged with a message explaining the change.

# 8. git push:git push sends my commits from my laptop to the remote repo on GitHub.

# 9. git status: git status shows me what’s changed, what’s staged, and what Git isn’t tracking yet.

# 10. git pull: git pull grabs the newest changes from GitHub and tries to merge them into my local repo.

# 11. pwd: pwd prints the folder I’m currently in (I always forget this one lol).

# 12. ls: ls lists all files and folders in the directory I’m in.

# 13. cd: cd moves me into a different directory I name.

# 14. nano: nano opens a tiny text editor right in the terminal so I can edit a file fast.

# 15. touch: touch makes a new empty file or updates an old one’s timestamp (kinda weird but useful).

# 16. mv: mv moves or renames a file. Easy command but easy to mess up too.

# 17. rm: rm deletes a file for real, not like send-to-trash delete, so I gotta be careful.

# 18. cat: cat prints out the contents of a file so I can read it quickly in the terminal.


#HOMEWORK 3.2 Directory Tree: 
#You have been plopped into Judy’s directory system. What command shows your current directory?
# pwd

#Terminal says I'm in ~/python decal/judy decal. What command lists all files there?
# ls

#Brianna fixed a typo in homework.py and I need to pull the updated version. 
# First I’d move into the brianna repo, then pull: cd brianna_repo   (or whatever the real folder name is)
# git pull origin main

#How would I move the new homework.py into my own homework/ folder?
# mv homework.py ~/my_repo/homework/

#How would I move myself to the same repo as homework.py?
# cd ~/my_repo/homework/

#I want to see the contents of homework.py in the terminal. How do I do that?
# cat homework.py

#I finished the homework. What commands let me save changes and push to GitHub?
# git add .
# git commit -m "finished my homework"
# git push origin main

#Git error: 
#  [rejected] main -> main (fetch first)
# What commands fix this, and what does it mean?
# git pull origin main

# fix any merge conflicts if needed: git push origin main
# The error means the remote repo has changes I dont have yet, so Git wont let me push until I pull and sync everything.

#What absolute path lets me move to Recents/?
# cd /Users/judy/Recents/



#4.1) Data Types
value = 3.14
def checkDataType(value):
    return type(value).__name__
print(checkDataType(value))

# 4.2 Conditionals

n = 7
def evenOrOdd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
print(evenOrOdd(n))

# 5 Loops
#Self reminder: DON'T use sum() function ~~

numbers = [1, 2, 3, 4, 5]
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sumWithLoop(numbers))


#HOMEWORK 4 REVIEW

# 6.1 Lists::
lst = (['a', 'b', 'c'])
def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list
print(duplicateList(lst))


# 6.2 Debugging:
num = 4
def square(num): #The error was that the code was missing ":" ar the end of this line
    return num * num
print(square(num))

#To call My favorite function
print(duplicateList(lst))
#&
print(square(num))

