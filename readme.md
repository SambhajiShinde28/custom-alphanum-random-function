# Alphanumeric Random Generator (Dockerized)

This project contains a Python script that generates random alphanumeric strings.  
The application is fully containerized using **Docker**, so you can run it anywhere without worrying about dependencies.

---

## 🚀 Getting Started

### Clone the repository
```bash
git clone https://github.com/your-username/alpha-num-random.git
cd alpha-num-random
```

### Build the Docker image
```bash
docker build -t alpha_num_random_img .
```

### Run the container
```bash
docker run sambhaji26/alpha_num_random_img
```

### Development Setup (without Docker)
```bash
pip install -r requirements.txt
python alalpha_num_random_function.py
```

### Project Structure
```bash

├── alalpha_num_random_function.py   # Main Python script
├── Dockerfile                       # Docker build instructions
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

### 🐳 Docker Hub (Optional)
```bash
docker pull sambhaji26/alpha_num_random_img
docker run sambhaji26/alpha_num_random_img
```

