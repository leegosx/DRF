# DRF Contact API

This is a simple Contact API built with Django Rest Framework (DRF). It allows users to manage contact information such as first name, last name, email, and phone number.

## Features

- List all contacts
- Retrieve contact by ID
- Retrieve contact by first name
- Retrieve contact by last name
- Retrieve contact by email
- Retrieve contact by phone number
- Create new contact
- Update existing contact
- Delete contact

![API Overview](https://www.dropbox.com/scl/fi/bm9xipbha1c31hde3ratw/apioverview.png?rlkey=n5ny3f148tfri38269k6ul61g&?raw=1)

## Installation

1. Clone the repository:

```
git clone https://github.com/leegosx/DRF.git
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Run the migrations:

```
python manage.py migrate
```

4. Run the server:

```
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Usage

### List all contacts

```
GET /contacts/
```

### Retrieve contact by ID

```
GET /contacts/api/list/?id=<ID>
```

### Retrieve contact by first name

```
GET /contacts/api/list/?first_name=<FIRST_NAME>
```

### Retrieve contact by last name

```
GET /contacts/api/list/?last_name=<LAST_NAME>
```

### Retrieve contact by email

```
GET /contacts/api/list/?email=<EMAIL>
```

### Retrieve contact by phone number

```
GET /contacts/api/list/?phone=<PHONE_NUMBER>
```

### Create new contact

```
POST /contacts/create/
```

### Update existing contact

```
PUT /contacts/<int:pk>/update/
```

### Delete contact

```
DELETE /contacts/<int:pk>/delete/
```

## License

MIT License
