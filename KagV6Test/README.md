# 1、介绍
## 1.1 主要内容                  
**KAG新版本V0.6功能测试**                              
主要内容:测试版本升级后的产品模式、开发者模式使用                                                              

## 1.2 KAG框架
**(1)KAG是什么**               
KAG是OpenSPG发布v0.5版本中推出的知识增强生成（KAG）的专业领域知识服务框架，旨在充分利用知识图谱和向量检索的优势，增强大型语言模型和知识图谱，以解决 RAG 挑战                         
OpenSPG是蚂蚁集团结合多年金融领域多元场景知识图谱构建与应用业务经验的总结，并与OpenKG联合推出的基于SPG(Semantic-enhanced Programmable Graph)框架研发的知识图谱引擎               
检索增强生成（RAG）技术推动了领域应用与大模型结合。然而，RAG 存在着向量相似度与知识推理相关性差距大、对知识逻辑（如数值、时间关系、专家规则等）不敏感等问题，这些缺陷阻碍了专业知识服务的落地            
官方网址:https://openspg.yuque.com/r/organizations/homepage                                                                                                                                  
Github地址:https://github.com/OpenSPG/KAG                            
**(2)KAGV6.0版本更新**                    
https://github.com/OpenSPG/KAG/releases/tag/v0.6                        

# 2、前期准备工作
## 2.1 开发环境搭建:anaconda、pycharm
anaconda:提供python虚拟环境，官网下载对应系统版本的安装包安装即可                                      
pycharm:提供集成开发环境，官网下载社区版本安装包安装即可                                               
**可参考如下视频:**                      
集成开发环境搭建Anaconda+PyCharm                                                          
https://www.bilibili.com/video/BV1q9HxeEEtT/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                             
https://youtu.be/myVgyitFzrA          

## 2.2 大模型相关配置
(1)GPT大模型使用方案(第三方代理方式)                               
(2)非GPT大模型(阿里通义千问、讯飞星火、智谱等大模型)使用方案(OneAPI方式)                         
(3)本地开源大模型使用方案(Ollama方式)                                             
**可参考如下视频:**                                   
提供一种LLM集成解决方案，一份代码支持快速同时支持gpt大模型、国产大模型(通义千问、文心一言、百度千帆、讯飞星火等)、本地开源大模型(Ollama)                       
https://www.bilibili.com/video/BV12PCmYZEDt/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                 
https://youtu.be/CgZsdK43tcY           


# 3、项目初始化
## 3.1 下载源码
GitHub或Gitee中下载工程文件到本地，下载地址如下:                                         
https://github.com/NanGePlus/KagV6Test                                                                                
https://gitee.com/NanGePlus/KagV6Test                         

## 3.2 构建项目
使用pycharm构建一个项目，为项目配置虚拟python环境                       
项目名称：KagV6Test                           
虚拟环境名称保持与项目名称一致                                       

## 3.3 将相关代码拷贝到项目工程中           
将下载的代码文件夹中的文件全部拷贝到新建的项目根目录下                      


