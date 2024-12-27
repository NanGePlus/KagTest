# 1、介绍
## 1.1 主要内容                      
KAG开源框架介绍及使用KAG实现知识增强生成应用                                                                            
本次实现功能为:产品模式测试、开发者模式测试                              
相关视频:                  
https://www.bilibili.com/video/BV1qWCsY1EtZ/                      
https://youtu.be/uhg5l5-K6rE                     

## 1.2 KAG框架
**(1)KAG是什么**               
KAG是OpenSPG发布v0.5版本中推出的知识增强生成（KAG）的专业领域知识服务框架，旨在充分利用知识图谱和向量检索的优势，增强大型语言模型和知识图谱，以解决 RAG 挑战                         
OpenSPG是蚂蚁集团结合多年金融领域多元场景知识图谱构建与应用业务经验的总结，并与OpenKG联合推出的基于SPG(Semantic-enhanced Programmable Graph)框架研发的知识图谱引擎               
检索增强生成（RAG）技术推动了领域应用与大模型结合。然而，RAG 存在着向量相似度与知识推理相关性差距大、对知识逻辑（如数值、时间关系、专家规则等）不敏感等问题，这些缺陷阻碍了专业知识服务的落地            
官方网址:https://openspg.yuque.com/ndx6g9/0.5/figkrornp0qwelhl                                                                                                                           
Github地址:https://github.com/OpenSPG/KAG                           
**(2)KAG技术框架**                    
kag框架包括 kg-builder、kg-solver、kag-model 三部分。v0.5版本发布只涉及前两部分，kag-model 将在后续逐步开源发布                        
**kg-builder**
实现了一种对大型语言模型（LLM）友好的知识表示，在 DIKW（Data、Information、Knowledge和Wisdom）的层次结构基础上，升级 SPG 知识表示能力               
在同一知识类型（如实体类型、事件类型）上兼容无 schema 约束的信息提取和有 schema 约束的专业知识构建，并支持图结构与原始文本块之间的互索引表示，为推理问答阶段的高效检索提供支持        
DIKW金字塔很好地描述了人类认识世界的规律和层次结构，分别是：                    
数据（Data原始的事实集合）、信息（Information可被分析测量的结构化数据）、知识（Knowledge需要洞察力和理解力进行学习）、智慧（Wisdom推断未来发生的相关性，指导行动）                      
数据是基础，信息是支撑，知识是核心，智慧是灵魂              
自底向上每一层都比下一层增加某些特质。数据层是最基本的原始素材；信息层加入了有逻辑的数据内容；知识层提炼信息之间的联系，加入“如何去使用”；智慧层加入预测能力，能回答“为什么用”                           
**kg-solver**                       
采用逻辑符号引导的混合求解和推理引擎，该引擎包括三种类型的运算符：规划、推理和检索，将自然语言问题转化为结合语言和符号的问题求解过程                               
在这个过程中，每一步都可以利用不同的运算符，如精确匹配检索、文本检索、数值计算或语义推理，从而实现四种不同问题求解过程的集成：检索、知识图谱推理、语言推理和数值计算                         


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
GitHub或Gitee中下载工程文件到本地，下载地址如下：                
https://github.com/NanGePlus/KagTest                                                                                
https://gitee.com/NanGePlus/KagTest                                                      

## 3.2 构建项目
使用pycharm构建一个项目，为项目配置虚拟python环境                       
项目名称：KagTest                           
虚拟环境名称保持与项目名称一致                                       

## 3.3 将相关代码拷贝到项目工程中           
将下载的代码文件夹中的文件全部拷贝到新建的项目根目录下                      


# 4、功能测试 
## 4.1 产品模式测试
## (1) 部署OpenSPG-Server                               
首先，使用docker部署和启动OpenSPG-Server，运行的指令为:                   
docker compose -f docker-compose.yml up -d                                                 
对于docker的使用，这里不做详细的赘述了，大家可以去看我这期视频，里面有对于docker非常详细的讲解，从安装部署到使用                       
https://www.bilibili.com/video/BV1LhUAYFEku/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                     
https://youtu.be/hD09V7jaXSo                    
## (2) 产品访问                 
浏览器输入 http://127.0.0.1:8887, 可访问openspg-kag 产品界面                     
浏览器输入 http://127.0.0.1:7474/browser/ , 可访问neo4j图数据库，用户名和密码分为neo4j  neo4j@openspg                                                    
## (3) 功能测试
**图存储配置:**               
{"database":"test","password":"neo4j@openspg","uri":"neo4j://release-openspg-neo4j:7687","user":"neo4j"}                        
**模型配置:**                    
{"api_key":"sk-zL8dD8hTwv0d5GRlYC0eUPH8QvWxnXIR6XTWsx7WKzoSO1uo","base_url":"https://yunwu.ai/v1","model":"gpt-4o-mini","client_type":"maas"}                        
**向量配置:**              
{"vectorizer":"kag.common.vectorizer.OpenAIVectorizer","api_key":"sk-zL8dD8hTwv0d5GRlYC0eUPH8QvWxnXIR6XTWsx7WKzoSO1uo","vector_dimensions":"1536","base_url":"https://yunwu.ai/v1","model":"text-embedding-ada-002"}                          
**提示词中英文配置:**                 
{"biz_scene":"default","language":"zh"}                            

## 4.2 开发者模式测试
### (1)安装依赖
新建命令行终端，按照如下指令进行依赖安装                                         
cd KAG                          
pip install -e .                    
安装完成之后可以运行如下指令验证是否安装成功                               
knext --version               
### (2)调整配置文件                                                          
先修改项目配置文件example.cfg,根据自己的实际情况，设置embedding、LLM配置参数                     
### (3)使用配置文件初始化项目                                   
新建命令行终端，运行如下命令进行项目创建和初始化                                     
knext project create --config_path ./example.cfg                                
### (4)脚本测试                                    
相关代码参考根目录下Demo文件夹                                                 
### (4-1)准备测试文档    
将测试文档拷贝到新建项目文件夹中的builder/data下，支持txt、pdf、markdown等                                               
### (4-2)构建索引                 
打开命令行终端，进入脚本所在目录，运行 python indexer.py 命令                        
### (4-3)检索                       
打开命令行终端，进入脚本所在目录，运行 python query.py 命令                          












