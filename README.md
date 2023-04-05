# Grant Guru
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-energy-drinks.svg)](https://forthebadge.com)


## MacOS Installation

1. Clone the repository
2. `CD` into the root directory
3. Create and activate the virtual environment
```C
$ python3 -m venv .venv
$ source .venv/bin/activate
```
4. Install requirements with `pip install -r requirements.txt`
5. Run `$ touch grant_guru_be/.env` to create a `.env` environment variable file in the grant_guru_be directory

6. Add your database environment variables to the `.env` file
```python
SECRET_KEY=<django-insecure>
DB_NAME=<your_database_name>
DB_USER=<your_database_user>
DB_PASSWORD=<your_database_password>
DB_HOST=<your_database_host>
PORT=<your_database_port>
```
7. Run migrations `python3 manage.py migrate`
8. Start the server `python3 manage.py runserver`

## Endpoints

### Get all scholarships

```http
GET /api/v1/scholarships
```

<details close>
<summary>  Details </summary>
<br>


Parameters: <br>
```
education=string
gender=string
state=string
lgbt=bool
ethnicity=array
veteran=bool
immigrant=bool
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
