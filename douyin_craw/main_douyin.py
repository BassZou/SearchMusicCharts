
import requests,json,sys
import threading,time
from mongo import MyMongodb
sys.path.append('..')
from mUtils.datetimeUtil import TimeUtil


"""
爬取抖音音乐榜单的数据，并提交至mongo
"""

def rgBang():
    """热歌榜
    """
    headers = {
        'authority': 'creator.douyin.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    params = (('billboard_type', '5'),)
    response = requests.get('https://creator.douyin.com/aweme/v1/creator/data/billboard/', headers=headers, params=params)
    return json.loads(response.text) 
    

def bsBang():
    """飙升榜
    """
    headers = {
        'authority': 'creator.douyin.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36',
        'content-type': 'application/json',
        'origin': 'https://creator.douyin.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://creator.douyin.com/creator-micro/billboard/6',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'passport_csrf_token_default=5cf41db1256d1cbb7c794f99efe466d8; passport_csrf_token=5cf41db1256d1cbb7c794f99efe466d8; s_v_web_id=klqbcet9_Ab2776tz_xiaB_4KJl_9Qaw_4hZARtODeEFk; ttwid=1%7CiSLaSzPARdJ5k5RhLL3x4Dpbg7Z09pDGID1uh8_x2Vk%7C1614424650%7Cf28fc67a6ba431335f5ec9f4b3c04ccb19cd0aae21ba94a9af7279d61d0ac0a5; n_mh=Z7ojtuFqkH25mwvcnVwxcg1JLMzf5QseQphujSDoPfc; oc_login_type=LOGIN_PERSON; csrf_session_id=79668c8bac3c4de888e7618146c47fac; csrf_token=dTRsFKRUEZjQhAjxEbiDcvoMxrVWdLgV; MONITOR_WEB_ID=6cffb9b6-9750-4c79-b179-e4421ba0602f; odin_tt=09ec4c727a022284ecbe69f2b81192df1aaa1e5dcac236148fe685fb8e34c123525583de270134a6fd40a0fe2aa379bf; sso_uid_tt=f366ce6dabd8187420f0971c1c22e80f; sso_uid_tt_ss=f366ce6dabd8187420f0971c1c22e80f; toutiao_sso_user=16744682c2e4280f67e20aba313accad; toutiao_sso_user_ss=16744682c2e4280f67e20aba313accad; passport_auth_status=836a66e0750b49249db92c2e3e7e535f%2C48f11a5479efa2f0d3380e3cb8d139e3; passport_auth_status_ss=836a66e0750b49249db92c2e3e7e535f%2C48f11a5479efa2f0d3380e3cb8d139e3; sid_guard=0950db366301fcfb8ad65e918b7931a3%7C1614746815%7C5184000%7CSun%2C+02-May-2021+04%3A46%3A55+GMT; uid_tt=ba204bc28cead57af38fdf3c4fa91a73; uid_tt_ss=ba204bc28cead57af38fdf3c4fa91a73; sid_tt=0950db366301fcfb8ad65e918b7931a3; sessionid=0950db366301fcfb8ad65e918b7931a3; sessionid_ss=0950db366301fcfb8ad65e918b7931a3; tt_scid=z9TcLz9v0oa7lBx7c28kORmY0rqUyty6E7HGW2vZOsZj8m3RFY-qTRnttYnOBkNG75a2',
    }

    params = (
        ('aid', '2906'),
    )

    data = '{"page":1,"page_size":50,"billboard_type":6}'

    response = requests.post('https://creator.douyin.com/aweme/v1/creator/data/v2/billboard_detail/', headers=headers, params=params, data=data)
    return json.loads(response.text) 
    

def ycBang():
    """原创榜
    """
    headers = {
        'authority': 'creator.douyin.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36',
        'content-type': 'application/json',
        'origin': 'https://creator.douyin.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://creator.douyin.com/creator-micro/billboard/7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'passport_csrf_token_default=5cf41db1256d1cbb7c794f99efe466d8; passport_csrf_token=5cf41db1256d1cbb7c794f99efe466d8; s_v_web_id=klqbcet9_Ab2776tz_xiaB_4KJl_9Qaw_4hZARtODeEFk; ttwid=1%7CiSLaSzPARdJ5k5RhLL3x4Dpbg7Z09pDGID1uh8_x2Vk%7C1614424650%7Cf28fc67a6ba431335f5ec9f4b3c04ccb19cd0aae21ba94a9af7279d61d0ac0a5; n_mh=Z7ojtuFqkH25mwvcnVwxcg1JLMzf5QseQphujSDoPfc; oc_login_type=LOGIN_PERSON; csrf_session_id=79668c8bac3c4de888e7618146c47fac; csrf_token=dTRsFKRUEZjQhAjxEbiDcvoMxrVWdLgV; MONITOR_WEB_ID=6cffb9b6-9750-4c79-b179-e4421ba0602f; odin_tt=09ec4c727a022284ecbe69f2b81192df1aaa1e5dcac236148fe685fb8e34c123525583de270134a6fd40a0fe2aa379bf; sso_uid_tt=f366ce6dabd8187420f0971c1c22e80f; sso_uid_tt_ss=f366ce6dabd8187420f0971c1c22e80f; toutiao_sso_user=16744682c2e4280f67e20aba313accad; toutiao_sso_user_ss=16744682c2e4280f67e20aba313accad; passport_auth_status=836a66e0750b49249db92c2e3e7e535f%2C48f11a5479efa2f0d3380e3cb8d139e3; passport_auth_status_ss=836a66e0750b49249db92c2e3e7e535f%2C48f11a5479efa2f0d3380e3cb8d139e3; sid_guard=0950db366301fcfb8ad65e918b7931a3%7C1614746815%7C5184000%7CSun%2C+02-May-2021+04%3A46%3A55+GMT; uid_tt=ba204bc28cead57af38fdf3c4fa91a73; uid_tt_ss=ba204bc28cead57af38fdf3c4fa91a73; sid_tt=0950db366301fcfb8ad65e918b7931a3; sessionid=0950db366301fcfb8ad65e918b7931a3; sessionid_ss=0950db366301fcfb8ad65e918b7931a3; tt_scid=bBRHSoj.0SYjhw4Pc7WJZ8zN00-v.s3UZrktuzR-CY4jXmfjQppbKnONhPGj-Syd4843',
    }

    params = (
        ('aid', '2906'),
        ('app_name', 'aweme_creator_platform'),
        ('device_platform', 'web'),
        ('referer', 'https://creator.douyin.com/'),
        ('user_agent', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36'),
        ('cookie_enabled', 'true'),
        ('screen_width', '400'),
        ('screen_height', '1241'),
        ('browser_language', 'zh-CN'),
        ('browser_platform', 'MacIntel'),
        ('browser_name', 'Mozilla'),
        ('browser_version', '5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36'),
        ('browser_online', 'true'),
        ('timezone_name', 'Asia/Shanghai'),
        ('_signature', '_02B4Z6wo02901j0Rl8gAAIDADUegXcqjDQI9BJNAAO-KntLMt4l.iZDIFN77vDSpdEfei8XRXFWGZDcO2rV6ra8ysjGfodXVwul7g5Zy377MsVkvRvlQ4e9ALHWzRmub772GbfFa51wO-Nao27'),
    )
    data = '{"page":1,"page_size":50,"billboard_type":7}'
    response = requests.post('https://creator.douyin.com/aweme/v1/creator/data/v2/billboard_detail/', headers=headers, params=params, data=data)
    return json.loads(response.text) 


def start():
    timer = threading.Timer(3601, start) 

    datetime = TimeUtil().get_datetime()
    mydb = MyMongodb()
    print(datetime,'请求热歌榜')
    for item in rgBang()['billboard_data']:
        item['time'] = datetime
        item['ranking'] = '热歌榜'
        mydb.post(item)

    time.sleep(5)
    print(datetime,'请求飙升榜')

    for item in bsBang()['billboard_data']['element_list']:
        item['time'] = datetime
        item['ranking'] = '飙升榜'
        item['rank'] = item['base_data']['rank']
        item['title'] = item['base_data']['title']
        item['author'] = item['base_data']['author']
        item['value'] = item['statistics_data']['hot_value']
        item['duration'] = item['base_data']['duration']
        item['link'] = item['base_data']['link']
        mydb.post(item)
    
    time.sleep(5)
    print(datetime,'请求原创榜')

    for item in bsBang()['billboard_data']['element_list']:
        item['time'] = datetime
        item['ranking'] = '原创榜'
        item['rank'] = item['base_data']['rank']
        item['title'] = item['base_data']['title']
        item['author'] = item['base_data']['author']
        item['value'] = item['statistics_data']['hot_value']
        item['duration'] = item['base_data']['duration']
        item['link'] = item['base_data']['link']
        mydb.post(item)
    
    print(datetime,'完成插入')
    timer.start()


if __name__ == '__main__':
    start()

    

"""热歌榜
curl 'https://creator.douyin.com/aweme/v1/creator/data/billboard/?billboard_type=5' \
  -H 'authority: creator.douyin.com' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'cookie: passport_csrf_token_default=5cf41db1256d1cbb7c794f99efe466d8; passport_csrf_token=5cf41db1256d1cbb7c794f99efe466d8; s_v_web_id=klqbcet9_Ab2776tz_xiaB_4KJl_9Qaw_4hZARtODeEFk; ttwid=1%7CiSLaSzPARdJ5k5RhLL3x4Dpbg7Z09pDGID1uh8_x2Vk%7C1614424650%7Cf28fc67a6ba431335f5ec9f4b3c04ccb19cd0aae21ba94a9af7279d61d0ac0a5; odin_tt=79b2825f48f7f68f7d725d1fdbf548012e0160b3cb75e5893ee88f73ec4c95cf1ca590fb0b690f43ea89a4472cb9c2c9; n_mh=Z7ojtuFqkH25mwvcnVwxcg1JLMzf5QseQphujSDoPfc; sso_uid_tt=7690616ad2150d143f1cca819556f418; sso_uid_tt_ss=7690616ad2150d143f1cca819556f418; toutiao_sso_user=d2c4899f381cc65ce426194c51b500de; toutiao_sso_user_ss=d2c4899f381cc65ce426194c51b500de; passport_auth_status=48f11a5479efa2f0d3380e3cb8d139e3%2C; passport_auth_status_ss=48f11a5479efa2f0d3380e3cb8d139e3%2C; sid_guard=47746a5be183e0d63087ae966846c5ce%7C1614586907%7C5184000%7CFri%2C+30-Apr-2021+08%3A21%3A47+GMT; uid_tt=a8e2ed7749c846e1e5385ae188a3f369; uid_tt_ss=a8e2ed7749c846e1e5385ae188a3f369; sid_tt=47746a5be183e0d63087ae966846c5ce; sessionid=47746a5be183e0d63087ae966846c5ce; sessionid_ss=47746a5be183e0d63087ae966846c5ce; oc_login_type=LOGIN_PERSON; csrf_session_id=79668c8bac3c4de888e7618146c47fac; csrf_token=dTRsFKRUEZjQhAjxEbiDcvoMxrVWdLgV; MONITOR_WEB_ID=640ea584-5d83-4c8b-8173-dce7ae638dec; tt_scid=xEnJwWZqfShFzantdryjfeBxD-MBKyhCGgJX4SX86trk82JkPrDaV7GsnaXlrXHRfc22' \
  --compressed


  curl 'https://creator.douyin.com/aweme/v1/creator/data/billboard/?billboard_type=5' \
  -H 'authority: creator.douyin.com' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  --compressed
"""

"""飙升榜
curl 'https://creator.douyin.com/aweme/v1/creator/data/v2/billboard_detail/?aid=2906' \
  -H 'authority: creator.douyin.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36' \
  -H 'content-type: application/json' \
  -H 'origin: https://creator.douyin.com' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://creator.douyin.com/creator-micro/billboard/6' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'cookie: passport_csrf_token_default=5cf41db1256d1cbb7c794f99efe466d8; passport_csrf_token=5cf41db1256d1cbb7c794f99efe466d8; s_v_web_id=klqbcet9_Ab2776tz_xiaB_4KJl_9Qaw_4hZARtODeEFk; ttwid=1%7CiSLaSzPARdJ5k5RhLL3x4Dpbg7Z09pDGID1uh8_x2Vk%7C1614424650%7Cf28fc67a6ba431335f5ec9f4b3c04ccb19cd0aae21ba94a9af7279d61d0ac0a5; n_mh=Z7ojtuFqkH25mwvcnVwxcg1JLMzf5QseQphujSDoPfc; oc_login_type=LOGIN_PERSON; csrf_session_id=79668c8bac3c4de888e7618146c47fac; csrf_token=dTRsFKRUEZjQhAjxEbiDcvoMxrVWdLgV; MONITOR_WEB_ID=6cffb9b6-9750-4c79-b179-e4421ba0602f; odin_tt=09ec4c727a022284ecbe69f2b81192df1aaa1e5dcac236148fe685fb8e34c123525583de270134a6fd40a0fe2aa379bf; sso_uid_tt=f366ce6dabd8187420f0971c1c22e80f; sso_uid_tt_ss=f366ce6dabd8187420f0971c1c22e80f; toutiao_sso_user=16744682c2e4280f67e20aba313accad; toutiao_sso_user_ss=16744682c2e4280f67e20aba313accad; passport_auth_status=836a66e0750b49249db92c2e3e7e535f%2C48f11a5479efa2f0d3380e3cb8d139e3; passport_auth_status_ss=836a66e0750b49249db92c2e3e7e535f%2C48f11a5479efa2f0d3380e3cb8d139e3; sid_guard=0950db366301fcfb8ad65e918b7931a3%7C1614746815%7C5184000%7CSun%2C+02-May-2021+04%3A46%3A55+GMT; uid_tt=ba204bc28cead57af38fdf3c4fa91a73; uid_tt_ss=ba204bc28cead57af38fdf3c4fa91a73; sid_tt=0950db366301fcfb8ad65e918b7931a3; sessionid=0950db366301fcfb8ad65e918b7931a3; sessionid_ss=0950db366301fcfb8ad65e918b7931a3; tt_scid=z9TcLz9v0oa7lBx7c28kORmY0rqUyty6E7HGW2vZOsZj8m3RFY-qTRnttYnOBkNG75a2' \
  --data-raw '{"page":1,"page_size":50,"billboard_type":6}' \
  --compressed
"""

"""原创榜
 curl 'https://creator.douyin.com/aweme/v1/creator/data/billboard/?billboard_type=7' \
  -H 'authority: creator.douyin.com' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  --compressed
"""

