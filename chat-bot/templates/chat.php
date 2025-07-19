<?php // templates/chat.php ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Ask Fitness ChatGPT</title>
  <link rel="stylesheet" href="/chat-bot/public/style.css">
  <script>
    (function(){
      const h = new Date().getHours();
      const theme = (h >= 20 || h < 6) ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', theme);
    })();
  </script>
</head>
<body>
  <main class="container">
    <h1>Ask Fitness ChatGPT</h1>

    <div class="chat-wrapper">
      <!-- Prompt Card -->
      <form method="POST" class="card chat-form">
        <textarea
          name="question"
          rows="6"
          placeholder="Type your fitness or nutrition question…"
          required
        ><?= htmlspecialchars($question, ENT_QUOTES, 'UTF-8') ?></textarea>
        <button type="submit">Get Answer</button>
      </form>

      <!-- Response Card -->
      <?php if ($answer !== ''): ?>
      <section class="card response-card">
        <h2>Fitness ChatGPT says:</h2>
        <p><?= nl2br(htmlspecialchars($answer, ENT_QUOTES, 'UTF-8')) ?></p>
      </section>
      <?php endif; ?>
    </div>
  </main>
</body>
</html>
