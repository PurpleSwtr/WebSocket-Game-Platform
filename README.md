# WebSockets TicTacToe

#### Backend:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

#### Frontend:
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

---

Проект был разработан мной, с целью изучить как работают веб-сокеты на практике, а также сделать свою собственную онлайн-платформу.

### Демонстрация взаимодействия двух пользователей (работает в пределах локальной сети)

https://github.com/user-attachments/assets/c22d7dd6-6e7a-4d2a-9bbb-f3923533d466

---

Мне не очень хотелось писать какой-то очередной чат, где будут комнаты для обычной отправки строк друг другу, boring...
Тут гораздо больше логики, данных которые нужно синхронизировать, состояний и т.д.
> **Идея:**
> — Я всегда смотрел на своих одногруппников, которые на скучных лекциях залипают в свои телефоны/ноутбуки, и хотел запустить какой-нибудь ивент, просто скинув в чат ссылку на свой сервер, и все могли бы собраться и поиграть в игру по типу "Мафии", "Квиза" или любого другого party-like развлечения. Потому что очень часто готовые решения предоставляют только взаимодействе в пределах одного экрана, а для целой аудитории это не очень эффективно.
>
> Так я и придумал этот проект который можно расширять в платформу!

### Лобби с отображением состояния по текущим сессиям

<img width="1195" height="555" alt="Image" src="https://github.com/user-attachments/assets/d071da5a-ac4e-4f27-87c7-edd9eb36039e" />

В дальнейшем этот проект будет базой для разработки моей изначальной задумки - сделать онлайн морской бой для локальной сети (но с расчётом на масштабирование, с прицелом на highload). Так как принцип этих двух игр максимально похож с точки зрения взаимодействия (поле 3x3/10x10, состояние каждой ячейки, её заполненность и условия выигрыша в зависимости от состояния на поле)

Поэтому для упрощения понимания для начала, выбрал именно этот концепт, добавляя свои собственные фичи в UX и геймдизайн.

### DEV: Запуск сервера FastAPI:
```
python -m uvicorn Backend.src.main:app --reload --host 0.0.0.0 --port 8000
```
### DEV: Запуск сервера NPM:
```
cd Frontend && npm run dev -- --host 0.0.0.0
```
```http://127.0.0.1:8000/docs```

### Дока:
```https://fastapi.tiangolo.com/ru```
