import ReadData
import DrawGraph
import subprocess

def run():
#ターミナルコマンド
    cmd = "ls"
    subprocess.call(cmd, shell=True)

#データ読み込みと集計、結果をCSVで出力
    rawdatafiles = ReadData.rawfilelisting("../data/updates/YoutubePakistan/")
    #ReadData.readupdatedata(rawdatafiles)

#データチェック
#    ReadData.checklink()
#    ReadData.checkupdate()

# CSVからグラフへ
    timerange = 60
    number_of_files = int(timerange / 15)
    DrawGraph.draw(number_of_files) #15分間分のファイル 4つ分読み込んでグラフへ

if __name__ == "__main__":
    run()