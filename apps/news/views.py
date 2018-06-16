import sys
import json
from django.http import HttpResponse
from util import mysqlutils

# Create your views here.
TOUTIAO_PAGE_SIZE = 10


def news(request):
    tag = request.GET.get("tag")
    page = request.GET.get("page")
    if tag is not None and int(page) > 0:
        func_name = getattr(sys.modules[__name__], tag)  # 获取字符串对应方法名
        return func_name(page)
    else:
        return HttpResponse("参数不正确:tag=%s,page=%s" % (tag, page))


def news_tech(page):
    """科技"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_tech", page=int(page))


def news_all(page):
    """推荐"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_all", page=int(page))


def news_entertainment(page):
    """娱乐"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_entertainment", page=int(page))


def news_fashion(page):
    """时尚"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_fashion", page=int(page))


def news_finance(page):
    """金融"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_finance", page=int(page))


def news_hot(page):
    """热点"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_hot", page=int(page))


def news_military(page):
    """军事"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_military", page=int(page))


def news_society(page):
    """社会"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_society", page=int(page))


def news_sport(page):
    """体育"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_sport", page=int(page))


def news_world(page):
    """世界"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_world", page=int(page))


def news_game(page):
    """游戏"""
    connect = mysqlutils.get_connect("toutiao")
    return query_more(connect, table="news_game", page=int(page))


def query_more(connect="toutiao", table="news_tech", page=1):
    """查询数据库"""
    dict_result = {}
    try:
        offset = TOUTIAO_PAGE_SIZE * (page - 1)
        connect = mysqlutils.get_connect("toutiao")
        with connect.cursor() as cursor:
            cursor.execute(
                "select datetime, title, abstract, url, image_url, behot_time, media_info, source_open_url, ban_comment,has_video, image_list, publish_time from " + table + " order by datetime desc limit " + str(
                    TOUTIAO_PAGE_SIZE) + " offset " + str(offset))
            ret = cursor.fetchone()
            json_list = []
            while ret is not None:
                item = {}
                item["datetime"] = ret[0].strftime('%Y-%m-%d %H:%M')
                item["title"] = ret[1]
                print("标题", ret[1])
                item["abstract"] = ret[2]
                item["url"] = ret[3]
                item["image_url"] = ret[4]
                item["behot_time"] = ret[5].strftime('%Y-%m-%d %H:%M')
                item["media_info"] = json.loads(ret[6]) if ret[6] is not None else None
                item["source_open_url"] = ret[7]
                item["ban_comment"] = ret[8]
                item["has_video"] = False if ret[9] == 0 else True
                item["image_list"] = json.loads(ret[10]) if ret[10] is not None else None
                item["publish_time"] = ret[11].strftime('%Y-%m-%d %H:%M')
                # item["_id"] = ret[12]
                json_list.append(item)
                ret = cursor.fetchone()
            dict_result["data"] = json_list
            dict_result["page_id"] = table
            dict_result["data_size"] = len(json_list)
            dict_result["result"] = 0
    except Exception as e:
        dict_result["result"] = 1
        dict_result["msg"] = "%s" % e
    return HttpResponse(json.dumps(dict_result, ensure_ascii=False))
