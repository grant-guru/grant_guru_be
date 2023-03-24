# Grant Guru

### Get all scholarships
### Get a user's favorites
### Create a favorite
### 


```http
GET /api/v1/scholarships
```

Parameters: <br>
```
LOCATION=string
VETERAN=boolean
GENDER=string
ETHNICITY=array
LGBT=bool
KEYWORDS=string
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Example Value:

```json

{
    "data": {
        [
        "id": "1",
        "type": "scholarship",
        "attributes": {
            "title": "DEF CON 31",
            "amount": "1234" dollar sign or no? USD?
            "content": "Lorem ipsum dolor sit amet, ..."
            "URL": "https://linkedin.com/..."
            }
        ],
        [
        "id": "2",
        "type": "scholarship"
        "attributes": {
            "title": "RailsConf 23",
            "amount": "1234"
            "content": "Lorem ipsum dolor sit amet, ..."
            "URL": "https://linkedin.com/..."
            }
        ],
        [...],
        [...]
    }
}
```
