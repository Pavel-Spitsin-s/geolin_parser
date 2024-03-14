from bs4 import BeautifulSoup
import re
import requests

url = "https://geolin.ru/milestones/home/event/1878"
r = requests.get(url)
f = open("cringe.html")
soup = BeautifulSoup(f, "html.parser")
b = str(soup)


def parse(matr: str) -> list:
    a = []
    for i in matr.split("\hline"):
        for j in i.split("\\"):
            x = j.strip()
            if not len(x):
                continue
            cur = j.split("&amp;amp;")
            for ind in range(len(cur)):
                cur[ind] = cur[ind].strip()
            cur = list(map(int, cur))
            a.append(cur)
    return a


def go_next(chose: str) -> list:
    chose = chose[chose.find("amp") - 3::]
    end = chose.find("\end")
    matr = chose[:end]
    chose = chose[end::]
    return [chose, matr]


def parse_all_statements(number_of_problems: int, b: str) -> list:
    all_tasks = []
    chose = b[b.find("amp") - 3::]
    end = chose.find("\end")
    matr = chose[:end]
    all_tasks.append(parse(matr))
    chose, matr = go_next(chose)
    for i in range(number_of_problems - 1):
        chose, matr = go_next(chose)[::]
        chose, matr = go_next(chose)[::]
        all_tasks.append(parse(matr))
    return all_tasks


def main():
    n = int(input("Number of problems:"))
    a = parse_all_statements(n, b)
    print(a)


if __name__ == "__main__":
    main()
