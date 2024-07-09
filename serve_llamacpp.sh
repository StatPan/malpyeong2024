cd ./llama.cpp && \ 
./llama-server -m /home/jovyan/python-project/malpyeong2024/models/qwen2/qwen2-7b-instruct-q2_K.gguf \
 -ngl 200 \
 -fa \
 -c 8192 \
 --port 8081 \
 #--main-gpu 1 \
 #--chat-template gemma 