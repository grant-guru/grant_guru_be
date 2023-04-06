# Grant Guru 🎓
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-energy-drinks.svg)](https://forthebadge.com)

Visit our API [here](https://grant-guru-be.herokuapp.com/api/v1/scholarships/)!

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
<details close>
<summary>  Details </summary>
<br>

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
    "relationships": {
        "grants": {
            "data": [
                {
                    "type": "Grant",
                    "id": "2"
                },
                {
                    "type": "Grant",
                    "id": "3"
                },
                {
                    "type": "Grant",
                    "id": "4"
                },
                {
                    "type": "Grant",
                    "id": "52"
                }
            ],
        "meta": {
            "count": 4
            }
        }
    }
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
</details>

## Schema

![Screen Shot 2023-04-06 at 11 37 34 AM](https://user-images.githubusercontent.com/111713452/230454687-e4f0acc4-0e3e-4e7a-a05a-5a44a78f4198.png)



## Contributors

<i>All participants in this project are graduates from the Turing School of Software & Design.</i> <br> <br>
  
<b>Kaylah Rose Mitchell</b> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: <a href="https://github.com/kaylahrose">@kaylahrose</a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: <a href="https://www.linkedin.com/in/kaylahrose/">kaylahrose</a> <br>

<b>Matisse Mallette</b> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: <a href="https://github.com/MatisseMallette">@MatisseMallette</a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: <a href="https://www.linkedin.com/in/matisse-mallette/">matisse-mallette</a> <br>

<b>Sergio Azcona</b> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: <a href="https://github.com/MatisseMallette">@Sergio-Azcona</a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: <a href="https://www.linkedin.com/in/sergio-azcona/">sergio-azcona</a> <br>


<b>Drew Layton</b> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub: <a href="https://github.com/dlayton66">@dlayton66</a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LinkedIn: <a href="https://www.linkedin.com/in/drew-layton/">drew-layton</a> <br>
