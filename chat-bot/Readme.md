# Fitness ChatGPT

A modular PHP chat-bot powered by OpenAI’s GPT-3.5-turbo, with automatic light/dark theming based on time of day. Built to run under XAMPP (Windows) or MAMP (macOS), and fully unit-tested with PHPUnit.

---

## 🚀 Features

- **Light/Dark Theme**: Auto-switches after 8 PM local time  
- **Modular Architecture**: PSR-4 services, controllers, templates  
- **Composer-Managed**: Dependency management & autoloading  
- **Env-Driven**: Securely load your OpenAI API key from `.env`  
- **Unit Tested**: PHPUnit tests for both service & controller  

---

## 📂 Project Structure

chat-bot/
├── public/
│ ├── index.php # Front controller & autoloader bootstrap
│ └── style.css # Light/dark themed UI styles
├── src/
│ ├── Controller/
│ │ └── ChatController.php
│ └── Service/
│ └── OpenAiService.php
├── templates/
│ └── chat.php # HTML view template
├── tests/
│ ├── Controller/
│ │ └── ChatControllerTest.php
│ └── Service/
│ └── OpenAiServiceTest.php
├── vendor/ # Composer dependencies
├── composer.json # Composer config & PSR-4 autoload
├── composer.lock
├── phpunit.xml # PHPUnit suite config
└── .env # Your OpenAI API key (git-ignored)


---

## 🛠️ Prerequisites

### Windows (XAMPP)

1. **XAMPP** (Apache & PHP)  
2. **Composer** (https://getcomposer.org/)  
3. **Git** (optional)

### macOS (MAMP)

1. **MAMP** (Apache & PHP)  
2. **Composer**  
3. **Git** (optional)

---

## 🔧 Installation & Setup

1. **Clone** the repo into your web root:  
   - **Windows**  
     ```bat
     cd C:\xampp\htdocs
     git clone https://github.com/your-username/chat-bot.git
     cd chat-bot
     ```
   - **macOS**  
     ```bash
     cd /Applications/MAMP/htdocs
     git clone https://github.com/your-username/chat-bot.git
     cd chat-bot
     ```

2. **Point your shell** to the bundled PHP CLI:  
   - **Windows**: Add `C:\xampp\php` to your PATH.  
   - **macOS (zsh)**:  
     ```bash
     echo 'export PATH="/Applications/MAMP/bin/php/php8.1.0/bin:$PATH"' >> ~/.zshrc
     source ~/.zshrc
     ```

3. **Install PHP dependencies**:  
   ```bash
   composer install


🌐 Server Configuration
Windows (XAMPP)
Start Apache in XAMPP Control Panel.

Ensure DocumentRoot is set to:

swift
Copy
Edit
C:/xampp/htdocs/chat-bot/public
(edit httpd.conf if needed).

In browser, visit:

arduino
Copy
Edit
http://localhost/chat-bot/
macOS (MAMP)
Open the MAMP app → Preferences → Web Server.

Set Document Root to:

swift
Copy
Edit
/Applications/MAMP/htdocs/chat-bot/public
Start Apache & MySQL.

Visit:

arduino
Copy
Edit
http://localhost:8888/
🎯 Usage
Open the chat page in your browser.

Type any fitness or nutrition question.

Click Get Answer.

See AI’s response in the adjacent card (or below on mobile).

UI automatically switches to dark mode after 8 PM.

🧪 Running Tests
Execute all unit tests with PHPUnit:

bash:
./vendor/bin/phpunit --colors=always
Expected output:

python-repl:
PHPUnit 9.x by Sebastian Bergmann and contributors.

...                                                             5 / 5 (100%)

Time: 00.03s, Memory: 6.00 MB
-------------------------
👩‍💻 Development Guide
Add Services in src/Service, tests in tests/Service.

Add Controllers in src/Controller, tests in tests/Controller.

Templates in templates/—keep PHP minimal.

Assets (CSS/JS) remain in public/.

Run composer dump-autoload after adding classes.