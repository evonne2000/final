#Celebrity check out linebot
輸入名字後可快速獲得名人基本資料的linebot

##Build Process
使用此份python程式需要:

* linebot
* ngrok

linebot建立步驟:

1.直接在瀏覽器上搜尋line bot並登入帳號

2.登入後選擇建立一個新的`provider`

3.provider建立完成後建立一個新的`Message API Channel`

4.依據需求和喜好完成設定

5.建立完成後進入 `channel`

6.在`basic setting`下方的`Channel secret`右邊按下`issue`獲取channel secret

7.在`Messaging API`最下方的`Channel access token`右邊按下`issue`獲取channel secret

8.將main中的channel secret 和 channel secre替換成自己的

9.下載ngrok並將ngrok的執行黨和本python檔放在同一個資料夾

10.先執行本python檔後執行ngrok

11.將ngrok執行檔中的第二個`Forwarding`的網址(https開頭到箭頭之前)複製起來，並更改在linebot設定介面的`Messaging API`中的`Webhook URL`，網址後面要加上`/callback`

12.加入linebot為好友後即可測試你的linebot


##Introduction

本專案原設計為透過爬蟲取得明星相關:
*在維基百科取得明星基本資料
*在名為 **愛豆app** 的網站取得明星的近期公開行程

