## Состояния игры:

```
waiting -> ready -> prepared -> 
starting -> playing -> finished 
-> restart -> exit -> waiting
```
---
**choose_img**: выбор фигуры которой игрок будет ходить
```json
{"user": "uuid", "action": "choose", "type": "circle"}
```
---
**prepare**: Пользователь нажимает готов!
```json
{"user": "uuid", "action": "prepared"}
```
---
**move**: ход в клетку
```json
{"user": "uuid", "action": "move", "row": 1, "col": 2}
```
---
**restart**: Пользователь готов к реваншу
```json
{"user": "uuid", "action": "restart"}
```
---
**exit**: Пользователь вышел из сессии
```json
{"user": "uuid", "action": "exit"}
```
---
Совсем в будущем:
**emote**: Отправляет определённый эмодзи второму игроку
```json
{"user": "uuid", "action": "emote", "emoji": "char"}
```


