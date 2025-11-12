# Profile Website with web server integration
This is a 2-in-1 project where it incorporates making an http server from scratch and making a website all about the developer

#### Structure guide
<pre>
    htdocs/
    │
    ├── index.php                 # Main entry point (home page)
    ├── .htaccess                 # Apache configuration file (optional)
    │
    ├── about.php                 # Another page
    ├── contact.php               # Contact page
    │
    ├── assets/                   # Static assets (CSS, JS, images)
    │   ├── css/
    │   │   ├── style.css
    │   │   └── bootstrap.min.css
    │   ├── js/
    │   │   ├── main.js
    │   │   └── jquery.min.js
    │   └── images/
    │       ├── logo.png
    │       └── background.jpg
    │
    ├── includes/                 # Reusable components
    │   ├── header.php
    │   ├── footer.php
    │   └── db_connect.php
    │
    ├── admin/                    # Admin section
    │   ├── index.php
    │   ├── dashboard.php
    │   └── assets/
    │       ├── css/
    │       └── js/
    │
    ├── api/                      # Backend API routes (if using PHP)
    │   ├── get_users.php
    │   ├── add_user.php
    │   └── delete_user.php
    │
    └── uploads/                  # Folder for uploaded files
        ├── profile_pics/
        └── documents/`
</pre>