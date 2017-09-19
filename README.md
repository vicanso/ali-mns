# ali-mns

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