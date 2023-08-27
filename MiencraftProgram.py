import os
import git
from git import Repo, Remote
# instancePath = input("Enter the Mods Instance Path!")
import zipfile
instanceDir = ""
workingDir = "E:\\Testcase"


def clonerepo():
    git.Repo.clone_from('https://github.com/Devoodie/Madlib.git', workingDir, branch="main")


def unzip():
    with zipfile.ZipFile(workingDir+"\\mods.zip") as mods:
        mods.extractall(instanceDir)


def main():
    try:
        clonerepo()
    except git.GitCommandError:
        print("repo found in directory!")
        repo = git.Repo.init(workingDir)
        origin = repo.remote()
        origin.fetch()


if __name__ == '__main__':
    main()
