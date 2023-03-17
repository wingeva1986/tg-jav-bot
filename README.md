# tg-jav-bot

**一个万能 Telegram 番号查询机器人。基于 Javbus，Sukebei，Avgle，Dmm，Javlibrary，维基百科，谷歌翻译等进行构建，集成了 Pikpak 作为磁链保存网盘。**

欢迎 issue 和 pr，也可通过邮箱 [akynazh@qq.com](mailto://akynazh@qq.com) 或电报 [@jackbryant286](https://t.me/jackbryant286) 联系我。

子项目： [jvav](https://github.com/akynazh/jvav)

## 功能简介

**主要功能：**

发送给机器人一条含有番号的消息，机器人会匹配并通过 Javbus 和 Sukebei 搜索消息中所有符合“字母-数字”格式的番号（其它格式的番号可通过 /av 命令查找）。如果搜索到结果，将返回番号对应 AV 的封面，标题，日期，演员，磁链等。

**附加功能：**

以下功能按开发完成时间进行排序，后续有新功能将持续补充。

- 支持收藏演员和番号
- 支持过滤磁链（过滤顺序：无码，高清，有字幕）
- 支持配置代理
- 支持通过 Javbus 获取影片截图
- 支持通过 Javbus 获取演员最新 AV，随机获取演员 AV
- 支持让机器人自动将最优磁链发送到 Pikpak（随机获取时不会自动发送）
- 支持通过 Dmm 获取预览视频，女优排行榜，AV 评分 （由于 DMM 限制，只支持日本 IP）
- 支持通过 Avgle 获取预览视频和完整视频
- 支持通过 Javlibrary 各种排行榜随机获取番号
- 支持通过维基百科获取演员中文名
- 支持通过谷歌翻译日文标题
- 支持通过 Javbus 和维基百科以日文或中文搜索演员（演员名称需要和维基对应词条一致）
- 支持通过 Dmm 随机获取女优高分 AV
- 支持通过 Redis 进行缓存

注：配置，记录和日志等文件存放在 `~/.tg_jav_bot` 目录下。

**机器人指令：**

- /help  查看指令帮助
- /star  后接演员名称可搜索该演员
- /av  后接番号可搜索该番号
- /stars  查看收藏的演员
- /avs  查看收藏的番号
- /nice  随机获取一部高分 AV
- /new  随机获取一部最新 AV
- /rank  获取 DMM 女优排行榜
- /record  获取收藏记录文件
- /clear  清空缓存

**部分结果展示：**

![部分结果展示](res.png)

## 使用教程

### 配置机器人

编辑 `~/.tg-jav-bot/config.yaml`：

```
# TG 对话 ID
tg_chat_id: 
# TG 机器人 Token
tg_bot_token: 
# 全局是否使用代理 1 是 | 0 否
use_proxy: 
# 访问 dmm 时是否使用代理，如果全局使用代理，则忽略该字段 1 是 | 0 否
use_proxy_dmm: 
# 代理服务器地址，如果不使用代理，则忽略该字段
proxy_addr: 
# 是否使用 Pikpak 自动发送功能 1 是 | 0 否
use_pikpak: 
# 配置 TG API，如果不使用 Pikpak 自动发送功能，则忽略以下两个字段，可在这里申请 API: https://my.telegram.org/apps
tg_api_id: 
tg_api_hash: 
# 是否使用缓存 1 是 | 0 否
use_cache: 
# redis 地址，如果不使用缓存，则忽略以下两个字段
redis_host: 
redis_port: 
```

如需使用 Pikpak 自动发送功能，需要先手动授权 [Pikpak 官方机器人](https://t.me/PikPak6_Bot)，然后在初次运行机器人时进行登录操作。

### 运行机器人

**通过 docker 运行：**

```
docker-compose up -d
```

**或通过普通方法运行：**

```
# 如果使用缓存的话需先开启 redis 服务
# Python >=3.7
pip install -r requirements.txt
python3 bot.py
```