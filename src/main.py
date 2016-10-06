import ReadData
import DrawGraph
import subprocess

#MATRIX_SIZE = 1024

def run():
#ターミナルコマンド
    cmd = "ls"
    subprocess.call(cmd, shell=True)

#データ読み込みと集計、結果をCSVで出力
    #ReadData.readupdatedata()

#データチェック
#    ReadData.checklink()
#    ReadData.checkupdate()


# CSVからグラフへ
    DrawGraph.draw()

if __name__ == "__main__":
    run()