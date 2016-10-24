# rabbitMQ-persistence

### 单一模式持久化

#### 1.创建rabbitmq节点.

```
oc run rabbit --image=registry.dataos.io/wfw2046/rabbitmq:3-management --env RABBITMQ_ERLANG_COOKIE='!@KLHSDAHSUDASDLAJSD' --env RABBITMQ_DEFAULT_USER=admin --env RABBITMQ_DEFAULT_PASS=<password> --env HOSTNAME=testrabbit

```
  ##### 参数说明：
  
    RABBITMQ_ERLANG_COOKIE
    RABBITMQ_DEFAULT_USER  //指定一个默认用户
    RABBITMQ_DEFAULT_PASS  //默认用户的密码
    HOSTNAME               //指定主机名，必须指定，防止pod删除或重启后，pod与svc不匹配
