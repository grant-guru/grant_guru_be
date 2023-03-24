# grant_guru_be

### Get all scholarships
### Get a user's favorites
### Create a favorite
### 


```http
GET /api/v1/users/:id
```

Parameters: <br>
```
GOOGLE_UID=12345678901234567890
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Example Value:

```json

{
    "data": {
        "id": "1",
        "type": "user",
        "attributes": {
            "first_name": "Kaylah",
            "last_name": "Rose",
            "phone_number": null,
            "email": "kaylahrosem@gmail.com",
            "emergency_contact_name": null,
            "emergency_contact_phone_number": null,
            "google_uid": "12345678901234567890"
        }
    }
}
```
