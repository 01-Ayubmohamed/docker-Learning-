#Stage 1: Build Stage

FROM python:3.8-slim AS build
WORKDIR /app
COPY . .
RUN pip install flask redis
EXPOSE 5002
CMD ["python", "count.py"] 