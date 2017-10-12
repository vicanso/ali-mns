# ali-mns

curl -XPOST '{
	"sign": "npmtrend网站短信",
	"template": "SMS_91840090",
	"content": "abcd your test",
	"params": {
		"code": "432432"
	}
}' 'http://127.0.0.1:3080/sms/13800138000'

```bash
docker run \
  -d --restart=always \
  -p 5000:5000 \
  -e END_POINT=https://???.mns.cn-shenzhen.aliyuncs.com \
  -e ACCESS_ID=??? \
  -e ACCESS_KEY=??? \
  -e TOPIC=sms.topic-cn-shenzhen \
  -e ACCESS_TOKEN=??? \
  --name=cat vicanso/ali-mns
```