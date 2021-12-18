import requests
params = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
cookie = {
    '_uuid':"96E7A30A-4822-6409-F108-31E5DC641E0342892infoc",
    'bili_jct':"5d12b8c61493f0474a0d74d233169326",
    'blackside_state':"1",
    'bp_t_offset_1563773517':"551788871026588328",
    'bp_video_offset_1563773517':"550628615668125762",
    'buvid_fp':"671B0D27-9731-48B2-A3F5-4DF19FFA5AEE148820infoc",
    'buvid_fp_plain':"671B0D27-9731-48B2-A3F5-4DF19FFA5AEE148820infoc",
    'buvid3':"671B0D27-9731-48B2-A3F5-4DF19FFA5AEE148820infoc",
    'CURRENT_FNVAL':"80",
    'DedeUserID':"1563773517",
    'DedeUserID__ckMd5':"755ab0e9916b515d",
    'fingerprint':"44d3ac61ffdddac43da69f11769c3f5f",
    'fingerprint_s':"8b3628065c3c57ec0b7e681280a14fcb",
    'fingerprint3':"311199732a2b6be4593eab5bd94e75be",
    'LIVE_BUVID':"AUTO9516268081923349",
    'PVID':"1",
    'rpdid':"|(ukkm~J)mum0J'uYk~|Rm|RR",
    'SESSDATA':"cb3a2f81,1642359109,65bbc*71",
    'sid':"l8k3bm9h"
}
reply = requests.get("https://api.bilibili.com/x/msgfeed/unread",params=params, cookies=cookie).text
print(reply)
