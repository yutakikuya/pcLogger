import pyautogui as pa
import time
from pynput import mouse
import ctypes
from datetime import datetime

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0}'.format((x, y)))
# # Collect events until released
# with mouse.Listener(
# on_scroll=on_scroll) as listener:
#  listener.join()

if __name__=="__main__":
    f = open('text'+str(time.time())+'.csv', 'w') # 書き込みモードで開く
    one_sec_cnt = 0.0
    while True :
        time_ = time.time()
        clicked = False
        x,y = pa.position()
        left_click = ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000
        right_click = ctypes.windll.user32.GetAsyncKeyState(0x02) == 0x8000
        enter = ctypes.windll.user32.GetAsyncKeyState(0x0D) == 0x8000
        if left_click or right_click or enter:
            #スクリーンショット クリックした位置、時間付き
            img = pa.screenshot(
                imageFilename="time_"+str(time_)+"_pos_x_"+str(x)+"_pos_y_"+str(y)+".png"    # 保存先ファイル名
            )
            clicked = True
        #ログ出力
        if clicked == True:
            #f.writelines("time:"+str(time_)+",x:"+str(x)+",y:"+str(y)+",clicked:true\n")
            f.writelines(str(time_)+","+str(x)+","+str(y)+",true\n")
        else :
            if one_sec_cnt > 0.10:
                #不要なログ出力を避けるため0.1sec感覚のログを取得する
                f.writelines(str(time_)+","+str(x)+","+str(y)+",false\n")
                one_sec_cnt = 0.0
        if ctypes.windll.user32.GetAsyncKeyState(0x1B) == 0x8000:
            f.close()
            break

        one_sec_cnt += 0.01
        time.sleep(0.01)
