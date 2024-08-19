FROM python:3.9

WORKDIR /python

COPY ../requirements.txt .

# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

CMD ["python", "main.py"]
