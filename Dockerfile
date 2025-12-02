# 基础镜像：使用官方轻量级Python 3.9环境
FROM python:3.9-slim
# 设置容器内工作目录
WORKDIR /app
# 复制当前目录下所有文件到容器的/app目录
COPY . .
# （可选）若项目有依赖文件requirements.txt，执行依赖安装（取消注释即可）
# RUN pip install -r requirements.txt
# 声明容器对外暴露的端口
EXPOSE 8080
# 容器启动命令（-u参数确保日志实时输出，便于调试）
CMD ["python", "-u", "api_server.py"]
