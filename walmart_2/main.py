from datetime import datetime
import upload_data
import time
import get_data
def main(statu):
    data_recode=''
    run_time=1

    while statu:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("RumTime:", run_time, "||", "current_time:", current_time)
        run_time=run_time+1
        #time stamp
        new_recode= get_data.processed_data()
        if data_recode!= new_recode:
            data_recode= new_recode
            #check it items changed and update
            upload_data.upload()
            #gettoken/upload
            # print('item info updated')
        else:
            # print('nothing happened')
            pass
        time.sleep(600)
        #stop for 10 min