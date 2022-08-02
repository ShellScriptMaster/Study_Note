# Kubernetes教程

## 介绍说明

### 课程概要

#### 适合群体

软件工程师 测试工程师  运维工程师 软件架构师  项目经理

#### 课程概览

> - 介绍说明
>   - 课程背景概要
>   - Kubernetes框架
>   - Kubernetes关键字含义
> - 基础概念
>   - Pod的概念
>   - 控制器类型
>   - K8S网络通讯模式
> - Kubernetes
>   - 构建K8S集群
> - 资源清单
>   - 资源的概念
>   - 掌握资源清单的语法
>   - 通过资源清单编写Pod
>   - 掌握Pod的生命周期 ★★★
> - Pod控制器
>   - 掌握各种控制器的特点以及使用定义方式
> - 服务发现
>   - 掌握Service原理及其构建方式
> - 存储
>   - 掌握多种存储类型的特点
>   - 在不同环境中选择合适的存储方案
> - 调度器
>   - 掌握调度器原理
>   - 根据要求把Pod定义到指定节点运行
> - 集群安全机制
>   - 集群的认证原理及其流程 
>   - 集群的鉴权原理及其流程 
>   - 访问控制原理及其流程 
> - HELM
>   - 掌握HELM原理
>   - HELM模板自定义
>   - HELM部署一些常用插件
> - 运维
>   - Kubeadm源码修改
>   - 构建高可用的Kubernetes集群

#### 相关概念说明

> **1.服务分类**
> 	`有状态服务：DBMS`
>
> ​	`无状态服务：LVS、APACHE`
>
> **2.高可用集群副本数**
>
> ​	`最好是>=3的奇数`

### K8S发展背景

#### 容器化资源管理平台

Apache-MESOS：分布式资源管理框架：早期最大使用者Twitter，后宣布转用Kubernetes

Docker-SWARM：Docker集群化方案：功能太少

Google-Kubernetes：10年容器化基础架构Borg，GO语言重新编写成Kubernetes

`特点：轻量级（消耗资源小）、开源、弹性伸缩、负载均衡（IPVS）`

### K8S组件说明

#### Borg组件说明

