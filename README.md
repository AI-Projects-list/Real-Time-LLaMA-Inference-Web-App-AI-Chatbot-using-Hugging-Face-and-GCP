# 🦙 Real-Time LLaMA Inference Web App AI Chatbot using Hugging Face and GCP

This project runs a heavy LLaMA model (e.g., LLaMA 2 7B) with a simple Streamlit interface, deployed on a GCP VM with GPU support.

## 📦 Features
- Loads large model with Hugging Face Transformers
- Caches model with Streamlit for faster response
- Deployable on GCP GPU instances (e.g., A100, T4)
- Optional Docker containerization

## 🚀 Setup on GCP

1. **Create GCP VM with GPU**
   - Type: `n1-standard-16` or higher
   - GPU: T4 / A100
   - Disk: ≥ 50GB SSD
   - Enable Jupyter or SSH access

2. **Install dependencies**

```bash
sudo apt update
sudo apt install git -y
git clone <your-repo-url>
cd <repo>
pip install -r requirements.txt
```

3. **Run app**

```bash
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

4. **Access app**
   - Go to `http://<VM_IP>:8501`

## 🐳 Docker Option

```bash
docker build -t llama-streamlit .
docker run -p 8501:8501 llama-streamlit
```

## 📌 Notes
- Set `LLAMA_MODEL` env variable to use different HF model name.
- You must have access to LLaMA weights on Hugging Face or local copy.

---
