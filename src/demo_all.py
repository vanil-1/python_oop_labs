from src.lab01.demo import main as lab01
from src.lab02.demo import main as lab02
from src.lab03.demo import main as lab03
from src.lab04.demo import main as lab04
from src.lab05.demo import main as lab05
from src.lab06.demo import main as lab06

LABS = [
    ("LAB-01", lab01),
    ("LAB-02", lab02),
    ("LAB-03", lab03),
    ("LAB-04", lab04),
    ("LAB-05", lab05),
    ("LAB-06", lab06),
]

def run_all() -> None:
    for name, fn in LABS:
        print(name)
        fn()

if __name__ == "__main__":
    run_all()