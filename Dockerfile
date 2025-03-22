FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/yangtb2024/siliconflow-balance.git

WORKDIR /app/siliconflow-balance

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
