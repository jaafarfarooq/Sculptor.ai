<?php
declare(strict_types=1);

require __DIR__ . '/../vendor/autoload.php';

use Dotenv\Dotenv;
use App\Service\OpenAiService;
use App\Controller\ChatController;

// Load .env
Dotenv::createImmutable(__DIR__ . '/..')->load();

// Instantiate your service & controller
$apiKey     = $_ENV['OPENAI_API_KEY'] ?? '';
$service    = new OpenAiService($apiKey);
$controller = new ChatController($service);

// Handle request & render view
$controller->handle();