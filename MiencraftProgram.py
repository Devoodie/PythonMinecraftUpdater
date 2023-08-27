import os
import git
import dearpygui.dearpygui as dpg
import zipfile
instanceDir = ""
workingDir = ""


def clonerepo():
    git.Repo.clone_from('https://github.com/BicBoiTaco/Codys-Perfect-Modpack.git', workingDir, branch="main")


def unzip():
    with zipfile.ZipFile(workingDir+"\\mods.zip") as mods:
        mods.extractall(instanceDir)


def main():
    try:
        clonerepo()
    except git.GitCommandError:
        print("repo found in directory!")
    finally:
        repo = git.Repo.init(workingDir)
        origin = repo.remote()
        origin.fetch()
        os.chdir(workingDir)
        os.system("git lfs pull")

if __name__ == '__main__':
    dpg.create_context()
    with dpg.window(width=600, height=100):
        def setinstance():
            global instanceDir
            instanceDir = dpg.get_value(input_txt1)

        def setworkingdir():
            global workingDir
            workingDir = dpg.get_value(input_txt2)
        input_txt1 = dpg.add_input_text(
            label="Instance Directory"
        )
        # The value for input_text2 will have a starting value
        # of "This is a default value!"
        input_txt2 = dpg.add_input_text(
            label="Script Directory",
            default_value=os.getcwd(),
        )
        button = dpg.add_button(tag="xmit", label="Submit!")
        dpg.set_item_callback(button, main)
        dpg.set_item_callback(input_txt1, setinstance)
        dpg.set_item_callback(input_txt2, setworkingdir)

    dpg.create_viewport(title="Christaphor's Mod Installer!", width=600, height=100)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
