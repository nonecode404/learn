import json
from random import random


def get_request(self, url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
    except Exception as e:
        print("请求出错：", e)

    return None


def search_music(self, key):
    # 20: 查询 20 条数据，key：关键字
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=%d&w=%s' % (20, key)
    resp = self.get_request(url)
    resp_json = json.loads(resp.text[9:][:-1])
    data_song_list = resp_json['data']['song']['list']
    song_list = []
    for song in data_song_list:
        singers = [s.get("name", "") for s in song.get("singer", "")]
        song_list.append({'name': song['songname'], 'songmid': song['songmid'], 'singer': '|'.join(singers)})

    return song_list

def download_url(self, song):
    guid = str(random.randrange(1000000000, 10000000000))

    purl_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?' \
                '&data={"req":{"param":{"guid":" %s"}},' \
                        '"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"%s","songmid":["%s"],"uin":"%s"}},"comm":{"uin":%s}}' \
                % (guid, guid, song['songmid'], 0, 0)

    resp = self.get_request(purl_url)

    if resp is None:
        return 'N', 'None', '.m4a'

    resp_json = json.loads(resp.text)

    purl = resp_json['req_0']['data']['midurlinfo'][0]['purl']

    # 有些音乐在网站上不能听
    if len(purl) < 1:
        msg = 'N'

    download_url = 'http://ws.stream.qqmusic.qq.com/' + purl
    song_data = self.get_request(download_url)
    if song_data:
        msg = 'Y'
    return msg, download_url, '.m4a'

import os

from qqMusic import QQMusic
from miguMusic import MiGuMusic
from prettytable import PrettyTable


class MusicBox(object):

    def __init__(self):
        pass

    def download(self, data, songName, type):

        save_path = 'music/' + songName + '.' + type
        file = 'music'
        if os.path.exists(file):
            pass
        else:
            os.mkdir('music')

        try:
            print("{}下载中.....".format(songName), end='')
            with open(save_path, 'wb') as f:
                f.write(data)
            print("已下载完成")
        except Exception as err:
            print("文件写入出错:", err)
            return None

    def main(self):
        print('请输入需要下载的歌曲或者歌手：')
        key = input()
        print('正在查询..\033[32mQQ音乐\033[0m', end='')
        qqMusic = QQMusic()
        qq_song_list = qqMusic.main(key)
        print('...\033[31m咪咕音乐\033[0m')
        miguMusic = MiGuMusic()
        migu_song_list = miguMusic.main(key)

        qq_song_list.extend(migu_song_list)
        song_dict = {}
        for song in qq_song_list:
            key = song['name'] + '\\' + song['singer']
            s = song_dict.get(key)
            if s:
                if s['msg'] != 'Y':
                    song_dict[key] = song
            else:
                song_dict[key] = song

        i = 0

        table = PrettyTable(['序号', '歌手', '下载', '歌名'])
        table.border = 0
        table.align = 'l'
        for song in list(song_dict.values()):
            i = i + 1
            table.add_row([str(i), song['singer'], song['msg'], song['name']])
        print(table)

        while 1:
            print('\n请输入需要下载，按 q 退出：')
            index = input()
            if index == 'q':
                return

            song = list(song_dict.values())[int(index) - 1]
            data = qqMusic.get_request(song['downloadUrl'])
            if song['msg'] == 'Y':
                self.download(data.content, song['name'], song['type'])
            else:
                print('该歌曲不允许下载')

if __name__ == '__main__':
    musicBox = MusicBox()
    musicBox.main()