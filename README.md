# Grant Guru

### Get all scholarships

```http
GET /api/v1/scholarships
```

<details close>
<summary>  Details </summary>
<br>


Parameters: <br>
```
EDUCATION=string
GENDER=string
STATE=string
LGBT=bool
ETHNICITY=array
VETERAN=bool
IMMIGRANT=bool
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Example Response:

```json
{
    "data": [
        {
            "id": "1",
            "type": "scholarship",
            "attributes": {
                "title": "Female Privacy Leaders Scholarship",
                "organization": "Women in Security and Privacy (WISP)",
                "amount": "1234",
                "description": "Lorem ipsum dolor sit amet, ...",
                "deadline": "March 01, 2023",
                "education": "Graduate",
                "state": "Colorado",
                "women": "False",
                "lgbt": "True",
                "ethnicity": [
                    "Black",
                    "Hispanic"
                ],
                "veteran": "False",
                "immigrant": "True",
                "url": "https://linkedin.com/...",
                "image_url": "https://shutter_stock_static_image"
            }
        },
        {
            "id": "2",
            "type": "scholarship",
            "attributes": {
                "title": "RailsConf 23",
                "organization": "Ruby Central",
                "amount": "1234",
                "description": "Lorem ipsum dolor sit amet, ...",
                "deadline": "March 01, 2023",
                "education": "Graduate",
                "state": "",
                "women": "False",
                "lgbt": "True",
                "ethnicity": [],
                "veteran": "False",
                "immigrant": "True",
                "url": "https://linkedin.com/...",
                "image_url": "https://static_image.wow_nice"
            }
        },
        {...},
        {...}
    ]
}
```
</details>

### Get a user's favorites

```http
GET /api/v1/users/:id/favorites
```

<details close>
<summary>  Details </summary>
<br>
    
| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Example Response:

```json
{
    "data": [
        {
            "id": "1",
            "type": "scholarship",
            "attributes": {
                "title": "Female Privacy Leaders Scholarship",
                "organization": "Women in Security and Privacy (WISP)",
                "amount": "1234",
                "description": "Lorem ipsum dolor sit amet, ...",
                "deadline": "March 01, 2023",
                "education": "Graduate",
                "state": "Colorado",
                "women": "False",
                "lgbt": "True",
                "ethnicity": [
                    "Black",
                    "Hispanic"
                ],
                "veteran": "False",
                "immigrant": "True",
                "url": "https://linkedin.com/...",
                "image_url": "https://shutter_stock_static_image"
            }
        },
        {
            "id": "2",
            "type": "scholarship",
            "attributes": {
                "title": "RailsConf 23",
                "organization": "Ruby Central",
                "amount": "1234",
                "description": "Lorem ipsum dolor sit amet, ...",
                "deadline": "March 01, 2023",
                "education": "Graduate",
                "state": "",
                "women": "False",
                "lgbt": "True",
                "ethnicity": [],
                "veteran": "False",
                "immigrant": "True",
                "url": "https://linkedin.com/...",
                "image_url": "https://static_image.wow_nice"
            }
        },
        {...},
        {...}
    ]
}
```
</details>

### Get a scholarship

```http
GET /api/v1/scholarships/:id
```

<details close>
<summary>  Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Example Response:

```json
{
    "data": {
        "id": "1",
        "type": "scholarship",
        "attributes": {
            "title": "Female Privacy Leaders Scholarship",
            "organization": "Women in Security and Privacy (WISP)",
            "amount": "1234",
            "description": "Lorem ipsum dolor sit amet, ...",
            "deadline": "March 01, 2023",
            "education": "Graduate",
            "state": "Colorado",
            "women": "False",
            "lgbt": "True",
            "ethnicity": [
                "Black",
                "Hispanic"
            ],
            "veteran": "False",
            "immigrant": "True",
            "url": "https://linkedin.com/...",
            "image_url": "https://shutter_stock_static_image"
        }
    } 
}
```
</details>

### Create a favorite
```http
POST /api/v1/users/:user_id/scholarships/:scholarship_id
```

<details close>
<summary>  Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 201 | `created` |
    
Example Response:

```json
{
    "data": {
        "id": "1",
        "type": "scholarship",
        "attributes": {
            "title": "Female Privacy Leaders Scholarship",
            "organization": "Women in Security and Privacy (WISP)",
            "amount": "1234",
            "description": "Lorem ipsum dolor sit amet, ...",
            "deadline": "March 01, 2023",
            "education": "Graduate",
            "state": "Colorado",
            "women": "False",
            "lgbt": "True",
            "ethnicity": [
                "Black",
                "Hispanic"
            ],
            "veteran": "False",
            "immigrant": "True",
            "url": "https://linkedin.com/...",
            "image_url": "https://shutter_stock_static_image"
        }
    } 
}
```
</details>

### Delete a favorite
```http
DELETE /api/v1/users/:user_id/scholarships/:scholarship_id
```

<details close>
<summary>  Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Example Response:

```json
{
    "data": {
        "id": "1",
        "type": "scholarship",
        "attributes": {
            "title": "Female Privacy Leaders Scholarship",
            "organization": "Women in Security and Privacy (WISP)",
            "amount": "1234",
            "description": "Lorem ipsum dolor sit amet, ...",
            "deadline": "March 01, 2023",
            "education": "Graduate",
            "state": "Colorado",
            "women": "False",
            "lgbt": "True",
            "ethnicity": [
                "Black",
                "Hispanic"
            ],
            "veteran": "False",
            "immigrant": "True",
            "url": "https://linkedin.com/...",
            "image_url": "https://shutter_stock_static_image"
        }
    } 
}
```
</details>

### Get a user
```http
GET /api/v1/users/:user_id
```

<details close>
<summary>  Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Example Response:

```json
{
    "data": {
        "id": "1",
        "type": "user",
        "attributes": {
            "first_name": "Hugh",
            "last_name": "Jackman",
            "image_url": "http://www.image-url.com"
        }
    }  
}
```
</details>
