from core.result_base import ResultBase
from api.user import user
from common.logger import logger


def get_all_user_info():
    """
    获取全部用户信息
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = user.list_all_users()
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    return result


def get_one_user_info(username):
    """
    获取单个用户信息
    :param username:  用户名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = user.list_one_user(username)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "查询用户 ==>> 接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("查看单个用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def register_user(username, password, telephone, sex="", address=""):
    """
    注册用户信息
    :param username: 用户名
    :param password: 密码
    :param telephone: 手机号
    :param sex: 性别
    :param address: 联系地址
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "username": username,
        "password": password,
        "sex": sex,
        "telephone": telephone,
        "address": address
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.register(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def login_user(username, password):
    """
    登录用户
    :param username: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = {
        "username": username,
        "password": password
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = user.login(data=payload, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
        result.token = res.json()["login_info"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def update_user(id, admin_user, new_password, new_telephone, token, new_sex="", new_address=""):
    """
    根据用户ID，修改用户信息
    :param id: 用户ID
    :param admin_user: 当前操作的管理员用户
    :param new_password: 新密码
    :param new_telephone: 新手机号
    :param token: 当前管理员用户的token
    :param new_sex: 新性别
    :param new_address: 新联系地址
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }
    json_data = {
        "admin_user": admin_user,
        "password": new_password,
        "token": token,
        "sex": new_sex,
        "telephone": new_telephone,
        "address": new_address
    }
    res = user.rank(id, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("修改用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def delete_user(username, admin_user, token):
    """
    根据用户名，删除用户信息
    :param username: 用户名
    :param admin_user: 当前操作的管理员用户
    :param token: 当前管理员用户的token
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "admin_user": admin_user,
        "token": token,
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.delete(username, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("删除用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

def get_rank(activityId, timestamp):
    logger.info(f"activityId:{activityId},timestamp:{timestamp}")

    """
    登录用户
    :param activityId: 活动id
    :param timestamp: 时间戳
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {
        'Host': 'ppg.viviv.com',
        'Cookie': 'odid=A21BB374-E7EB-4589-BF08-332B29CABFEF; lon=; kpf=IPHONE; power_mode=0; foreign=0; darkMode=false; isp=CMCC; token=c6ffc111d52c4bc284fad0a1f70e91a7-1281010042; browseType=4; appver=12.6.51.8850; thermal=10000; ll_client_time=1722991613823.773; cdid_tag=7; cdidTag=7; mcc=46000; session_id=0D4FB732-03CD-4BDF-9AA9-F7728C0D7D1F; weblogger_switch=; os=17.5.1; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAfwo-PX0gs0UL6MotAKp2kpz4JwBc1FOY6C8rVK4dnxWmuLasJQrDkO_TuGd3O_etnJRYknPKJ0SbLe-JhF1cw0SVAAZZwbGmcIY5evS8o3Ebowrn5_4_6jDNLsRTY43dEgG4vGwzPIC0HYH4h9EUHy9AWXFK2LSp1AqmXFP_uZGaBrBc3RV2J5xRupPSLAcmlGh1fnDowxrcJUdLC9VUTMaEtIXc_XUTivPxSOZo8JjD5AnfSIg2mOXGtvbhVQVcu16nVk7iw_ito8xRKLnPcnYtlDQLOAoBTAB; userId=1281010042; sh=2796; grant_browse_type=AUTHORIZED; c=a; oDid=A21BB374-E7EB-4589-BF08-332B29CABFEF; ud=1281010042; lat=; egid=DFPC43138E687D971C2452E56E14F2AE5EA60EABBA5C4CFB198CD63A664DB608; sid=0D4FB732-03CD-4BDF-9AA9-F7728C0D7D1F; pUid=qQYF2asB8NX4GS3tLzpaJMcoQbnT4_44e6155bec62ae8bb; ver=12.6; global_id=DFPC43138E687D971C2452E56E14F2AE5EA60EABBA5C4CFB198CD63A664DB608; kpn=KUAISHOU; net=WIFI; cl=0; __NSWJ=; country_code=cn; ftt=; lkvr=MDVEQTE0QUYtRUJGO2iXUXDdtRWokxVqqzk9jJ8Admz_nwouEcKguox3e0VllqhMukU4MQ; deviceBit=0; randomDid=A21BB374-E7EB-4589-BF08-332B29CABFEF; kuaishou.sixin.login_st=ChdrdWFpc2hvdS5zaXhpbi5sb2dpbi5zdBKgAZRBCxwJJVYsJYoXxGJmo8t5O_SoWEfjQNUUl5WmogQpdskg7BR0Vwzcz0RM4KyyOkSO7ymClUYAlTOxtx5vFW6F1enDmpn6d8p3Kdr99Vp-pWTDWDePCzLs1Zcf6S-PfDRA7B6kRZdLxyW27VZdJZMEUb0M6t8tyHd3DMfHbuo-C2ijp16mx7-Cs5dqW_NUhGdlYcjAKjv-0cr3wigcZwgaEuC4KMyhe0K_rKZl3x6y16o84yIgbgWnCJNeWW22OeKCTQ6ziMeAN0-0t65dzeGsbsgaf_EoBTAB; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAFPIjcfN0zPaD0cN-hTYOv51CXviamd5C7mG1wUMCyDXe9SmaKultj7Ooalcy13I4MyCgfI5xVTuJ84axjLIo5jCCHCvA1leH2TaHAEiqw-wZEhdSNd65IRvE7r7u5IrezIO25ZZOz1ewJK8iY1gYdzGCUhRBuAAX0zmQM_XYYGa1H-mr_DKyFztDGcpDaoynb6X24gYFcxHJAQo259rd4PGhK2EeQEuchJ_Ltqw2OKbJffXDwiIF_rP36yjKcX4er-gyXWgvVcrFABNII_OudOuh4sRxhNKAUwAQ; ll=; uQaTag=1%23; gid=; rdid=A21BB374-E7EB-4589-BF08-332B29CABFEF; urlencode_mod=iPhone15%252C3; didTag=0; did_tag=0; client_key=56c3713c; did=5F89E01C-C869-4B99-AD78-6BB47AF5BA39; language=zh-Hans-CN%3Bq%3D1; mod=iPhone15%2C3; userRecoBit=0; sys=iOS_17.5.1; sw=1290; countryCode=cn',
        'content-type': 'application/json',
        'jimu-token': 'AKbgBWZu',
        'pgid': '02B27654-1CFB-4A1F-A23C-4491FE4BF61C',
        'accept': 'application/json, text/plain, */*',
        'resourcetag': 'AKbgBWZu',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'zyck': 'jimu.jimu_AKbgBWZu',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'sec-fetch-mode': 'cors',
        'origin': 'https://ppg.viviv.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Kwai/12.6.51.8850 ISLP/0 StatusHT/54 KDT/PHONE ISDM/0 TitleHT/44 NetType/WIFI ICFO/0 locale/zh-Hans CT/0 Yoda/2.13.9.2 ISLB/0 CoIS/2 ISLM/0 WebViewType/WK BHT/102 AZPREFIX/az2',
        'referer': 'https://ppg.viviv.com/doodle/AKbgBWZu.html?hyId=jimu%2Cjimu_AKbgBWZu&bizId=jimu_AKbgBWZu&layoutType=4&noBackNavi=true&padSplit=1&padBgColor=40caf5&splitScreenPriority=2&uni_src=ks_summer_hpjy16',
        'sec-fetch-dest': 'empty'
    }

    json_data = {
        "activityId":activityId,
        "timestamp":timestamp
    }
    res = user.rank(activityId,timestamp,json=json_data, headers=headers)
    res=res.json()


    # result.success = False
    # if res.json()["code"] == 0:
    #     result.success = True
    #     result.token = res.json()["data"]["rankList"]
    # else:
    #     result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["result"], res.json()["message"])
    #
    # result.msg = res.json()["message"]
    # result.response = res
    # logger.info("排行榜用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    # return result
    return res