FROM postgres:latest

ENV POSTGRES_USER=test_user
ENV POSTGRES_PASSWORD=test_password
ENV POSTGRES_DB=test_db
ENV POSTGRES_HOST=pg_db