import json
from django.http import HttpResponse
from util import mysqlutils

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')# win会有乱码，linux没问题


# Create your views here.

TOUTIAO_PAGE_SIZE = 10


def news_tech(request):
    # print("获取参数：", args[0])
    # page_num = str(args[0]).split("=")[1]
    page_num = request.GET.get("page")
    # print("页码传递页码=",page_)
    print("页码=%s" % page_num)
    data = query_more(table="news_tech", page=int(page_num))
    return data


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
            dict_result["count"] = len(json_list)
            dict_result["result"] = 0
    except Exception as e:
        dict_result["result"] = 1
        dict_result["msg"] = "%s" % e
    return HttpResponse(json.dumps(dict_result, ensure_ascii=False))
