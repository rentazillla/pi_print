
FROM python:3.10-slim

# Install build dependencies for GMP and C compilation
RUN apt-get update && apt-get install -y gcc libgmp-dev make && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Compile the binary inside the container
RUN gcc -O3 gmp-chudnovsky_terms.c -o chudnovsky -lgmp -lm

# Install python dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

EXPOSE 8080
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
