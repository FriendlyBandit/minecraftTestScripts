import os
import shutil
import subprocess


def main():
    os.system("taskkill /f /im cmd.exe")
    os.system("taskkill /f /im java.exe")
    terms = ["world", "world_nether", "world_the_nether", "logs", "world_the_end"]
    cwd = os.getcwd()
    for x in terms:
        temp_cwd = cwd + "\\" + x
        shutil.rmtree(temp_cwd, ignore_errors=True, onerror=None)
    batch_path = cwd + "\\launch.bat"
    subprocess.call(batch_path)


main()