![image-20220119160425262](https://s2.loli.net/2022/01/19/OpIN1atQmfgXSVc.png)

1. **访问方式**：浏览器、命令行、配置文件

2. 用户通过3种访问方式，将请求交给BorgMaster负责处理

3. **BorgMaster**：集群的统筹中心
4. **scheduler**：将BorgMaster接受到的请求写入Paxos数据库，分发给Borglet
5. **Paxos**：Borg存放数据的数据库
6. **Borglet**：提供服务的工作节点，监听Paxos数据库，接受任务并提供服务

#### K8S结构说明

![image-20220119161839154](https://s2.loli.net/2022/01/19/5xEGHnWZKNoqC28.png)

**集群管理工具**

​	`kubectl：命令行管理工具`

​	`web UI：web可视化管理工具`

**集群组件说明**

Master

​	`api server：所有服务访问统一入口`

​	`controller manager（replication controller）：维持副本期望数目`

​	`scheduler：负责接收任务，选择合适的节点进行分配任务`

​	`etcd：键值对数据库，存储K8S集群所有需要持久化的重要信息`

node

​	`kubelet：直接跟底层容器引擎交互实现容器的生命周期管理`

​	`kube proxy：负责写入规则至firewall（IPTABLES）或IPVS（新版本已支持）实现服务映射访问`

> **kubelet补充说明**
>
> kubelet负责Node节点上Pod的全生命周期；
>
> 执行apiserver分配的任务，并通过apiserver读取etcd上的集群配置信息；
>
> 同时，也会定时上报本地Node的状态信息给apiserver。

**其它组件说明**

​	`CoreDNS：为集群中的Service创建一个域名-IP的对应解析（实现负载均衡的其中一部分）`

​	`Dashboard：为K8S集群提供浏览器可视化的B/S访问`

​	`Ingress Controller：K8S默认只能实现四层代理，Ingress可以实现七层代理`

​	`Federation：提供一个可以跨集群中心多K8S统一管理的功能`

​	`Prometheus：提供K8S集群的监控能力`

​	`ELK：提供K8S集群日志统一分析接入平台`

> **Etcd版本说明**
>
> ​	Etcd v2:Memory（不支持数据持久化存储）
>
> ​	Etcd v3:Database
>
> `新版的Kubernetes默认使用Etcd v3`
>
> `注意：Kubernetes v1.11及之前版本，仅支持Etcd v2`

## Kubernetes基础概念

### Pod

#### Pod基本概念

Pod是k8s进行资源调度的最小单位，每个Pod中运行着一个或多个密切相关的业务容器，这些业务容器共享`Pause容器（伴随Pod的创建而生成的容器）`的IP和Volume。

我们以这个不易死亡的Pause容器作为Pod的根容器，以它的状态表示整个容器组的状态。

一个Pod一旦被创建就会放到etcd中存储，然后由Master调度到一个Node绑定，由这个Node上的Kubelet进行实例化。

> **Pod和容器的区别**
>
> Pod只是一个逻辑概念，在K8S中是最基本的调度单元，它将一个或者多个容器捆绑在一起，共享了一些资源（如，namespace、network、volume），并将他们作为一个基本的调度单元进行管理；所以Pod相对于容器来说，是个更高级别的结构。

#### 自主式Pod

自行创建的Pod，不具备副本机制，Pod删除或出现故障不会自动重新拉起Pod。

#### 控制器管理的Pod

Kubernetes中内建了很多controller（控制器），这些相当于一个状态机，用来控制Pod的具体状态和行为。


#### 服务发现

Pod通过Service对外提供一个统一的服务访问入口。

Service的功能是应用暴露，Pod是有生命周期的，也有独立的IP地址，随着Pod的创建与销毁，Pod的IP地址可能发生改变，而Service可以统一代表Pod，是固定不变的。

<img src="https://s2.loli.net/2022/01/20/vDT4Y5zHVKuRnbj.png" alt="服务发现" style="zoom:48%;" />

### K8S网络通讯

#### 网络通讯模式说明

Kubernetes的网络模型假定了所有Pod都在一个可以直接连通的扁平的网络空间中。

因为在GCE（Google云计算引擎）里面有现成的网络模型，所以Kubernetes设计中是假定这个网络已经存在。

而在自行搭建的Kubernetes集群，就不能假定这个网络已经存在了。

我们需要自己实现这个网络假设，将不同节点上的Docker容器之间的互相访问先打通，再运行Kubernetes。

> 同一个Pod内的多个容器之间：Pause的loopback端口
>
> 各Pod之间的通讯`（自行搭建K8S集群需要解决）`：Overlay Network
>
> Pod与Service之间的通讯：各节点的IPTABLES规则或IPVS规则

![image-20220120142255740](https://s2.loli.net/2022/02/08/bwgF2tk4xjLvoZf.png)

**K8S三层网络**

节点网络：只有节点网络是物理网络

Pod网络

Service网络

#### 组件通讯模式说明

Flannel是CoreOS团队针对Kubernetes设计的一个网络规划服务。功能是让集群中的不同节点主机创建的Docker容器都具有全集群唯一的虚拟IP地址。而且它还能在这些IP地址之间建立一个覆盖网络（Overlay Network），通过这个覆盖网络，将数据包原封不动地传递到目标容器内。

![image-20220120135813297](https://s2.loli.net/2022/01/20/WdoLF71jEJKlgIn.png)

**同一个Pod内部通讯**

​	同一个Pod共享同一个网络命名空间，共享同一个Linux协议栈

**Pod1至Pod2**

​	`Pod1与Pod2不在同一台主机`

​	Pod的地址是与Docker0在同一个网段。

​	Docker0网段与宿主机网卡是不同的IP网段，且不同Node之间的通信只能通过宿主机的物理网卡进行。

​	所以需要将Pod的IP和所在Node的IP关联起来（多加一层宿主机的源目IP封装），通过这个关联让Pod可以互相访问。

​    `Pod1与Pod2在同一台机器`

​	由Docker0网桥直接转发请求至Pod2，不需要经过Flannel

**Pod至Service的网络**

​	由IPTABLES或LVS维护和转发

**Pod到外网**

​	Pod向外网发送请求，查找路由表, 转发数据包到宿主机的网卡，宿主网卡完成路由选择后，

​	iptables执行Masquerade（伪装），把源IP更改为宿主网卡的IP，然后向外网服务器发送请求。

**外网访问Pod**

​	Service（NodePort）

> **ETCD-Flannel调用关系说明**
>
> ​	存储管理Flannel可分配的IP地址段资源
>
> ​	监控ETCD中每个Pod的实际地址，并在内存中建立维护Pod节点路由表

## Kubernetes安装

### 初始化部署

#### 创建虚拟机

按照以下配置创建5台虚拟机，网络模式均选择`仅主机网络模式`

虚拟机k8s-master01、k8s-node01、k8s-node02

​	`CentOS7-2*2处理器-2GB内存-SCSI磁盘-100GB磁盘`

虚拟机Harbor

​	`CentOS7-1*2处理器-2GB内存-SCSI磁盘-100GB磁盘`

虚拟机koolshare

​	`Windows10-BIOS模式-1*2处理器-4GB内存-IDE磁盘-100GB磁盘`

> 虚拟机k8s-master01、k8s-node01、k8s-node02、Harbor均安装`CentOS-7系统`
>
> 虚拟机koolshare暂不安装系统

#### koolshare安装部署

`在虚拟机koolshare完成以下操作`

1. 虚拟机使用LaoMaoTao.iso镜像光盘进入PE环境

2. 启动Win10 X64 PE

3. 等待PE完全进入系统后，更换虚拟机光盘为koolshare的系统镜像（20190419_184043.iso）

4. 打开光盘，以管理员身份运行IMG写盘工具.exe，浏览选择openwrt-koolshare的img文件，写入磁盘（写入完成即完成系统安装）

5. 虚拟机断开光盘连接，并关机

6. 调整koolshare虚拟机的配置为`1*1处理器-1GB内存`，添加一张NAT网卡或`桥接模式网卡（方便内网穿透【防火墙开放WAN入接口方向】，将koolshare作为跳板机在公网访问K8S集群）`

7. 修改物理机VMnet1网卡，添加两个IP地址`192.168.1.2/24`和`192.168.66.44`

8. 物理机浏览器访问软路由web管理页面192.168.1.1`（管理密码：koolshare）`

9. 修改软路由设置

   ​	`网络-接口-删除WAN6`

   ​	`网络-接口-编辑LAN-基本设置-IPv4地址：192.168.66.1-物理设置-取消桥接接口-保存并应用`

10. 使用新地址192.168.66.1访问软路由web管理页面

11. 离线安装插件koolss_2.2.2.tar.gz，配置ssr

#### K8S各主机系统初始化部署

`在虚拟机k8s-master01、k8s-node01、k8s-node02完成以下操作`

配置网络和主机名

| 虚拟机       | 主机名       | IP地址           | 网关和DNS    |
| ------------ | ------------ | ---------------- | ------------ |
| k8s-master01 | k8s-master01 | 192.168.66.10/24 | 192.168.66.1 |
| k8s-node01   | k8s-node01   | 192.168.66.20/24 | 192.168.66.1 |
| k8s-node02   | k8s-node02   | 192.168.66.21/24 | 192.168.66.1 |

修改所有主机的hosts解析

``` sh
echo '192.168.66.10 k8s-master01
192.168.66.20 k8s-node01
192.168.66.21 k8s-node02' >> /etc/hosts
```

配置yum源

``` sh
rm -rf /etc/yum.repos.d/*
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
```

安装必要软件包和K8S依赖包

``` sh
yum -y install conntrack ntpdate ntp ipvsadm ipset jq iptables curl sysstat libseccomp wget vim net-tools git bash-completion tree bzip2 unzip
```

停用firewalld，启用iptables并清空防火墙规则

``` sh
systemctl stop firewalld
systemctl disable firewalld
yum -y install iptables-services
systemctl restart iptables
systemctl enable iptables
iptables -F
service iptables save
```

禁用SELinux和SWAP

``` sh
setenforce 0 && sed -i 's/^SELinux=.*/SELinux=disabled/g' /etc/selinux/config
swapoff -a && sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
```

调整内核参数

``` sh
cat > kubernetes.conf <<EOF
net.bridge.bridge-nf-call-iptables=1
net.bridge.bridge-nf-call-ip6tables=1
net.ipv4.ip_forward=1
net.ipv4.tcp_tw_recycle=0
# 禁止使用swap空间，只有当系统OOM时才允许使用它
vm.swappiness=0 
# 不检查物理内存是否够用
vm.overcommit_memory=1 
# 开启 OOM
vm.panic_on_oom=0 
fs.inotify.max_user_instances=8192
fs.inotify.max_user_watches=1048576
fs.file-max=52706963
fs.nr_open=52706963
net.ipv6.conf.all.disable_ipv6=1
net.netfilter.nf_conntrack_max=2310720
EOF
cp kubernetes.conf /etc/sysctl.d/kubernetes.conf
sysctl -p /etc/sysctl.d/kubernetes.conf
```

> **OOM说明**
>
> 当系统内存不够时，会产生OOM（Out of Memory）。当我们设置panic_on_oom为0时，表示内存不足时，就会启动OOM killer进程，选择一个合适的进程，将该进程杀死，这样就能释放一部分内存
>
> **报错说明**
>
> sysctl: cannot stat XXXXXXXXXXXXX: No such file or directory
>
> 出现以上报错是内核版本不兼容问题，暂时忽略，待升级内核后即可解决问题

调整系统时区

``` sh
# 设置系统时区为上海
timedatectl set-timezone Asia/Shanghai
# 将当前的UTC时间写入硬件时钟
timedatectl set-local-rtc 0
# 重启依赖于系统时间的服务
systemctl restart rsyslog
systemctl restart crond
```

关闭系统不必要的服务

``` sh
systemctl stop postfix && systemctl disable postfix
```

设置rsyslogd和systemd journald

``` sh
# 持久化保存日志的目录
mkdir /var/log/journal 
mkdir /etc/systemd/journald.conf.d
cat > /etc/systemd/journald.conf.d/99-prophet.conf <<EOF
[Journal]
# 持久化保存到磁盘
Storage=persistent
# 压缩历史日志
Compress=yes
SyncIntervalSec=5m
RateLimitInterval=30s
RateLimitBurst=1000
# 最大占用空间10G
SystemMaxUse=10G
# 单日志文件最大200M
SystemMaxFileSize=200M
# 日志保存时间2周
MaxRetentionSec=2week
# 不将日志转发到 syslog
ForwardToSyslog=no
EOF
systemctl restart systemd-journald
```

升级系统内核

`CentOS-7.X默认3.10.X内核版本与Docker、Kubernetes存在一些兼容性问题，会导致环境运行不稳定`

``` sh
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm
# 安装完成后检查/boot/grub2/grub.cfg中对应内核menuentry中是否包含 initrd16 配置，如果没有，再安装一次！
yum --enablerepo=elrepo-kernel install -y kernel-lt
# 查询新版内核完整名称
grep menuentry /boot/grub2/grub.cfg
# 设置开机从新内核启动(新内核版本号根据实际情况修改)
grub2-set-default 'CentOS Linux (5.4.173-1.el7.elrepo.x86_64) 7 (Core)'
# 完成设置后重启虚拟机，让系统从新内核启动
reboot
```

> 重启后检查内核版本是否刷新

### Kubeadm部署安装K8S

`在虚拟机k8s-master01、k8s-node01、k8s-node02完成以下操作`

kube-proxy开启ipvs的前置条件

``` sh
modprobe br_netfilter
cat > /etc/sysconfig/modules/ipvs.modules <<EOF
#!/bin/bash
modprobe -- ip_vs
modprobe -- ip_vs_rr
modprobe -- ip_vs_wrr
modprobe -- ip_vs_sh
modprobe -- nf_conntrack
#modprobe -- nf_conntrack_ipv4
# 内核5.4版本中nf_conntrack_ipv4模块更名为nf_conntrack
EOF
chmod 755 /etc/sysconfig/modules/ipvs.modules && bash /etc/sysconfig/modules/ipvs.modules
lsmod | grep -e ip_vs -e nf_conntrack
```

安装Docker软件

``` sh
安装相关依赖包
yum install -y yum-utils device-mapper-persistent-data lvm2

yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum update -y && yum install -y docker-ce

完成安装后重启虚拟机
reboot

重启后内核版本回退，重新设置默认内核版本为最新并再次重启
grub2-set-default 'CentOS Linux (5.4.173-1.el7.elrepo.x86_64) 7 (Core)'
reboot

# 创建/etc/docker目录
mkdir /etc/docker
# 配置daemon
cat > /etc/docker/daemon.json <<EOF
{
"exec-opts": ["native.cgroupdriver=systemd"],
"log-driver": "json-file",
"log-opts": {
"max-size": "100m"
}
}
EOF
mkdir -p /etc/systemd/system/docker.service.d
# 重启docker服务
systemctl daemon-reload && systemctl restart docker && systemctl enable docker
```

安装Kubeadm（主从配置）

``` sh
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
yum -y install kubeadm-1.15.1 kubectl-1.15.1 kubelet-1.15.1
systemctl enable kubelet.service
```

`在虚拟机k8s-master01完成以下操作`

初始化主节点

```sh
# 打印kubeadm的默认初始化配置模板，并保存为yaml配置文件
kubeadm config print init-defaults > kubeadm-config.yaml

# 修改配置文件中以下配置项
vim kubeadm-config.yaml
# 修改对外地址为本机地址
第12行 advertiseAddress: 192.168.66.10
# 修改Kubernetes版本
第34行 kubernetesVersion: v1.15.1
# 添加指定pod的网段的配置（Flannel组件默认使用的网段）
第35行 networking:
第36行   dnsDomain: cluster.local
第37行   podSubnet: 10.244.0.0/16
第38行   serviceSubnet: 10.96.0.0/12
# 添加一段配置，指定默认的调度方式为ipvs调度模式
第40行 ---
第41行 apiVersion: kubeproxy.config.k8s.io/v1alpha1
第42行 kind: KubeProxyConfiguration
第43行 featureGates:
第44行   SupportIPVSProxyMode: true
第45行 mode: ipvs

# 初始化主节点，并将输出结果保存到文件kubeadm-init.log
# 输出信息中包含了token，可用于一些验证
kubeadm init --config=kubeadm-config.yaml --experimental-upload-certs | tee kubeadm-init.log
```

kubeadm-init.log中包含的关键信息

``` sh
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.66.10:6443 --token abcdef.0123456789abcdef \
    --discovery-token-ca-cert-hash sha256:07c67ecf0b949a632778856d7da0763c55ca9214ee0302d847333f65d07e8281
```

根据kubeadm-init.log的提示，执行命令

``` sh
# 创建目录，拷贝集群管理员配置文件并授予权限
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# 查询集群的状态，目前状态为NotReady，这是因为还未安装网络插件
kubectl get node

# 创建一个目录存放所有关键文件
mkdir -p install-k8s/core install-k8s/plugin/flannel
mv kubeadm-init.log kubeadm-config.yaml install-k8s/core/

# 部署Flannel
wget -O  install-k8s/plugin/flannel/kube-flannel.yml https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
kubectl create -f install-k8s/plugin/flannel/kube-flannel.yml

# 查看kube-system（K8S所有组件默认安装名称空间）中是否已创建好flannel的pod
kubectl get pod -n kube-system

# 物理机也生成了一个flannel的网卡配置
ifconfig | grep flannel


# 再次查询集群的状态，目前状态为Ready
kubectl get node
```

`在虚拟机k8s-node01、k8s-node02完成以下操作`

将Node01和Node02加入集群

```sh
# 从kubeadm-init.log中复制命令（包含了token）
kubeadm join 192.168.66.10:6443 --token abcdef.0123456789abcdef \
--discovery-token-ca-cert-hash sha256:07c67ecf0b949a632778856d7da0763c55ca9214ee0302d847333f65d07e8281
```

`在虚拟机k8s-master01完成以下操作`

查看节点状态

``` sh
# 查看节点状态，先是状态为NotReady
kubectl get node

# 可以查看Pod的详细信息（可以看到集群正在哪些节点上创建哪些Pod）
kubectl get pod -n kube-system -o wide

# 待所有Pod都创建完成，显示为Running状态后，再次查看节点状态，显示为Ready
kubectl get node
```

到这里，集群已完成基本安装工作，整理安装过程的文件

```sh
mv install-k8s/ /usr/local/
rm -rf kube*
```

> **设置K8S管理命令kubectl的参数Tab键补全**
>
> ```sh
> echo 'source <(kubectl completion bash)' >> /etc/bashrc
> chmod +x /etc/bashrc
> source /etc/bashrc
> ```

## Harbor私有仓库

### Harbor安装部署

`在虚拟机Harbor完成以下操作`

配置网络和主机名

| 虚拟机 | 主机名 | IP地址            | 网关和DNS    |
| ------ | ------ | ----------------- | ------------ |
| Harbor | hub    | 192.168.66.100/24 | 192.168.66.1 |

修改主机的hosts解析

``` sh
echo '192.168.66.10 k8s-master01
192.168.66.20 k8s-node01
192.168.66.21 k8s-node02
192.168.66.100 hub hub.example0.com' >> /etc/hosts
```

> 将配置同步到K8S集群各主机
>
> scp /etc/hosts root@k8s-master01:/etc/hosts
>
> scp /etc/hosts root@k8s-node01:/etc/hosts
>
> scp /etc/hosts root@k8s-node02:/etc/hosts

配置yum源

``` sh
rm -rf /etc/yum.repos.d/*
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
```

安装必要软件包

``` sh
yum -y install conntrack ntpdate ntp ipvsadm ipset jq iptables curl sysstat libseccomp wget vim net-tools git bash-completion tree bzip2 unzip
```

停用firewalld，启用iptables并清空防火墙规则

``` sh
systemctl stop firewalld
systemctl disable firewalld
yum -y install iptables-services
systemctl restart iptables
systemctl enable iptables
iptables -F
service iptables save
```

禁用SELinux和SWAP

``` sh
setenforce 0 && sed -i 's/^SELinux=.*/SELinux=disabled/g' /etc/selinux/config
swapoff -a && sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
```

调整内核参数

``` sh
cat > kubernetes.conf <<EOF
net.bridge.bridge-nf-call-iptables=1
net.bridge.bridge-nf-call-ip6tables=1
net.ipv4.ip_forward=1
net.ipv4.tcp_tw_recycle=0
vm.swappiness=0 
vm.overcommit_memory=1 
vm.panic_on_oom=0 
fs.inotify.max_user_instances=8192
fs.inotify.max_user_watches=1048576
fs.file-max=52706963
fs.nr_open=52706963
net.ipv6.conf.all.disable_ipv6=1
net.netfilter.nf_conntrack_max=2310720
EOF
cp kubernetes.conf /etc/sysctl.d/kubernetes.conf
sysctl -p /etc/sysctl.d/kubernetes.conf
```

调整系统时区

``` sh
timedatectl set-timezone Asia/Shanghai
timedatectl set-local-rtc 0
systemctl restart rsyslog && systemctl restart crond
```

关闭系统不必要的服务

``` sh
systemctl stop postfix && systemctl disable postfix
```

设置rsyslogd和systemd journald

``` sh
mkdir /var/log/journal 
mkdir /etc/systemd/journald.conf.d
cat > /etc/systemd/journald.conf.d/99-prophet.conf <<EOF
[Journal]
Storage=persistent
Compress=yes
SyncIntervalSec=5m
RateLimitInterval=30s
RateLimitBurst=1000
SystemMaxUse=10G
SystemMaxFileSize=200M
MaxRetentionSec=2week
ForwardToSyslog=no
EOF
systemctl restart systemd-journald
```

升级系统内核

``` sh
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm
yum --enablerepo=elrepo-kernel install -y kernel-lt
grep menuentry /boot/grub2/grub.cfg
grub2-set-default 'CentOS Linux (5.4.173-1.el7.elrepo.x86_64) 7 (Core)'
reboot
```

> `重启后检查内核版本是否刷新`

安装Docker软件

``` sh
安装相关依赖包
yum install -y yum-utils device-mapper-persistent-data lvm2

yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum update -y && yum install -y docker-ce

完成安装后重启虚拟机
reboot

重启后内核版本回退，重新设置默认内核版本为最新并再次重启
grub2-set-default 'CentOS Linux (5.4.173-1.el7.elrepo.x86_64) 7 (Core)'
reboot

# 创建/etc/docker目录
mkdir /etc/docker
# 配置daemon
cat > /etc/docker/daemon.json <<EOF
{
"exec-opts": ["native.cgroupdriver=systemd"],
"log-driver": "json-file",
"log-opts": {
"max-size": "100m"
},
  "insecure-registries": ["https://hub.example0.com"]
}
EOF

mkdir -p /etc/systemd/system/docker.service.d
# 所有主机上均重启docker服务
systemctl daemon-reload && systemctl restart docker && systemctl enable docker
```

> 将配置同步到K8S各节点
>
> scp /etc/docker/daemon.json root@k8s-master01:/etc/docker/daemon.json
>
> scp /etc/docker/daemon.json root@k8s-node01:/etc/docker/daemon.json
>
> scp /etc/docker/daemon.json root@k8s-node02:/etc/docker/daemon.json
>
> 并重启K8S各节点的docker服务
>
> systemctl daemon-reload && systemctl restart docker && systemctl enable docker

从`物理机`上传`docker-compose`和`harbor-offline-installer-v1.2.0.tgz`到`虚拟机Harbor`

解压Harbor安装压缩包

``` sh
mv docker-compose /usr/local/bin/
chmod +x /usr/local/bin/docker-compose
tar xvf harbor-offline-installer-v1.2.0.tgz
mv harbor /usr/local/
```

修改Harbor配置文件

``` sh
vim /usr/local/harbor/harbor.cfg
# 修改域名
第5行 hostname = hub.example0.com
# 修改为https协议提供服务
第9行 ui_url_protocol = https
# 复制证书的存放路径
第24行 ssl_cert = /data/cert/server.crt
```

创建证书

```
# 创建证书存放目录
mkdir -p /data/cert

# 生成证书
openssl genrsa -des3 -out server.key 2048
【Enter pass phrase for server.key:根据提示输入密码】
【Verifying - Enter pass phrase for server.key:确认密码】
openssl req -new -key server.key -out server.csr
Enter pass phrase for server.key:【输入前面的密码】
Country Name (2 letter code) [XX]:【CN】
State or Province Name (full name) []:【GD】
Locality Name (eg, city) [Default City]:【GZ】
Organization Name (eg, company) [Default Company Ltd]:【example0】
Organizational Unit Name (eg, section) []:【example0】
Common Name (eg, your name or your server's hostname) []:【hub.example0.com】
Email Address []:【kubernetes@example0.com】
A challenge password []: 【默认直接回车】
An optional company name []:【默认直接回车】
cp server.key server.key.org
openssl rsa -in server.key.org -out server.key
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

# 将证书存放到对应目录并赋予权限
mv server.* /data/cert/
chmod -R 777 /data/cert
```

安装Harbor

``` sh
/usr/local/harbor/install.sh
```

### Harbor使用测试

完成安装后，`物理机浏览器`访问测试`https://hub.example0.com`

默认管理员账号密码：

`admin`

`Harbor12345`

![image-20220121180042359](https://s2.loli.net/2022/02/08/pDqbMuWkFQUKjX4.png) 

**测试使用Harbor**

`在虚拟机k8s-node01完成以下操作`

将docker登录到hub.example0.com

```sh
docker login https://hub.example0.com
Username: 【admin】
Password: 【Harbor12345】
```

上传镜像测试

``` sh
# 从docker公共镜像源下载镜像作为测试使用
docker pull nginx
docker images

# 参考Harbor的web管理界面中默认项目library的推送命令
	在项目中标记镜像：
	docker tag SOURCE_IMAGE[:TAG] hub.example0.com/library/IMAGE[:TAG]
	推送镜像到当前项目：
	docker push hub.example0.com/library/IMAGE[:TAG]

# 修改镜像的名称:标签
docker tag nginx:latest hub.example0.com/library/nginx:v1

# 上传镜像到Harbor
docker push hub.example0.com/library/nginx:v1
```
测试K8S使用Harbor

```sh
【在虚拟机k8s-node01完成以下操作】
# 删除这两个镜像，排除是本地镜像的可能性
docker rmi -f hub.example0.com/library/nginx:v1
docker rmi -f nginx:latest

【在虚拟机k8s-master01完成以下操作】
# 在K8S中使用镜像启动容器
kubectl run nginx-deployment --image=hub.example0.com/library/nginx:v1 --port=80 --replicas=1
kubectl get deployment
kubectl get rs
kubectl get pod -o wide（命令中包含Pod的详细信息，包括IP地址、运行在哪个节点）

# 测试访问
curl 【'kubectl get pod -o wide'查询到的IP地址】

# 删除Pod测试自愈能力
kubectl delete pod 【'kubectl get pod'查询到的Pod名称】

# 再次查看，K8S重新启动了一个Pod
kubectl get pod

# 扩容到3个副本
kubectl scale --replicas=3 deployment/nginx-deployment
kubectl get pod

# 再次测试删除一个Pod
kubectl delete pod 【'kubectl get pod'查询到的Pod名称】

# 再次查看，K8S又重新启动一个Pod来替代前面删除的Pod，使得副本数始终保持在3
kubectl get pod

# 为3个副本创建一个对外统一的负载均衡访问入口Service
# --port集群内端口，--target-port容器端口，nodeport是集群外端口
kubectl expose deployment nginx-deployment --port=30000 --target-port=80

# 测试访问Service提供的统一访问入口（Service提供负载均衡轮询的访问，只能通过集群内部访问，外部无法访问）
kubectl get svc
curl 【'kubectl get svc'查询到的CLUSTER IP地址】:30000	

# 通过查询ipvs策略可看到关于3个副本的负载均衡轮询策略
# ipvs策略中的地址与'kubectl get pod -o wide'查询到的3个副本Pod的地址一致
ipvsadm -Ln | grep -A3 :30000
kubectl get pod -o wide

# 修改Service的Type
kubectl edit svc nginx-deployment
第25行   type: NodePort

# 再次查看Service的信息中类型已经发生了改变，并自动分配了一个可以外部访问的端口
kubectl get svc

# 物理机浏览器使用该端口测试访问（所有节点地址都可以访问）
访问地址：
http://192.168.66.10:30638/
或
http://192.168.66.20:30638/
或
http://192.168.66.21:30638/
```

> **Harbor如果开关机导致无法访问处理办法**
>
> cd /usr/local/harbor/ && docker-compose up -d
>

## Kubernetes资源清单

### Kubernetes资源

**资源的定义**

K8S中所有的内容都抽象为资源， 资源实例化之后（被运行、调用、执行后），叫做对象

**资源的分类**

1. 名称空间级别：只有在相同名称空间中可见

   > **工作负载型资源（workload）**
   >
   > Pod、ReplicaSet、Deployment、StatefulSet、DaemonSet、Job、CronJob、ReplicationController
   >
   > **服务发现及负载均衡型资源（ServiceDiscovery LoadBalance）**
   >
   > Service、Ingress...
   >
   > **配置与存储型资源**
   >
   > Volume（存储卷）、CSI（容器存储接口,用于扩展第三方存储卷）
   >
   > **特殊类型的存储卷**
   >
   > ConfigMap（当配置中心来使用的资源类型）、Secret（保存敏感数据）、DownwardAPI（把外部环境中的信息输出给容器）

2. 集群级别：整个集群都可见、可被调用

   > Namespace、Node、Role、ClusterRole、RoleBinding、ClusterRoleBinding

3. 元数据型：根据系统指标进行对应操作的资源

   > HPA、PodTemplate、LimitRange

### 资源清单YAML语法

> **简单说明**
> > 是一个可读性高，用来表达数据序列的格式。
>
> **基本语法**
>
> > 缩进时不允许使用Tab键，只允许使用空格
> >
> > 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
> >
> > #标识注释，从这个字符一直到行尾，都会被解释器忽略
>
> **YAML支持的数据结构**
> > 对象：键值对的集合，又称为映射（mapping）/哈希（hashes）/字典（dictionary）
> >
> > 数组：一组按次序排列的值，又称为序列（sequence）/ 列表（list）
> >
> > 纯量（scalars）：单个的、不可再分的值
> >
> > > **对象类型**
> > > 对象的一组键值对，使用冒号结构表示
> > > ``` yaml
> > > name: Steve
> > > age: 18
> > > ```
> > > Yaml也允许另一种写法，将所有键值对写成一个行内对象
> > > ``` yaml
> > > hash: { name: Steve, age: 18 }
> > > ```
> > > **数组类型**
> > > 一组连词线开头的行，构成一个数组
> > >
> > > ``` yaml
> > > animal
> > > - Cat
> > > - Dog
> > > ```
> > > 数组也可以采用行内表示法
> > > ``` yaml
> > > animal: [Cat, Dog]
> > > ```
> > > **复合结构**
> > > 对象和数组可以结合使用，形成复合结构
> > >
> > > ``` yaml
> > > languages:
> > > - Ruby
> > > - Perl
> > > - Python
> > > websites:
> > >   YAML: yaml.org
> > >   Ruby: ruby-lang.org
> > >   Python: python.org
> > >   Perl: use.perl.org
> > > ```
> > > **纯量**
> > > 纯量是最基本的、不可再分的值。
> > >
> > > 以下数据类型都属于纯量：
> > >
> > > 字符串、布尔值、整数、浮点数、Null、时间、日期
> > >
> > > ``` yaml
> > > 数值直接以字面量的形式表示
> > > number: 12.30
> > > 
> > > 布尔值用true和false表示
> > > isSet: true
> > > 
> > > null用 ~ 表示
> > > parent: ~
> > > 
> > > 时间采用ISO8601格式
> > > iso8601: 2001-12-14t21:59:43.10-05:00
> > > 
> > > 日期采用复合ISO8601格式的年、月、日表示
> > > date: 1976-07-31
> > > 
> > > YAML 允许使用两个感叹号，强制转换数据类型
> > > e: !!str 123
> > > f: !!str true
> > > ```
> > > 字符串默认不使用引号表示
> > >
> > > ``` yaml
> > > str: 这是一行字符串
> > > ```
> > >
> > > 如果字符串之中包含空格或特殊字符，需要放在引号之中
> > >
> > > ``` yaml
> > > str: '内容：字符串'
> > > ```
> > > 单引号和双引号都可以使用，双引号不会对特殊字符转义
> > > ``` yaml
> > > s1: '内容\n字符串'
> > > s2: "内容\n字符串"
> > > ```
> > > 单引号之中如果还有单引号，必须连续使用两个单引号转义（类似shell里面的\\'写法）
> > > ``` yaml
> > > str: 'labor''s day'
> > > ```
> > > 字符串可以写成多行，从第二行开始，必须有一个单空格缩进。换行符会被转为空格
> > > ``` yaml
> > > str: 这是一段
> > >   多行
> > >   字符串
> > > ```

### 资源清单常用字段

**必要参数**

| 参数名                  | 类型   | 说明                                                         |
| ----------------------- | ------ | ------------------------------------------------------------ |
| apiVersion              | String | K8S API的版本，目前基本是v1，可以用kubectl api-versions命令查询 |
| kind                    | String | 指yaml文件定义的资源类型和角色，如：Pod                      |
| metadata                | Object | 元数据对象，固定值就写metadata                               |
| metadata.name           | String | 元数据对象的名称，自定义编写，如：Pod的名称                  |
| metadata.namespace      | String | 元数据对象的名称空间，自定义编写，如省略默认为default名称空间 |
| Spec                    | Object | 详细定义对象的属性（如定义Pod的镜像、名称...），固定值就写Spec |
| spec.containers[]       | List   | Spec对象的容器列表定义，是个列表                             |
| spec.containers[].name  | String | 定义容器的名字                                               |
| spec.containers[].image | String | 定义要用到的镜像名称                                         |

> **apiVersion说明**
>
> `背景`
>
> Kubernetes的官方文档中并没有对apiVersion的详细解释，而且因为K8S本身版本也在快速迭代，有些资源在低版本还在beta阶段，到了高版本就变成了stable。
>
> 例如Deployment:
>
> ​	1.6版本之前：extensions/v1beta1
>
> ​	1.6版本到1.9版本之间：apps/v1beta1
>
> ​	1.9版本之后:apps/v1
>
> 
>
> `各种apiVersion的含义`
>
> - alpha
>
>   - 该软件可能包含错误，启用一个功能可能会导致bug
>
>   - 随时可能会丢弃对该功能的支持，恕不另行通知
>
>
> - beta
>
>   - 软件经过很好的测试，启用功能被认为是安全的。
>
>   - 默认情况下功能是开启的
>
>   - 细节可能会改变，但功能在后续版本不会被删除
>
>
> - stable
>
>   - 该版本名称命名方式：vX这里X是一个整数
>
>   - 稳定版本、放心使用
>
>   - 将出现在后续发布的软件版本中
>
>
> - v1
>   - Kubernetes API的稳定版本，包含很多核心对象：pod、service等
>
>
> - apps/v1beta2
>   - 在kubernetes1.8版本中，新增加了apps/v1beta2的概念，apps/v1beta1同理
>   - DaemonSet、Deployment、ReplicaSet和StatefulSet的当时版本迁入apps/v1beta2，兼容原有的extensions/v1beta1
>
>
> - apps/v1
>   - 在kubernetes1.9版本中，引入apps/v1，Deployment等资源从extensions/v1beta1,apps/v1beta1和 apps/v1beta2迁入apps/v1，原来的v1beta1等被废弃。
>   - apps/v1代表：包含一些通用的应用层的api组合，如：Deployments、RollingUpdates、ReplicaSets
>
>
> - batch/v1
>
>   - 代表job相关的api组合
>
>   - 在kubernetes1.8版本中，新增了batch/v1beta1，后CronJob已经迁移到了batch/v1beta1，然后再迁入batch/v1
>
>
> - autoscaling/v1
>   - 代表自动扩缩容的api组合，kubernetes1.8版本中引入。 这个组合中后续的alpha 和
>    beta版本将支持基于memory使用量、其他监控指标进行扩缩容
>
>
> - extensions/v1beta1
>
>   - Deployment等资源在1.6版本时放在这个版本中，后迁入到apps/v1beta2,再到apps/v1中统一管理
>
>   -certificates.k8s.io/v1beta1
>
>   - 安全认证相关的api组合
>
> - authentication.k8s.io/v1
>   - 资源鉴权相关的api组合
>
> 
>
> `查看当前可用的API版本`
>
> kubectl api-versions

**主要对象**

| 参数名                                      | 类型   | 说明                                                         |
| ------------------------------------------- | ------ | ------------------------------------------------------------ |
| spec.containers[].imagePullPolicy           | String | 定义镜像拉取策略，可选值：Always：每次都尝试重新拉取在线镜像；Never：仅使用本地镜像；IfNotPresent：如果本地有镜像则使用本地镜像，否则拉取在线镜像，`默认值是Always` |
| spec.containers[].command[]                 | List   | 指定容器启动命令，可以指定多个，不指定则使用容器镜像打包时的启动命令 |
| spec.containers[].args[]                    | List   | 指定容器启动命令参数，可以指定多个                           |
| spec.containers[].workingDir                | String | 指定容器的工作目录                                           |
| spec.containers[].volumeMounts[]            | List   | 指定容器内部的存储卷配置                                     |
| spec.containers[].volumeMounts[].name       | String | 指定可以被容器挂载的存储卷的名称                             |
| spec.containers[].volumeMounts[].mountPath  | String | 指定可以被容器挂载的存储卷的路径                             |
| spec.containers[].volumeMounts[].readOnly   | String | 设置存储卷路径的读写模式，true或false，`默认是读写模式`      |
| spec.containers[].ports[]                   | List   | 指定容器需要用到的端口列表                                   |
| spec.containers[].ports[].name              | String | 指定端口名称                                                 |
| spec.containers[].ports[].containerPort     | String | 指定容器需要监听的端口号                                     |
| spec.containers[].ports[].hostPort          | String | 指定容器所在主机需要监听的端口号，默认与containerPort相同，`注意：设置了hostPort同一台主机无法启动该容器的相同副本（因为主机的端口号不能相同，会冲突）` |
| spec.containers[].ports[].protocol          | String | 指定端口协议，支持TCP和UDP，`默认值是TCP`                    |
| spec.containers[].env[]                     | List   | 指定容器运行前需要的环境变量列表                             |
| spec.containers[].env[].name                | String | 指定环境变量名称                                             |
| spec.containers[].env[].value               | String | 指定环境变量的值                                             |
| spec.containers[].resources                 | Object | 指定资源限制和资源请求的值（设置容器的资源限制）             |
| spec.containers[].resources.limits          | Object | 指定容器`运行时`资源的运行上限                               |
| spec.containers[].resources.limits.cpu      | String | 指定CPU的限制，单位是core数量                                |
| spec.containers[].resources.limits.memory   | String | 指定内存的限制，单位是MiB、GiB                               |
| spec.containers[].resources.requests        | Object | 指定容器`启动和调度时`的限制设置                             |
| spec.containers[].resources.requests.cpu    | String | CPU请求，单位是core数量，容器启动时的初始化可用数量          |
| spec.containers[].resources.requests.memory | String | 内存请求，单位是MiB、GiB，容器启动时的初始化可用数量         |

**其它参数**

| 参数名                | 类型    | 说明                                                         |
| --------------------- | ------- | ------------------------------------------------------------ |
| spec.restartPolicy    | String  | 定义Pod的重启策略，可选值：Always：Pod一旦终止运行，则无论容器是如何终止的，Kubelet服务都将重启它；OnFailure：只有Pod以非0退出码终止时，Kubelet才会重启该容器，如果容器正常结束（退出码0），则Kubelet不会重启它；Never：Pod终止后，Kubelet将退出码报告给Master，不会重启该Pod，`默认值是Always` |
| spec.nodeSelector     | Object  | 定义Node的Label过滤标签，以key:value格式指定                 |
| spec.imagePullSecrets | Object  | 定义pull镜像时使用的secret名称，以name:secretkey格式指定     |
| spec.hostNetwork      | Boolean | 定义是否使用主机网络模式，`默认值是false`，设置true表示使用宿主机网络，不使用docker网桥，`注意：设置了true将无法在同一台主机上启动第二个副本` |

**更多参数**

通过命令可以获取更多参数

``` sh
# 例如查看spec相关的参数
kubectl explain spec
```

### 通过资源清单创建Pod

```sh
vim pod.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata: 
  name: myapp-pod
  namespace: default
  labels: 
    app: myapp
    version: v1
spec: 
  containers: 
  - name: app
    image: hub.example0.com/library/nginx:v1
  - name: test
    image: hub.example0.com/library/nginx:v1
```

``` sh
# 应用pod.yaml以创建Pod
kubectl apply -f pod.yaml
```

> `此处是2个容器使用了相同的镜像，这将会导致错误端口冲突而错误`
>
> ``` sh
> # 查看观察Pod状态变化
> kubectl get pod
> 
> # 查看Pod详细信息，发现是test容器报错
> kubectl describe pod myapp-pod
> 
> # 查看容器test的日志
> kubectl logs myapp-pod -c test 
> 
> # 删除Pod
> kubectl delete pod myapp-pod
> 
> # 删除文件pod.yaml的13-14行关于容器test配置
> sed -i '13,14d' pod.yaml
> 
> # 重新应用pod.yaml以创建Pod
> kubectl apply -f pod.yaml
> ```

## Pod的生命周期

![image-20220125141156092](https://s2.loli.net/2022/01/25/quPKeJYsTQfcyI4.png)

1. 完成容器环境的初始化，启动Pause的基础容器
2. 进行init C初始化容器
3. START：进入Main C状态之前执行容器启动的命令
4. STOP：MainC退出之前也可以执行一条退出命令
5. readiness：可以规定在容器运行n秒后，运行readiness（探测、检测Pod的状态，检测成功后显示Pod的状态为Running/Ready）
6. Liveness：Liveness探测容器出现损坏、无法正常工作，根据重启策略执行重启、删除命令

### Init Containers

**概念与特点**

Pod除了应用容器外，还可以定义1个或多个在应用容器启动之前运行的初始化容器（Init Containers）。

> **Init Containers的特点**
>
> - Init Containers与普通容器类似，主要区别：
>   - Init Containers总是运行到成功完成为止；
>   - 每个Init Containers都必须在下一个Init Containers启动之前成功完成并退出。
> - 如果Pod的Init Containers失败，Kubernetes`默认`会不断地重启该Init Containers直到成功为止。
> - 如果Pod对应的`restartPolicy值为"Never"`，并且Pod的Init Containers失败，则Kubernetes会将整个Pod状态设置为失败。
> - 因为Init Containers具有与应用程序容器分离的单独镜像，所以Init Containers具有如下优势：
>   - Init Containers可以包含并运行一些安装过程中应用容器不存在的实用工具或个性化代码，例如：没有必要仅为了在安装过程中使用类似sed、awk、python或dig这样的工具，而去FROM另一个镜像来生成一个新的；
>   - Init Containers可以运行一些出于安全考虑，不建议在应用容器镜像中包含的实用工具；
>   - Init Containers使用Linux Namespace，所以相对应用程序容器来说具有不同的文件系统视图。因此，它们能够具有访问Secret的权限，而应用程序容器则不能；
>   - Init Containers可以在应用程序启动之前完成，而应用程序容器是并行运行的，所以Init Containers能够提供了一种简单的阻塞或延迟应用容器的启动的方法，直接满足了一组先决条件。
> - 其它特性：
>   - 在Pod启动过程中，Init Containers会按顺序在网络和数据卷初始化之后启动。
>   - 在所有的Init Containers没有成功之前，Pod将不会变成Ready状态。
>   - Init Containers的端口不会在Service中汇聚对外提供访问。
>   - 正在初始化中的Pod处于Pending状态，且会将Initializing状态设置为false。
>   - 如果Pod重启，所有Init Containers必须重新执行。
>   - 对Init Containers中spec的修改被限制在image字段，修改其他字段都不会生效。更改Init Containers的image字段，等价于重启该Pod。
>   - Init Containers具有应用容器的所有字段。然而Kubernetes禁止使用readinessProbe，因为Init Containers不能定义不同于完成态（Completion）的就绪态（Readiness）。Kubernetes会在校验时强制执行此检查。
>   - 在Pod中的每个应用容器和Init Containers的名称必须唯一；与任何其他容器共享同一个名称，会在验证时报错。

**Init Containers样例**

编写包含Init Containers的Pod资源清单

``` sh
# 为防止与前面实验冲突，先删除此前创建的一些资源（不指定名称空间，默认删除default名称空间的资源）
kubectl delete deployment --all
kubectl delete pod --all
kubectl delete svc --all

# 创建资源清单文件
vim init-pod.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
  - name: myapp-container
    image: busybox
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
  initContainers:
  - name: init-myservice
    image: busybox
    command: ['sh', '-c', 'until nslookup myservice; do echo waiting for myservice; sleep 2; done;']
  - name: init-mydb
    image: busybox
    command: ['sh', '-c', 'until nslookup mydb; do echo waiting for mydb; sleep 2; done;']
```

应用init-pod.yaml以创建Pod

``` sh
kubectl apply -f init-pod.yaml
```

查看Pod状态

``` sh
kubectl get pod

# 结果如下，当前状态为Init:0/2
# 因为init进程未结束，所以Pod无法READY
NAME        READY   STATUS     RESTARTS   AGE
myapp-pod   0/1     Init:0/2   0          6s
```

编写并应用资源清单创建Service，使得init进程能成功完成

1. 编写对应第一个Init Containers（init-myservice）的Service

``` sh
vim myservice.yaml
```

``` yaml
kind: Service
apiVersion: v1
metadata:
  name: myservice
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
```

应用myservice.yaml创建Service

``` sh
kubectl apply -f myservice.yaml 
```

查看Pod状态

``` sh
# 等待第一个Init Containers（init-myservice）运行完成后，状态变更为Init:1/2
kubectl get pod
NAME        READY   STATUS     RESTARTS   AGE
myapp-pod   0/1     Init:1/2   0          10m
```

2. 编写对应第二个Init Containers（init-mydb）的service

``` sh
vim mydb.yaml
```

``` yaml
kind: Service
apiVersion: v1
metadata:
  name: mydb
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9377
```
应用mydb.yaml创建Service

``` sh
kubectl apply -f myservice.yaml 
```

查看Pod状态

``` sh
# 等待第二个Init Containers（init-myservice）也运行完成后，状态变更Running
kubectl get pod
NAME        READY   STATUS    RESTARTS   AGE
myapp-pod   1/1     Running   0          18m
```

### 容器探针

**概念**

探针是由Kubelet对容器执行的定期诊断。要执行诊断，Kubelet调用由容器实现的Handler。

**分类**

有三种类型的处理程序：

​	HTTPGetAction：根据指定路径、端口对容器IP执行HTTP Get请求。如果响应的状态码大于或等于200且小于400，则认为诊断成功。

​	ExecAction: 在容器内执行指定命令。如果命令退出时返回码为0则认为诊断成功。

​	TCPSocketAction：对指定端口上的容器的IP地址进行TCP检查。如果端口打开，则诊断被认为是成功的。

每次探测将获得以下三种结果之一：

​	成功：容器通过了诊断

​	失败：容器未通过诊断

​	位置：诊断失败，因此不会采取任何行动

**探测方式**

ReadinessProbe就绪检测

指示容器是否准备好服务请求。如果就绪探测失败，端点控制器将从与Pod匹配的所有Service的端点中删除该Pod的IP地址。初始延迟之前的就绪状态默认为Failure。如果容器不提供就绪探针，则默认状态为Success。

LivenessProbe存活检测

指示容器是否正在运行。如果存活检测失败，则Kubelet会杀死容器，并且容器将受到其重启策略的影响。如果容器不提供存活探针，则默认状态为Success

**容器探针样例**

`样例1：就绪检测`

创建一个HTTPGetAction类型的ReadinessProbe资源清单

``` sh
vim readiness-httpget.yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: readiness-httpget-pod
  namespace: default
spec:
  containers:
  - name: readiness-httpget-container
    image: hub.example0.com/library/nginx:v1
    imagePullPolicy: IfNotPresent
    readinessProbe:
      httpGet:
        port: 80
        path: /index1.html						# 检测访问index1.html
      initialDelaySeconds: 1					# 开始检测的等待时间
      periodSeconds: 3							# 重新检测的等待时间
```

使用资源清单创建Pod

``` sh
kubectl apply -f readiness.yaml
```

查看Pod创建情况

``` sh
# 当前READY状态为0/1
kubectl get pod
NAME                    READY   STATUS    RESTARTS   AGE
myapp-pod               1/1     Running   0          40m
readiness-httpget-pod   0/1     Running   0          26s

# 查看日志，因为检测到缺少index1.html，报错404
kubectl logs readiness-httpget-pod | tail -1
[27/Jan/2022:15:05:10 +0000] "GET /index1.html HTTP/1.1" 404 153 "-" "kube-probe/1.15" "-"

# 进入容器管理终端
kubectl exec -it readiness-httpget-pod /bin/sh

# 在容器管理终端中创建index1.html（exit退出）
echo hello world! > /usr/share/nginx/html/index1.html
```

再次查看Pod创建情况

``` sh
# 当前READY状态为1/1
kubectl get pod
NAME                    READY   STATUS    RESTARTS   AGE
myapp-pod               1/1     Running   0          56m
readiness-httpget-pod   1/1     Running   0          16m
```

`样例2：存活检测-ExecActionl`

清空原有default名称空间的资源，防止干扰

``` sh
kubectl delete pod --all
kubectl delete svc mydb myservice
```

创建一个ExecAction类型的LivenessProbe资源清单

``` sh
vim liveness-exec.yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: liveness-exec-pod
  namespace: default
spec:
  containers:
  - name: liveness-exec-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ["/bin/sh","-c","touch /tmp/live ; sleep 60; rm -rf /tmp/live; sleep 3600"]
    livenessProbe:
      exec:
        command: ["test","-e","/tmp/live"]		# 测试/tmp/live是否存在，存在返回值为0，不存在返回值非0
      initialDelaySeconds: 1
      periodSeconds: 3
```

使用资源清单创建Pod

``` sh
kubectl apply -f liveness-exec.yaml
```

查看Pod创建情况

``` sh
# 当前状态Pod已经创建好Running且Ready
kubectl get pod
AME                READY   STATUS    RESTARTS   AGE
liveness-exec-pod  1/1     Running   0          11s
```

监测Pod情况，等待一段时间后（容器启动命令中休眠1分钟删除/tmp/live），Pod会因为缺少/tmp/live自动重启

``` sh
kubectl get pod -w
NAME                READY   STATUS    RESTARTS   AGE
liveness-exec-pod   1/1     Running   0          14s
liveness-exec-pod   1/1     Running   1          101s
```

删除Pod避免浪费资源

``` sh
kubectl delete pod --all
```

`样例3：存活检测-HTTPGetAction`

创建一个HTTPGetAction类型的LivenessProbe资源清单

``` sh
vim liveness-httpget.yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: liveness-httpget-pod
  namespace: default
spec:
  containers:
  - name: liveness-httpget-container
    image: hub.example0.com/library/nginx:v1
    imagePullPolicy: IfNotPresent
    ports:
    - name: http
      containerPort: 80
    livenessProbe:
      httpGet:
        port: http
        path: /index.html
      initialDelaySeconds: 1
      periodSeconds: 3
      timeoutSeconds: 10
```

使用资源清单创建Pod

``` sh
kubectl apply -f liveness-httpget.yaml
```

查看Pod创建情况

``` sh
kubectl get pod
NAME                   READY   STATUS    RESTARTS   AGE
liveness-httpget-pod   1/1     Running   0          11s

# 进入容器管理终端
kubectl exec -it liveness-httpget-pod /bin/bash

# 在容器管理终端中删除index.html（exit退出）
rm -rf /usr/share/nginx/html/index.html
```

监测Pod情况，等待一段时间后（检测有等待时间），Pod因缺少主页文件index.html报错自动重启

``` sh
kubectl get pod
NAME                   READY   STATUS    RESTARTS   AGE
liveness-httpget-pod   1/1     Running   0          11s
liveness-httpget-pod   1/1     Running   1          18s
```

删除Pod避免浪费资源

```sh
kubectl delete pod --all
```

`样例4：存活检测-TCPSocketAction`

创建一个TCPSocketAction类型的LivenessProbe资源清单

``` sh
vim liveness-tcp.yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: probe-tcp
spec:
  containers:
  - name: nginx
    image: hub.example0.com/library/nginx:v1
    livenessProbe:
      initialDelaySeconds: 5
      timeoutSeconds: 1
      tcpSocket:
        port: 8080
      periodSeconds: 3
```

使用资源清单创建Pod

``` sh
kubectl apply -f liveness-tcp.yaml
```

监测Pod情况，Pod一直在自动重启（探针探测容器的TCP-8080端口，而这个容器镜像使用80端口，所以在等待时间结束后检测不到8080端口即重启）

``` sh
kubectl get pod -w
NAME        READY   STATUS    RESTARTS   AGE
probe-tcp   1/1     Running   0          4s
probe-tcp   1/1     Running   1          14s
probe-tcp   1/1     Running   2          26s
probe-tcp   1/1     Running   3          38s
```

删除Pod避免浪费资源

``` sh
kubectl delete pod --all
```

`样例5：就绪检测-存活检测并用`

复制liveness-httpget.yaml命名为liveness-readiness.yaml并编辑

``` sh
cp liveness-httpget.yaml liveness-readiness.yaml
vim liveness-readiness.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: liveness-httpget-pod
  namespace: default
spec:
  containers:
  - name: liveness-httpget-container
    image: hub.example0.com/library/nginx:v1
    imagePullPolicy: IfNotPresent
    ports:
    - name: http
      containerPort: 80
    readinessProbe: 						# 增加readiness配置
      httpGet:
        port: 80
        path: /index1.html
      initialDelaySeconds: 1
      periodSeconds: 3
    livenessProbe:
      httpGet:
        port: http
        path: /index.html
      initialDelaySeconds: 1
      periodSeconds: 3
      timeoutSeconds: 10
```

使用资源清单创建Pod

``` sh
kubectl apply -f liveness-readiness.yaml
```

查看Pod创建情况

``` sh
# 未通过就绪检测
kubectl get pod
NAME                   READY   STATUS    RESTARTS   AGE
liveness-httpget-pod   0/1     Running   0          6s
```

进入容器管理终端

``` sh
kubectl exec -it liveness-httpget-pod /bin/bash
```

创建index1.html

```
echo hello world! > /usr/share/nginx/html/index1.html
```

再次查看Pod创建情况

``` sh
# 通过就绪检测
kubectl get pod
NAME                   READY   STATUS    RESTARTS   AGE
liveness-httpget-pod   1/1     Running   0          20s
```

进入容器管理终端，删除容器中的index.html

``` sh
kubectl exec -it liveness-httpget-pod -- rm -rf /usr/share/nginx/html/index.html
```

不符合存活检测条件，自动重启Pod，重新拉起的Pod不包含index1.html，所以就绪检测一直无法通过

``` sh
kubectl get pod
NAME                   READY   STATUS    RESTARTS   AGE
liveness-httpget-pod   0/1     Running   1          10m
```

### 启动和退出

**概念**

Pod Hook（钩子）是由Kubernetes管理的Kubelet发起的，当容器中的进程启动前或者容器中的进程终止之前运行，这是包含在容器的生命周期之中。可以同时为pod中的所有容器都配置Hook。

**分类**

Hook的类型包括两种：

​	exec：执行一段命令

​	HTTP：发送http请求

**Pod Hook样例**

创建资源清单

```sh
vim hook-pod.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: lifecycle-demo
spec:
  containers:
  - name: lifecycle-demo-container
    image: nginx
    lifecycle:
      postStart:
        exec:
          command: ["/bin/sh", "-c", "echo Hello from the postStart handler > /usr/share/message"]
      preStop:
        exec:
          command: ["/bin/sh", "-c", "echo Hello from the postStop handler > /usr/share/message"]
```

使用资源清单创建Pod

``` sh
kubectl apply -f hook-pod.yaml
```

查看Pod创建情况

``` sh
kubectl get pod
```

进入容器管理终端，验证启动命令是否执行成功（退出命令无法检验，因为退出时文件丢失）

``` sh
kubectl exec lifecycle-demo -it -- /bin/cat /usr/share/message
```

### Pod生命周期阶段

**概念**

Pod Phase是Pod在其生命周期中所处位置的简单宏观概述，Phase即为阶段，也就是Pod的STATUS字段。

**Phase阶段**

| Phase阶段           | 描述                                                         |
| -- | ------------------------------------------------------------ |
| Pending | Pending挂起：Pod已被Kubernetes系统接受，但有一个或者多个容器尚未创建亦未运行。此阶段包括等待Pod被调度的时间和通过网络下载镜像的时间，一般需要等待一段时间。 |
| Running   | Running运行中：Pod已经绑定到了某个节点，Pod中所有的容器都已被创建。至少有一个容器仍在运行，或者正处于启动或重启状态。 |
| Succeeded   | Succeeded成功：Pod中的所有容器都已成功终止，并且不会再重启。   |
| Failed      | Failed失败：Pod中的所有容器都已终止，并且至少有一个容器是因为失败终止。也就是说，容器以非0状态退出或者被系统终止。 |
| Unknown     | Unknown未知：因为某些原因无法取得Pod的状态。这种情况通常是因为与Pod所在主机通信失败。 |

## 控制器

### 概念

Kubernetes中内建了很多controller（控制器），这些相当于一个状态机，用来控制Pod的具体状态和行为。

### 分类和应用场景

**ReplicationController（RC）**

用来确保容器应用的副本数始终保持在用户定义的副本数，即如果有容器异常退出，会自动创建新的Pod来替代；而如果异常多出来的容器也会自动回收。

> ReplicationController在v1.11版本已被淘汰

**ReplicaSet（RS）**

在新版本的Kubernetes中建议使用ReplicaSet来取代ReplicationController。

ReplicaSet跟ReplicationController没有本质的不同，只是名字不一样，并且ReplicaSet支持集合式的selector。

> **ReplicaSet使用说明**
>
> 虽然ReplicaSet可以独立使用，但一般还是建议使用Deployment来自动管理ReplicaSet，这样就无需担心跟其他机制的不兼容问题。
>
> （比如ReplicaSet不支持rolling-update滚动更新，但Deployment支持）

**Deployment**

为Pod和ReplicaSet提供了一个`声明式定义`方法，用来替代以前的ReplicationController来方便的管理应用。

> **名词解释**
>
> `命令式编程`
>
> ​	它侧重于如何实现程序，就像我们刚接触编程的时候那样，我们需要把程序的实现过程按照逻辑逐步写下来。
>
> `声明式编程(定义)`
>
> ​	它侧重于定义想要什么，然后告诉计算机／引擎，让他帮你去实现。
>
> **应用场景**
>
> 1. 定义Deployment来创建Pod和ReplicaSet
>
> 2. 滚动升级和回滚应用
>
> 3. 扩容和缩容
>
> 4. 暂停和继续Deployment

**HorizontalPodAutoScale（HPA）**

应用的资源使用率通常都有高峰和低谷的时候，HPA可以让Service中的Pod个数自动调整，实现削峰填谷，提高集群的整体资源利用率。

HPA仅适用于Deployment和ReplicaSet。在V1版本中仅支持根据Pod的CPU利用率扩缩容;在v1alpha版本中，支持根据内存和用户自定义的metric扩缩容。

**StatefullSet**

StatefulSet是为了解决有状态服务的问题。（对应Deployments和ReplicaSets是为无状态服务而设计）

> **应用场景**
>
> 1. 稳定的持久化存储，即Pod重新调度后还是能访问到相同的持久化数据，基于PVC来实现
> 2. 稳定的网络标志，即Pod重新调度后其PodName和HostName不变，基于Headless Service（即没有Cluster IP的Service）来实现
> 3. 有序部署，有序扩展，即Pod是有顺序的，在部署或者扩展的时候要依据定义的顺序依次依次进行（即从0到N-1，在下一个Pod运行之前所有之前的Pod必须都是Running和Ready状态），基于init containers来实现
> 4. 有序收缩，有序删除（即从N-1到0）

**DaemonSet**

DaemonSet确保全部`（或者一部分，可以在Node上打上污点，使这个Node不被调度）`Node上运行一个Pod的副本。当有Node加入集群时，也会为他们新增一个Pod 。当有Node从集群移除时，这些Pod也会被回收。

删除DaemonSet将会删除它创建的所有Pod。

> **应用场景**
>
> 1. 运行集群存储daemon，例如在每个Node上运行glusterd、ceph
>
> 2. 在每个Node上运行日志收集daemon，例如fluentd、logstash
>
> 3. 在每个Node上运行监控daemon，例如Prometheus Node Exporter

**Job/CronJob**

Job负责批处理任务，即仅执行一次的任务，它保证批处理任务的一个或多个Pod成功结束（正常执行结束并退出）。

CronJob管理基于时间的Job。

	`在给定时间点只运行一次`
	
	`周期性地在给定时间点运行`

> **应用场景**
>
> 在给定的时间点调度Job运行
>
> 创建周期性运行的Job，例如：数据库备份、发送邮件

### 控制器样例

**样例1：ReplicaSet**

创建资源清单

``` sh
vim replicaset.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: ReplicaSet
metadata:
  name: frontend
spec:
  replicas: 3
  selector:					# 选择器
    matchLabels:			# 匹配标签
      tier: frontend
  template:
    metadata:
      labels:				# 指定Pod的标签
        tier: frontend
    spec:
      containers:
      - name: myapp
        image: hub.example0.com/library/nginx:v1
        env:
        - name: GET_HOSTS_FROM
          value: dns
        ports:
        - containerPort: 80
```

应用资源清单创建ReplicaSet

```sh
kubectl apply -f replicaset.yaml
```

检验控制器ReplicaSet的效果

``` sh
# 查看Pod创建情况
[root@k8s-master01 ~]# kubectl get pod 
NAME                   READY   STATUS    RESTARTS   AGE
frontend-5fw64         1/1     Running   0          17s
frontend-8nqvf         1/1     Running   0          17s
frontend-w68fl         1/1     Running   0          17s
lifecycle-demo         1/1     Running   1          17h
liveness-httpget-pod   0/1     Running   2          18h

# 删除所有Pod
[root@k8s-master01 ~]# kubectl delete pod --all

# ReplicaSet控制的Pod会保持副本数在3，此前创建的自主式Pod被删除后不会自动重新拉起
[root@k8s-master01 ~]# kubectl get pod
NAME             READY   STATUS    RESTARTS   AGE
frontend-5sr4d   1/1     Running   0          15s
frontend-8flp4   1/1     Running   0          15s
frontend-snp6w   1/1     Running   0          15s

# 查看Pod的标签
kubectl get pod --show-labels=true
NAME             READY   STATUS    RESTARTS   AGE    LABELS
frontend-5sr4d   1/1     Running   0          118s   tier=frontend
frontend-8flp4   1/1     Running   0          118s   tier=frontend
frontend-snp6w   1/1     Running   0          118s   tier=frontend

# 修改其中一个Pod的标签
kubectl label pod frontend-5sr4d tier=frontend1 --overwrite=true

# ReplicaSet中的选择器根据标签标记Pod
# 所以修改标签后的Pod不计入副本数中，为了维持副本数3会新拉起1个Pod
kubectl get pod --show-labels=true
NAME             READY   STATUS    RESTARTS   AGE     LABELS
frontend-2rgkp   1/1     Running   0          18s     tier=frontend
frontend-5sr4d   1/1     Running   0          4m10s   tier=frontend1
frontend-8flp4   1/1     Running   0          4m10s   tier=frontend
frontend-snp6w   1/1     Running   0          4m10s   tier=frontend

# 删除rs
kubectl delete rs --all

# 删除rs时，被修改过标签的Pod也不认为属于rs，所以不会被删除
kubectl get pod --show-labels=true
NAME             READY   STATUS        RESTARTS   AGE     LABELS
frontend-2rgkp   0/1     Terminating   0          59s     tier=frontend
frontend-5sr4d   1/1     Running       0          4m51s   tier=frontend1
frontend-8flp4   0/1     Terminating   0          4m51s   tier=frontend
frontend-snp6w   0/1     Terminating   0          4m51s   tier=frontend

kubectl get pod --show-labels=true
NAME             READY   STATUS    RESTARTS   AGE    LABELS
frontend-5sr4d   1/1     Running   0          5m7s   tier=frontend1
```

清除所有资源

``` sh
kubectl delete pod --all
```

**样例2：Deployment**

创建资源清单

``` sh
vim deployment.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: cheungjune/myapp:v1
        ports:
        - containerPort: 80
```

应用资源清单创建Deployment

``` sh
## --record参数可以记录命令，我们可以很方便的查看每次 revision 的变化
kubectl apply -f deployment.yaml --record
```

检验控制器Deployment的效果

``` sh
# 查看Deployment的信息
kubectl get deployment
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   3/3     3            3           33s

# Deployment不直接创建Pod，而是创建对应的ReplicaSet
kubectl get replicaset
NAME                          DESIRED   CURRENT   READY   AGE
nginx-deployment-6dfcd75df6   3         3         3       52s

# 查看Pod创建情况
kubectl get pod
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-6dfcd75df6-4p5fq   1/1     Running   0          64s
nginx-deployment-6dfcd75df6-jgh6p   1/1     Running   0          64s
nginx-deployment-6dfcd75df6-p7458   1/1     Running   0          64s
```

扩容

``` sh
# 指定副本数为5
kubectl scale deployment nginx-deployment --replicas=5

# 查看Deployment的变化
kubectl get deployment
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   5/5     5            5           10m

# 查看Pod的变化
kubectl get pod
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-6dfcd75df6-4p5fq   1/1     Running   0          11m
nginx-deployment-6dfcd75df6-b8x54   1/1     Running   0          86s
nginx-deployment-6dfcd75df6-jgh6p   1/1     Running   0          11m
nginx-deployment-6dfcd75df6-m8j8p   1/1     Running   0          86s
nginx-deployment-6dfcd75df6-p7458   1/1     Running   0          11m
```

> **其它应用场景**
>
> 如果集群支持`HPA`的话，还可以为Deployment设置自动扩展
>
> ```sh
> kubectl autoscale deployment nginx-deployment --min=10 --max=15 --cpu-percent=80
> ```

滚动更新

``` sh
# 更新前先访问应用，查看版本
curl 【'kubectl get pod -o wide'查询到的IP地址】
Hello MyApp | Version: v1 | <a href="hostname.html">Pod Name</a>

# 更新：更改Deployment中的容器镜像版本
kubectl set image deployment/nginx-deployment nginx=cheungjune/myapp:v2

# 查看ReplicaSet的变化
kubectl get rs
NAME                          DESIRED   CURRENT   READY   AGE
nginx-deployment-656f47ddd6   5         5         5       86s
nginx-deployment-7b58d4bd55   0         0         0       9m57s

# 查看Pod的变化
kubectl get pod
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-656f47ddd6-f9zg7   1/1     Running   0          117s
nginx-deployment-656f47ddd6-v9xc6   1/1     Running   0          117s
nginx-deployment-656f47ddd6-wf4qn   1/1     Running   0          117s
nginx-deployment-656f47ddd6-xlsfc   1/1     Running   0          117s
nginx-deployment-656f47ddd6-zxzmk   1/1     Running   0          117s

# 再次访问应用，版本发生变化
curl 【'kubectl get pod -o wide'查询到的IP地址】
Hello MyApp | Version: v2 | <a href="hostname.html">Pod Name</a>
```

> **Deployment热编辑**
>
> 通过命令`kubectl edit deployment/nginx-deployment`修改Deployment的配置同样可以达到以上效果
>
> 
>
> **Deployment更新策略**
>
> 1. Deployment可以保证在升级时只有一定数量的Pod是down的：
>
> ​	默认，Deployment会确保最少(期望值-1)个Pod是up状态（最多一个不可用）
>
> 2. Deployment同时也可以确保只创建出超过期望数量的一定数量的Pod：
>
> ​	默认，Deployment会确保最多(期望值+1)个Pod是up状态（最多1个surge） 
>
> ​	未来的Kuberentes版本中，将从1-1变成25%-25%

版本回滚

``` sh
#执行回滚，默认回滚至上一次的版本
kubectl rollout undo deployment/nginx-deployment

# 查看ReplicaSet的变化
kubectl get replicaset
NAME                          DESIRED   CURRENT   READY   AGE
nginx-deployment-656f47ddd6   0         0         0       10m
nginx-deployment-7b58d4bd55   5         5         5       18m

# 访问应用，版本发生变化
curl 【'kubectl get pod -o wide'查询到的IP地址】
Hello MyApp | Version: v1 | <a href="hostname.html">Pod Name</a>

# 查看rollout的更新状态
kubectl rollout status deployment/nginx-deployment
```

> **版本回滚说明**
>
> 创建了一个5副本的Deployment；
>
> 如果当还只有3个副本创建出来的时候，就开始更新含有5个副本Deployment；
>
> 在这种情况下，Deployment会立即杀掉已创建的3个旧版本的Pod，并开始创建新版本的Pod；
>
> 它不会等到所有的5个旧版本的Pod都创建完成后才开始改变航道。
>
> 
>
> **其它回滚/更新操作**
>
> `查看版本历史`
>
> kubectl rollout history deployment/nginx-deployment
>
> `暂停Deployment的更新`
>
> kubectl rollout pause deployment/nginx-deployment
>
> `可以使用--revision参数指定某个历史版本`
>
> ​	可以通过设置spec.revisonHistoryLimit项来指定Deployment最多保留多少revision历史记录
>
> ​	默认的会保留所有的revision
>
> ​	如果将该项设置为0，Deployment就不允许回退了
>
> kubectl rollout undo deployment/nginx-deployment --to-revision=2
>
> `暂停Deployment的更新`
>
> kubectl rollout pause deployment/nginx-deployment 

清除所有资源

``` sh
kubectl delete deployment --all
```

**样例3：DaemonSet**

创建资源清单

``` sh
vim daemonset.yaml
```

``` yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: deamonset-example
  labels:
    app: daemonset
spec:
  selector:
    matchLabels:
      name: deamonset-example
  template:
    metadata:
      labels:
        name: deamonset-example
    spec:
      containers:
      - name: daemonset-example
        image: hub.example0.com/library/nginx:v1
```

应用资源清单创建DaemonSet

``` sh
kubectl apply -f daemonset.yaml
```

检验控制器DaemonSet的效果

``` sh
kubectl get pod
NAME                      READY   STATUS    RESTARTS   AGE
deamonset-example-fprxd   1/1     Running   0          13s
deamonset-example-scfjz   1/1     Running   0          13s

# 分别在Node01和Node02创建了1个副本
kubectl get pod -o wide
NAME                      READY   STATUS    RESTARTS   AGE   IP            NODE
deamonset-example-fprxd   1/1     Running   0          16s   10.244.1.33   k8s-node01
deamonset-example-scfjz   1/1     Running   0          16s   10.244.2.28   k8s-node02

kubectl get daemonset
NAME                DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
deamonset-example   2         2         2       2            2           <none>          82s
```

清除所有资源

```sh
kubectl delete daemonset --all
```

**样例4：Job**

创建资源清单

``` sh
vim job.yaml
```

``` yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    metadata:
      name: pi
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
```

应用资源清单创建Job

``` sh
kubectl apply -f job.yaml
```

检验控制器Job的效果

``` sh
# 查看Job，等待一段时间后COMPLETIONS变为1/1代表完成Job
kubectl get job
NAME   COMPLETIONS   DURATION   AGE
pi     1/1           65s        98s

# 查看Pod，等待一段时间后STATUS显示为Completed，代表已完成
kubectl get pod
NAME                      READY   STATUS      RESTARTS   AGE
pi-pzjk5                  0/1     Completed   0          2m17s

# 查看Pod的日志，可以看到perl应用计算出的2000位pi值
kubectl logs 【'kubectl get pod'查询到的Pod名称】
3.14159265358979323846264338327950288419716939937510582097494459230781...
```

清除所有资源

``` sh
kubectl delete job --all
```

> **Job说明**
> RestartPolicy仅支持Never或OnFailure
>
> 单个Pod时，默认Pod成功运行后Job即结束
>
> .spec.completions
>
> ​	标志Job结束需要成功运行的Pod个数，默认为1
>
> .spec.parallelism
>
> ​	标志并行运行的Pod的个数，默认为1
>
> spec.activeDeadlineSeconds
>
> ​	标志失败Pod的重试最大时间，超过这个时间不会继续重试

**样例5：CronJob**

创建资源清单

``` sh
vim cronjob.yaml
```

``` yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            args:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure
```

应用资源清单创建CronJob

```sh
kubectl apply -f cronjob.yaml
```

检验控制器CronJob的效果

```sh
kubectl get cronjob
NAME    SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
hello   */1 * * * *   False     0        <none>          3s

kubectl get job
NAME              COMPLETIONS   DURATION   AGE
hello-1643383320   1/1           5s         14s

kubectl logs 【'kubectl get pod'查询到的Pod名称】
Fri Jan 28 15:25:05 UTC 2022
Hello from the Kubernetes cluster
```

清除所有资源

``` sh
kubectl delete cronjob --all
```

> **CronJob说明**
>
> CronJob的限制：CronJob只是周期性按计划创建Job，只能判断CronJob是否执行成功，对于Job是否执行成功是未知的
>
> 
>
> **CronJob spec字段用法**
>
> `.spec.schedule`
>
> ​	调度，必需字段，指定任务运行周期，格式同Cron
>
> `.spec.jobTemplate`
>
> ​	Job模板，必需字段，指定需要运行的任务，格式同Job
>
> `.spec.startingDeadlineSeconds`
>
> ​	启动Job的期限（秒级别），该字段是可选的
>
> ​	如果因为任何原因而错过了被调度的时间，那么错过执行时间的Job将被认为是失败的
>
> ​	如果没有指定，则没有期限
>
> `.spec.concurrencyPolicy`
>
> ​	并发策略，该字段也是可选的。它指定了如何处理被CronJob创建的Job的并发执行。
>
> ​	只允许指定下面策略中的一种：
>
> ​		Allow（默认）：允许并发运行Job
>
> ​		Forbid：禁止并发运行，如果前一个还没有完成，则直接跳过下一个
>
> ​		Replace：取消当前正在运行的Job，用一个新的来替换
>
> ​	注意，这个策略只能应用于同一个CronJob创建的Job。如果存在多个CronJob，它们创建的Job之间总是允许并发运行。
>
> `.spec.suspend`
>
> ​	挂起，该字段也是可选的，默认值为false
>
> ​	如果设置为true，后续所有执行都会被挂起，它对已经开始执行的Job不起作用
>
> `.spec.successfulJobsHistoryLimit`
>
> `.spec.failedJobsHistoryLimit`
>
> ​	历史限制，是可选的字段
>
> ​	它们指定了可以保留多少完成和失败的Job
>
> ​	默认情况下，它们分别设置为3和1
>
> ​	设置限制的值为0，相关类型的Job完成后将不会被保留

## Service

### Service基本概念

Service是将运行在一组Pod上的应用程序公开为网络服务的抽象方法。

Kubernetes为Pod提供自己的IP地址，并为一组Pod提供相同的DNS名。

Service通常是通过Label Selector访问Pod组的。

![img](https://s2.loli.net/2022/01/28/kaJwXfQ6yOEjxeN.png)

Service能够提供负载均衡的能力，但是在使用上有以下限制：只提供4层负载均衡能力（通过IP地址负载均衡），而没有7层功能（通过域名负载均衡），但有时我们可能需要更多的匹配规则来转发请求，这点上4层负载均衡是不支持的。

### Service分类

**ClusterIp**

默认类型，自动分配一个仅集群`(Cluster)`内部可以访问的虚拟`IP`

<img src="https://img-blog.csdnimg.cn/20200810111312896.png" alt="img" style="zoom:80%;" /> 

**NodePort**

在ClusterIP基础上为Service在每台机器上绑定一个端口`(NodePort)`，这样就可以通过`节点IP地址:NodePort`来访问该服务。

<img src="https://img-blog.csdnimg.cn/20200810112040939.png" alt="img" style="zoom: 50%;" /> 

> 可以在K8S集群基础上添加一个前端负载均衡器（如：Nginx，当然也可以是高可用的Nginx负载均衡集群），轮询访问Node1:30001和Node2:30002，以防止当Node1或Node2出现故障后，原来对外发布的`节点IP:端口号`不可用。

**LoadBalancer**

在`NodePort`的基础上，借助`云供应商`创建一个外部负载均衡器，并将请求转发到`NodePort`

<img src="https://img-blog.csdnimg.cn/2020081011250113.png" alt="img" style="zoom: 50%;" /> 

> **LoadBalancer说明**
>
> 通常建议在云原生部署的Kubernetes集群上使用。

**ExternalName**

把集群外部的服务引入到集群内部来，在集群内部直接使用，没有任何类型代理被创建（只有Kubernetes1.7或更高版本的kube-dns才支持）

### Service组件工作流程

<img src="https://img-blog.csdnimg.cn/20200810112911662.png" style="zoom:50%;" />

客户端`client`访问节点是通过`iptables`实现的

`iptables`规则是通过`kube-proxy`写入的

`apiserver`通过监控`kube-proxy`去进行服务和端点信息的发现

`kube-proxy`通过`pod`的标签（`lables`）去判断这个端点信息是否写入到`SVC-Endpoints`里

### Service代理模式

在Kubernetes集群中，每个Node运行一个kube-proxy进程。

kube-proxy负责为Service实现了一种VIP（虚拟IP）的形式，而不是ExternalName的形式。

​	Kubernetes v1.0：代理完全在userspace：Service是4层概念（TCP/UDP over IP）

​	Kubernetes v1.1：新增iptables代理，但不是默认的运行模式：新增Ingress API（beta版），用来表示7层（HTTP）服务

​	Kubernetes v1.2：默认使用iptables代理

​	Kubernetes v1.8.0-beta.0：添加ipvs代理

​	Kubernetes v1.14：默认使用ipvs代理。

**userspace代理模式**

<img src="https://s2.loli.net/2022/01/28/OvTbmGWSqQXfctK.png" alt="img" style="zoom:50%;" />

**iptables代理模式**

<img src="https://s2.loli.net/2022/01/28/GfPqmgReti3OnlH.png" alt="img" style="zoom:50%;" />

 **ipvs代理模式**



<img src="https://s2.loli.net/2022/01/28/4CNzyfIwiGpkYcF.png" alt="img" style="zoom:50%;" />

> ipvs代理模式中kube-proxy会监视Kubernetes Service对象和Endpoints，调用netlink接口相应地创建ipvs规则并定期与Kubernetes Service对象和Endpoints对象同步ipvs规则，以确保ipvs状态与期望一致。
>
> 访问服务时，流量将被重定向到其中一个后端Pod。
>
> 与iptables类似，ipvs于netfilter的hook功能，但使用哈希表作为底层数据结构并在内核空间中工作。这意味着ipvs可以更快地重定向流量，并且在同步代理规则时具有更好的性能。
>
> ipvs为负载均衡算法提供了更多选项：轮询调度rr、最小连接数ls、目标哈希dh、源哈希sh、最短期望延迟sed、不排队调度nq。

### Service样例

> **说明**
>
> 以下所有关于iptables的描述：
>
> 如果在Kubernetes集群部署中如果选用了ipvs，那么均将iptables换成ipvs理解即可。
>
> 无论是iptables还是ipvs，除了代理模式不同，其它均同理。

**ClusterIP**

ClusterIP主要在每个Node节点使用iptables，将发向ClusterIP对应端口的数据，转发到kube-proxy中。

然后kube-proxy内部有可以实现负载均衡的方法，并可以查询到这个Service下对应Pod的地址和端口，进而把数据转发给对应的Pod的地址和端口。

<img src="https://s2.loli.net/2022/01/29/m4TxIXMAiycjG7s.png" alt="img" style="zoom: 67%;" />

ClusterIP工作原理

apiserver：用户通过kubectl命令向apiserver发送创建Service的命令，apiserver接收到请求后将数据存储到etcd中

kube-proxy：Kubernetes每个节点都有一个kube-porxy进程，这个进程负责感知Service、Pod的变化（通过apiserver读取etcd的数据），并将变化的信息写入本地的iptables规则中

iptables：使用NAT等技术将virtualIP的流量转至endpoint（Pod）中

`样例1：ClusterIP`

创建一个Deployment资源清单

```sh
vim myapp-deployment.yaml
```

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deploy
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      release: stable
  template:
    metadata:
      labels:
        app: myapp
        release: stable
        env: test
    spec:
      containers:
      - name: myapp
        image: cheungjune/myapp:v1
        imagePullPolicy: IfNotPresent
        ports:
        - name: http
          containerPort: 80
```

创建一个Service资源清单

``` sh
vim service.yaml
```

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp
  namespace: default
spec:
  type: ClusterIP
  selector:
    app: myapp
    release: stable
  ports:
  - name: http
    port: 80
    targetPort: 80
```

应用清单创建Deployment

``` sh
kubectl apply -f myapp-deployment.yaml
```

检验Deployment

``` sh
# 查看Pod情况
kubectl get pod -o wide
NAME                            READY   STATUS    RESTARTS   AGE   IP             NODE      
myapp-deploy-754bf8d64b-4t78w   1/1     Running   0          81s   10.244.1.112   k8s-node01
myapp-deploy-754bf8d64b-dzkhj   1/1     Running   0          81s   10.244.2.118   k8s-node02
myapp-deploy-754bf8d64b-n6x58   1/1     Running   0          81s   10.244.1.111   k8s-node01

# 测试访问
curl 【'kubectl get pod -o wide'查询到的IP地址】
```

应用清单创建Service

``` sh
kubectl apply -f service.yaml
```

检验Service

``` sh
# 查看Service
kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   3d17h
myapp        ClusterIP   10.100.62.204   <none>        80/TCP    4s

# 查看ipvs代理信息
ipvsadm -Ln | grep -A3 `kubectl get svc | grep myapp | awk '{print $3}'`
TCP  10.100.62.204:80 rr
  -> 10.244.1.111:80              Masq    1      0          0         
  -> 10.244.1.112:80              Masq    1      0          0         
  -> 10.244.2.118:80              Masq    1      0          0         

# 多次使用Service地址访问/hostname.html页面，测试轮询
curl 【'kubectl get svc'查询到的IP地址】/hostname.html
第1次访问：myapp-deploy-754bf8d64b-4t78w
第2次访问：myapp-deploy-754bf8d64b-n6x58
第3次访问：myapp-deploy-754bf8d64b-dzkhj
```

**Headless Service**

Headless是ClusterIP分类的一种特殊使用方法。

有时不需要负载均衡和单独的Service IP。

遇到这种情况，可以通过指定`spec.clusterIP`的值为`None`来创建Headless Service。

这类Service并不会分配Cluster IP，kube-proxy不会处理它们，而Kubernetes也不会为它们进行负载均衡和路由。

`样例2：Headless Service`

一组Pod是可以对应多个Service的，无需再创建Deployment部署新的Pod。

创建Headless Service资源清单

``` sh
vim myapp-headless.yaml
```

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-headless
  namespace: default
spec:
  selector:
    app: myapp
  clusterIP: "None"
  ports:
  - port: 80
	targetPort: 80
```

应用清单创建Headless Service

``` sh
kubectl apply -f myapp-headless.yaml
```

检验Service

``` sh
# 查看Pod及其IP地址
kubectl get pod -o wide
NAME                            READY   STATUS    RESTARTS   AGE   IP             NODE      
myapp-deploy-754bf8d64b-4t78w   1/1     Running   0          81s   10.244.1.112   k8s-node01
myapp-deploy-754bf8d64b-dzkhj   1/1     Running   0          81s   10.244.2.118   k8s-node02
myapp-deploy-754bf8d64b-n6x58   1/1     Running   0          81s   10.244.1.111   k8s-node01

# 查看Service，myapp-headless的CLUSTER-IP字段是None
kubectl get svc
NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP   4d16h
myapp            ClusterIP   10.100.62.204   <none>        80/TCP    22h
myapp-headless   ClusterIP   None            <none>        80/TCP    9s

# 所有创建的Service都会默认写入CoreDNS，并分配一个域名（格式：Service名称.名称空间.svc.cluster.local.）

# 安装DNS解析工具的软件包
yum -y install bind-utils

# 查询Kubernetes集群内DNS服务器CoreDNS的IP地址
kubectl get pod -n kube-system -o wide | grep coredns
coredns-5c98db65d4-cpwmk               1/1     Running   12         8d    10.244.0.17     k8s-master01   
coredns-5c98db65d4-h52x5               1/1     Running   12         8d    10.244.0.16     k8s-master01   

# 使用dig解析CoreDNS分配给myapp-headless的默认域名
dig -t A myapp-headless.default.svc.cluster.local. @【'kubectl get pod -n kube-system -o wide | grep coredns'查询到的coredns的IP地址】
...
;; ANSWER SECTION:
myapp-headless.default.svc.cluster.local. 29 IN	A 10.244.1.111
myapp-headless.default.svc.cluster.local. 29 IN	A 10.244.1.112
myapp-headless.default.svc.cluster.local. 29 IN	A 10.244.2.118
...


# 也可以使用nslookup查询解析
nslookup myapp-headless.default.svc.cluster.local. 【'kubectl get pod -n kube-system -o wide | grep coredns'查询到的coredns的IP地址】
Server:		10.244.0.17
Address:	10.244.0.17#53

Name:	myapp-headless.default.svc.cluster.local
Address: 10.244.1.111
Name:	myapp-headless.default.svc.cluster.local
Address: 10.244.1.112
Name:	myapp-headless.default.svc.cluster.local
Address: 10.244.2.118
```

**NodePort**

NodePort的原理是在Node上开了一个端口，将向该端口的流量导入到kube-proxy，然后由kube-prox写入iptables策略，进一步将流量导向对应的Pod。

`样例3：NodePort`

创建NodePort的资源清单

``` sh 
vim nodeport.yaml
```

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp
  namespace: default
spec:
  type: NodePort
  selector:
    app: myapp
    release: stabel
  ports:
  - name: http
    port: 80
    targetPort: 80
```

应用资源清单创建NodePort Service

``` sh
kubectl apply -f nodeport.yaml
```

检验Service

``` sh
# 查看Service及其PORT字段中的外部端口号
kubectl get svc
NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP        4d17h
myapp            NodePort    10.100.62.204   <none>        80:30431/TCP   23h
myapp-headless   ClusterIP   None            <none>        80/TCP         48m

# 查看集群各节点是否已监听外部端口号（分别在k8s-master01、k8s-node01、k8s-node02执行命令）
ss -nultp | grep :30431

# 查看集群个节点的ipvs策略（分别在k8s-master01、k8s-node01、k8s-node02执行命令）
ipvsadm -Ln | grep -A3 `ifconfig | grep 192.168.66 | awk '{print $2}'`:30431

# 集群外（物理机）访问测试
curl 192.168.66.10:30431
```

**LoadBalancer**

`LoadBalancer`和`NodePort`其实是同一种方式。

区别在于`LoadBalancer`比`NodePort`多了一步，就是可以调用`云供应商（Cloud provider）`去创建`LB`来向节点导流。

> 此处由于LoadBalancer的样例演示需要使用到外部云厂商资源，不作样例分析
>
> 结合各云供应商的具体使用方法，参考链接：[Kubernetes官方文档-Service-LoadBalancer类型](https://kubernetes.io/zh/docs/concepts/services-networking/service/#loadbalancer)

**ExternalName **

ExternalName是Service的特例，它没有selector，也没有定义任何的端口和Endpoint。

相反地，对于运行在集群外部的服务（例如：Harbor），它通过返回该外部服务的别名这种方式来提供服务。

这种类型的Service通过返回CNAME和它的值，可以将服务映射到externalName字段的内容（例如：hub.example0.com）。

`样例4：ExternalName`

创建资源清单

``` sh
vim externalname.yaml
```

``` yaml
kind: Service
apiVersion: v1
metadata:
  name: my-service-1
  namespace: default
spec:
  type: ExternalName
  externalName: hub.example0.com
```

应用资源清单创建ExternalName Service

``` sh
kubectl apply -f externalname.yaml
```

检验Service

``` sh
查看svc
kubectl get svc
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP        PORT(S)        AGE
kubernetes       ClusterIP      10.96.0.1       <none>             443/TCP        4d18h
my-service-1     ExternalName   <none>          hub.example0.com   <none>         13s
myapp            NodePort       10.100.62.204   <none>             80:30431/TCP   24h
myapp-headless   ClusterIP      None            <none>             80/TCP         92m

# 查询Kubernetes集群内DNS服务器CoreDNS的IP地址
kubectl get pod -n kube-system -o wide | grep coredns
coredns-5c98db65d4-cpwmk               1/1     Running   12         8d    10.244.0.17     k8s-master01   
coredns-5c98db65d4-h52x5               1/1     Running   12         8d    10.244.0.16     k8s-master01   

# 使用nslookup查询解析CoreDNS分配给my-service-1的默认地址
nslookup my-service-1.default.svc.cluster.local. 【'kubectl get pod -n kube-system -o wide | grep coredns'查询到的coredns的IP地址】
Server:		10.244.0.17
Address:	10.244.0.17#53

my-service-1.default.svc.cluster.local	canonical name = hub.example0.com.

# 查询解析CoreDNS分配给my-service-1的默认地址时，将返回一个值"hub.example0.com"的CNAME记录。
# 访问这个服务的工作方式和其他的服务相同，唯一不同的是重定向发生在DNS层，而且不会进行代理或转发。
```

清除所有资源

```sh
kubectl delete svc --all
kubectl delete deployment --all 
```

### Ingress

#### 概念简介

> **背景**
>
> Service只支持4层负载均衡，而Ingress有7层功能。
>
> Ingress实现的解决方案不止一种（如Ingress-Nginx、Ingress-Haproxy...）
>
> 本教程以Ingress-Nginx为例：
>
> Ingress-Nginx github项目地址：[GitHub-kubernetes/ingress-nginx](https://github.com/kubernetes/ingress-nginx)
>
> Ingress-Nginx官方网站：[NGINX Ingress](https://kubernetes.github.io/ingress-nginx/)
>
> `Nginx`可以通过虚拟主机域名区分不同的服务，而每个服务可以通过`upstream配置`进行定义不同的负载均衡池，再加上`location配置`进行负载均衡的反向代理，在日常使用中只需要修改`nginx.conf`即可实现，但是在`K8S`中又该如何实现这种方式调度呢？

K8S引入了Ingress自动进行服务的调度，Ingress包含两大组件：Ingress和Ingress Controller。

![image](https://s2.loli.net/2022/01/30/UwR3NLv8JtK5Fld.jpg)

**工作原理**

Ingress：修改Nginx配置的操作，被抽象成了Ingress对象。

Ingress Controller：Ingress Controller通过与kubernetes API交互，动态地感知集群中Ingress规则变化，然后读取它，按照自己的模板生成一段Nginx配置，再写到Nginx Pod中，最后reload重置Nginx读取配置。

#### Ingress安装

> **安装说明**
>
> 目前Ingress-Nginx的官方在线安装教程已不支持旧版本K8S（1.18或更早）
>
> 本教程将采用github（[ingress-nginx0.25.0/deploy/GitHub](https://github.com/kubernetes/ingress-nginx/tree/nginx-0.25.1/deploy/static)）的资源清单进行安装
>
> 新版在线安装可参考Ingress-Nginx官方安装向导：[Installation Guide](https://kubernetes.github.io/ingress-nginx/deploy/)

下载资源清单

``` sh
# 创建Ingress资源存放目录
mkdir /usr/local/install-k8s/plugin/ingress

# 下载两个资源清单
wget -O /usr/local/install-k8s/plugin/ingress/mandatory.yaml https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.25.1/deploy/static/mandatory.yaml

wget -O /usr/local/install-k8s/plugin/ingress/service-nodeport.yaml https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.25.1/deploy/static/provider/baremetal/service-nodeport.yaml
```

应用资源清单创建Ingress Controller

``` sh
# 应用资源清单
kubectl apply -f /usr/local/install-k8s/plugin/ingress/mandatory.yaml

# 查看是否完成创建
kubectl get pod -n ingress-nginx 
NAME                                        READY   STATUS    RESTARTS   AGE
nginx-ingress-controller-7995bd9c47-gb9rn   1/1     Running   0          23s
```

为Ingress Controller创建一个Service（模式为NodePort，提供集群外访问Ingress的入口）

``` sh
# 应用资源清单
kubectl apply -f /usr/local/install-k8s/plugin/ingress/service-nodeport.yaml

# 查看是否完成创建
kubectl get svc -n ingress-nginx 
NAME            TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx   NodePort   10.101.27.122   <none>        80:31922/TCP,443:31616/TCP   61s
```

#### Ingress样例

**样例1：Ingress-HTTP代理访问**

创建应用的Deployment和Service资源清单

``` sh
vim ingress-deployment-svc-http.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-dm
spec:
  replicas: 2
  template:
    metadata:
      labels:
        name: nginx
    spec:
      containers:
        - name: nginx
          image: cheungjune/myapp:v1
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 80
 
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  selector:
    name: nginx
```

应用清单创建应用的Deployment和Service

``` sh
kubectl apply -f ingress-deployment-svc-http.yaml
```

查看检验Deployment和Service

``` sh
# 查看Pod
kubectl get pod
NAME                            READY   STATUS    RESTARTS   AGE
myapp-deploy-754bf8d64b-4t78w   1/1     Running   3          2d2h
myapp-deploy-754bf8d64b-dzkhj   1/1     Running   3          2d2h
myapp-deploy-754bf8d64b-n6x58   1/1     Running   3          2d2h
nginx-dm-5946567889-f5kdq       1/1     Running   0          12s
nginx-dm-5946567889-gjlhz       1/1     Running   0          12s

# 查看Service
kubectl get svc
NAME             TYPE           CLUSTER-IP       EXTERNAL-IP        PORT(S)        AGE
kubernetes       ClusterIP      10.96.0.1        <none>             443/TCP        5d19h
my-service-1     ExternalName   <none>           hub.example0.com   <none>         25h
myapp            NodePort       10.100.62.204    <none>             80:30431/TCP   2d2h
myapp-headless   ClusterIP      None             <none>             80/TCP         27h
nginx-svc        ClusterIP      10.100.173.202   <none>             80/TCP         17s
```

创建Ingress，为Service：nginx-svc做基于域名的7层负载均衡

``` sh
vim ingress-http.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: nginx-test
spec:
  rules:
    - host: www1.example0.com
      http:
        paths:
        - path: /
          backend:
            serviceName: nginx-svc
            servicePort: 80
```

``` sh
kubectl create -f ingress-http.yaml
```

查看检验Ingress

``` sh
# 查看Ingress
kubectl get ingress -o wide
NAME         HOSTS               ADDRESS   PORTS   AGE
nginx-test   www1.example0.com             80      7s

# 查看Ingress的Service外部端口号
kubectl get svc -n ingress-nginx 
NAME            TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx   NodePort   10.101.27.122   <none>        80:31922/TCP,443:31616/TCP   14h
```

【修改物理机host文件，增加对域名www1.example0.com--master01虚拟机IP地址的解析】

然后物理机浏览器访问测试：

【其中端口号为'kubectl get svc -n ingress-nginx'查询到的80对应外部端口号】

地址：http://www1.example0.com:31922/hostname.html

多次刷新访问，在两个副本之间轮询

【第一次访问】

<img src="https://s2.loli.net/2022/01/31/EzDC4GMRj7VNt2H.png" alt="image-20220131140807365" style="zoom:80%;" /> 

【第二次访问】

![image-20220131140909720](https://s2.loli.net/2022/01/31/PU1BqwvdN8469lJ.png) 

清除所有资源

``` sh
kubectl delete svc --all
kubectl delete deployment --all 
kubectl delete ingress --all
```

**样例2：Ingress-VirtualHost**

创建Ingress虚拟WEB主机资源存放目录

``` sh
mkdir ingress-virtualhost
```

创建第一个虚拟主机的Deployment和Service

``` sh
vim ingress-virtualhost/deployment1-svc1.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: deployment1
spec:
  replicas: 2
  template:
    metadata:
      labels:
        name: nginx1
    spec:
      containers:
        - name: nginx1
          image: cheungjune/myapp:v1
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 80
 
---
apiVersion: v1
kind: Service
metadata:
  name: svc1
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  selector:
    name: nginx1
```

``` sh
kubectl apply -f ingress-virtualhost/deployment1-svc1.yaml
```

查看检验Deployment和Service

``` sh
# 查看Deployment
kubectl get deployment
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
deployment1   2/2     2            2           5s

# 查看Service
kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   2m22s
svc1         ClusterIP   10.105.11.217   <none>        80/TCP    8s

# 访问测试
curl 【'kubectl get svc'查询到的IP地址】
Hello MyApp | Version: v1 | <a href="hostname.html">Pod Name</a>

```

创建第二个虚拟主机的Deployment和Service

``` sh
vim ingress-virtualhost/deployment2-svc2.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: deployment2
spec:
  replicas: 2
  template:
    metadata:
      labels:
        name: nginx2
    spec:
      containers:
        - name: nginx2
          image: cheungjune/myapp:v2
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 80
 
---
apiVersion: v1
kind: Service
metadata:
  name: svc2
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  selector:
    name: nginx2
```

``` sh
kubectl apply -f ingress-virtualhost/deployment2-svc2.yaml
```

查看检验Deployment和Service

``` sh
# 查看Deployment
kubectl get deployment
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
deployment1   2/2     2            2           10m
deployment2   2/2     2            2           16s

# 查看Service
kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   12m
svc1         ClusterIP   10.105.11.217    <none>        80/TCP    10m
svc2         ClusterIP   10.109.173.143   <none>        80/TCP    3s

# 访问测试
curl 【'kubectl get svc'查询到的IP地址】
Hello MyApp | Version: v2 | <a href="hostname.html">Pod Name</a>
```

创建Ingress，实现svc1和svc2基于域名的虚拟web主机

``` sh
vim ingress-virtualhost/ingressrule.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress1
spec:
  rules:
    - host: www1.example0.com
      http:
        paths:
        - path: /
          backend:
            serviceName: svc1
            servicePort: 80
--- 
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress2
spec:
  rules:
    - host: www2.example0.com
      http:
        paths:
        - path: /
          backend:
            serviceName: svc2
            servicePort: 80
```

``` sh
kubectl apply -f ingress-virtualhost/ingressrule.yaml
```

进入Ingress容器查看配置

``` sh
# 连接容器管理终端
kubectl -it exec -n ingress-nginx `kubectl get pod -n ingress-nginx | awk '/nginx/{print $1}'` -- /bin/bash

在容器管理终端'www-data@nginx-ingress-controller-7995bd9c47-gb9rn:/etc/nginx$'执行命令
cat nginx.conf 
```

查看检验Ingress

``` sh
kubectl get svc -n ingress-nginx 
NAME            TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx   NodePort   10.101.27.122   <none>        80:31922/TCP,443:31616/TCP   15h
```

【修改物理机host文件，增加对域名www2.example0.com--master01虚拟机IP地址的解析】

然后物理机浏览器访问测试：

【其中端口号为'kubectl get svc -n ingress-nginx'查询到的80对应外部端口号】

地址：http://www1.example0.com:31922

![image-20220131144829985](https://s2.loli.net/2022/01/31/VLKFGv8ltEYfQry.png) 

地址：http://www2.example0.com:31922

![image-20220131144912787](https://s2.loli.net/2022/01/31/szeTrQmCvBbfwah.png) 

清除所有资源

``` sh
kubectl delete svc --all
kubectl delete deployment --all 
kubectl delete ingress --all
```

**样例3：Ingress-HTTPS代理访问**

创建证书和Secret

> **Secret说明**
>
> 用于保存敏感信息的对象，例如密码、OAuth令牌和SSH密钥等。
>
> 将这些信息放Secret中比放在Pod的定义或者容器镜像中来说更加安全和灵活。

``` sh
# 创建证书和密钥
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt -subj "/CN=nginxsvc/O=nginxsvc"

# 查看证书和密钥
ls server.*

# 创建Secret保存证书和密钥
kubectl create secret tls server-secret --key server.key --cert server.crt 

# 查看Secret
kubectl get secret
NAME                  TYPE                                  DATA   AGE
default-token-z7qzt   kubernetes.io/service-account-token   3      9d
server-secret         kubernetes.io/tls                     2      8s
```

创建Deployment和Service

``` sh
vim ingress-deployment-svc-https.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-https
spec:
  replicas: 2
  template:
    metadata:
      labels:
        name: nginx
    spec:
      containers:
        - name: nginx
          image: cheungjune/myapp:v1
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 80

---
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  selector:
    name: nginx
```

``` sh
kubectl apply -f ingress-deployment-svc-https.yaml
```

查看检验Deployment和Service

``` sh
kubectl get deployment
kubectl get svc
```

创建Ingress，实现HTTPS代理访问

``` sh
vim ingress-https.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: nginx-https
spec:
  tls:
    - hosts:
      - www3.example0.com
      secretName: server-secret
  rules:
    - host: www3.example0.com
      http:
        paths:
        - path: /
          backend:
            serviceName: nginx-svc
            servicePort: 80
```

``` sh
kubectl apply -f ingress-https.yaml
```

查看检验Ingress

``` sh
kubectl get svc -n ingress-nginx 
NAME            TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx   NodePort   10.101.27.122   <none>        80:31922/TCP,443:31616/TCP   2d16h
```

【修改物理机host文件，增加对域名www3.example0.com--master01虚拟机IP地址的解析】

然后物理机浏览器访问测试：

【其中端口号为'kubectl get svc -n ingress-nginx'查询到的443对应外部端口号】

地址：https://www3.example0.com:31616/hotname.html

多次刷新访问，在两个副本之间轮询

【第一次访问】

![image-20220202160250910](https://s2.loli.net/2022/02/02/Rj1aEw7uheBcS53.png) 

【第二次访问】

![image-20220202160311031](https://s2.loli.net/2022/02/02/JXTaFhUznq8BdxN.png) 

清除所有资源

``` sh
kubectl delete svc --all
kubectl delete deployment --all 
kubectl delete ingress --all
```

**样例4：Ingress-BasicAuth**

创建一个包含BasicAuth验证用户的信息文件

``` sh
# 安装apache-httpd软件包获取htpasswd命令
yum -y install httpd

# 生成一个验证用户的信息文件（用户名tom和密码readhat）
htpasswd -c -b auth tom redhat
```

创建Secret保存验证用户的信息文件

``` sh
kubectl create secret generic basic-auth --from-file=auth
```

创建Deployment和Service

``` sh
vim ingress-deployment-svc-auth.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-auth
spec:
  replicas: 2
  template:
    metadata:
      labels:
        name: nginx
    spec:
      containers:
        - name: nginx
          image: cheungjune/myapp:v1
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 80

---
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  selector:
    name: nginx
```

``` sh
kubectl apply -f ingress-deployment-svc-auth.yaml
```

查看检验Deployment和Service

``` sh
kubectl get deployment
kubectl get svc
```

创建Ingress，实现Auth验证登录访问

``` sh
vim ingress-auth.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-with-auth
  annotations:
    nginx.ingress.kubernetes.io/auth-type: basic
    nginx.ingress.kubernetes.io/auth-secret: basic-auth
    nginx.ingress.kubernetes.io/auth-realm: 'Authentication Required - tom'
spec:
  rules:
  - host: auth.example0.com
    http:
      paths:
      - path: /
        backend:
          serviceName: nginx-svc
          servicePort: 80
```

``` yaml
kubectl apply -f ingress-auth.yaml
```

查看检验Ingress

``` sh
kubectl get svc -n ingress-nginx 
NAME            TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx   NodePort   10.101.27.122   <none>        80:31922/TCP,443:31616/TCP   2d16h
```

【修改物理机host文件，增加对域名auth.example0.com--master01虚拟机IP地址的解析】

然后物理机浏览器访问测试：

【其中端口号为'kubectl get svc -n ingress-nginx'查询到的80对应外部端口号】

地址：http://auth.example0.com:31922

【根据提示输入用户名tom和密码redhat】

<img src="https://s2.loli.net/2022/02/02/Va4Ns3TSRzFJYWZ.png" alt="image-20220202174956191"  />

【验证通过后，返回网页内容】

![image-20220202175047927](https://s2.loli.net/2022/02/02/fRn63XaxqTQp5dF.png) 

清除所有资源

``` sh
kubectl delete svc --all
kubectl delete deployment --all 
kubectl delete ingress --all
```

**样例4：Ingress-ReWrite**

常用Nginx-Rewrite字段

| 名称                                           | 描述                                                         | 值     |
| ---------------------------------------------- | ------------------------------------------------------------ | ------ |
| nginx.ingress.kubernetes.io/rewrite-target     | 必须重定向流量的目标URI                                      | 字符串 |
| nginx.ingress.kubernetes.io/ssl-redirect       | 指示位置部分是否仅可访问SSL（当Ingress包含证书时默认为True） | 布尔   |
| nginx.ingress.kubernetes.io/force-ssl-redirect | 即使Ingress未启用TLS，也强制重定向到HTTPS                    | 布尔   |
| nginx.ingress.kubernetes.io/app-root           | 定义Controller必须重定向的应用程序根，如果它在'/'上下文中    | 字符串 |
| nginx.ingress.kubernetes.io/use-regex          | 指示Ingress上定义的路径是否使用正则表达式                    | 布尔   |

创建Ingress，实现地址重定向访问

> **说明**
>
> 样例中将会把访问重定向指向Kubernetes官网（https://kubernetes.io/zh/），所以不需要再创建Deployment和Service。

``` sh
vim ingress-rewrite.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: nginx-rewrite
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: https://kubernetes.io/zh/
spec:
  rules:
  - host: rewrite.example0.com
    http:
      paths:
      - path: /
        backend:
          serviceName: nginx-svc
          servicePort: 80
```

``` yaml
kubectl apply -f ingress-rewrite.yaml
```

查看检验Ingress

``` sh
kubectl get svc -n ingress-nginx 
NAME            TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx   NodePort   10.101.27.122   <none>        80:31922/TCP,443:31616/TCP   2d16h
```

【修改物理机host文件，增加对域名rewrite.example0.com--master01虚拟机IP地址的解析】

然后物理机浏览器访问测试：

【其中端口号为'kubectl get svc -n ingress-nginx'查询到的80对应外部端口号】

地址：http://rewrite.example0.com:31922

![image-20220202184333722](https://s2.loli.net/2022/02/02/TJsbR6NKrdLuYnS.png) 

【访问会重定向自动跳转到指定的https://kubernetes.io/zh/】

![image-20220202184509024](https://s2.loli.net/2022/02/02/64PCkxtwdb1OS5q.png) 

清除所有资源

``` sh
kubectl delete svc --all
kubectl delete deployment --all 
kubectl delete ingress --all
```

> **Ingress-Nginx样例说明**
>
> Ingress-Nginx的用法还有很多，官网也列举了一些用法样例，详情可参考：[NGINX Ingress Examples](https://kubernetes.github.io/ingress-nginx/examples/)

## 存储

> **存储-背景**
>
> 在K8S中，容器本身是非持久化的，当容器崩溃后，Kubelet将以镜像的初始状态重新启动容器，但是此时之前容器的数据已经丢失，我们该如何保护好容器的数据呢？
>
> 在同一Pod中的容器往往需要共享一些数据，此时我们又该如何实现呢？
>
> 这个时候就需要存储来解决这两个问题。

### ConfigMap

#### 概念

ConfigMap功能在Kubernetes1.2版本中引入，应用程序会从配置文件、命令行参数、环境变量中读取配置信息。

ConfigMap提供了向容器中注入配置信息的机制。

ConfigMap可以用于保存单个属性，也可以保存整个配置文件或者JSON二进制对象。

#### 创建ConfigMap

**基于目录创建ConfigMap**

创建目录

``` sh
mkdir -p resource/configmap
```

创建两个测试文件，写入键值对测试内容

``` sh
vim resource/configmap/fruit.properties
```

``` tex
apple=8.0
orange=3.5
```

``` sh
vim resource/configmap/food.properties
```

``` tex
beef=55.0
pork=28.0
```

创建ConfigMap

``` sh
# 创建名为test-0-config的ConfigMap
kubectl create configmap test-0-config --from-file=/root/resource/configmap 

# 查看ConfigMap
kubectl get configmap
kubectl describe configmap test-0-config
kubectl get configmap test-0-config -o yaml
```

**基于文件创建ConfigMap**

创建一个测试文件，写入键值对测试内容

``` sh
vim resource/configmap/drink.properties
```

``` tex
tea=3.0
coffee=4.0
```

创建ConfigMap

``` sh
# --from-file参数可以多次使用指定多个文件
kubectl create configmap test-1-config --from-file=/root/resource/configmap/drink.properties --from-file=/root/resource/configmap/fruit.properties

# 查看ConfigMap
kubectl get configmap test-1-config -o yaml
```

**基于命令行指定值创建ConfigMap**

创建ConfigMap

``` sh
# --from-literal参数可以多次使用指定多个值
kubectl create configmap test-2-config --from-literal=chips=6.9 --from-literal=burger=4.0

# 查看ConfigMap
kubectl get configmap test-2-config -o yaml
```

#### Pod调用ConfigMap

**调用ConfigMap导入到环境变量**

创建ConfigMap资源清单,并应用清单创建ConfigMap

``` sh
vim configmap-env.yaml
```

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: special-config
  namespace: default
data:
  special.how: very
  special.type: charm
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: env-config
  namespace: default
data:
  log_level: INFO
```

```sh
kubectl apply -f configmap-env.yaml 
kubectl get configmap
```

创建Pod资源清单，导入ConfigMap中的值为环境变量

``` sh
vim pod-configmap-env.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod-0
spec:
  containers:
  - name: test-container-0
    image: cheungjune/myapp:v1
    command: [ "/bin/sh", "-c", "env" ]
    env:
      - name: SPECIAL_LEVEL_KEY
        valueFrom:
          configMapKeyRef:
            name: special-config
            key: special.how
      - name: SPECIAL_TYPE_KEY
        valueFrom:
          configMapKeyRef:
            name: special-config
            key: special.type
    envFrom:
    - configMapRef:
        name: env-config
  restartPolicy: Never
```

查看检验ConfigMap

``` sh
# 查看Pod
kubectl get pod
NAME            READY   STATUS      RESTARTS   AGE
dapi-test-pod-0   0/1     Completed   0          8s

# 查看Pod日志，过滤输出的环境变量值
kubectl logs dapi-test-pod-0 | egrep 'SPECIAL_LEVEL_KEY|SPECIAL_TYPE_KEY|log_level'
SPECIAL_TYPE_KEY=charm
SPECIAL_LEVEL_KEY=very
log_level=INFO

# 比对环境变量值和资源清单指定的值
# SPECIAL_LEVEL_KEY=ConfigMap资源清单special-config中special.how的值very
# SPECIAL_TYPE_KEY=ConfigMap资源清单special-config中special.type的值charm
# 导入ConfigMap资源清单env-config中的键值对log_level=INFO
```

**调用ConfigMap设置命令行参数**

创建Pod资源清单，导入ConfigMap中的值为命令行参数

``` sh
vim pod-configmap-cmd.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod-1
spec:
  containers:
  - name: test-container-1
    image: cheungjune/myapp:v1
    command: [ "/bin/sh", "-c", "echo $var_a $var_b" ]
    env:
    - name: var_a
      valueFrom:
        configMapKeyRef:
          name: special-config
          key: special.how
    - name: var_b
      valueFrom:
        configMapKeyRef:
          name: special-config
          key: special.type
  restartPolicy: Never
```

查看检验ConfigMap

``` sh
# 查看Pod
kubectl get pod
NAME              READY   STATUS      RESTARTS   AGE
dapi-test-pod-0   0/1     Completed   0          110s
dapi-test-pod-1   0/1     Completed   0          2s

# 查看Pod日志，过滤输出的环境变量值
kubectl logs dapi-test-pod-1
very charm

# 比对命令输出的变量值
# 容器启动命令'echo $var_a $var_b'中的$var_a和$var_a分别是
# special-config中special.how的值very
# special-config中special.type的值charm
# 所以日志中保存的输出结果是very charm
```

**通过数据卷插件调用ConfigMap**

创建Pod资源清单，数据卷插件有不同的选项。

最基本的用法是将文件写入数据卷，在这个文件中，键就是文件名，值就是文件内容。

``` sh
vim pod-configmap-volume.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod-2
spec:
  containers:
  - name: test-container-2
    image: cheungjune/myapp:v1
    command: [ "/bin/sh", "-c", "sleep 600" ]
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: special-config
  restartPolicy: Never
```

查看检验ConfigMap

``` sh
# 查看Pod
kubectl get pod
NAME              READY   STATUS      RESTARTS   AGE
dapi-test-pod-0   0/1     Completed   0          17m
dapi-test-pod-1   0/1     Completed   0          9m38s
dapi-test-pod-2   0/1     Completed   0          4s


# 进入容器管理终端
kubectl exec -it dapi-test-pod-2 -- /bin/sh

# 在容器管理终端中执行命令，查看文件是否创建成功
ls /etc/config
special.how   special.type

# 在容器管理终端中执行命令，查看文件内容
cat /etc/config/special.how
very

cat /etc/config/special.type
charm
```

#### 热更新ConfigMap

创建Deployment资源清单，导入ConfigMap中的键值对为Volume卷文件

``` sh
vim deployment-configmap-update_ol.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: my-nginx
spec:
  replicas: 1
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: cheungjune/myapp:v1
        ports:
        - containerPort: 80
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
      volumes:
      - name: config-volume
        configMap:
          name: env-config
```

查看检验ConfigMap

``` sh
# 查看Pod
kubectl get pod
NAME                        READY   STATUS      RESTARTS   AGE
dapi-test-pod-0             0/1     Completed   0          32m
dapi-test-pod-1             0/1     Completed   0          25m
dapi-test-pod-2             0/1     Completed   0          12m
my-nginx-564556959f-jkpwk   1/1     Running     0          17s

# 进入容器管理终端
kubectl exec -it my-nginx-564556959f-jkpwk -- /bin/sh

# 在容器管理终端中执行命令，查看文件是否创建成功
ls /etc/config
log_level

# 在容器管理终端中执行命令，查看文件内容
cat /etc/config/log_level
INFO
```

热更新ConfigMap

``` sh
# kubectl edit命令热更新修改ConfigMap的内容，将INFO改为DEBUG
kubectl edit configmap env-config
【末行模式匹配替换:% s/INFO/DEBUG/g】
```

查看检验热更新是否成功

``` sh
# 热更新修改后约10秒后，再次查看文件内容
kubectl exec -it my-nginx-564556959f-jkpwk -- cat /etc/config/log_level
```

清除所有资源

``` sh
kubectl delete deployment --all
kubectl delete pod --all
```

> **注意**
>
> 热更新ConfigMap后，原来导入的env不会同步更新，使用Volume挂载的数据需要一段时间后（约10秒）会同步更新。
>
> 
>
> 热更新ConfigMap只是触发文件内容发生改变。
>
> 应用通常不会自动感知配置文件的变化，也不会自动读取新的配置。

### Secret

#### 概念

Secret解决了密码、token、密钥等敏感数据的保存问题，使用Secret保存可以避免这些敏感数据暴露到Pod的资源清单或镜像中。

Secret可以通过Volume或者环境变量的方式被调用。

#### 分类

**ServiceAccount**

用来访问Kubernetes API，由Kubernetes自动创建，并自动挂载到Pod的/var/run/secrets/kubernetes.io/serviceaccount目录中

**Opaque**

base64编码格式的Secert，用来保存密码、密钥等

**kubernetes.io/dockerconfigjson**

用来保存私有docker registry的认证信息

#### Secret样例

**样例1：ServiceAccount**

``` sh
# 进入容器管理终端
kubectl exec -it -n kube-system kube-proxy-gnnvb -- /bin/sh

# 在容器管理终端中执行命令，查看ServiceAccount的挂载目录
ls /var/run/secrets/kubernetes.io/serviceaccount
ca.crt	namespace  token
```

**样例2：Opaque**

Opaque类型的数据是一个键值对，要求value是base64编码格式

``` sh
echo -n admin | base64
YWRtaW4=
echo -n redhat | base64
cmVkaGF0
```

创建Opaque类型的Secret

``` sh
vim secret-opaque.yaml
```

``` yaml
apiVersion: v1
kind: Secret
metadata: 
  name: secret-0
type: Opaque
data: 
  username: YWRtaW4=
  password: cmVkaGF0
```

``` sh
kubectl apply -f secret-opaque.yaml
```

`将Secret挂载到Volume卷文件中`

创建Pod并挂载Secret到Volume卷文件中

``` sh
vim secret-opaque-volume.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata: 
  labels: 
    name: secret-test
  name: secret-test
spec: 
  containers: 
  - name: db
    image: cheungjune/myapp:v1
    volumeMounts: 
    - name: secrets
      mountPath: /etc/config
  volumes: 
  - name: secrets
    secret: 
      secretName: secret-0
```

``` sh
kubectl apply -f secret-opaque-volume.yaml
```

查看检验Secret

``` sh
# 查看Pod
kubectl get pod
NAME          READY   STATUS    RESTARTS   AGE
secret-test   1/1     Running   0          8s

# 查看容器中对应挂载Volume卷文件username的内容
kubectl exec -it secret-test -- cat /etc/config/username
admin

# 查看容器中对应挂载Volume卷文件password的内容
kubectl exec -it secret-test -- cat /etc/config/password
redhat
```

`将Secret导入到环境变量`

创建Deployment并将Secret导入到环境变量

``` sh
vim secret-opaque-env.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: pod-deployment
spec:
  replicas: 2
  template:
    metadata:
      labels:
        app: pod-deployment
    spec:
      containers:
      - name: pod-1
        image: cheungjune/myapp:v1
        command: [ "/bin/sh", "-c", "env" ]
        ports:
        - containerPort: 80
        env:
        - name: TEST_USER
          valueFrom:
            secretKeyRef:
              name: secret-0
              key: username
        - name: TEST_PASSWORD
          valueFrom:
            secretKeyRef:
              name: secret-0
              key: password 
```

``` sh
kubectl apply -f secret-opaque-env.yaml
```

查看检验Secret

``` sh
# 查看Pod
kubectl get pod
NAME                              READY   STATUS      RESTARTS   AGE
pod-deployment-6db9d84965-hq7rl   0/1     Completed   2          23s
pod-deployment-6db9d84965-lpzgh   0/1     Completed   2          23s
secret-test                       1/1     Running     0          91s

# 查看Pod日志，过滤输出的环境变量值
kubectl logs pod-deployment-6db9d84965-hq7rl | grep TEST
TEST_PASSWORD=redhat
TEST_USER=admin

kubectl logs pod-deployment-6db9d84965-lpzgh | grep TEST
TEST_PASSWORD=redhat
TEST_USER=admin
```

清除所有资源

``` sh
kubectl delete deployment --all
kubectl delete pod --all
```

**样例3：kubernetes.io/dockerconfigjson**

登录Harbor创建一个私有仓库private

![image-20220208202801110](https://s2.loli.net/2022/02/08/hDNPUnWeyJM5gkc.png) 

在k8s-node01节点上推送镜像到Harbor私有仓库private

```sh
docker pull busybox
docker login hub.example0.com
docker tag busybox:latest hub.example0.com/private/test-image:v1
docker push hub.example0.com/private/test-image:v1
```

在k8s-node01、k8s-node02节点上删除所有相关镜像

``` sh
docker rmi hub.example0.com/private/test-image:v1 busybox:latest
```

在k8s-node01、k8s-node02节点上确保退出登录Harbor

``` sh
docker logout hub.example0.com
```

创建docker registry认证的Secret

``` sh
kubectl create secret docker-registry registry-key0 --docker-server=hub.example0.com --docker-username=admin --docker-password=Harbor12345
```

创建Pod，通过imagePullSecrets引用Secret

``` sh
vim secret-docker-registry.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata: 
  name: secret-docker
spec: 
  containers: 
  - name: secret-docker
    image: hub.example0.com/private/test-image:v1
    command: [ "/bin/sh", "-c", "sleep 600" ]
```

``` sh
kubectl apply -f secret-docker-registry.yaml
```

查看Pod，状态为ImagePullBackOff，镜像下载失败

``` sh
kubectl get pod 
NAME            READY   STATUS             RESTARTS   AGE
secret-docker   0/1     ImagePullBackOff   0          8s
```

删除资源

``` sh
kubectl delete -f secret-docker-registry.yaml
```

修改Pod资源清单，通过imagePullSecrets引用Secret

``` sh
vim secret-docker-registry.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata: 
  name: secret-docker
spec: 
  containers: 
  - name: secret-docker
    image: hub.example0.com/private/test-image:v1
    command: [ "/bin/sh", "-c", "sleep 600" ]
    imagePullSecrets:
  - name: registry-key0
```

查看检验Secret

``` sh
# 查看Pod
kubectl get pod -o wide
NAME            READY   STATUS    RESTARTS   AGE     IP             NODE
secret-docker   1/1     Running   0          2m17s   10.244.1.145   k8s-node01

# 检查Pod所在节点k8s-node01查看镜像是否下载成功
ssh root@k8s-node01 docker images | grep private

# 再次尝试在节点k8s-node01上手动下载该镜像，依然会报错（证明该镜确实需要登录才能下载）
ssh root@k8s-node01 docker pull hub.example0.com/private/test-image:v1
Error response from daemon: pull access denied for hub.example0.com/private/test-image, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
```

清除所有资源

``` sh
kubectl delete deployment --all
kubectl delete pod --all
```

### Volume

#### 概念

容器磁盘上的文件生命周期是短暂的，这就使得在容器中运行重要应用时会出现一些问题：

​	当容器崩溃时，Kubelet会重启它，容器以干净的状态（镜像最初的状态）重新启动,这会导致容器中的文件将丢失。

​	在Pod中同时运行多个容器时，这些容器之间通常需要共享文件。Kubernetes中的Volume抽象就很好的解决了这些问题。

Kubernetes中卷（Volume）的寿命与封装它的Pod相同。

所以卷的生命比Pod中的容器长，当容器被重启时数据仍然得以保存，当Pod不再存在时，卷也将不复存在。

Kubernetes支持多种类型的卷，Pod可以同时使用任意数量的卷。

> **Volume说明**
>
> Kubernetes支持多种类型的卷，如：awsElasticBlockStore、azureDisk、azureFile、cephfs、glusterfs、iscsi、nfs、secret...
>
> 本教程仅列举Volume常用用法，更多类型介绍和使用参考：[Kubernetes-Volumes](https://kubernetes.io/zh/docs/concepts/storage/volumes/)

#### Volume样例

**emptyDir**

当Pod被分配给节点时，emptyDir卷（空目录卷）会被创建，并且当Pod在该节点上运行期间，卷一直存在。

虽然Pod中的容器挂载emptyDir卷的路径可能相同也可能不同，但这些容器都可以读写emptyDir卷中相同的文件。

当出于任何原因从节点中删除Pod时，emptyDir中的数据将被永久删除。

容器崩溃并不会导致 Pod 被从节点上移除，因此容器崩溃期间emptyDir卷中的数据是安全的。

> **emptyDir用法**
>
> 缓存空间，如多个容器之间数据的整合合并，emptyDir作为临时存放空间
>
> 为耗时较长的计算任务提供检查点，以便任务能方便地从崩溃重启前状态继续执行。
>
> 当Web型容器需要提供数据时，用于保存内容管理容器加载的文件。

`样例1：emptyDir`

创建Pod，包含两个容器，均挂载emptyDir卷

``` sh
vim volume-emptydir.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata: 
  name: test-pod
spec: 
  containers: 
  - image: cheungjune/myapp:v1
    name: test-container1
    volumeMounts: 
    - mountPath: /cache
      name: cache-volume
  - image: busybox
    name: test-container2
    imagePullPolicy: IfNotPresent
    command: ['/bin/sh','-c','sleep 3600']
    volumeMounts: 
    - mountPath: /test
      name: cache-volume
  volumes: 
  - name: cache-volume
    emptyDir: {}
```

``` sh
kubectl apply -f volume-emptydir.yaml
```

查看检验emptyDir

``` sh
# 查看Pod
kubectl get pod
NAME       READY   STATUS    RESTARTS   AGE
test-pod   2/2     Running   0          24s

# 进入容器test-container1管理终端
kubectl exec -it test-pod -c test-container1 -- /bin/sh

# 在容器管理终端中执行命令
date > /cache/date.log

# 进入容器test-container2管理终端
kubectl exec -it test-pod -c test-container2 -- /bin/sh

# 在容器管理终端中执行命令
cat /test/date.log
date >> /test/date.log

# 再次进入容器test-container1管理终端
kubectl exec -it test-pod -c test-container1 -- /bin/sh

# 在容器管理终端中执行命令
cat /cache/date.log
```

清除所有资源

``` sh
kubectl delete pod --all
```

**hostPath**

hostPath卷能将主机节点文件系统上的文件或目录挂载到Pod中。

> **hostPath用法**
>
> 运行一个需要访问Docker内部的容器；可使用hostPath挂载/var/lib/docker路径。
>
> 在容器中运行cAdvisor（谷歌的容器监控服务）时，需要以hostPath方式挂载/sys。
>
> 借助hostPath使用cephfs、azureDisk等存储。

> **hostPath使用注意事项**
>
> HostPath卷可能会暴露特权系统凭据（例如Kubelet）或特权API（例如容器运行时套接字），可用于容器逃逸或攻击集群的其他部分。
>
> 通过同一个资源清单创建的具有相同配置的多个Pod会由于节点上文件的不同而在不同节点上有不同的行为。
>
> 当Kubernetes按照计划添加资源感知调度时，无法考虑hostPath使用的资源。
>
> 节点主机上创建的文件或目录如果只能由root用户写入，那么需要修改主机上的文件权限以便容器能够写入hostPath卷，或者在特权容器中以root身份运行进程（[Kubernetes-security-context](https://kubernetes.io/zh/docs/tasks/configure-pod-container/security-context/)）。

除了所需的path属性之外，用户还可以通过type字段为hostPath卷指定卷的类型：

| 取值              | 行为说明                                                     |
| ----------------- | ------------------------------------------------------------ |
| 空                | （默认）空字符串用于向后兼容，这意味着在挂载hostPath卷之前不会执行任何检查 |
| DirectoryOrCreate | 如果在给定的路径上没有任何东西存在，那么将根据需要创建一个空目录，权限设置为0755，与Kubelet具有相同的归属关系 |
| Directory         | 给定的路径下必须存在目录                                     |
| FileOrCreate      | 如果在给定的路径上没有任何东西存在，那么会根据需要创建一个空文件，权限设置为0644，与Kubelet具有相同的归属关系 |
| File              | 给定的路径下必须存在文件                                     |
| Socket            | 给定的路径下必须存在UNIX套接字                               |
| CharDevice        | 给定的路径下必须存在字符设备                                 |
| BlockDevice       | 给定的路径下必须存在块设备                                   |

`样例2：hostPath`

创建Pod，挂载hostPath卷

``` sh
vim volume-hostpath.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata: 
  name: test-pod
spec: 
  containers: 
  - image: cheungjune/myapp:v1
    name: test-container
    volumeMounts: 
    - mountPath: /test
      name: test-volume
  volumes: 
  - name: test-volume
    hostPath: 
      path: /data				# 物理机上的目录
      type: Directory			# 可选，指定hostPath类型
```

``` sh
ssh root@k8s-node01 mkdir /data
ssh root@k8s-node02 mkdir /data
kubectl apply -f volume-hostpath.yaml
```

查看检验hostPath

``` sh
# 查看Pod
kubectl get pod -o wide
NAME       READY   STATUS    RESTARTS   AGE   IP             NODE
test-pod   1/1     Running   0          9s    10.244.2.149   k8s-node02

# 进入容器管理终端
kubectl exec -it test-pod -- /bin/sh

# 在容器管理终端中执行命令
date > /test/date.log

# 在Pod运行节点上查看检验/data目录
ssh k8s-node02 cat /data/date.log
```

清除所有资源

``` sh
kubectl delete pod --all
```

### PV-PVC

#### 概念

`PersistentVolume（PV）`

PV是由管理员设置供应的存储，属于群集的一部分，是集群中的资源（就像节点也是集群中的资源一样）。

PV和普通的Volume一样，也是使用卷插件来实现的，只是它们拥有独立于Pod的生命周期。

此API对象记录了存储实现的方式和相关配置，支持nfs、iscsi、云供应商的存储系统...

`PersistentVolumeClaim（PVC）`

PVC是用户对存储的请求，概念上可以类比Pod：

​	创建Pod消耗节点资源，创建PVC消耗PV资源。

​	Pod可以请求特定数量的资源（CPU和内存），PVC可以请求特定的大小和挂载访问模式。

> **PV的供应方式**
>
> `静态供应`
>
> 集群管理员创建的PV，其中包含了可供群集用户使用的实际存储的细节（实现方式和相关配置），存在于Kubernetes API中，可供用户消费（使用）。
>
> `动态供应`
>
> 当管理员创建的静态PV都不匹配用户的PVC时， 集群可以尝试为该PVC动态供应一个存储卷。
>
> 这个操作时基于StorageClass实现的：
>
> ​	PVC必须请求某个存储类，同时集群管理员必须创建并配置该存储类，才能进行动态创建。
>
> ​	如果PVC指定存储类为""，则相当于禁止使用动态供应的卷。
>
> ​	集群管理员需要启用API server上的DefaultStorageClass（准入控制器），也就是需要设置API server组件的--admission-control标志值	为DefaultStorageClass）。

> **PV-PVC概念说明**
>
> `绑定`
>
> 用户创建一个带有特定存储容量和特定访问模式需求的PVC对象后，master节点监测到新的PVC对象，会寻找跟它匹配的PV卷，并将二者绑定到一起。
>
> 如果需要为新的PVC动态供应PV卷，则会将该PV卷绑定到这一PVC。否则，用户总是能获得他们请求的资源，只是所获得的PV卷可能会超出所请求的配置。
>
> 一旦绑定关系建立，则PVC绑定就是排他性的，PVC和PV之间的绑定时一种一对一的映射。
>
> 如果找不到匹配的PV卷，PVC会无限期地处于未绑定状态，直到与之匹配的PV卷可用时，PVC才会被绑定，例如：即使集群上供应了很多50Gi大小的PV卷，也无法与请求100Gi大小的PVC匹配，知道当新的100Gi大小的PV卷被加入到集群时，该PVC才会被绑定。
>
> 
>
> `PVC保护`
>
> PVC保护的目的是确保Pod正在使用的PVC不会从系统中移除，因为如果被移除的话可能会导致数据丢失。
>
> 如果用户删除了Pod正在使用的PVC，则该PVC不会被立即删除。PVC的删除将被推迟，直到PVC不再被任何Pod使用。
>
> 此外，如果管理员删除已绑定到某PVC的PV卷，该PV卷也不会被立即移除。PV的移除也要推迟到该PV不再绑定任何PVC。
>
> 
>
> `PV类型`
>
> PV类型以插件形式实现，K8S支持：awsElasticBlockStore、azureDisk、azureFile、cephfs、csi...
>
> 本教程仅列举PV-PVC常用用法，更多类型介绍和使用参考：[Kubernetes-persistent-volumes](https://kubernetes.io/zh/docs/concepts/storage/persistent-volumes/#types-of-persistent-volumes)
>
> 
>
> `PV挂载访问模式`
>
> PersistentVolume可以以资源提供者支持的任何方式挂载到主机上。
>
> 不同PV类型的卷支持不同的访问模式（具体参考：[Kubernetes-persistent-volumes-access-modes](https://kubernetes.io/zh/docs/concepts/storage/persistent-volumes/#access-modes)）。
>
> 每个卷同一时刻只能以一种访问模式挂载，即使该卷能够支持多种访问模式。
>
> 访问模式：
>
> ​	ReadWriteOnce：该卷可以被单个节点以读/写模式挂载
>
> ​	ReadOnlyMany：该卷可以被多个节点以只读模式挂载
>
> ​	ReadWriteMany：该卷可以被多个节点以读/写模式挂载
>
> 在命令行中，访问模式缩写为： 
>
> ​	RWO：ReadWriteOnce
>
> ​	ROX：ReadOnlyMany
>
> ​	RWX：ReadWriteMany
>
> 
>
> `回收策略`
>
> Retain（保留）：手动回收
>
> Recycle（回收）：基本擦除（rm -rf /thevolume/*）
>
> Delete（删除）：关联的存储资源（如：Azure Disk资源）被彻底删除
>
> 目前，只有NFS和HostPath支持Recycle策略，AWS EBS、GCE PD、Azure Disk和Cinder卷支持删除策略。
>
> 
>
> `状态`
>
> 卷可以处于以下的某种状态：
>
> ​	Available（可用）：一块空闲资源还没有被任何声明绑定
>
> ​	Bound（已绑定）：卷已经被声明绑定
>
> ​	Released（已释放）：声明被删除，但是资源还未被集群重新声明
>
> ​	Failed（失败）：该卷的自动回收失败
>
> 命令行会显示绑定到PV的PVC的名称

#### PV-PVC样例

**样例1：PersistentVolume-NFS**

在`Harbor`安装NFS服务器

``` sh
# 安装相关软件包
yum -y install nfs-common nfs-utils rpcbind

# 创建共享目录并设置权限和归属关系
mkdir /nfsdata{1..3}
chmod 666 /nfsdata1 /nfsdata2 /nfsdata3
chown nfsnobody /nfsdata{1..3}

# 修改配置文件发布共享目录
echo '/nfsdata1 *(rw,no_root_squash,no_all_squash,sync)' >>  /etc/exports
echo '/nfsdata2 *(rw,no_root_squash,no_all_squash,sync)' >>  /etc/exports
echo '/nfsdata3 *(rw,no_root_squash,no_all_squash,sync)' >>  /etc/exports

# 重启服务并设置服务开机自启
systemctl restart rpcbind && systemctl enable rpcbind
systemctl restart nfs && systemctl enable nfs

# 查看服务是否发布成功
showmount -e 192.168.66.100
```

在`k8s-node01`和`k8s-node02`安装nfs依赖包

``` sh
yum -y install nfs-utils rpcbind
```

创建PersistentVolume

``` sh
vim persistentvolume-nfs.yaml
```

``` yaml
apiVersion: v1
kind: PersistentVolume
metadata: 
  name: nfs-pv1
spec: 
  capacity: 
    storage: 1Gi
  accessModes: 
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: nfs
  nfs: 
    path: /nfsdata1
    server: 192.168.66.100
---
apiVersion: v1
kind: PersistentVolume
metadata: 
  name: nfs-pv2
spec: 
  capacity: 
    storage: 5Gi
  accessModes: 
  - ReadOnlyMany
  persistentVolumeReclaimPolicy: Retain
  storageClassName: nfs
  nfs: 
    path: /nfsdata2
    server: 192.168.66.100
---
apiVersion: v1
kind: PersistentVolume
metadata: 
  name: nfs-pv3
spec: 
  capacity: 
    storage: 1Gi
  accessModes: 
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: slow
  nfs: 
    path: /nfsdata3
    server: 192.168.66.100
```

``` sh
# 应用资源清单创建PersistentVolume
kubectl apply -f persistentvolume-nfs.yaml

# 查看PersistentVolume
kubectl get pv
NAME      CAPACITY   ACCESS MODES   RECLAIM POLICY    STATUS      CLAIM   STORAGECLASS
nfs-pv1   1Gi        RWO            Retain            Available           nfs                     
nfs-pv2   5Gi        ROX            Retain            Available           nfs                     
nfs-pv3   1Gi        RWO            Retain            Available           slow                    
```

创建Pod和PersistentVolumeClaim

``` sh
vim pod-persistentvolume-nfs-pvc.yaml
```

``` yaml
apiVersion: v1
kind: Service
metadata: 
  name: nginx
  labels: 
    app: nginx
spec: 
  ports: 
  - port: 80
    name: web
  clusterIP: None
  selector: 
    app: nginx
--- 
apiVersion: apps/v1
kind: StatefulSet
metadata: 
  name: web
spec: 
  selector: 
    matchLabels: 
      app: nginx
  serviceName: "nginx"
  replicas: 3
  template: 
    metadata:
      labels: 
        app: nginx
    spec: 
      containers: 
      - name: nginx
        image: cheungjune/myapp:v1
        ports: 
        - containerPort: 80
          name: web
        volumeMounts: 
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates: 					# 定义PV
  - metadata: 
      name: www
    spec: 
      accessModes: ["ReadWriteOnce"]
      storageClassName: "nfs"
      resources: 
        requests: 
          storage: 1Gi
```

``` sh
kubectl apply -f pod-persistentvolume-nfs-pvc.yaml
```

查看检验PersistentVolume和PersistentVolumeClaim

``` sh
# 查看Pod,因为accessModes和storageClassName只有一个PV对应，所以web-1挂起
# 由于StatefulSet是按顺序逐个创建Pod的，所以第二个Pod为创建完成不会创建第三个Pod
kubectl get pod
NAME    READY   STATUS    RESTARTS   AGE
web-0   1/1     Running   0          13s
web-1   0/1     Pending   0          10s

# 将nfs-pv2的accessModes修改为ReadWriteOnce
# 将nfs-pv3的storageClassName修改为nfs
sed -i 's/ReadOnlyMany/ReadWriteOnce/g' persistentvolume-nfs.yaml
sed -i 's/slow/nfs/g' persistentvolume-nfs.yaml
kubectl delete pv nfs-pv2 nfs-pv3
kubectl apply -f persistentvolume-nfs.yaml

# 修改后3个PersistentVolume都符合要求，再次查看PersistentVolume和Pod
kubectl get pv
NAME      CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM               STORAGECLASS
nfs-pv1   1Gi        RWO            Retain           Bound    default/www-web-0   nfs
nfs-pv2   5Gi        RWO            Retain           Bound    default/www-web-2   nfs
nfs-pv3   1Gi        RWO            Retain           Bound    default/www-web-1   nfs

kubectl get pod -o wide
NAME    READY   STATUS    RESTARTS   AGE     IP             NODE
web-0   1/1     Running   0          20m     10.244.2.150   k8s-node02
web-1   1/1     Running   0          20m     10.244.1.147   k8s-node01
web-2   1/1     Running   0          5m54s   10.244.2.151   k8s-node02

# 在k8s-master01上挂载nfs并写入一个文件index.html
mount -t nfs 192.168.66.100:/nfsdata1 /tmp
echo hello world > /tmp/index.html

# 访问测试（Pod中挂载点是Nginx的网页文件根目录，可通过HTTP协议访问）
curl 10.244.2.150

# 删除Pod
kubectl delete pod web-0

# 再次访问自愈重新拉起Pod后，数据不变
kubectl get pod -o wide
NAME    READY   STATUS    RESTARTS   AGE   IP             NODE
web-0   1/1     Running   0          38s   10.244.2.152   k8s-node02
web-1   1/1     Running   0          26m   10.244.1.147   k8s-node01
web-2   1/1     Running   0          12m   10.244.2.151   k8s-node02
curl 10.244.2.152
```

> **StatefulSet特点补充**
>
> 1. StatefulSet创建的Pod名称(PodName)固定格式是：`StatefulSet名称-序号`，如：样例中web-0、web-1
> 2. StatefulSet为每个Pod副本创建了一个DNS域名，这个域名的格式是：`Pod名称.Headless ServerName`，即服务间是通过Pod域名来通信而非Pod IP，因为当Pod所在Node发生故障时，Pod会被飘移到其它Node上，Pod IP会发生变化，但是Pod域名不会有变化
> 3. StatefulSet使用Headless服务来控制Pod的域名，这个域名的FQDN格式是：`Service名称.名称空间.svc.cluster.local.`，其中cluster.local指的是集群的域名
> 4. 根据volumeClaimTemplates，为每个Pod创建一个PVC，PVC的命名规则格式是：VolumeClaimTemplates名称-Pod名称，如：样例中VolumeClaimTemplates名称是www，Pod名称是web-0，则创建出来的PVC是www-web-0
> 5. 删除Pod不会删除其PVC，手动删除PVC将自动释放PV（释放后还需要手动配置解除PVC和PV绑定关系才可以回收再使用）

删除控制器StatefulSet、Service

``` sh
kubectl delete statefulset --all
kubectl delete service nginx
```

删除PersistentVolumeClaim，回收PersistentVolume

``` sh
# 删除PersistentVolumeClaim
kubectl delete pvc --all

# 查看PersistentVolume，状态变成Released
kubectl get pv
NAME      CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS     CLAIM               STORAGECLASS
nfs-pv1   1Gi        RWO            Retain           Released   default/www-web-0   nfs
nfs-pv2   5Gi        RWO            Retain           Released   default/www-web-2   nfs
nfs-pv3   1Gi        RWO            Retain           Released   default/www-web-1   nfs

# 回收PersistentVolume
# claimRef字段的配置是PV和PVC的绑定关系配置
# 该配置在PVC删除后不会自动解除，需要手动删除
# 删除claimRef配置后，将会解除PV和PVC的绑定关系，PV才能被重新使用
kubectl edit pv nfs-pv1
【删除第24-30行，claimRef字段的配置】
kubectl edit pv nfs-pv2
【删除第24-30行，claimRef字段的配置】
kubectl edit pv nfs-pv3
【删除第24-30行，claimRef字段的配置】

# 再次查看PersistentVolume
kubectl get pv
NAME      CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS
nfs-pv1   1Gi        RWO            Retain           Available           nfs
nfs-pv2   5Gi        RWO            Retain           Available           nfs
nfs-pv3   1Gi        RWO            Retain           Available           nfs
```

## 集群调度

### 调度器简介

#### Scheduler

Scheduler是Kubernetes的调度器，主要的任务是把定义的Pod分配到集群的节点上，这个过程需要考虑以下问题：

公平：如何保证每个节点都能被分配资源

资源高效利用：集群所有资源最大化被使用

效率：调度的性能要好，能够尽快地对大批量的Pod完成调度工作

灵活：允许用户根据自己的需求控制调度的逻辑

Scheduler是单独运行的程序，启动之后会一直与apiserver保持连接，以获取PodSpec.NodeName为空的Pod，然后对每个Pod创建一个binding，表明该Pod应该放到哪个节点上。

#### 调度过程

1. 先是过滤掉不满足条件的节点，这个过程称为Predicate（预选）

   > **Predicate算法**
   >
   > PodFitsResources：节点上剩余的资源是否大于Pod请求的资源
   >
   > PodFitsHost：如果Pod指定了NodeName，检查节点名称是否和NodeName匹配
   >
   > PodFitsHostPorts：节点上已经使用的Port是否和Pod申请的Port冲突
   >
   > PodSelectorMatches：过滤掉和Pod指定的Label不匹配的节点
   >
   > NoDiskConflict：已经mount的Volume和Pod指定的Volume不冲突，除非它们都是只读
   >
   > 
   >
   > `如果在Predicate过程中没有合适的节点，Pod会一直在pending状态，不断重试调度，直到有节点满足条件。`

2. 经过Predicate，如果有多个节点满足条件，就对通过的节点按照优先级排序，这个是Priority（优选）

   > `优先级由一系列键值对组成，键是该优先级选项的名称，值是它的权重。`
   >
   > 
   >
   > **Priority选项**
   >
   > LeastRequestedPriority：通过计算CPU和Memory的使用率来决定权重，使用率越低权重越高。即这个优先级指标倾向于资源使用比例更低的节点
   >
   > BalancedResourceAllocation：节点上CPU和Memory使用率越接近，权重越高。通常与LeastRequestedPriority一起使用，不单独使用
   >
   > ImageLocalityPriority：倾向于已经下载过Pod要使用镜像的节点，镜像总大小值越大，权重越高
   >
   > 
   >
   > `通过算法对所有的优先级项目和权重进行计算，得出最终的结果。`

3. 最后从中选择优先级最高的节点

#### 自定义调度器

除了K8S自带的调度器，还可以自定义调度器。

通过spec:schedulername参数指定调度器的名字，可以为Pod选择某个调度器进行调度。

> 关于自定义创建和指定调度器，详情参考：[Kubernetes | configure-multiple-schedulers](https://kubernetes.io/zh/docs/tasks/extend-kubernetes/configure-multiple-schedulers/)

### 调度选择

#### Node亲和性

**分类**

spec.affinity.nodeAffinity：

硬策略：requiredDuringSchedulingIgnoredDuringExecution（要求执行计划，不服从调剂）

软策略：preferredDuringSchedulingIgnoredDuringExecution（优先执行计划,服从调剂）

**键值说明**

| 键           | 说明                    |
| ------------ | ----------------------- |
| In           | Label的值在某个列表中   |
| NotIn        | Label的值不在某个列表中 |
| Gt           | Label的值大于某个值     |
| Lt           | Label的值小于某个值     |
| Exists       | 某个Label存在           |
| DoesNotExist | 某个Label不存在         |

> **说明**
>
> 以上所说的Label是指代命令'kubectl get node --show-labels'输出中的LABELS字段。

**样例1：requiredDuringSchedulingIgnoredDuringExecution**

创建一个3副本的Deployment（硬策略：不在k8s-node01创建）和一个Pod（硬策略：在k8s-node03创建）

``` sh
vim affinity-required.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: affinity-deployment
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: node-affinity-pod
    spec:
      containers:
      - name: with-node-affinity
        image: cheungjune/myapp:v1
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms: 
            - matchExpressions:
              - key: kubernetes.io/hostname
                operator: NotIn
                values:
                - k8s-node01
---
apiVersion: v1
kind: Pod
metadata: 
  name: affinity-pod
spec: 
  containers: 
  - name: with-node-affinity
    image: cheungjune/myapp:v1
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms: 
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: In
            values:
            - k8s-node03
```

``` sh
kubectl apply -f affinity-required.yaml
```

查看检验requiredDuringSchedulingIgnoredDuringExecution

``` sh
# 查看Pod
# Deployment部署的3副本均在k8s-node02创建
# Pod affinity-pod因为不存在k8s-node03，无法创建，状态为Pending
kubectl get pod -o wide
NAME                                   READY   STATUS    RESTARTS   AGE     NODE
affinity-deployment-748c4ddf95-gzq79   1/1     Running   0          3m19s   k8s-node02
affinity-deployment-748c4ddf95-r4pkn   1/1     Running   0          3m19s   k8s-node02
affinity-deployment-748c4ddf95-xdd76   1/1     Running   0          3m19s   k8s-node02
affinity-pod                           0/1     Pending   0          3m19s   <none>

# 描述Pod affinity-pod
kubectl describe pod affinity-pod
...
Events:
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  10s   default-scheduler  0/3 nodes are available: 3 node(s) didn't match node selector.
```

清除所有资源

``` SH
kubectl delete deployment --all
kubectl delete pod --all
```

**样例2：preferredDuringSchedulingIgnoredDuringExecution**

创建一个Pod（软策略：优先在k8s-node03创建，权重为1）

``` sh
vim affinity-preferred.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: affinity-preferred
  labels:
    app: node-affinity-pod
spec:
  containers:
  - name: with-node-affinity
    image: cheungjune/myapp:v1
  affinity:
    nodeAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference: 
          matchExpressions:
          - key: kubernetes.io/hostname
            operator: In
            values:
            - k8s-node03
```

``` sh
kubectl apply -f affinity-preferred.yaml
```

查看检验preferredDuringSchedulingIgnoredDuringExecution

```sh
# 查看Pod
# 软策略不强制执行，不存在k8s-node03则调度到其它节点创建
NAME                 READY   STATUS    RESTARTS   AGE   IP             NODE
affinity-preferred   1/1     Running   0          64s   10.244.1.151   k8s-node01
```

清除所有资源

```sh
kubectl delete deployment --all
kubectl delete pod --all
```

#### Pod亲和性

**分类**

spec.affinity.podAffinity/podAntiAffinity：

软策略：preferredDuringSchedulingIgnoredDuringExecution（优先执行计划）

硬策略：requiredDuringSchedulingIgnoredDuringExecution（要求执行计划）

**亲和性/反亲和性调度策略：**

| 调度策略        | 匹配标签                               | 操作符                             | 调度目标                   |
| --------------- | -------------------------------------- | ---------------------------------- | -------------------------- |
| nodeAffinity    | Node（kubectl get node --show-labels） | In,NotIn,Exists,DoesNotExist,Gt,Lt | 指定主机                   |
| podAffinity     | Pod（kubectl get pod --show-labels）   | In,NotIn,Exists,DoesNotExist       | Pod与指定Pod同一拓扑域     |
| podAnitAffinity | Pod（kubectl get pod --show-labels）   | In,NotIn,Exists,DoesNotExist       | Pod与指定Pod不在同一拓扑域 |

**样例1：podAffinity-podAnitAffinity**

创建Deployment（存储）并配置podAntiAffinity

用来确保调度器不会将所有副本调度到同一节点上

``` sh
vim deployment-podantiaffinity.yaml
```

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
spec:
  selector:
    matchLabels:
      app: store
  replicas: 2
  template:
    metadata:
      labels:
        app: store
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - store
            topologyKey: "kubernetes.io/hostname"
      containers:
      - name: redis-server
        image: redis
```

``` sh
kubectl apply -f deployment-podantiaffinity.yaml
```

查看检验Pod

``` sh
kubectl get pod -o wide
NAME                     READY   STATUS    RESTARTS   AGE   IP             NODE
redis-56d4776777-c8f8f   1/1     Running   0          38s   10.244.1.157   k8s-node01
redis-56d4776777-jvjpg   1/1     Running   0          38s   10.244.2.182   k8s-node02
```

再创建一个Deployment（网站）并配置配置了podAntiAffinity和podAffinity

将网站服务器的所有副本与具有app=store选择器标签的Pod放置在一起，同时这还确保了不会有两个web服务器的副本被调度到同一节点上

``` sh
vim deployment-podantiaffinity-podaffinity.yaml
```

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-server
spec:
  selector:
    matchLabels:
      app: web-store
  replicas: 2
  template:
    metadata:
      labels:
        app: web-store
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - web-store
            topologyKey: "kubernetes.io/hostname"
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - store
            topologyKey: "kubernetes.io/hostname"
      containers:
      - name: web-app
        image: cheungjune/myapp:v1
```

``` sh
kubectl apply -f deployment-podantiaffinity-podaffinity.yaml
```

查看检验效果

```sh
# 查看Pod所在节点和标签
kubectl get pod -o wide --show-labels
NAME                          READY   STATUS    NODE         LABELS
redis-56d4776777-c8f8f        1/1     Running   k8s-node01   app=store,pod-template-hash=56d4776777
redis-56d4776777-jvjpg        1/1     Running   k8s-node02   app=store,pod-template-hash=56d4776777
web-server-77d4c97d99-vznkx   1/1     Running   k8s-node01   app=web-store,pod-template-hash=77d4c97d99
web-server-77d4c97d99-xhp2s   1/1     Running   k8s-node02   app=web-store,pod-template-hash=77d4c97d99
```

清除所有资源

``` 
kubectl delete deployment --all
```

#### Taint

Taint（污点）：节点亲和性是Pod的一种属性，它使Pod被吸引到一类特定的节点，Taint则相反，它使节点能够排斥一类特定的Pod。

> **Taint组成**
>
> 每个污点的组成：key=value:effect
>
> 每个污点有一个key和value作为污点的标签，其中value可以为空（key:effect），effect描述污点的作用。
>
> effect支持如下三个选项：
>
> NoSchedule：K8S将不会把Pod调度到具有该污点的Node上
>
> PreferNoSchedule：K8S将尽量避免Pod调度到具有该污点的Node上
>
> NoExecute：K8S将不会把Pod调度到具有该污点的Node上，同时会将Node上已经存在的Pod驱逐出去
>
> 
>
> `Node被设置上污点之后就和Pod之间存在了一种相斥的关系，可以让Node拒绝Pod的调度执行，甚至将Node已经存在的Pod驱逐出去。`

**Taint用法**

``` sh
# 查看节点污点
kubectl describe node 节点名称 | grep Taints

# 设置污点
kubectl taint nodes 节点名称 key=value:effect

# 去除污点
kubectl taint nodes 节点名称 key:effect-
```

#### Toleration

Toleration（容忍）：我们可以`在Pod上设置`Toleration，设置了Toleration的Pod将可以（但不要求）容忍Taint的存在被调度到存在Taint的Node上。

**Toleration用法**

``` yaml
spec:
  tolerations:
    - key: "key1"
      operator: "Equal"
      value: "value1"
      effect: "NoSchedule"
      tolerationSeconds: 3600
    - key: "key1"
      operator: "Equal"
      value: "value1"
      effect: "NoExecute"
    - key: "key2"
      operator: "Exists"
      effect: "NoSchedule"
```

> **说明**
>
> key、value、effect要与Node上的Taint保持一致
>
> opprator的值是Exists时，忽略value值，只要存在key即可
>
> tolerationSeconds：当Pod需要被驱逐时可以在Pod上继续保留运行的时间

**其它用法**

当不指定key时，表示容忍所有的污点key

``` yaml
tolerations: 
- operator: "Exists"
```

当不指定effect时，表示容忍所有的污点作用

``` yaml
tolerations: 
- key: "key1"
operator: "Exists"
```

当有多个Master时，防止浪费资源，可以设置尽可能不在该节点运行（Node资源不足时会在Master创建Pod）

``` sh
kubectl taint nodes 节点名称 node-role.kubernetes.io/master=:PreferNoSchedule
```

**样例1：Taint-Toleration**

给k8s-node01和k8s-node01设置污点

``` sh
kubectl taint nodes k8s-node01 node_taint=k8s-node01:NoSchedule
```

创建一个Pod并设置容忍

``` sh
vim pod-taint-toleration.yaml
```

``` yaml
apiVersion: v1
kind: Pod
metadata: 
  name: pod01
  labels: 
    app: pod01
spec: 
  containers: 
  - name: c1
    image: cheungjune/myapp:v1
  tolerations: 
  - key: "node_taint"
    operator: "Equal"
    value: "k8s-node01"
    effect: "NoSchedule"
```

``` sh
kubectl apply -f pod-taint-toleration.yaml
```

查看检验

``` sh
# 查看Pod
kubectl get pod -o wide
NAME    READY   STATUS    RESTARTS   AGE   IP             NODE
pod01   1/1     Running   0          5s    10.244.2.186   k8s-node02

# 给k8s-node02设置污点
kubectl taint nodes k8s-node02 node_taint=k8s-node02:NoExecute

# K8S将Pod驱逐出去
kubectl get pod -o wide
NAME    READY   STATUS        RESTARTS   AGE   IP             NODE
pod01   0/1     Terminating   0          86s   10.244.2.186   k8s-node02

# 重新应用资源清单创建Pod
kubectl apply -f pod-taint-toleration.yaml

# k8s-node01可以容忍Pod
kubectl get pod -o wide
NAME    READY   STATUS    RESTARTS   AGE   IP             NODE
pod01   1/1     Running   0          3s    10.244.1.165   k8s-node01
```

清除所有资源，并去除污点

``` sh
kubectl delete pod --all
kubectl taint nodes k8s-node01 node_taint:NoSchedule-
kubectl taint nodes k8s-node02 node_taint:NoExecute-
```

#### 固定节点调度

**分类**

Pod.spec.nodeName：将Pod直接调度到指定的Node节点上，跳过Scheduler的调度策略，该匹配规则是强制匹配

Pod.spec.nodeSelector：通过Kubernetes的label-selector机制选择节点，由调度器调度策略匹配label，而后调度Pod到目标节点，该匹配规则是强制匹配

**样例1：Pod.spec.nodeName**

创建Pod并指定节点k8s-node01

``` sh
vim pod-nodename.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: myweb
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: myweb
    spec:
      nodeName: k8s-node01
      containers:
      - name: myweb
        image: cheungjune/myapp:v1
        ports:
        - containerPort: 80
```

``` sh
kubectl apply -f pod-nodename.yaml
```

查看检验

``` sh
# 查看Pod
kubectl get pod -o wide
NAME                     READY   STATUS    RESTARTS   AGE   IP             NODE
myweb-594f7ccfdc-6t8jw   1/1     Running   0          4s    10.244.1.164   k8s-node01
myweb-594f7ccfdc-7fngk   1/1     Running   0          4s    10.244.1.162   k8s-node01
myweb-594f7ccfdc-zldsp   1/1     Running   0          4s    10.244.1.163   k8s-node01
```

清除所有资源

``` sh
kubectl delete -f pod-nodename.yaml
```

**样例2：Pod.spec.nodeSelector**

给k8s-node02打标签type=backEndNode1

``` sh
kubectl label nodes k8s-node02 type=backEndNode1
```

``` sh
vim pod-nodeselector.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: myweb
spec:
  replicas: 2
  template:
    metadata:
      labels:
        app: myweb
    spec:
      nodeSelector:
        type: backEndNode1
      containers:
      - name: myweb
        image: cheungjune/myapp:v1
        ports:
        - containerPort: 80
```

``` sh
kubectl apply -f pod-nodeselector.yaml
```

查看检验

``` sh
# 确认type=backEndNode1标签是在哪个节点上
kubectl get node --show-labels | grep type=backEndNode1 | awk '{print $1}'
k8s-node02

# 查看Pod
kubectl get pod -o wide
NAME                    READY   STATUS    RESTARTS   AGE     IP             NODE
myweb-965b76d69-d8vfr   1/1     Running   0          2m10s   10.244.2.185   k8s-node02
myweb-965b76d69-h4nvp   1/1     Running   0          2m10s   10.244.2.184   k8s-node02
```

清除所有资源

``` sh
kubectl delete -f pod-nodeselector.yaml
```

## Kubernetes安全

### 安全机制

Kubernetes作为一个分布式集群的管理工具，保证集群的安全性是一个重要的任务。

API Server是集群内部各个组件通信的中枢，也是外部控制的入口，所以Kubernetes的安全机制基本就是围绕保护API Server来设计的。

Kubernetes使用了认证（Authentication）、鉴权（Authorization）、准入控制（AdmissionControl）三步来保证API Server的安全。

![image-20220214155901556](https://s2.loli.net/2022/02/14/sMBfU7CDwh1VzH9.png)

### Authentication

#### 认证方式分类

HTTP Token认证：通过一个Token来识别合法用户

- HTTP Token认证是用一个很长的特殊编码方式的并且难以被模仿的字符串Token来表达客户的一种方式。
- Token是一个很长的很复杂的字符串，每一个Token对应一个用户名存储在API Server能访问的文件中。
- 当客户端发起API调用请求时，需要在HTTP Header里放入Token

HTTP Base认证：通过用户名+密码的方式认证

- 用户名:密码用BASE64算法进行编码后的字符串放在HTTP Request中的HeatherAuthorization域里发送给服务端，服务端收到后进行反编码，获取用户名及密码

HTTPS证书认证：基于CA根证书签名的客户端身份认证方式

![img](https://s2.loli.net/2022/02/14/MEwRzpH2Qmx6Pgt.png) 

#### 认证组件说明

![image-20220214161439035](https://s2.loli.net/2022/02/14/i9AXzG87IOfmEjM.png) 

**需要认证的组件**

Kubenetes组件对API Server的访问：kubectl、Controller Manager、Scheduler、Kubelet、kube-proxy 

Kubernetes管理的Pod对容器的访问：Pod（dashborad也是以Pod形式运行）

![image-20220214162546589](https://s2.loli.net/2022/02/14/Ue3agqZ6r21sknb.png)

> **说明**
>
> Controller Manager、Scheduler与API Server在同一台机器，所以直接使用API Server的非安全端口访问，--insecure-bind-address=127.0.0.1
>
> kubectl、Kubelet、kube-proxy访问 API Server则需要证书进行HTTPS双向认证

**组件证书颁发**

手动签发：通过K8S集群的跟CA进行签发HTTPS证书 

自动签发：Kubelet首次访问API Server时，使用token进行认证，通过后，Controller Manager会为Kubelet生成一个证书，以后的访问都是用证书进行认证

#### kubeconfig

kubeconfig文件包含集群的参数（如：CA证书、API Server地址）、客户端参数（客户端生成的证书和私钥），集群context信息（集群名称、用户名）。

Kubernetes组件通过启动时指定不同的kubeconfig文件可以切换到不同的集群。

#### ServiceAccount

Pod中的容器访问API Server。因为Pod的创建、销毁是动态的，所以要为它手动生成证书是不可行的。 

Kubenetes使用了Service Account解决Pod访问API Server的认证问题。

#### Secret-ServiceAccount

Kubernetes设计了一种资源对象叫做Secret，分为两类，一种是用于ServiceAccount的service-account-token，另一种是用于保存用户自定义保密信息的Opaque。

ServiceAccount包含三个部分：token、ca.crt、namespace

​	token:使用API Server私钥签名的JWT，用于访问API Server时，Server端认证

​	ca.crt:根证书，用于Client端验证API Server发送的证书

​	namespace：标识这个service-account-token的作用域名空间

默认每个Namespace都会有一个ServiceAccount，如果Pod在创建时没有指定ServiceAccount，就会使用Pod所属的Namespace的ServiceAccount

### Authorization

Authentication认证过程，通信的双方都确认了对方是可信的，可以相互通信。

而Authorization鉴权是确定请求方有哪些资源的权限。

#### 鉴权方式分类

API Server目前支持以下几种授权策略（通过API Server的启动参数--authorization-mode设置）：

​	AlwaysDeny：表示拒绝所有的请求（一般用于测试）

​	AlwaysAllow：允许接收所有请求，如果集群不需要授权流程，则可以采用该策略（一般用于测试）

​	ABAC（Attribute-Based Access Control）：基于属性的访问控制，表示使用用户配置的授权规则对用户请求进行匹配和控制

​	Webhook：通过调用外部REST服务对用户进行授权

​	RBAC（Role-Based Access Control）：Kubernetes默认方式，基于角色的访问控制

#### RBAC鉴权

RBAC在Kubernetes 1.5中引入，现行版本的默认标准。

相对其它访问控制方式，RBAC拥有以下优势：

​	对集群中的资源和非资源均拥有完整的覆盖

​	整个RBAC由一些API对象完成，同其它API对象一样，可以用kubectl或API进行操作

​	可以在运行时进行调整，无需重启API Server

RBAC的API资源对象说明

RBAC包含4个资源对象：Role、ClusterRole、RoleBinding、ClusterRoleBinding，4种对象类型均可以通过kubectl与API操作。

<img src="https://s2.loli.net/2022/02/14/bLBylpITAfJGQmt.png" alt="图" style="zoom: 50%;" /> 

Kubenetes组件（kubectl、kube-proxy）或是其他自定义的用户在向CA申请证书时，需要提供一个证书请求文件(用户、组在这里面定义)

```json
{
	"CN": "admin",
	"hosts": [],
	"key": {
		"algo": "rsa",
		"size": 2048
	},
	"names": [{
		"C": "CN",
		"ST": "HangZhou",
		"L": "XS",
		"O": "system:masters",
		"OU": "System"
	}]
}
```

API Server会把客户端证书的CN字段作为User，把names.O字段作为Group；

Kubelet使用TLS Bootstaping认证时，API Server可以使用Bootstrap Tokens或者Token authenticationfile验证token，无论哪一种，Kubenetes都会为token绑定一个默认的User和Group；

Pod使用ServiceAccount认证时，service-account-token中的JWT会保存User信息；

有了用户信息，再创建一对角色/角色绑定(集群角色/集群角色绑定)资源对象，就可以完成权限绑定了。

#### Role和ClusterRole

在RBAC API中，Role表示一组规则权限，权限列表默认为空，需要什么权限则增加权限到列表（不存在拒绝某操作的规则）。

Role用于在某个Namespace内设置访问权限，在创建时，必须指定这个Role所属的名字空间。

相对地，ClusterRole则是一个集群作用域的资源。

ClusterRole有若干用法。你可以用它来：

​	定义对某Namespace对象的访问权限，并将在各个Namespace内完成授权

​	为Namespace作用域的对象设置访问权限，并跨所有Namespace执行授权

​	为集群作用域的资源定义访问权限

如果希望在Namespace内定义角色，应该使用Role。如果希望定义集群范围的角色，应该使用ClusterRole。

**Role示例**

下面是一个位于default名称空间的Role示例，可用来授予对Pod的读访问权限。

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
```

**ClusterRole示例**

ClusterRole具有与Role相同的权限角色控制能力，不同的是ClusterRole是集群级别的，ClusterRole可以用于：

​	集群级别的资源控制，如：Node访问权限

​	非资源型endpoints，如：/healthz访问

​	所有命名空间资源控制，如Pod

例如：可以使用ClusterRole来允许某特定用户执行命令'kubectl get pods --all-namespaces'

下面是一个ClusterRole的示例，可用来为任一特定Namespace中的Secret授予读访问权限，或者跨Namespace的访问权限：

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  # 不需要"namespace"，因为ClusterRoles不受名字空间限制
  name: secret-reader
rules:
- apiGroups: [""]
  # 在HTTP层面，用来访问Secret对象的资源的名称为"secrets"
  resources: ["secrets"]
  verbs: ["get", "watch", "list"]
```

#### RoleBinding和ClusterRoleBinding

RoleBinding是将角色中定义的权限赋予一个或者一组用户。

RoleBinding包含若干主体（用户、组或服务账户）的列表和对这些主体所获得的角色的引用。

RoleBinding在指定的Namespace中执行授权，而ClusterRoleBinding在集群范围执行授权。

**RoleBinding示例** 

下面的例子中的RoleBinding将名为pod-reader的Role授予在default名称空间中的用户jane。

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
# 你可以指定不止一个subject（主体）
- kind: User
  name: jane
  apiGroup: rbac.authorization.k8s.io
roleRef:
  # "roleRef"指定与某Role或ClusterRole的绑定关系
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

RoleBinding也可以引用ClusterRole，以将对应ClusterRole中定义的访问权限授予RoleBinding所在Namespace的资源。

这种引用方法使得管理者可以跨整个集群定义一组通用的角色，之后在多个Namespace中复用。

例如，下面的RoleBinding引用了一个ClusterRole，这个ClusterRole具有整个集群内对Secret的访问权限，但是其授权用户dave只能访问development空间中的Secret（因为RoleBinding定义在development命名空间）

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
# 此角色绑定使得用户dave能够读取development名字空间中的Secrets
kind: RoleBinding
metadata:
  name: read-secrets
  # RoleBinding的"namespace字段"决定了访问权限的授予范围
  namespace: development
subjects:
- kind: User
  name: dave
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

**ClusterRoleBinding示例** 

下面的ClusterRoleBinding允许manager组内的所有用户访问任何Namespace中的Secret。

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-secrets-global
subjects:
- kind: Group
  name: manager
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

> **注意**
>
> 创建了绑定之后，不能再修改绑定对象所引用的Role或ClusterRole。
>
> 试图改变绑定对象的roleRef将导致合法性检查错误。
>
> 如果想要改变现有绑定对象中roleRef字段的内容，必须删除重新创建绑定对象。
>
> subjects中kind:User或Group的name字段规定前缀system:是系统保留的，集群管理员应该确保普通用户不会使用这个前缀格式。

#### Resources

在Kubernetes API中，大多数资源都是使用对象名称的字符串表示来呈现与访问的。

例如，对于Pod应使用"pods"。RBAC使用对应API端点的URL中呈现的名字来引用资源。

有一些Kubernetes API涉及子资源（subresource），例如Pod的日志。对Pod日志的请求类似这样：

```http
GET /api/v1/namespaces/{namespace}/pods/{name}/log
```

在这里，pods对应名称空间作用域的Pod资源，而log是pods的子资源。在RBAC角色表达子资源时，使用斜线（/）来分隔资源和子资源。

要允许某主体读取pods同时访问这些Pod的log子资源，可以这么写：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-and-pod-logs-reader
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list"]
```

#### 创建用户和授权样例

创建系统用户

``` sh
useradd devuser
passwd devuser
```

创建名称空间

``` sh
kubectl create namespace dev
```

创建证书请求文件（指定用户名）

``` sh
mkdir -p /usr/local/install-k8s/cert/devuser
vim /usr/local/install-k8s/cert/devuser/devuser-csr.json
```

``` json
{
	"CN": "devuser",
	"hosts": [],
	"key": {
		"algo": "rsa",
		"size": 2048
	},
	"names": [{
		"C": "CN",
		"ST": "BeiJing",
		"L": "BeiJing",
		"O": "k8s",
		"OU": "System"
	}]
}
```

下载`cfssl`、`cfssl-certinfo`、`cfssljson`

``` sh
wget https://pkg.cfssl.org/R1.2/cfssl_linux-amd64
mv cfssl_linux-amd64 /usr/local/bin/cfssl

wget https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64
mv cfssljson_linux-amd64 /usr/local/bin/cfssljson

wget https://pkg.cfssl.org/R1.2/cfssl-certinfo_linux-amd64
mv cfssl-certinfo_linux-amd64 /usr/local/bin/cfssl-certinfo
chmod +x /usr/local/bin/cfssl
chmod +x /usr/local/bin/cfssl-certinfo
chmod +x /usr/local/bin/cfssljson
```

或从`物理机`上传`cfssl`、`cfssl-certinfo`、`cfssljson`到`虚拟机k8s-master01`

``` sh
ls cfssl*
cfssl  cfssl-certinfo  cfssljson

mv cfssl /usr/local/bin/cfssl
mv cfssl-certinfo /usr/local/bin/cfssl-certinfo
mv cfssljson /usr/local/bin/cfssljson

chmod +x /usr/local/bin/cfssl
chmod +x /usr/local/bin/cfssl-certinfo
chmod +x /usr/local/bin/cfssljson
```

生成证书、密钥

``` sh
cd /etc/kubernetes/pki/

cfssl gencert -ca=ca.crt -ca-key=ca.key  -profile=kubernetes /usr/local/install-k8s/cert/devuser/devuser-csr.json | cfssljson -bare devuser
```

设置集群参数

``` sh
cd /root

export KUBE_APISERVER="https://192.168.66.10:6443"
kubectl config set-cluster kubernetes \
--certificate-authority=/etc/kubernetes/pki/ca.crt \
--embed-certs=true \
--server=${KUBE_APISERVER} \
--kubeconfig=devuser.kubeconfig

cat devuser.kubeconfig
```

设置客户端认证参数

``` sh
kubectl config set-credentials devuser \
--client-certificate=/etc/kubernetes/pki/devuser.pem \
--client-key=/etc/kubernetes/pki/devuser-key.pem \
--embed-certs=true \
--kubeconfig=devuser.kubeconfig

cat devuser.kubeconfig
```

设置上下文参数

``` sh
kubectl config set-context kubernetes \
--cluster=kubernetes \
--user=devuser \
--namespace=dev \
--kubeconfig=devuser.kubeconfig

cat devuser.kubeconfig
```

赋予用户admin管理员角色

``` sh
kubectl create rolebinding devuser-admin-binding --clusterrole=admin --user=devuser --namespace=dev
```

复制文件至用户devuser家目录并重命名为config，修改归属关系

``` sh
mkdir /home/devuser/.kube
cp devuser.kubeconfig /home/devuser/.kube/config
chown devuser:devuser /home/devuser/.kube/config
```

切换到前面设置的上下文

``` sh
kubectl config use-context kubernetes --kubeconfig=/home/devuser/.kube/config
```

切换用户测试使用（ssh devuser@k8s-master01，使用devuser用户执行以下命令）

``` sh
# 创建Pod
kubectl run test-nginx --image=cheungjune/myapp:v1

# 查看Pod
kubectl get pod
NAME                          READY   STATUS    RESTARTS   AGE
test-nginx-7ff86b55fb-mhkqd   1/1     Running   0          53s

# 查看default名称空间下的Pod（提示无权限）
kubectl get pod -n default
Error from server (Forbidden): pods is forbidden: User "devuser" cannot list resource "pods" in API group "" in the namespace "default"
```

退出devuser用户登录，查看test-nginx所属名称空间

``` sh
kubectl get pod --all-namespaces -o wide | grep -B1 test-nginx
NAMESPACE   NAME                           READY   STATUS    RESTARTS   AGE
dev         test-nginx-7ff86b55fb-mhkqd    1/1     Running   0          7m58s
```

### AdmissionControl

准入控制是API Server的插件集合，通过添加不同的插件，实现额外的准入控制规则。甚至于API Server的一些主要的功能都需要通过Admission Controllers实现，比如ServiceAccount

列举部分插件的功能：

NamespaceLifecycle：防止在不存在的namespace上创建对象，防止删除系统预置namespace，删除namespace时，连带删除它的所有资源对象。

LimitRanger：确保请求的资源不会超过资源所在Namespace的LimitRange的限制。

ServiceAccount：实现了自动化添加ServiceAccount。

ResourceQuota：确保请求的资源不会超过资源的ResourceQuota限制。

## Helm

### 背景和概念

**背景**

在没使用Helm之前，向K8S部署应用，我们要依次部署Deployment、Service等，步骤较繁琐。同时，随着很多项目微服务化，许多应用的容器中部署和管理显得较为复杂，Helm通过打包的方式，支持发布的版本管理和控制，很大程度上简化了K8S应用的部署和管理。

**概念**

Helm本质就是让K8S的应用管理（Deployment、Service等）可配置，能动态生成。通过动态生成K8S资源清单文件（Deployment.yaml，Service.yaml），然后调用Kubectl自动执行K8S资源部署。

Helm是官方提供的类似于YUM的包管理器，是部署环境的流程封装。Helm有两个重要的概念：chart和release：

chart是创建一个应用的信息集合，包括各种Kubernetes对象的配置模板、参数定义、依赖关系、文档说明等。chart是应用部署的自包含逻辑单元。可以将chart想象成YUM中的软件安装包

release是chart的运行实例，代表了一个正在运行的应用。当chart被安装到Kubernetes集群，就生成一个release。chart能够多次安装到同一个集群，每次安装都是一个release。

Helm包含两个组件：Helm客户端和Tiller服务器，如下图所示：

<img src="https://img-blog.csdnimg.cn/2020081719545355.png" alt="img" style="zoom:50%;" /> 

Helm客户端负责chart和release的创建和管理以及和Tiller的交互。

Tiller服务器运行在K8S集群中，它会处理Helm客户端的请求，与Kubernetes API Server交互。

### 部署Helm

安装helm客户端

``` sh
wget https://source-82722.oss-cn-beijing.aliyuncs.com/helm/helm-v2.13.1-linux-amd64.tar.gz
tar -zxvf helm-v2.13.1-linux-amd64.tar.gz
cp -a linux-amd64/helm /usr/local/bin/
```

由于api server开启了RBAC访问控制，所以需要创建tiller使用的service account，并分配合适的角色给它，这样才能访问api server，详细内容可以参考：[Helm | 基于角色的访问控制](https://helm.sh/zh/docs/topics/rbac/)

练习环境为了简化配置，直接分配cluster-admin这个集群内置的ClusterRole给它。

``` sh
vim rbac-helm-config.yaml 
```

``` yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef: 
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount 
    name: tiller 
    namespace: kube-system
```

``` sh
kubectl apply -f rbac-helm-config.yaml
```

初始化Helm

``` sh
上传镜像helm-tiller.tar到所有Node节点，并导入
ssh root@k8s-node01 docker load -i helm-tiller.tar
ssh root@k8s-node02 docker load -i helm-tiller.tar

helm init --service-account tiller --skip-refresh

kubectl get pod -n kube-system | grep tiller
```

归档保存Helm插件安装文件

```sh
mkdir /usr/local/install-k8s/plugin/helm
mv linux-amd64/ /usr/local/install-k8s/plugin/helm/
mv helm* /usr/local/install-k8s/plugin/helm/
```

查看helm的版本

``` sh
helm version
Client: &version.Version{SemVer:"v2.13.1", GitCommit:"618447cbf203d147601b4b9bd7f8c37a5d39fbb4", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.13.1", GitCommit:"618447cbf203d147601b4b9bd7f8c37a5d39fbb4", GitTreeState:"clean"}
```

### Helm自定义模板

创建模板存放目录

``` sh
mkdir hello-world && cd hello-world
```

创建自描述文件Chart.yaml（文件名固定不可变），这个文件必须包含name和version字段

``` sh
vim Chart.yaml
```

``` yaml
name: hello-world
version: 1.0.0
```

创建模板文件（模板文件存放目录名templates固定不可变）

``` sh
mkdir templates
```

``` sh
vim templates/deployment.yaml
```

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:  
  name: hello-world
spec:  
  replicas: 1  
  template:    
    metadata:      
      labels:        
        app: hello-world    
    spec:      
      containers:        
        - name: hello-world          
          image: cheungjune/myapp:v1          
          ports:            
            - containerPort: 80              
              protocol: TCP
```

``` sh
vim templates/service.yaml
```

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-world
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 80
    protocol: TCP
  selector:    
    app: hello-world
```

使用helm install创建一次Release

``` sh
helm install .
```

查看检验

``` sh
# 查看Pod
kubectl get pod 
NAME                           READY   STATUS    RESTARTS   AGE
hello-world-5b5bd47487-v69zq   1/1     Running   0          36s

# 查看Service
kubectl get service
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
hello-world   NodePort    10.102.114.26   <none>        80:31131/TCP   87s
kubernetes    ClusterIP   10.96.0.1       <none>        443/TCP        12d

# 查看Helm已部署的Release
helm list
NAME            	REVISION	UPDATED                 	STATUS  	CHART            	APP VERSION	NAMESPACE
belligerent-crab	1       	Wed Feb 16 00:56:16 2022	DEPLOYED	hello-world-1.0.0	           	default  

# 删除Release（仅移除该Release相关Kubernetes资源，Release是可以恢复的）
helm delete belligerent-crab

# 查看被删除的Release
helm ls --deleted

# 查看Release的历史版本
helm history belligerent-crab

# 历史版本回滚
helm rollback belligerent-crab 1

# 彻底删除Release
helm delete --purge belligerent-crab
```

修改模板可动态切换版本

``` sh
vim values.yaml
```

``` yaml
image: 
  repository: cheungjune/myapp
  tag: "v1"
```

``` sh
sed -i 's@cheungjune/myapp:v1@{{ .Values.image.repository}}:{{ .Values.image.tag }}@g' templates/deployment.yaml
```

安装版本v1，并查看检验

``` sh
# 安装
helm install .

# 查看Release
helm list
NAME          	REVISION	UPDATED                 	STATUS  	CHART            	APP VERSION	NAMESPACE
elevated-tiger	1       	Wed Feb 16 01:30:51 2022	DEPLOYED	hello-world-1.0.0	           	default  

# 查看Service端口
helm status elevated-tiger | grep -A2 Service
==> v1/Service
NAME         TYPE      CLUSTER-IP     EXTERNAL-IP  PORT(S)       AGE
hello-world  NodePort  10.107.92.101  <none>       80:30591/TCP  63s

# 访问测试
curl 192.168.66.10:30591
Hello MyApp | Version: v1 | <a href="hostname.html">Pod Name</a>
```

升级版本v2，并查看检验

``` sh
# 替换values.yaml中的版本号
sed -i 's/v1/v2/g' values.yaml 

# 安装
helm upgrade elevated-tiger .

# 查看Release
helm list
NAME          	REVISION	UPDATED                 	STATUS  	CHART            	APP VERSION	NAMESPACE
elevated-tiger	2       	Wed Feb 16 01:32:51 2022	DEPLOYED	hello-world-1.0.0	           	default 

# 访问测试
curl 192.168.66.10:30591
Hello MyApp | Version: v2 | <a href="hostname.html">Pod Name</a>
```

通过set image.tag='' 参数修改版本

``` sh
helm upgrade elevated-tiger --set image.tag='v1' .

curl 192.168.66.10:30591
Hello MyApp | Version: v1 | <a href="hostname.html">Pod Name</a>
```

Debug：预览模板效果：只会打印出生成的清单文件内容，不会实际执行部署

``` sh
helm install . --dry-run --debug --set image.tag='latest'
```

清除所有资源

``` sh
helm delete --purge elevated-tiger
```

### Helm部署功能性组件

#### Dashboard

替换Helm默认stable源

``` sh
helm repo list
NAME  	URL                                             
stable	https://kubernetes-charts.storage.googleapis.com
local 	http://127.0.0.1:8879/charts                    

helm repo add stable https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
helm repo update

helm repo list
NAME  	URL                                                   
stable	https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
local 	http://127.0.0.1:8879/charts    
```

下载解压Dashboard的Chart

``` sh
helm fetch stable/kubernetes-dashboard
tar -zxvf kubernetes-dashboard-0.6.0.tgz
```

创建一个变量文件到Chart目录中

``` sh
vim kubernetes-dashboard/k8s-dashboard-values.yaml
```

``` yaml
image:
  repository: k8s.gcr.io/kubernetes-dashboard-amd64  
  tag: v1.10.1
ingress:  
  enabled: true  
  hosts:    
    - k8s.frognew.com  
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"    
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"  
  tls:    
    - secretName: frognew-com-tls-secret      
      hosts:      
      - k8s.frognew.com
rbac:  
  clusterAdminRole: true
service:
  type: NodePort
```

使用Helm安装Dashboard

``` sh
helm install /root/kubernetes-dashboard -n kubernetes-dashboard --namespace kube-system -f /root/kubernetes-dashboard/k8s-dashboard-values.yaml
```

查看Dashboard使用的外部端口号

``` sh
helm status kubernetes-dashboard | grep -A2 Service$
==> v1/Service
NAME                  TYPE      CLUSTER-IP    EXTERNAL-IP  PORT(S)        AGE
kubernetes-dashboard  NodePort  10.106.60.60  <none>       443:31152/TCP  74s
```

查询Dashboard的token

```sh
kubectl -n kube-system describe secrets `kubectl -n kube-system get secrets | awk '/kubernetes-dashboard-token/{print $1}'` | awk '/^token/{print $2}'
eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJrdWJlcm5ldGVzLWRhc2hib2FyZC10b2tlbi1zYmN4biIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjgyMTk2NTEzLTM4M2QtNDZkNC1hNDVjLTVkMDA3Y2NjMmNmNyIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlLXN5c3RlbTprdWJlcm5ldGVzLWRhc2hib2FyZCJ9.VX2PZLECL1peJBsu5p4QG9mYnFQiU6rCxQovmQ4sZdsMYzTG-qqu2xC7JQbqTYpWe2TIgroMnLhhxDzNBv6uUdl-Yq2jJRR3h1mpdCP8jnxAqQcmWp0YLmi_0WsI913zTTv9uBAyLWT6w4h4x3_g0flvEvMIyfIu2zMdkJllRalf8rbffs_YpFUeGDd-kfzPPUv43b2M8Y2Jpeenh3kURgZRenYkfOAE25GQgYbWWqzSGhRciHCdxI2KK8J-w1uxzErr8DmSl6o-lnUg4s1S2jSHapr363uvF4a3442fZPWGjPypW-EHX7i785kSyYgriran6DwrU8FEG-Cq0C6RdA
```

访问测试

物理机浏览器访问地址：https://192.168.66.10:31152

使用Google-Chrome内核的浏览器无法直接访问，需要使用自签名证书替换Dashboard证书

或者在以下风险提示界面输入thisisunsafe（注意：不是在地址栏输入！），即可自动跳转到页面

<img src="https://s2.loli.net/2022/02/16/jnUbqzVioGWc469.png" alt="image-20220216110604191" style="zoom: 67%;" /> 

建议使用Firefox浏览器进行访问

<img src="https://s2.loli.net/2022/02/16/gIeLHkMnq6DwdAl.png" alt="image-20220216105327995" style="zoom: 50%;" /> 

<img src="https://s2.loli.net/2022/02/16/WfAZL6NRXUh3jq5.png" alt="image-20220216105447989" style="zoom: 50%;" /> 

归档保存Dashboard插件安装文件

``` sh
mkdir /usr/local/install-k8s/plugin/dashboard
mv kubernetes-dashboard* /usr/local/install-k8s/plugin/dashboard
```

## 监控和资源控制

### Prometheus

#### 简介

Prometheus是由SoundCloud开发的开源监控报警系统和时序列数据库。Prometheus使用Go语言开发，是Google BorgMon监控系统的开源版本。2016年由Google发起Linux基金会旗下的原生云基金会，将Prometheus纳入第二大开源项目，Prometheus目前在开源社区相当活跃。

Prometheus和Heapster(Heapster是K8S的一个子项目，用于获取集群的性能数据)相比功能更完善、更全面。Prometheus性能也足够支撑上万台规模的集群。

#### 组件

MetricServer：是K8S集群资源使用情况的聚合器，收集数据给K8S集群内使用，如kubectl、hpa、scheduler等。

PrometheusOperator：是一个系统监测和警报工具箱，用来存储监控数据。

NodeExporter：用于各Node的关键度量指标状态数据。

KubeStateMetrics：收集K8S集群内资源对象数据，制定告警规则。

Prometheus：通过http协议传输，采用pull方式收集apiserver，scheduler，controller-manager，kubelet组件数据。

Grafana：可视化数据统计和监控平台。

#### 部署Prometheus

在所有主机上进行时间同步

`Prometheus监控各个节点对时间要求严格，在部署服务之前务必将所有机器的时间进行同步，包括用来展示和查询的windows机器。`

``` sh
# 修改ntp配置文件
vim /etc/ntp.conf
第21行 server ntp4.aliyun.com iburst
第22行 #server 1.centos.pool.ntp.org iburst
第23行 #server 2.centos.pool.ntp.org iburst
第24行 #server 3.centos.pool.ntp.org iburst

# 重启服务，并设置服务开机自启
systemctl restart ntpd
systemctl enable ntpd
```

从github下载Prometheus部署文件（包含资源清单）

``` sh
wget https://codeload.github.com/prometheus-operator/kube-prometheus/zip/refs/heads/release-0.3 
unzip release-0.3 
cd kube-prometheus-release-0.3/
```

修改配置文件，设置grafana-service.yaml、prometheus-service.yaml、alertmanager-service.yaml的类型为NodePort，并分别设置nodePort为30100、30200、30300

``` sh
sed -i '/spec/a\\  type: NodePort' manifests/grafana-service.yaml
sed -i '/target/a\\    nodePort: 30100' manifests/grafana-service.yaml

sed -i '/spec/a\\  type: NodePort' manifests/prometheus-service.yaml
sed -i '/targetPort: web/a\\    nodePort: 30200' manifests/prometheus-service.yaml

sed -i '/spec/a\\  type: NodePort' manifests/alertmanager-service.yaml
sed -i '/targetPort: web/a\\    nodePort: 30300' manifests/alertmanager-service.yaml
```

应用资源清单部署Prometheus

``` sh
kubectl apply -f manifests/setup/
kubectl apply -f manifests/
```

归档保存Prometheus插件安装文件

``` sh
cd /root
mkdir /usr/local/install-k8s/plugin/prometheus
mv kube-prometheus/ /usr/local/install-k8s/plugin/prometheus/
```

查看检验Prometheus

``` sh
# 查看Pod
kubectl get pod -n monitoring
NAME                                  READY   STATUS    RESTARTS   AGE
alertmanager-main-0                   2/2     Running   0          13m
alertmanager-main-1                   2/2     Running   0          13m
alertmanager-main-2                   2/2     Running   0          13m
grafana-77978cbbdc-dk9nv              1/1     Running   0          13m
kube-state-metrics-7f6d7b46b4-kglxw   3/3     Running   0          13m
node-exporter-bvdws                   2/2     Running   0          13m
node-exporter-cn26b                   2/2     Running   0          13m
node-exporter-mtvbf                   2/2     Running   0          13m
prometheus-adapter-68698bc948-tq5xm   1/1     Running   0          13m
prometheus-k8s-0                      3/3     Running   1          13m
prometheus-k8s-1                      3/3     Running   1          13m
prometheus-operator-6685db5c6-5strg   1/1     Running   0          13m

# 测试使用'kuberctl top'命令
kubectl top node
NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
k8s-master01   158m         3%     1213Mi          65%
k8s-node01     89m          2%     1320Mi          70%
k8s-node02     90m          2%     1248Mi          67%

kubectl top pod -A
NAMESPACE       NAME                                        CPU(cores)   MEMORY(bytes)
default         myapp-pod                                   0m           9Mi
dev             test-nginx-7ff86b55fb-mhkqd                 0m           4Mi
ingress-nginx   nginx-ingress-controller-7995bd9c47-pl4x4   1m           117Mi
kube-system     coredns-5c98db65d4-cpwmk                    4m           26Mi
kube-system     coredns-5c98db65d4-h52x5                    4m           26Mi
kube-system     etcd-k8s-master01                           15m          86Mi
kube-system     kube-apiserver-k8s-master01                 36m          300Mi
kube-system     kube-controller-manager-k8s-master01        17m          83Mi
kube-system     kube-flannel-ds-4mdkh                       1m           30Mi
kube-system     kube-flannel-ds-cbzfq                       1m           25Mi
kube-system     kube-flannel-ds-nz5qs                       1m           31Mi
kube-system     kube-proxy-924bp                            3m           38Mi
kube-system     kube-proxy-dtb2v                            2m           36Mi
kube-system     kube-proxy-gnnvb                            2m           35Mi
kube-system     kube-scheduler-k8s-master01                 1m           35Mi
kube-system     kubernetes-dashboard-79599d7b8d-qr5hf       0m           19Mi
kube-system     tiller-deploy-58565b5464-hg8pw              0m           20Mi
monitoring      alertmanager-main-0                         2m           19Mi
monitoring      alertmanager-main-1                         2m           20Mi
monitoring      alertmanager-main-2                         2m           22Mi
monitoring      grafana-77978cbbdc-dk9nv                    3m           47Mi
monitoring      kube-state-metrics-7f6d7b46b4-kglxw         0m           39Mi
monitoring      node-exporter-bvdws                         1m           23Mi
monitoring      node-exporter-cn26b                         1m           16Mi
monitoring      node-exporter-mtvbf                         1m           23Mi
monitoring      prometheus-adapter-68698bc948-tq5xm         0m           13Mi
monitoring      prometheus-k8s-0                            11m          164Mi
monitoring      prometheus-k8s-1                            11m          190Mi
monitoring      prometheus-operator-6685db5c6-5strg         0m           22Mi
```

浏览器访问测试

访问Prometheus（http://192.168.66.10:30200）

除了页面可点击获取的信息外，prometheus的WEB界面上提供了基本的查询K8S集群中每个Pod的CPU使用情况，查询条件如下：

``` tex
sum by (pod_name)( rate(container_cpu_usage_seconds_total{image!="", pod_name!=""}[1m] ) )
```

![image-20220218151705959](https://s2.loli.net/2022/02/18/y8GOZdkplC7qJmS.png)

访问grafana（http://192.168.66.10:30100），初始密码均为admin

依次操作添加数据来源模板

![](https://s2.loli.net/2022/02/16/QcAte1u3Yb5CDa8.png) 

![img](https://s2.loli.net/2022/02/16/IxGwQ1TsEzecotH.png) 

![img](https://s2.loli.net/2022/02/16/BjpFm4v5d6HxtfK.png) 

![img](https://s2.loli.net/2022/02/16/9lrXGVMtKe7bsPI.png) 

选择想要查看的数据图表，如：Kubernetes / Pods

![image-20220218152316508](https://s2.loli.net/2022/02/18/hojm3fiJCpvgdQD.png) 

![image-20220218152352583](https://s2.loli.net/2022/02/18/wW1IfibYnaxyp8g.png) 

grafana提供一个更人性化的图形化监控界面

![img](https://s2.loli.net/2022/02/18/FBLDzPK2H9buANh.png)

### HPA-自动调整Pod副本数

HorizontalPodAutoscaling可以根据CPU利用率自动伸缩一个ReplicationController、Deployment或者ReplicaSet中的Pod数量。

在`k8s-node01`和`k8s-node02`上下载HPA压力测试镜像

``` sh
docker pull gcr.io/google_containers/hpa-example
```

使用HPA压力测试镜像运行Pod

``` sh
kubectl run php-apache --image=gcr.io/google_containers/hpa-example --requests=cpu=200m --expose --port=80

kubectl get deployment
kubectl get pod
```

创建HPA控制器：以CPU使用率50%为临界点，自动扩缩Pod副本数，且副本数最少为1，最多为10

``` sh
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10
```

新开终端新建容器通过循环访问Pod提供的服务，增加Pod的访问负载

``` sh
# 新建Pod，并交互式打开管理终端
kubectl run -i --tty load-generator --image=busybox /bin/sh

# 在容器交互式管理终端执行命令
while true; do wget -q -O- http://php-apache.default.svc.cluster.local; done
```

同时打开两个终端，查看监测hpa和pod的状态

``` sh
# 终端1
kubectl get hpa -w
NAME         REFERENCE               TARGETS    MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   0%/50%     1         10        1          2m12s
php-apache   Deployment/php-apache   42%/50%    1         10        1          4m48s
php-apache   Deployment/php-apache   45%/50%    1         10        1          5m3s
php-apache   Deployment/php-apache   88%/50%    1         10        1          5m19s
php-apache   Deployment/php-apache   92%/50%    1         10        2          5m34s
php-apache   Deployment/php-apache   138%/50%   1         10        2          5m49s
php-apache   Deployment/php-apache   148%/50%   1         10        3          6m4s

# 终端2
kubectl get pod
NAME                             READY   STATUS    RESTARTS   AGE
load-generator-7d549cd44-xt9gk   1/1     Running   0          3m31s
php-apache-69dd84889f-bnmzt      1/1     Running   0          60s
php-apache-69dd84889f-hpskc      1/1     Running   0          90s
php-apache-69dd84889f-j7ptc      1/1     Running   0          11m
php-apache-69dd84889f-ml5fw      1/1     Running   0          29s
php-apache-69dd84889f-xphrc      1/1     Running   0          2m

# 随着CPU占用率越来越高，Pod副本数自动增加，最终会一直增加到上限10副本。
```

> **注意**
>
> 停止压力测试后，Pod副本数不会立即减少，这是为了防止瞬间突发流量时，可正常访问的用户数量降低，HPA误认为访问流量低而减少副本数，进一步加大单个Pod的承载压力，并陷入恶性循环。

### 资源限制配额

Kubernetes对资源的限制实际上是通过cgroup来控制的，cgroup是容器的一组用来控制内核如何运行进程的相关属性集合。针对内存、CPU和各种设备都有对应的cgroup。

**资源限制-Pod**

默认情况下，Pod运行没有CPU和内存的限额。这意味着系统中的任何Pod将能够消耗足够多的CPU和内存。一般会针对某些应用的Pod进行资源限制，这个资源限制是通过resources的requests和limits来实现。

requests代表要分配的资源，limits代表最高请求的资源值，可以简单理解为初始值和最大值。

``` yaml
spec:   
  containers:   
  - image: xxxx     
    imagePullPolicy: Always   
    name: auth       
    resources:       
      limits:     
        cpu: "4"          
        memory: 2Gi       
      requests:  
        cpu: 250m           # 1m=1/1000核，250m=0.25核
        memory: 250Mi
```

**资源限制-Namespace**

基于Namespace的资源限制，是Namespace中所有Pod可用的总资源配额。

`计算资源配额限制`

``` yaml
apiVersion: v1
kind: ResourceQuota
metadata:  
  name: compute-resources 
spec:
  hard: 
    pods: "20"   
    requests.cpu: "20" 
    requests.memory: 100Gi  
    limits.cpu: "40" 
    limits.memory: 200Gi
```

`对象数量配额限制`

``` yaml
apiVersion: v1
kind: ResourceQuota
metadata:  
  name: object-counts 
spec:  
  hard:  
    configmaps: "10"  
    persistentvolumeclaims: "4" 
    replicationcontrollers: "20"   
    secrets: "10"    
    services: "10"   
    services.loadbalancers: "2"
```

`CPU和内存LimitRange`

```yaml
apiVersion: v1
kind: LimitRange
metadata:  
  name: mem-limit-range
spec:  
  limits: 
  - default:   # 即limit的值
    memory: 50Gi    
    cpu: 5   
  defaultRequest:  # 即request的值 
    memory: 1Gi     
    cpu: 1   
  type: Container
```

## 部署高可用-Kubernetes集群

### 集群架构介绍

只需解决Master高可用，Node节点加入集群即可。

Master高可用中，Haproxy作为集群apiserver反向代理对集群其它组件提供统一的VIP访问地址。

其它组件由集群自动解决高可用即可。

<img src="https://s2.loli.net/2022/02/18/ZNrtPi9dDKVW8sA.png" alt="image-20220218222104624" style="zoom:50%;" /> 

### 高可用部署

#### Breeze部署方案

项目地址：[GitHub|Breeze](https://github.com/wise2c-devops/breeze/blob/master/README.md)

**介绍**

Breeze项目旨在提供一个可信的、安全的、稳定的Kubernetes集群部署工具，它可以帮助您通过图形化操作界面快捷地在生产环境部署一个或多个Kubernetes集群，而不需要连入互联网环境。

**功能特点**

`运行简单`

Breeze将部署Kubernetes集群所需的全部资源文件打包在一个docker镜像内，这包括Kubernetes的组件镜像、docker、etcd、harbor、kubernetes集群部署的ansible playbook脚本文件等。同时，Breeze部署主机自身也作为一个RHEL/CentOS的yum或Ubuntu的apt仓库服务器角色存在，因此，只需准备一台安装了docker和docker-compose命令的主机即可轻松的使Breeze运行起来并进行Kubernetes集群的部署。

`简化Kubernetes集群部署流程`

仅需几条简单命令，就能使Breeze程序运行起来，接下来的Kubernetes集群部署工作全都通过图形化操作界面完成。

`支持离线部署`

在仅有的5个镜像(playbook, yum-repo/apt-source, pagoda, deploy-ui) 被加载在Breeze部署主机之后，所有操作都不需要互联网的访问。Breeze自身作为RHEL/CentOS的yum仓库或Ubuntu的apt仓库对被部署机提供yum/apt源服务并使用kubeadm进行Kubernetes的部署工作，同时Breeze还会部署一个Harbor服务器用于内网的镜像下载服务。

`支持多个集群批量部署`

Breeze支持批量部署多个Kubernetes集群。

`支持高可用架构`

使用Breeze部署的Kubernetes集群，默认提供3个master节点和3个etcd节点, 结合haproxy+keepalived架构服务，所有工作节点都使用虚拟浮动IP地址和主节点服务器通信。

**Brezz架构原理图**

Breeze通过Ansible-playbook自动化部署Kubernetes集群，然后通过可视化图形UI简化安装过程。

<img src="https://s2.loli.net/2022/02/18/O4MtL5nZhQvNVof.png" alt="Wise2C-Breeze-Architecture" style="zoom: 50%;" /> 

<img src="https://s2.loli.net/2022/02/18/ULM4Jda2NzTOrus.png" alt="image-20220218232310395" style="zoom:80%;" /> 

**组件**

breeze: 用于部署docker, harbor, haproxy+keepalived, etcd, kubernetes等组件的Ansible playbook。

yum-repo: 用于RHEL/CentOS安装docker, docker-compose, kubelet, kubectl, kubeadm, kubernetes-cni等的yum仓库源。

apt-source: 用于Ubuntu安装docker, docker-compose, kubelet, kubectl, kubeadm, kubernetes-cni等的apt仓库源。

deploy-ui: 图形界面组件。

pagoda: 提供操作Ansible playbook的API。

kubeadm-version: 获取Kubernetes组件版本清单，采用命令"kubeadm config"

**安装和运行要求**

breeze部署机

​	docker 1.31.1+ and docker-compose 1.12.0+

适用操作系统（最小安装）

​	RHEL/CentOS: 7.4/7.5/7.6/7.7/7.8/7.9/8.4+

#### 安装部署

Breeze部署指南：[Github|Breeze部署指南](https://github.com/wise2c-devops/breeze/blob/master/BreezeManual-CN.md)

**Breeze部署机准备**

| 虚拟机名称    | 虚拟机配置                                                 | 主机名        | IP地址         |
| ------------- | ---------------------------------------------------------- | ------------- | -------------- |
| Breeze-deploy | 2*2处理器-2GB内存-SCSI磁盘-100GB磁盘-网卡1仅主机+网卡2桥接 | Breeze-deploy | 192.168.66.254 |

取消SELINUX设定及放开防火墙

``` sh
setenforce 0
sed --follow-symlinks -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config
firewall-cmd --set-default-zone=trusted
firewall-cmd --complete-reload
```

安装docker-compose命令

``` sh
curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

安装docker-io 1.13.1

``` sh
rm -rf /etc/yum.repos.d/*
curl -L https://mirrors.163.com/.help/CentOS7-Base-163.repo -o /etc/yum.repos.d/CentOS7.repo
yum -y install docker
systemctl start docker
systemctl enable docker
```

下载用于部署某个Kubernetes版本的docker-compose文件（镜像使用阿里云镜像）

``` sh
curl -L https://raw.githubusercontent.com/wise2c-devops/breeze/v1.23.3/docker-compose-centos-aliyun.yml -o docker-compose.yml
```

使用docker-compose部署

``` sh
docker-compose up -d
```

测试访问Breeze网页端（地址：192.168.66.254:88）

![image-20220219002537417](https://s2.loli.net/2022/02/19/87GNkjETrHsBMhb.png) 

**集群主机准备**

| 虚拟机名称   | 虚拟机配置                                       | 主机名           | IP地址         |
| ------------ | ------------------------------------------------ | ---------------- | -------------- |
| k8s-master00 | 2*2处理器-2GB内存-SCSI磁盘-100GB磁盘-网卡1仅主机 | k8s-master00     | 192.168.66.10  |
| k8s-master01 | 2*2处理器-2GB内存-SCSI磁盘-100GB磁盘-网卡1仅主机 | k8s-master01     | 192.168.66.11  |
| k8s-node00   | 2*2处理器-2GB内存-SCSI磁盘-100GB磁盘-网卡1仅主机 | k8s-node00       | 192.168.66.20  |
| Harbor       | 2*2处理器-2GB内存-SCSI磁盘-100GB磁盘-网卡1仅主机 | hub.example0.com | 192.168.66.100 |

Breeze部署机免密登录集群主机

``` sh
ssh-keygen
ssh-copy-id 192.168.66.10
ssh-copy-id 192.168.66.11
ssh-copy-id 192.168.66.20
ssh-copy-id 192.168.66.100
```

**从Breeze网页端部署集群**

添加一个集群

![image-20220219120645446](https://s2.loli.net/2022/02/19/Bi2NZn7Ogw4MmPd.png) 

![image-20220219120842155](https://s2.loli.net/2022/02/19/gzsIFOxDELYhHi5.png) 

进入集群配置界面，添加主机

![image-20220219120927514](https://s2.loli.net/2022/02/19/oTMykDXl9ZQi2Pg.png) 

![image-20220219122018291](C:\Users\cheun\AppData\Roaming\Typora\typora-user-images\image-20220219122018291.png) 

![image-20220219121228524](https://s2.loli.net/2022/02/19/FkircfRBQoHbZmW.png) 

<img src="https://s2.loli.net/2022/02/19/jSCTblQyV9WwLNq.png" alt="image-20220219121530685" style="zoom:67%;" /> 

进入下一步，对每个组件指定安装的服务器

![image-20220219122045613](https://s2.loli.net/2022/02/19/8zTc3hE1XOMgmWI.png) 

![image-20220219122113630](https://s2.loli.net/2022/02/19/Pa4uJD7i5rCQw8x.png) 

添加容器环境crio

![image-20220219123540616](https://s2.loli.net/2022/02/19/gdLC5ITf74qb96E.png) 

> **说明**
>
> 从2021年7月开始的版本，Docker也被更换为CRI-O（Harbor角色机除外）
>
> CRI-O是专门针对在Kubernetes中运行所设计的，它会交付一个最小化的运行时，该运行时实现了Kubernetes容器运行时接口（Container Runtime Interface，CRI）的标准组件。
>
> 早期版本的Kubernetes只支持Docker运行时的容器。当Kubernetes团队决定支持新的运行时的时候，他们开发并发布CRI，以便于将Kubernetes与特定的容器运行时解耦。
>
> CRI是一个插件接口，由protocol buffers和gRPC API组成，它允许Kubernetes通过Kubelet与任意满足CRI接口的容器运行时进行交互。CRI主要的两个RPC是Image Service和Runtime Service，它们分别规定了如何拉取镜像以及管理容器的生命周期。
>
> CRI-O能够让Kubernetes使用任意兼容OCI的运行时作为运行pod的容器运行时。因为只关注在Kubernetes中运行容器，所以项目的范围仅限于：
>
> ​	支持多种镜像格式，包括现有的Docker镜像格式；
>
> ​	支持多种方式下载镜像，包括信任和镜像验证；
>
> ​	容器镜像管理（管理镜像层、覆盖文件系统等）；
>
> ​	容器进程的生命周期管理；
>
> ​	满足CRI所需的监控和日志记录；
>
> ​	CRI所需的资源隔离。

添加harbor

![image-20220219122848729](https://s2.loli.net/2022/02/19/XqFahvcULAM3Cl1.png) 

添加loadbalancer，即haproxy+keepalived

![image-20220219122756939](https://s2.loli.net/2022/02/19/bV8W75eGlp9vPrB.png) 

> **注意**
>
> 所有节点的网卡名称需要保持一致

添加etcd

![image-20220219123737448](https://s2.loli.net/2022/02/19/zioVKh9f4RbDkUy.png) 

添加kubernetes

![image-20220219125137647](https://s2.loli.net/2022/02/19/3CpYVAKbNedTLRk.png) 

> **说明**
>
> Kubernetes entry point选项是高可用的一个设定值，如果生产环境有硬件或软件负载均衡指向所有Master节点，那么可以在这里填写负载均衡的统一入口地址。本次部署使用Breeze自带的HAProxy+Keepalived组合模块进行负载均衡，所以这个选项填写loadbalancer组件的VIP与默认端口6444，Node节点会使用这个地址访问API Server。
>
> Just add new worker nodes, do not reinstall this cluster选项用于向现有集群添加计算Node节点
>
> Upgrade existing cluster和Upgrade K8s nodes automatically选项用于升级现有集群而不是新装集群，而在生产环境升级集群一般采用对节点逐步进行，Breeze只负责将需要升级的镜像及脚本发到工作节点，应由管理员手动执行，并在执行过程中观察业务应用的高可用不受影响，如果勾选了 Upgrade K8s nodes automatically这这一切会全自动进行，如果所有业务都是有多副本分布在不同计算节点，那么这不会影响业务服务，否则不推荐使用这种方式进行集群在线升级。关于升级的详情，请参考Breeze部署指南中的演示视频。
>
> Kubernetes的界面里还有CNI模型供选择，请按实际需求选择部署Flannel、Calico还是Canal，至于Calico又分为IPIP隧道模式和BGP路由模式，还需要注意集群规模，详情请参考Calico官方网站文档解释。
>
> 对于网络地址范围CIDR参数共有三个，分别是Pod、Service、和ClusterIP的地址范围定义，默认值即可正常工作，除非它与你实际网络分配相冲突，才需要手动修改后进行部署。

添加Prometheus

![image-20220219131822780](https://s2.loli.net/2022/02/19/gjpUAhCowiZtyS9.png) 

> **说明**
>
> Prometheus是可选安装项，基于Prometheus Operator方式部署，集成Prometheus、Alertmanager、Grafana，选择一台Node节点进行部署即可，Prometheus、Alertmanager、Grafana对应三个服务暴露端口可自行设定，需要注意NodePort端口号必须大于30000，且不可是30300（Dashboard默认已占用30300端口）。

![image-20220219125636332](https://s2.loli.net/2022/02/19/gOCnJvZIyLjS6V8.png) 

如果机器性能不是特别强，建议第一次部署时不勾选Prometheus角色，等k8s集群部署并运行就绪后单独勾选Prometheus角色进行部署以免失败。

进入下一步，开始安装

![image-20220219122045613](https://s2.loli.net/2022/02/19/8zTc3hE1XOMgmWI.png) 

![image-20220219125735247](https://s2.loli.net/2022/02/19/4SGPYhXNdvc23Mb.png) 

等待自动执行安装

![image-20220219125847944](https://s2.loli.net/2022/02/19/8LNlbQUeIVWAuqt.png)

![image-20220219131538557](https://s2.loli.net/2022/02/19/hAqwjSkQPrF2mlz.png)  

> **部署说明**
>
> 以上是2台etcd、2台Master、1台Node、1台Harbor镜像仓库的环境。实际可以增减规模。
>
> 集群部署包含Dashboard，可以通过查询Dashboard的Service获取访问地址。
>
> 重置组件相关注意事项：
>
> - 重置所有组件不可以一次性勾选所有组件并点击重置，因为重置动作依赖于docker（crio），因此应按照以下顺序进行组件的重置：prometheus、kubernetes、etcd、loadbalancer、harbor可以一并勾选，上述组件重置完毕后再勾选docker（crio）进行重置。
>
> - 重置开始后，UI并不能动态刷新日志，需要人工手动刷新日志页面，待看见所有的重置都正常完成才表示重置过程结束。
>
> - 重置过程并不能多次执行，例如第一次重置正常，那么组件已经被删除，再做重置就会报错了。
>
> - 在宿主机某些软件设置不规范导致了K8S的安装失败，比如内存配置过低，提高了内存后重新部署，建议只需重置etcd和kubernetes组件再重新部署这两个组件即可。其它组件无需重新部署。
