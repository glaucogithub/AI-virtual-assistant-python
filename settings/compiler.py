
from settings.settings import bot

compiler = {
    "c++" : "g++ {filename} -o {executable} && ./{executable}",
    "c++ debug" : "g++ -std=c++17 -O2 -DPAUL -Wshift-overflow=2  -Wshadow  -Wall {filename} -o {executable} && ./{executable}",
    "python" :"python3 {filename}",

}

template_path = {
    'c++' :'/media/saurav/Programming/GIthub/Code-Lab/geany/ai_template.cpp',
    'python':'/media/saurav/Programming/GIthub/Code-Lab/geany/ai_template.py',
}

coder_name = bot['Boss']