# Intro

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg" height="40" width="40"  style="background-color:#fff;border-radius:25%;padding:5px" alt="nextjs logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" height="40" width="40" alt="django logo"  style="background-color:#fff;border-radius:25%;padding:5px" />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="40" width="40"  style="background-color:#fff;border-radius:25%;padding:5px" alt="postgresql logo"  />
</div>

###


In this project, I've tried to maintain `DRY` and clean code as much as possible. Created `Highly Re-usable Components` on the FrontEnd/NextJS, on the other hand, used `Class-Based Views` on BackEnd/DRF. Tried to avoid additional packages or library as much as possible, since I'm using Two Frameworks, one on the FrontEnd and another on the BackEnd 😅. Used their native solutions to implement necessary features.

## Resources

| Name         | Link                                                                                                                |
|-------------------|---------------------------------------------------------------------------------------------------------------------|
| FrontEnd Repo     | **[GitHub ↗ ](https://github.com/foy4748/phitron-django-005-frontend)**
| BackEnd Repo      | **[GitHub ↗ ](https://github.com/foy4748/phitron-django-005)**
| Requirements      | **[Notion ↗ ](https://screeching-plough-4fd.notion.site/Final-Assignment-sdt-assignment-05-1390adbafc6c80b0a057cee72b3419b3?pvs=4)**
| API Documentation | **[POSTMAN ↗ ](https://documenter.getpostman.com/view/14857923/2sAYBbf9su)**

## Getting Started
After cloning this repository, you need to initiate a virtual environment. Then install necessary packages within it.

1. Go to project root directory
```console
cd phitron-django-005
```
Here `project` is the main project folder, where the `settings.py` is the root settings file for the whole project, `urls.py` is the main url pattern handler. 


2. Run the command given below to create a virtual environment within the .venv directory
```console
# For Linux/MacOS
python3 -m venv .venv
```

```console
# For Windows
python -m venv .venv
```
**You need to do this once, after cloning the project. .venv folder is ignored within .gitignore file**    


3. Now run the command below to activate the virtual environment.
```console
# For Linux/MacOS
source .venv/bin/activate
```

```console
# For Windows
.\.venv\Scripts\activate
```


4. Now run this once to install all the packages
```console
pip install -r requirements.txt
```


5. You are good to go. To start the development server, simply run
```console
python manage.py runserver 3001
```
**Important [❗]: The Server uses `3001` as default port on development phase**

**Make sure you are within the right directory by entering `ls` or `dir` command to check if manage.py exists**

## Test Credentials

```json
{
    "username":  "test",
    "password":  "TestTest$1"
}
```

## API Documentation

Open this document after running the server locally

- **[POSTMAN Document Page ↗](https://documenter.getpostman.com/view/14857923/2sAYBbf9su)**

## Environment Variables [ Example ]

You may start by copying the `env.example` file into `project/.env` file. Content of `env.example` file

```
# Path
# project/.env

# Settings
DEBUG=True # On Development || Change to False on production
SECRET_KEY=SOME-RANDOM-SECRET-KEY

# Email Related
EMAIL_HOST_USER="THE GMAIL Account from where you've retreived app password"
EMAIL_HOST_PASSWORD="THE APP PASSWORD"


# Parameters for constructing your own PostgreSQL connection string
PGHOST="GET IT FROM VERCEL/NEON DB"
PGUSER="GET IT FROM VERCEL/NEON DB"
PGDATABASE="GET IT FROM VERCEL/NEON DB"
PGPASSWORD="GET IT FROM VERCEL/NEON DB"
PGPORT=5432 # Default is 5432


# FRONTEND_LINK=https://phitron-sdt-assignment-05-frontend.vercel.app # Production
FRONTEND_LINK=http://localhost:3000 # Development
```
There is also a seperate `.env` file on the `purchase_item` app to connect with the `SSLCommerze Store` simply copy these `.env` variables in the `purchase_item/.env` file
```
# Path
# purchase_item/.env

# SSLCOMMERZ Related
SSLCOMMERZ_STORE_KEY=GET-IT-FROM-SSLCOMMERZ-Sandbox-Account
SSLCOMMERZ_STORE_PASS=GET-IT-FROM-SSLCOMMERZ-Sandbox-Account

```

## Technologies

### FrontEnd
- NextJS (TypeScript)
- NextAuth
- TailwindCSS
- ShadCN
- React Hook Form
- Zod
- SSLCommerze (Payment Gateway)

#### Strategies
- Used NextJS built-in `fetch` function to perform network requests to Django to utilize the native `Caching System` of NextJS
- Most of the components are `Server Component`. Kept the number of `Client Component` as minimum as possible.
- Most of the data fetching is done using `Server Actions`.
- Re-used `CREATE` forms for `UPDATE` as well.
- `ProductPagination` and `ProductSearch` form are highly re-usable components. These are used on `ListView` pages such as - Product List Pages for Any User, or User/Admin dashboard.
- Used `NextAuth` to handle Authentication as well as Authorization using the `middleware.ts` file.

### BackEnd
- Django (Python)
- Django Rest Framework (DRF)
- PostgreSQL (on Vercel/NeonDB)
- SSLCommerze-Lib (Payment Gateway)

#### Strategies
- Used `Class-Based Views` as much as possible to write simple CRUD API endpoints
- Utilized Built-in solutions in Django REST Framework (aka DRF) for - Pagination, Search and Filter functionalites for Product.
- Wrote a Python script in the `scripts/populate_product_data.py` file to generate `Test Random Product` data to populate the Database to check whether everyting works or not.
- Used `Transaction & Rollback` to handle product purchase, since it performs delete operations on the `CartItem` and inserts data in the `PurchasedItem` model, as well as creates a `Transaction` model instance to keep the payment record.

### Deployments
- FrontEnd - **[Vercel ↗ ](https://phitron-sdt-assignment-05.vercel-frontend.app)**
- BackEnd - **[Vercel ↗ ](https://phitron-sdt-assignment-05.vercel.app)**

### Deployment Guide

Just run the command below to deploy the app on vercel
```bash
vercel --prod
```

