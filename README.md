# AutismSupportHub

## 项目介绍

青少年自闭症咨询助理是一个公益性项目，其目的是为患有自闭症的青少年提供咨询服务。

## 安装

本项目采用docker容器部署，安装步骤如下：

1. 下载源码：`git clone https://github.com/autismchina/AutismSupportHub.git `

2. 在用户目录创建如下目录： `~/data/.streamlit` ，并创建配置文件：

   - config.toml

     ```toml
     [theme]
     base="dark"
     [client]
     showErrorDetails = false
     toolbarMode = "minimal"
     [server]
     port=8501
     ```

     详细配置参考 ：https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps#build-a-simple-chatbot-gui-with-streaming

   - secrets.toml

     ```toml
     OPENAI_API_KEY='YOUR_OPENAI_API_KEY'
     ```

3. 创建 `.env文件`

   ```properties
   #容器名称
   CONTAINER_NAME=YOUR_CONTAINER_NAME
   #应用路径
   BASE_URL=/autism
   #访问端口
   PORT=8501
   #应用路径
   WORK_DIR=/app
   #启动脚本
   SETUP_FILE=setup.py
   #streamlit配置文件数据卷
   STREAMLIT_VOLUME=~/data/.streamlit
   ```

4. 检查dokcer服务是否启动：`docker ps`

5. 进入项目根目录，构建镜像：`docker-compose build`

6. 运行容器：`docker-compose up -d`

## 访问页面

服务启动成功可以访问：http://localhost:8501/autism



