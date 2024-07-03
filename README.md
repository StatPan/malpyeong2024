
# StatPan 일상 대화 요약(가 유형)


## 목차
- [개요](#개요)
- [설치](#개발환경구성)
- [사용법](#사용법)
- [개발 환경 구성](#개발-환경-구성)
- [기여 방법](#기여-방법)
- [라이선스](#라이선스)

## 개요
‘일상 대화 요약’ 과제는 다자간 대화에서 발생하는 여러 주제를 식별하고 각 주제에 대한 요약문을 생성하는 것을 목표로 한다. 이 과제의 데이터는 일상에서 이루어지는 대화를 대상으로 하며, 대화 내 각 주제의 핵심 내용을 효율적으로 추출하여 요약 정보를 제공한다. 주제별 요약 기술은 정보의 분류와 검색, 지식 관리, 의사 결정 지원 등에 유용하게 활용될 수 있다.

## 개발환경구성

```bash
# llama.cpp 리포지토리 클론
git clone https://github.com/ggerganov/llama.cpp.git

# 디렉토리 이동
cd llama.cpp

# make 또는 CMake로 llama.cpp 리포지토리 빌드
make GGML_CUDA=1
# 또는
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release
```

### requirements.txt 설치

```bash
pip install -r requirements.txt
```

### model 다운로드
requirements를 설치하고 나면, transformers 라이브러리가 설치되며, 종속 라이브러리로 huggingface-cli를 사용할 수 있습니다.

```bash
# 터미널에서
huggingface-cli download --repo-type model --local-dir ./models Qwen/Qwen2-7B-Instruct-GGUF qwen2-7b-instruct-q8_0.gguf
```