# 4、功能测试 
## 4.1 OpenSPG-Server部署                                    
首先，下载官方提供的最新版本的OpenSPG-Server的docker-compose.yml文件                 
链接:https://github.com/OpenSPG/openspg/blob/master/dev/release/docker-compose.yml                        
然后，进入到配置文件所在目录使用docker部署和启动OpenSPG-Server，运行的指令为:                     
docker compose -f docker-compose.yml up -d                       
启动成功后，对应的服务查看方式如下:                          
**neo4j:** 浏览器输入 http://127.0.0.1:7474/browser/ , 访问neo4j图数据库，默认用户名和密码:neo4j  neo4j@openspg                                                          
**Minio:** 浏览器输入 http://127.0.0.1:9000 , 访问Minio存储，默认用户名和密码:minio  minio@openspg                 
**mysql:** 打开mysql客户端软件，远程访问数据库，默认用户名和密码:root  openspg             
对于docker的使用，这里不做详细的赘述了，大家可以去看我这期视频，里面有对于docker非常详细的讲解，从安装部署到使用                       
https://www.bilibili.com/video/BV1LhUAYFEku/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                     
https://youtu.be/hD09V7jaXSo                    
## 4.2 产品模式测试
### (1) 访问WEB端                 
浏览器输入 http://127.0.0.1:8887, 可访问openspg-kag产品模式的WEB端，默认用户名和密码:openspg openspg@kag            
首次登录会要求修改密码                   
### (2) 全局配置
**图存储配置参数:**                    
database:JayChou  自定义                                             
password:neo4j@openspg                                    
uri:neo4j://release-openspg-neo4j:7687                                           
user:neo4j                                 
**向量配置参数:**                            
type:openai                                  
model:text-embedding-3-small                                                                      
base_url:https://yunwu.ai/v1                                                       
api_key:sk-MqUugKDFN7cgWzmX0XM1reUb6I3rm5WgA2LdHl6WhDqlz2fp                                                        
**提示词中英文配置参数:**                          
biz_scene:default                                      
language:zh                                
**模型配置参数-maas:**                                                        
model:gpt-4o-mini                                                                                         
api_key:sk-MqUugKDFN7cgWzmX0XM1reUb6I3rm5WgA2LdHl6WhDqlz2fp                                                                                   
base_url:https://yunwu.ai/v1                                             
### (3) 按照如下流程测试
创建知识库-编辑知识模型-创建任务-构建知识库、查看日志、抽取结果知识图谱-知识探查-知识库配置权限配置-推理问答                    
### (4) HTTP API接口测试
使用Apifox工具进行接口验证测试，并将提供的接口文档KagTest.apifox.json导入到Apifox              

## 4.3 开发者模式测试                
### (1) 安装依赖
下载KAG源码 https://github.com/OpenSPG/KAG 解压后将源码工程拷贝到项目根目录，截止2025-01-10,最新版本是v0.6.0                          
新建命令行终端，按照如下指令进行依赖安装               
cd KAG                          
pip install -e .                    
安装完成之后可以运行如下指令验证是否安装成功                               
knext --version                        
### (2)调整配置文件                                                          
将根目录下的other/config目录下的example_config.yaml文件拷贝一份到根目录,根据自己的业务修改配置参数             
KAG支持txt、pdf、markdown、docx、json、csv、语雀等，根据自己要处理的文本类型进行相关设置                 
### (3)使用配置文件初始化项目                                   
新建命令行终端，运行如下命令进行项目创建和初始化                                     
knext project create --config_path ./example_config.yaml             
若项目创建完成，修改了配置文件，需要运行如下命令进行更新                  
knext project update --proj_path .                  
### (3)提交schema
项目初始化完成后，进入到对应的项目文件夹下，根据实际业务需求调整schema，调整完成后再执行提交schema                
knext schema commit                     
### (4)构建索引                                   
首先将文档拷贝到新建项目文件夹中的builder/data下，支持txt、pdf、markdown、docx、json、csv等                         
并可以根据自身业务需求，在builder/prompt目录下新增:ner.py、std.py、triple.py                
**注意:** 代码中是通过注解的方式配置到配置文件中                     
打开命令行终端，进入脚本所在目录cd builder，运行 python indexer.py 命令
构建脚本启动后，会在当前工作目录下生成任务的 checkpoint 目录，记录了构建链路的 checkpoint 和统计信息           
KAG 框架基于 checkpoint 文件提供了断点续跑的功能。如果由于程序出错或其他外部原因（如 LLM 余额不足）导致任务中断，可以重新执行 indexer.py，KAG 会自动加载 checkpoint 文件并复用已有结果                         
索引构建成功后，可登录到 http://127.0.0.1:8887/或 http://127.0.0.1:7474/browser/ 查看知识图谱                
### (5)检索                             
打开命令行终端，进入脚本所在目录solver，运行 python query.py 命令                            
根据自身业务需求，可设置相关prompt内容:如resp_generator.py                         
也可以在产品端进行测试 http://127.0.0.1:8887/                  