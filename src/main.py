import ReadData
import DrawGraph
import subprocess

#MATRIX_SIZE = 1024

def run():
    cmd = "ls"
    subprocess.call(cmd, shell=True)
    ReadData.readupdatedata()
#    ReadData.checklink()
#    ReadData.checkupdate()
#    DrawGraph.draw()

if __name__ == "__main__":
    run()