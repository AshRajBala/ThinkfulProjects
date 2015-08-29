# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:21:21 2015

@author: AshRajBala
"""

"""
using Github
1. Created username and repository "ThinkfulProjects" here:
https://github.com/AshRajBala/ThinkfulProjects

2. Downloaded GitHub for Mac

3. Typed the following at the terminal:
git config --global user.name "AshRajBala"
git config --global user.email shunyata.aishwarya@gmail.com

cd /Users/AshRajBala/Repositories/ThinkfulProjects
git init

Terminal output: "Initialized empty git repository in /Users/AshRajBala/Repositories/Thinkfulprojects.git

git status #check where you are
"""

"""
MASTER BRANCH: A single repository can contain multiple branches, each containing a different version of the 
code. 
"""

"""
SAVING FILES: In git, saving a file requires two steps: 
1. Tell git to track the file (also called "adding");
2. Tell git to save the file (by "committing" it)
"""

"""
Place .py files in /Users/AshRajBala/Repositories/ThinkfulProjects
git add .
git commit -m "Initial commit"
git status
Terminal output (if successful commit): "Nothing to commit, working directory clean".
git remote add origin git@github.com:AshRajBala/ThinkfulProjects.git #Do this only once
git push origin master

For specific file (e.g. example.py; located at /Users/AshRajBala/Repositories/ThinkfulProjects)
At terminal (cd /Users/AshRajBala/Repositories/ThinkfulProjects; i.e. @ pwd), type:
git add example.py
git commit -m 'Create example.py'
git remote add origin git@github.com:AshRajBala/ThinkfulProjects.git #Do this only once
git push origin master
"""




