import ReadData
import DrawGraph
import subprocess

#MATRIX_SIZE = 1024

def run():
    #ターミナルコマンド
    cmd = "ls"
    subprocess.call(cmd, shell=True)
    #データ読み込み
    ReadData.readupdatedata()
    #CSVから集計

#    ReadData.checklink()
#    ReadData.checkupdate()
#    DrawGraph.draw()

if __name__ == "__main__":
    run()