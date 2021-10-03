import time
import pathlib
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.164 '
                  'Safari/537.36',
}

cookie = {
    '_uuid': 'AB5A6FFA-7965-34F8-191E-A6CABDC176D286439infoc',
    'buvid3': '55A79A46-C249-4390-93EE-F51B1A4A19D1148827infoc',
    'fingerprint': 'b70b18c4c28cbaaaa2c51cfa2643b66e',
    'buvid_fp': '5F0C73BC-B75F-4ECA-AE85-1138C4329C23167613infoc',
    'buvid_fp_plain': '5F0C73BC-B75F-4ECA-AE85-1138C4329C23167613infoc',
    'PVID': '1',
    'CURRENT_FNVAL': '80',
    'SESSDATA': '8b7108c1%2C1642886233%2Cd4a44%2A71',
    'bili_jct': '63c72b06aa405872c8b70fa494678d9a',
    'DedeUserID': '328456121',
    'DedeUserID__ckMd5': 'dffc4f0440137ad2',
    'sid': '4igjj519',
    'dy_spec_agreed': '1',
    'bp_video_offset_328456121': '556708000141032013',
    'bp_t_offset_328456121': '552696251588082979',
    'blackside_state': '1'
}
wishper_url = 'http://api.vc.bilibili.com/web_im/v1/web_im/send_msg'
fetch_url = 'http://api.bilibili.com/x/space/arc/search'
comment_url = 'http://api.bilibili.com/x/v2/reply/add'
PATH = str(pathlib.Path(__file__).parent.resolve())
UID=1563773517
DEV_ID='15DDF831-B3EE-406B-9447-44160F7BEE0B'