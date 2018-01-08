import Mods.env
import os
import shutil
import subprocess

def find_version ():
    if os.path.exists(Mods.env.launcher_preferenses_mac):
        file = open(os.path.join(Mods.env.launcher_preferenses_mac, Mods.env.launcher_preferenses_file))
    else:
        file = open(os.path.join(Mods.env.launcher_preferenses_win, Mods.env.launcher_preferenses_file))

    for line in file:
        if "builds" in line:
            continue
        elif "Stable" in line:
            continue
        elif "ToolSet" in line:
            continue
        elif "build_type" in line:
            version = line[27:51]
            break
    file.close()
    return version


def mac_command_download():
    full_command_download = Mods.env.command_download + " " + Mods.env.download_folder + " " + Mods.env.tools_Stable_list[4] + " " + Mods.env.branch_info_list[0] + " > log.txt"
    print ("Downloading Started. Command: ", full_command_download)
    subprocess.call(full_command_download, shell=True)

def mac_command_install():
    subprocess.call(Mods.env.command_install, shell=True)

def win_cmd_download():
    subprocess.call(Mods.env.cmd_download, shell=True)

def win_cmd_install():
    subprocess.call(Mods.env.cmd_install, shell=True)

if os.path.exists(os.path.expanduser('~/Library/')):
    mac_command_install()
    mac_command_download()
else:
    win_cmd_download()

if os.path.exists(Mods.env.launcher_preferenses_mac):
    launcher_preferenses_file = os.path.join(Mods.env.launcher_preferenses_mac, Mods.env.launcher_preferenses_file)
    version = find_version()
    print("Application version: ", version)
else:
    launcher_preferenses_file = os.path.join(Mods.env.launcher_preferenses_win, Mods.env.launcher_preferenses_file)
    version = find_version()
    print("Application version: ", version)

if os.path.exists(Mods.env.launcher_folder):
    log = open("log.txt")
    for log_line in log:
        if version in log_line:
            print ("the same version")
        # else:
        #     Add ERROR
    log.close()
    os.remove("log.txt")
    print("log file removed")
    shutil.rmtree(Mods.env.download_folder)
    print("DAVATools folder removed")
    if os.path.exists(Mods.env.launcher_preferenses_mac):
        shutil.rmtree(Mods.env.launcher_preferenses_mac)
        print("Settings folder mac removed")
    else:
        shutil.rmtree(Mods.env.launcher_preferenses_win)
        print("Settings folder win removed")