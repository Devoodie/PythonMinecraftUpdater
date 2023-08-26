import os
import git
from git import Repo, Remote

# instancePath = input("Enter the Mods Instance Path!")

repo = git.Repo.init("E:\\Testcase")
def clonerepo():
    git.Repo.clone_from('https://github.com/Devoodie/Madlib.git', "E:\\Testcase", branch="master")


if __name__ == '__main__':
    def main():
        clonerepo()
