msg.topic = msg.payload.topicPath

let data = {
    "result": "telloに、命令しました"
}
msg.payload = JSON.stringify(data)
msg.delay = 500
return msg;