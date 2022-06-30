# Meal_Garage 
Backend with FastAPI

# API
## User
略
## Food
### POST /api/v1/foods
#### リクエスト(ユーザーが送る情報)
```
{
    'name': '豚肉',
    'quantity': 300,
    'limit_at': '2022-06-18'
}
```
#### レスポンス(ユーザが受け取る情報)
```
{
    'id': 'xxxx-xxxx-xxxxxxxx'(ユーザーが別でも既に同じ食材があれば同じIDで)
    'name': '豚肉',
    'quantity': 300,
    'limit_at': '2022-06-18'
}
```

### GET /api/v1/foods
#### リクエスト
なし
#### レスポンス
```
[
    {
        'id': 'xxxx-xxxx-xxxxxxxx'
        'name': '豚肉',
        'quantity': 300,
        'limit_at': '2022-06-18'
    },
    {
        'id': 'xxxx-xxxx-xxxxxxxx'
        'name': '豚肉',
        'quantity': 300,
        'limit_at': '2022-06-18'
    },
    {
        'id': 'xxxx-xxxx-xxxxxxxx'
        'name': '豚肉',
        'quantity': 300,
        'limit_at': '2022-06-18'
    }
]
```

### DELETE /api/v1/foods/{id}
#### リクエスト
path: id(食材のID)
#### レスポンス
ユーザー削除と同じ

### GET /api/v1/foods/recipe
#### リクエスト(ユーザーが送る情報)
```
{
    'name': '豚肉',
    'quantity': 300,
    'limit_at': '2022-06-18'
}
```
#### レスポンス(ユーザが受け取る情報)
```
{
    'id': 'xxxx-xxxx-xxxxxxxx'
    'name': '豚肉',
    'quantity': 300,
    'limit_at': '2022-06-18'
}
```
