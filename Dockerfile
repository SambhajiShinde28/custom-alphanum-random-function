FROM python:3.11.3-slim

WORKDIR /app
COPY . .

CMD ["python", "alpha_num_random_function.py"]
