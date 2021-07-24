from datetime import datetime
from event import Event
#直近1分間および直近1時間の累積カウントを記録する
#例えば、帯域幅の仕様譲許を確認するのに使える
class MinuteHourCounter:
    def __init__(self):
        self.events = []
         
    #新しいデータ点を追加する（count>=0)
    #それから1分間は、miniute_count()の返す値が+countだけ増える
    #それから1時間は、hour_count()の返す値が+countだけ増える
    def add(self, count:int):
        self.events.append(Event(count, time=datetime.now().timestamp()))
         

    #直近60秒間の累積のカウントを返す
    def minute_count(self):
         pass

    #直近3600秒間の累積カウントを返す
    def hour_count(self):
         pass